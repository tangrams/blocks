#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;


uniform sampler2D u_random; // https://tangrams.github.io/blocks/generative/imgs/tex16.png

#define NOISE_TEXSAMPLE_SIZE 256.0

#define NUM_OCTAVES 8

// varying vec4 v_position;
// varying vec4 v_color;
// varying vec3 v_normal;
varying vec2 v_texcoord;


vec3 random3 (vec2 p) {
    #ifdef RANDOM_TEXSAMPLE
    return texture2D(u_random,fract(p*2.),-100.).rgb;
    #else
    return fract(sin(vec3( dot(p,vec2(127.1,311.7)), dot(p,vec2(269.5,183.3)), dot(p,vec2(419.2,371.9)) ))*43758.5453); 
    #endif
}
vec3 random3 (vec3 p) {
    #ifdef RANDOM_TEXSAMPLE
    vec2 uv = fract(p.xy+vec2(37.0,17.0)*p.z);
    return texture2D(u_random, fract(uv*2.), -100.0).rgb;
    #else
    float j = 4096.0*sin(dot(p,vec3(17.0, 59.4, 15.0)));
    vec3 r;
    r.z = fract(512.0*j);
    j *= .125;
    r.x = fract(512.0*j);
    j *= .125;
    r.y = fract(512.0*j);
    return r-0.5;
    #endif
}
vec2 random2 (vec2 p) { 
    #ifdef RANDOM_TEXSAMPLE
    return random3(p).rg;
    #else
    return fract(sin(vec2(dot(p,vec2(127.1,311.7)),dot(p,vec2(269.5,183.3))))*43758.5453); 
    #endif
}
float random (float x) { 
    return fract(sin(x)*43758.5453);
}
float random (vec2 p) { 
    #ifdef RANDOM_TEXSAMPLE
    return random3(p).r;
    #else
    return fract(1e4 * sin(17.0 * p.x + p.y * 0.1) * (0.1 + abs(sin(p.y * 13.0 + p.x)))); 
    #endif
}
float random (vec3 p) { 
    #ifdef RANDOM_TEXSAMPLE
    return random3(p).r;
    #else
    return fract(sin(dot(p.xyz, vec3(70.9898,78.233,32.4355)))* 43758.5453123); 
    #endif
}
// 1D Value Noise for 1, 2 and 3 dimentions
// ================================
float noise (in float x) {
    float i = floor(x);
    float f = fract(x);
    f = f * f * (3.0 - 2.0 * f);
    #ifdef NOISE_TEXSAMPLE
    return texture2D(u_random, vec2(fract((x+.5)/NOISE_TEXSAMPLE_SIZE),.5), -100.).r;
    #else
    return mix(random(i), random(i + 1.0), f);
    #endif
}

float noise (vec2 p) {
    vec2 i = floor(p);
    vec2 f = fract(p);
    f = f * f * (3.0 - 2.0 * f);
    #ifdef NOISE_TEXSAMPLE
    return texture2D(u_random, fract((p+.5)/NOISE_TEXSAMPLE_SIZE), -100.).r;
    #else
    float a = random(i);
    float b = random(i + vec2(1.0, 0.0));
    float c = random(i + vec2(0.0, 1.0));
    float d = random(i + vec2(1.0, 1.0));
    return mix(a, b, f.x) + (c - a) * f.y * (1.0 - f.x) + (d - b) * f.x * f.y;
    #endif
}

float noise (vec3 p) {
    vec3 i = floor(p);
    vec3 f = fract(p);
    f = f*f*(3.0-2.0*f);
    #ifdef NOISE_TEXSAMPLE
    vec2 uv = (i.xy+vec2(37.0,17.0)*i.z) + f.xy;
    vec2 rg = texture2D(u_random, fract((uv+.5)/NOISE_TEXSAMPLE_SIZE), -100.0 ).yx;
    return mix( rg.x, rg.y, f.z );
    #else
    const vec3 step = vec3(110.0, 241.0, 171.0);
    float n = dot(i, step);
    return mix( mix(mix(random(n + dot(step, vec3(0,0,0))),
                        random(n + dot(step, vec3(1,0,0))), f.x),
                    mix(random(n + dot(step, vec3(0,1,0))),
                        random(n + dot(step, vec3(1,1,0))), f.x),
                    f.y),
                mix(mix(random(n + dot(step, vec3(0,0,1))),
                        random(n + dot(step, vec3(1,0,1))), f.x),
                    mix(random(n + dot(step, vec3(0,1,1))),
                        random(n + dot(step, vec3(1,1,1))), f.x),
                f.y),
            f.z);
    #endif
}

