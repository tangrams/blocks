#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

uniform float u_scroll;

float smoothedge(float v) {
    return smoothstep(0.0, 1.0 / u_resolution.x, v);
}

float triangle(vec2 p, float size) {
    vec2 q = abs(p);
    return max(q.x * 0.514 + p.y * 0.5, -p.y * 0.5) - size * 0.5;
}

float rect(vec2 p, vec2 size) {  
  vec2 d = abs(p) - size;
  return min(max(d.x, d.y), 0.0) + length(max(d,0.0));
}

float square(vec2 p, float size) {
     return rect(p, vec2(size));
}

float random (in float x) {
    return fract(sin(x)*43758.5453);
}

mat2 rotate2d(float angle){
    return mat2(cos(angle),-sin(angle),
                sin(angle),cos(angle));
}

vec3 myPalette(in float x) {
    return mix(vec3(0.000,0.912,0.877), 
               vec3(1.265,0.037,0.074), 
               vec3(smoothstep(0.0,0.800, x),
                    sin(x*3.1415), 
                    x));
}

void main() {
    vec2 st = gl_FragCoord.xy/u_resolution.xy;
    st = (st-.5)*1.+.5;
    if (u_resolution.y < u_resolution.x ) {
        st.y *= u_resolution.y/u_resolution.x;
        st.y -= (u_resolution.y*.5-u_resolution.x*.5)/u_resolution.x;
    } else {
        st.x *= u_resolution.x/u_resolution.y;
        st.x -= (u_resolution.x*.5-u_resolution.y*.5)/u_resolution.y;
    }

    st -= .5;
    
    float rInv = 1./abs(st.x);
    vec2 pos = st * rInv - vec2(rInv,0.0);
    rInv *= .2+smoothstep(.0,.1,u_scroll);

    float t = u_time;
    pos *= 6.;
    pos.y += sin(t*0.01)*100.;
    
    float seed = random(floor(pos.y))+.1;

    pos.x -= (t*seed)*5.;
    
    vec2 ipos = floor(pos);
    vec2 fpos = fract(pos);    
	fpos -= .5;
    fpos = rotate2d(t-seed) * fpos;
    
    float d = 1.;
    float p = random(seed*ipos.x);
    if (p <= .125) {
        d = min(d, triangle(fpos, 0.186));
    } else if (p <= .25) {
        d = min(d, square(fpos, 0.234));
    } else if (p <= .5) {
        d = min(d, square((fpos+1.)+vec2(fpos.y)-1., 0.2));
    }
    
    vec3 color = myPalette(fract(p+seed));
    color = mix(vec3(1.0),
                color,
                clamp((1.-smoothedge(d))*(1.-smoothstep(.6,1.,rInv)),0.,1.));
    
    gl_FragColor = vec4(color,1.0);
}