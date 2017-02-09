#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;



#define TANGRAM_FRAGMENT_SHADER 1

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