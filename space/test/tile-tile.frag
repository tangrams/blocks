#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;

#define u_device_pixel_ratio (1.0)
#define u_meters_per_pixel (1.0)
#define u_map_position vec3((v_texcoord.xy-.5)*5000.,17.5)
#define TANGRAM_FRAGMENT_SHADER



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