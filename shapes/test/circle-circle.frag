#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;



#define STROKE 0.15

varying vec2 v_texcoord;


// AntiAliased Step function
//=============================
float aastep(float threshold, float value) {
    #ifdef TANGRAM_FRAGMENT_SHADER
        #ifdef TANGRAM_EXTENSION_OES_standard_derivatives
            float afwidth = length(vec2(dFdx(value), dFdy(value))) * 0.70710678118654757;
            return smoothstep(threshold-afwidth, threshold+afwidth, value);
        #else
            return step(threshold, value);
        #endif  
    #else
        return step(threshold, value);
    #endif
}
float fill (in float size, in float x) {
    return 1.-aastep(size, x);
}

float stroke (in float size, in float x) {
    return aastep(size, x+STROKE) - aastep(size, x);
}
// get distance field of a Circle
// ================================
float circleDF (vec2 st) {
    return dot(st,st)*3.03;
}
//
// Draw a circle in the middle of the ST space
// ================================
float circle (vec2 st, float radius) {
    return fill(radius, circleDF(st-vec2(0.5)));
}

//
// Draw a circle in the middle of the ST space
// ================================
float circleBorder (vec2 st, float radius) {
    return stroke(radius, circleDF(st-vec2(0.5)));
}
void main() {
    vec3 normal = vec3(0.,0.,1.);
    vec4 color = vec4(0.,0.,0.,1.);


    color.rgb += circle(v_texcoord.xy,.5);

    gl_FragColor = color;
}