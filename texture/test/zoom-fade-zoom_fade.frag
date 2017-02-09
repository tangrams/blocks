#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;


uniform sampler2D u_tex0; // http://tangrams.github.io/tangram-sandbox/styles/imgs/hatch_1.png


#define v_pos v_texcoord

#define u_map_position vec3(0.,0.,.5)

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

vec4 TileTexture (sampler2D tex, float scale) {
    vec2 IN = getTileCoords()*scale;
    vec2 OUT = getTileCoords()*scale*2.;
    return mix(texture2D(tex,fract(IN)), texture2D(tex,fract(OUT)), fract(u_map_position.z));
}
void main() {
    vec3 normal = vec3(0.,0.,1.);
    vec4 color = vec4(0.,0.,0.,1.);


color.rgb = vec3(1.);
color.rgb -= TileTexture(u_tex0,1.).a;


    gl_FragColor = color;
}