// Description : GLSL 2D simplex noise function
//      Author : Ian McEwan, Ashima Arts
//  Maintainer : ijm
//     Lastmod : 20110822 (ijm)
//     License : 
//  Copyright (C) 2011 Ashima Arts. All rights reserved.
//  Distributed under the MIT License. See LICENSE file.
//  https://github.com/ashima/webgl-noise
vec3 mod289(vec3 x) { 
    return x - floor(x * (1.0 / 289.0)) * 289.0; 
}
vec2 mod289(vec2 x) { 
    return x - floor(x * (1.0 / 289.0)) * 289.0; 
}
vec3 permute(vec3 x) { 
    return mod289(((x*34.0)+1.0)*x); 
}
float snoise(vec2 v) {

    // Precompute values for skewed triangular grid
    const vec4 C = vec4(0.211324865405187,
                        // (3.0-sqrt(3.0))/6.0
                        0.366025403784439,  
                        // 0.5*(sqrt(3.0)-1.0)
                        -0.577350269189626,  
                        // -1.0 + 2.0 * C.x
                        0.024390243902439); 
                        // 1.0 / 41.0

    // First corner (x0)
    vec2 i  = floor(v + dot(v, C.yy));
    vec2 x0 = v - i + dot(i, C.xx);

    // Other two corners (x1, x2)
    vec2 i1 = vec2(0.0);
    i1 = (x0.x > x0.y)? vec2(1.0, 0.0):vec2(0.0, 1.0);
    vec2 x1 = x0.xy + C.xx - i1;
    vec2 x2 = x0.xy + C.zz;

    // Do some permutations to avoid
    // truncation effects in permutation
    i = mod289(i);
    vec3 p = permute(
            permute( i.y + vec3(0.0, i1.y, 1.0))
                + i.x + vec3(0.0, i1.x, 1.0 ));

    vec3 m = max(0.5 - vec3(
                        dot(x0,x0), 
                        dot(x1,x1), 
                        dot(x2,x2)
                        ), 0.0);

    m = m*m ;
    m = m*m ;

    // Gradients: 
    //  41 pts uniformly over a line, mapped onto a diamond
    //  The ring size 17*17 = 289 is close to a multiple 
    //      of 41 (41*7 = 287)

    vec3 x = 2.0 * fract(p * C.www) - 1.0;
    vec3 h = abs(x) - 0.5;
    vec3 ox = floor(x + 0.5);
    vec3 a0 = x - ox;

    // Normalise gradients implicitly by scaling m
    // Approximation of: m *= inversesqrt(a0*a0 + h*h);
    m *= 1.79284291400159 - 0.85373472095314 * (a0*a0+h*h);

    // Compute final noise value at P
    vec3 g = vec3(0.0);
    g.x  = a0.x  * x0.x  + h.x  * x0.y;
    g.yz = a0.yz * vec2(x1.x,x2.x) + h.yz * vec2(x1.y,x2.y);
    return 130.0 * dot(m, g);
}


//
// Simplex Noise
//
const float F3 =  0.3333333;
const float G3 =  0.1666667;
float snoise (vec3 p) {
    vec3 s = floor(p + dot(p, vec3(F3)));
    vec3 x = p - s + dot(s, vec3(G3));
    vec3 e = step(vec3(0.0), x - x.yzx);
    vec3 i1 = e*(1.0 - e.zxy);
    vec3 i2 = 1.0 - e.zxy*(1.0 - e);
    vec3 x1 = x - i1 + G3;
    vec3 x2 = x - i2 + 2.0*G3;
    vec3 x3 = x - 1.0 + 3.0*G3;
    vec4 w, d;
    w.x = dot(x, x);
    w.y = dot(x1, x1);
    w.z = dot(x2, x2);
    w.w = dot(x3, x3);
    w = max(0.6 - w, 0.0);
    d.x = dot(random3(s), x);
    d.y = dot(random3(s + i1), x1);
    d.z = dot(random3(s + i2), x2);
    d.w = dot(random3(s + 1.0), x3);
    w *= w;
    w *= w;
    d *= w;
    return dot(d, vec4(52.0));
}
// Fractional Brownian motion for 1, 2 and 3 dimensions
float fbm (in float x) {
    float v = 0.0;
    float a = 0.5;
    float shift = float(100.0);
    for (int i = 0; i < int(NUM_OCTAVES); ++i) {
        v += a * noise(x);
        x = x * 2.0 + shift;
        a *= 0.5;
    }
    return v;
}
float fbm (in vec2 xy) {
    float v = 0.0;
    float a = 0.5;
    vec2 shift = vec2(100.0);
    mat2 rot = mat2(cos(0.5), sin(0.5), 
                    -sin(0.5), cos(0.50));
    for (int i = 0; i < int(NUM_OCTAVES); ++i) {
        v += a * noise(xy);
        xy = rot * xy * 2.0 + shift;
        a *= 0.5;
    }
    return v;
}
float fbm (in vec3 xyz) {
    float v = 0.0;
    float a = 0.5;
    vec3 shift = vec3(100.0);
    for (int i = 0; i < int(NUM_OCTAVES); ++i) {
        v += a * noise(xyz);
        xyz = xyz * 2.0 + shift;
        a *= 0.5;
    }
    return v;
}
void main() {
    // vec3 normal = v_normal;
    vec4 color = vec4(0.,0.,0.,1.);

color += fbm(v_texcoord.x);
    gl_FragColor = color;
}