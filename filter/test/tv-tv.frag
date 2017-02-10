#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;

#define u_device_pixel_ratio (1.0)
#define u_meters_per_pixel (1.0)
#define u_map_position vec3((v_texcoord.xy-.5)*5000.,17.5)
#define TANGRAM_FRAGMENT_SHADER


uniform sampler2D u_tex0; // https://tangrams.github.io/tangram-sandbox/styles/imgs/grid-0002.jpg


#define TV_FREQ 2.7

#define TWO_PI 6.28318530718

#define TV_AMOUNT 1.0

#define HALF_PI 1.57079632679

#define EPSILON 1e-07

#define QUATER_PI 0.785398163

#define TV_SPEED 5.0

#define TV_BLEND MULTIPLY

#define ADD +

#define MULTIPLY *

#define deg2rad(d) (((d)*3.1415926535897932384626433832795)/180.0)

#define PI 3.14159265359

#define SUBTRACT -

#define rad2deg(d) (((d)*180.0)/3.1415926535897932384626433832795)

varying vec2 v_texcoord;


void main() {
    vec3 normal = vec3(0.,0.,1.);
    vec4 color = vec4(0.,0.,0.,1.);


    color = texture2D(u_tex0,v_texcoord.xy);

color = color TV_BLEND (abs(cos((gl_FragCoord.y*(TV_FREQ/u_device_pixel_ratio)+u_time*TV_SPEED)))*TV_AMOUNT);

    gl_FragColor = color;
}