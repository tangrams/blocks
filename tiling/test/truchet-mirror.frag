#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;

#define u_device_pixel_ratio (1.0)
#define u_meters_per_pixel (1.0)
#define u_map_position vec3((v_texcoord.xy-.5)*5000.,17.5)
#define TANGRAM_FRAGMENT_SHADER



#define TWO_PI 6.28318530718

#define HALF_PI 1.57079632679

#define EPSILON 1e-07

#define QUATER_PI 0.785398163

#define ADD +

#define MULTIPLY *

#define deg2rad(d) (((d)*3.1415926535897932384626433832795)/180.0)

#define PI 3.14159265359

#define SUBTRACT -

#define rad2deg(d) (((d)*180.0)/3.1415926535897932384626433832795)

varying vec2 v_texcoord;


// Rotate in 2, 3 and 4 dimensions
// ================================
mat2 rotate2D (float angle) {
    return mat2(cos(angle),-sin(angle),
                sin(angle),cos(angle));
}
vec2 rotate2D (vec2 st, float a) {
    return (rotate2D(a)*(st-.5))+.5;
}
mat3 rotateX3D (float phi) {
    return mat3(
        vec3(1.,0.,0.),
        vec3(0.,cos(phi),-sin(phi)),
        vec3(0.,sin(phi),cos(phi)));
}
mat4 rotateX4D (float phi) {
    return mat4(
        vec4(1.,0.,0.,0),
        vec4(0.,cos(phi),-sin(phi),0.),
        vec4(0.,sin(phi),cos(phi),0.),
        vec4(0.,0.,0.,1.));
}
mat3 rotateY3D (float theta) {
    return mat3(
        vec3(cos(theta),0.,-sin(theta)),
        vec3(0.,1.,0.),
        vec3(sin(theta),0.,cos(theta)));
}
mat4 rotateY4D (float theta) {
    return mat4(
        vec4(cos(theta),0.,-sin(theta),0),
        vec4(0.,1.,0.,0.),
        vec4(sin(theta),0.,cos(theta),0.),
        vec4(0.,0.,0.,1.));
}
mat3 rotateZ3D (float psi) {
    return mat3(
        vec3(cos(psi),-sin(psi),0.),
        vec3(sin(psi),cos(psi),0.),
        vec3(0.,0.,1.));
}
mat4 rotateZ4D (float psi) {
    return mat4(
        vec4(cos(psi),-sin(psi),0.,0),
        vec4(sin(psi),cos(psi),0.,0.),
        vec4(0.,0.,1.,0.),
        vec4(0.,0.,0.,1.));
}
//
// Scale 4 dimensions
// ================================
mat4 scale4D (float x, float y, float z) {
    return mat4(
        vec4(x,   0.0, 0.0, 0.0),
        vec4(0.0, y,   0.0, 0.0),
        vec4(0.0, 0.0, z,   0.0),
        vec4(0.0, 0.0, 0.0, 1.0)
    );
}
//
// Translate in 4 dimensions
mat4 translate4D (float x, float y, float z) {
    return mat4(
        vec4(1.0, 0.0, 0.0, 0.0),
        vec4(0.0, 1.0, 0.0, 0.0),
        vec4(0.0, 0.0, 1.0, 0.0),
        vec4(x,   y,   z,   1.0)
    );
}

// Truchet Patern reference
// ================================
//
//        |
//    0   |   1
//        |
//  --------------
//        |
//    2   |   3
//        |
//

// A- Mirror tiles acording to a Truchet patern
// ================================
vec2 truchetMirror (vec2 st) {
    // Shapes mirror pattern
    vec2 f_st = fract(st*2.);
    vec2 i_st = floor(st*2.);
    // non-even row + non-even col 
    float index = 0.0;
    index += mod(i_st.x,2.0);
    index += mod(i_st.y,2.0)*2.;
    // rotate acording
    if(index == 1.0){
        f_st.x = 1.-f_st.x;
    } else if(index == 2.0){
        f_st.y = 1.-f_st.y;
    } else if(index == 3.0){
        f_st.x = 1.-f_st.x;
        f_st.y = 1.-f_st.y;
    }
    return f_st;
}
//
// B- Rotate tiles acording to a Truchet patern
// ================================
vec2 truchetRotate (vec2 st) {
    //  Scale the coordinate system by 2x2 
    st *= 2.0;
    //
    //  Give each cell an index number
    //  according to its position
    float index = 0.0;
    index += step(1., mod(st.x,2.0));
    index += step(1., mod(st.y,2.0))*2.0;
    //
    // Make each cell between 0.0 - 1.0
    st = fract(st);
    //
    // Rotate each cell according to the index
    if(index == 1.0){
        //  Rotate cell 1 by 90 degrees
        st = rotate2D(st,PI*0.5);
    } else if(index == 2.0){
        //  Rotate cell 2 by -90 degrees
        st = rotate2D(st,PI*-0.5);
    } else if(index == 3.0){
        //  Rotate cell 3 by 180 degrees
        st = rotate2D(st,PI);
    }
    //
    return st;
}
void main() {
    vec3 normal = vec3(0.,0.,1.);
    vec4 color = vec4(0.,0.,0.,1.);


    color.rg += truchetMirror(v_texcoord.xy);

    gl_FragColor = color;
}