#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;

#define u_device_pixel_ratio (1.0)
#define u_meters_per_pixel (1.0)
#define u_map_position vec3((v_texcoord.xy-.5)*5000.,17.5)
#define TANGRAM_FRAGMENT_SHADER



varying vec2 v_texcoord;


// Repeats a coordinate space (st) in diferent tiles
// ================================
vec2 tile (vec2 st, float zoom) {
    st *= zoom;
    return fract(st);
}
void main() {
    vec3 normal = vec3(0.,0.,1.);
    vec4 color = vec4(0.,0.,0.,1.);


    color.rg += tile(v_texcoord.xy,5.);

    gl_FragColor = color;
}