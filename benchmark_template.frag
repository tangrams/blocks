#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;

#pragma tangram: uniforms

#pragma tangram: camera
#pragma tangram: material
#pragma tangram: lighting
#pragma tangram: raster
#pragma tangram: defines

varying vec2 v_texcoord;

#pragma tangram: global

void main() {
    vec3 normal = vec3(0.,0.,1.);
    vec4 color = vec4(0.,0.,0.,1.);

#pragma tangram: normal

#pragma tangram: color

#pragma tangram: filter

    gl_FragColor = color;
}