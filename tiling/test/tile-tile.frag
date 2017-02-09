#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;



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