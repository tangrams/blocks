#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;



#define TWO_PI 6.28318530718

#define HALF_PI 1.57079632679

#define EPSILON 1e-07

#define QUATER_PI 0.785398163

#define STROKE 0.15

#define ADD +

#define MULTIPLY *

#define deg2rad(d) (((d)*3.1415926535897932384626433832795)/180.0)

#define PI 3.14159265359

#define SUBTRACT -

#define rad2deg(d) (((d)*180.0)/3.1415926535897932384626433832795)

varying vec2 v_texcoord;


// AntiAliased Step function
//=============================
float aastep(float threshold, float value) {
    #ifdef TANGRAM_FRAGMENT_SHADER
        #ifdef TANGRAM_EXTENSION_OES_standard_derivatives
            float afwidth = length(vec2(dFdx(value), dFdy(value))) * 0.70710678118654757;
            return smoothstep(threshold-afwidth, threshold+afwidth, value);
        #else
            return step(threshold, value);
        #endif  
    #else
        return step(threshold, value);
    #endif
}
float fill (in float size, in float x) {
    return 1.-aastep(size, x);
}

float stroke (in float size, in float x) {
    return aastep(size, x+STROKE) - aastep(size, x);
}
// get distance field of a polygon in the center
// where N is the number of sides of it
// ================================
float shapeDF (vec2 st, int N) {
    st = st *2.-1.;
    float a = atan(st.x,st.y)+PI;
    float r = TWO_PI/float(N);
    return cos(floor(.5+a/r)*r-a)*length(st);
}

// draw a polygon in the center
// where N is the number of sides of it
// ================================
float shape (vec2 st, int N, float width) {
    return fill(width, shapeDF(st,N));
}

// draw a polygon border in the center
// where N is the number of sides of it
// ================================
float shapeBorder (vec2 st, int N, float width) {
    return stroke(width, shapeDF(st,N));
}
void main() {
    vec3 normal = vec3(0.,0.,1.);
    vec4 color = vec4(0.,0.,0.,1.);


    color.rgb += shapeBorder(v_texcoord.xy,5,.5);

    gl_FragColor = color;
}