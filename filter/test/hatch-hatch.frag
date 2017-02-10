#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;

#define u_device_pixel_ratio (1.0)
#define u_meters_per_pixel (1.0)
#define u_map_position vec3((v_texcoord.xy-.5)*5000.,17.5)
#define TANGRAM_FRAGMENT_SHADER


uniform sampler2D u_hatchmap; // https://tangrams.github.io/blocks/filter/imgs/hatch.png

uniform sampler2D u_tex0; // https://tangrams.github.io/blocks/test.jpg


varying vec2 v_texcoord;


float getHatch (vec2 st, float brightness) {
    st  = fract(st)/3.;
    brightness = clamp(brightness,0.,0.9999999);
    vec2 pos1 = vec2(floor(brightness*9.0)/3.,
                     floor(brightness*3.0)/3.) + st;
    float minBrightness = clamp(brightness-0.111111111,0.,1.0);
    vec2 pos2 = vec2(floor(minBrightness*9.0)/3.,
                     floor(minBrightness*3.0)/3.)+st;
    return mix(texture2D(u_hatchmap, fract(pos1) ).a,
               texture2D(u_hatchmap, fract(pos2) ).a,
               1.0-fract(brightness*9.0));
}
void main() {
    vec3 normal = vec3(0.,0.,1.);
    vec4 color = vec4(0.,0.,0.,1.);


float brightness = texture2D(u_tex0,v_texcoord.xy).r;
color.rgb = vec3(1.);
color.rgb -= getHatch(v_texcoord.xy*10., brightness);


    gl_FragColor = color;
}