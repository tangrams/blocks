#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;

#define u_device_pixel_ratio (1.0)
#define u_meters_per_pixel (1.0)
#define u_map_position vec3((v_texcoord.xy-.5)*5000.,17.5)
#define TANGRAM_FRAGMENT_SHADER


uniform sampler2D u_tex0; // https://tangrams.github.io/blocks/test.jpg


#define GRID_AMOUNT 0.2

#define TWO_PI 6.28318530718

#define HALF_PI 1.57079632679

#define EPSILON 1e-07

#define QUATER_PI 0.785398163

#define GRID_BLEND ADD

#define v_pos v_texcoord

#define ADD +

#define MULTIPLY *

#define deg2rad(d) (((d)*3.1415926535897932384626433832795)/180.0)

#define PI 3.14159265359

#define SUBTRACT -

#define rad2deg(d) (((d)*180.0)/3.1415926535897932384626433832795)

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

// Draw a grid in the space a specific resolution and pressition
bool grid (vec2 st, float res, float press) {
    vec2 grid = fract(st*res);
    return grid.x < res*press || grid.y < res*press;
}
//
// Draw a grid in the space a specific resolution
bool grid (vec2 st, float res) {
    return grid(st, res, 1.0);
}

//
// Draw a grid in 45 degress with a specific width
float diagonalGrid(vec2 st, float width){
    return step(.5,max( smoothstep(st.x-width,st.x,st.y)*(1.-smoothstep(st.x,st.x+width,st.y)),
                        smoothstep(st.x-width,st.x,1.0-st.y)*(1.-smoothstep(st.x,st.x+width,1.0-st.y))));
}

// Draw a grid using tile coordenates in a specific resolution
float tileGrid (float res) {
    vec2 st = getTileCoords()*100.*res;
    float pct = 0.0;
    float press = 0.4+(1.0-fract(u_map_position.z))*0.1;
    if (grid(st,0.01,press)) pct += 0.5;
    if (grid(st,0.1,press)) pct += 0.1;
    return pct;
}

// Draw two grid that smoothly interpolates acording to zooms
float tileGrid() { 
    return mix(tileGrid(1.),tileGrid(2.),fract(u_map_position.z)); 
}
void main() {
    vec3 normal = vec3(0.,0.,1.);
    vec4 color = vec4(0.,0.,0.,1.);


    color = texture2D(u_tex0,v_texcoord.xy);

color.rgb = color.rgb GRID_BLEND (tileGrid()*GRID_AMOUNT);

    gl_FragColor = color;
}