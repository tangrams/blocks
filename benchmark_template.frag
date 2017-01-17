#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;

#pragma tangram: uniforms
#pragma tangram: defines

varying vec4 v_position;
varying vec4 v_color;
varying vec3 v_normal;
varying vec2 v_texcoord;

#pragma tangram: global

void main() {
    vec3 normal = v_normal;
    vec4 color = vec4(0.,0.,0.,1.);

#pragma tangram: normal
#pragma tangram: color

    gl_FragColor = color;
}