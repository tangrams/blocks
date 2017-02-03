#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;


#define TAU 6.28318530718

#define CAUSTIC_ITERATIONS 3

varying vec4 v_position;
varying vec4 v_color;
varying vec3 v_normal;
varying vec2 v_texcoord;


// Caustic effect from https://www.shadertoy.com/view/4ljXWh
vec3 getCaustic (vec2 uv) {
    vec2 p = mod(uv*TAU, TAU)-250.0;
    float time = u_time * .5+23.0;
    vec2 i = vec2(p);
    float c = 1.0;
    float inten = .005;
    for (int n = 0; n < int(CAUSTIC_ITERATIONS); n++) {
        float t = time * (1.0 - (3.5 / float(n+1)));
        i = p + vec2(cos(t - i.x) + sin(t + i.y), sin(t - i.y) + cos(t + i.x));
        c += 1.0/length(vec2(p.x / (sin(i.x+t)/inten),p.y / (cos(i.y+t)/inten)));
    }
    c /= float(CAUSTIC_ITERATIONS);
    c = 1.17-pow(c, 1.4);
    vec3 color = vec3(pow(abs(c), 8.0));
    color = clamp(color + vec3(0.0, 0.35, 0.5), 0.0, 1.0);
    color = mix(color, vec3(1.0,1.0,1.0),0.3);
    return color;
}
void main() {
    vec3 normal = v_normal;
    vec4 color = vec4(0.,0.,0.,1.);

color.rgb += getCaustic(v_texcoord);
    gl_FragColor = color;
}