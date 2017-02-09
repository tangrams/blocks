#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;



varying vec2 v_texcoord;


vec2 brick (vec2 st, float zoom) {
    st *= zoom;
    // Here is where the offset is happening
    st.x += step(1., mod(st.y,2.0)) * 0.5;
    return fract(st);
}
void main() {
    vec3 normal = vec3(0.,0.,1.);
    vec4 color = vec4(0.,0.,0.,1.);


    color.rg += brick(v_texcoord.xy,5.);

    gl_FragColor = color;
}