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


vec2 getConstantCoords () {
    #ifdef TANGRAM_FRAGMENT_SHADER
    const float pixel_scale = 695.;
    float meter_pixels = u_meters_per_pixel / u_device_pixel_ratio;
    vec2 st = gl_FragCoord.xy/pixel_scale;
    const float dot_wrap = 1000.;
    st += mod(u_map_position.xy / meter_pixels, dot_wrap)/pixel_scale;
    return st;
    #else
    return vec2(0.0,0.0);
    #endif
}
void main() {
    vec3 normal = vec3(0.,0.,1.);
    vec4 color = vec4(0.,0.,0.,1.);


vec2 st = getConstantCoords();
color.rg += fract(st*3.);


    gl_FragColor = color;
}