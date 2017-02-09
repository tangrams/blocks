#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;



#define v_pos v_texcoord

varying vec2 v_texcoord;


// Variant to be add to both vertex and fragments shaders
#ifndef v_pos
varying vec3 v_pos;
#endif

//
// Get the coordinates in tile space
// ================================
vec2 getTileCoords() {
    return fract(v_pos.xy);
}

void main() {
    vec3 normal = vec3(0.,0.,1.);
    vec4 color = vec4(0.,0.,0.,1.);


vec2 st = getTileCoords();
color.rg += fract(st*3.);


    gl_FragColor = color;
}