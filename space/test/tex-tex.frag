#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;



varying vec2 v_texcoord;


vec2 getTexCoords () {
    return v_texcoord.xy;
}
void main() {
    vec3 normal = vec3(0.,0.,1.);
    vec4 color = vec4(0.,0.,0.,1.);


vec2 st = getTexCoords();
color.rg += fract(st*3.);


    gl_FragColor = color;
}