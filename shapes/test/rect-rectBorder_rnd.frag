#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;


#define STROKE 0.15

varying vec4 v_position;
varying vec4 v_color;
varying vec3 v_normal;
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
// get distance field of a rectangle in the center
// ================================
float rectDF (in vec2 st, in vec2 size) {
    st = st*2.-1.;
    return length(max(abs(st)-size,.0));
}
float rectDF (in vec2 st, in float size) {
    return rectDF(st, vec2(size));
}

// Draw a round corners rectangle in the center
// ================================
float rect (in vec2 st, in vec2 size, in float radio) {
    radio = max(.000001, radio);
    return fill(radio, rectDF(st, size-radio));
}

float rect (vec2 st, float size, float radio) {
    return rect(st,vec2(size),radio);
}

// Draw a round corners rectangle border in the center
// ================================
float rectBorder (in vec2 st, in vec2 size, in float radio) {
    radio = max(.000001, radio);
    return stroke(radio, rectDF(st, size-radio));
}

float rectBorder (vec2 st, float size, float radio) {
    return rect(st,vec2(size),radio);
}

// Draw a rectangle in the center
// ================================
float rect (vec2 st, vec2 size){
    size = .25-size*.125;
    vec2 uv = step(size,st*(1.0-st));
    return (uv.x*uv.y);
}

float rect (vec2 st, float size){
    return rect(st, vec2(size));
}

void main() {
    vec3 normal = v_normal;
    vec4 color = vec4(0.,0.,0.,1.);

color.rgb += rectBorder(v_texcoord,vec2(.5),.5);
    gl_FragColor = color;
}