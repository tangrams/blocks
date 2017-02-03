#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;


uniform sampler2D u_random; // https://tangrams.github.io/blocks/generative/imgs/tex16.png

varying vec4 v_position;
varying vec4 v_color;
varying vec3 v_normal;
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
void main() {
    vec3 normal = v_normal;
    vec4 color = vec4(0.,0.,0.,1.);

color.rgb += random(v_texcoord.xy*2.);
    gl_FragColor = color;
}