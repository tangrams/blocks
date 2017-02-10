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


#ifdef TANGRAM_FRAGMENT_SHADER
vec2 getScreenCoords () {
    return gl_FragCoord.xy / u_resolution.xy;
}

vec2 getScreenNonStretchCoords () {
    vec2 st = getScreenCoords();
    if (u_resolution.y > u_resolution.x ) {
        st.y *= u_resolution.y/u_resolution.x;
        st.y -= (u_resolution.y*.5-u_resolution.x*.5)/u_resolution.x;
    } else {
        st.x *= u_resolution.x/u_resolution.y;
        st.x -= (u_resolution.x*.5-u_resolution.y*.5)/u_resolution.y;
    } 
    return st;
}
#endif
void main() {
    vec3 normal = vec3(0.,0.,1.);
    vec4 color = vec4(0.,0.,0.,1.);


vec2 st = getScreenCoords();
color.rg += fract(st*3.);


    gl_FragColor = color;
}