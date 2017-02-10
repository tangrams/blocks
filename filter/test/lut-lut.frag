#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;

#define u_device_pixel_ratio (1.0)
#define u_meters_per_pixel (1.0)
#define u_map_position vec3((v_texcoord.xy-.5)*5000.,17.5)
#define TANGRAM_FRAGMENT_SHADER


uniform sampler2D u_lut; // https://tangrams.github.io/blocks/filter/imgs/lut-0001.png

uniform sampler2D u_tex0; // https://tangrams.github.io/blocks/test.jpg


#define LUT_AMOUNT 0.5

varying vec2 v_texcoord;


// Apply Look up table on a color
// The user need to provide a valid url to the uniform "u_lut"
// ================================
vec3 getLut (vec3 textureColor, sampler2D lookupTable) {
    textureColor.g = 1.-textureColor.g;
    textureColor = clamp(textureColor, 0.0, 1.0);
    float blueColor = textureColor.b * 63.0;
    vec2 quad1 = vec2(0.0);
    quad1.y = floor(floor(blueColor) / 8.0);
    quad1.x = floor(blueColor) - (quad1.y * 8.0);
    vec2 quad2 = vec2(0.0);
    quad2.y = floor(ceil(blueColor) / 8.0);
    quad2.x = ceil(blueColor) - (quad2.y * 8.0);
    vec2 texPos1 = vec2(0.0);
    texPos1.x = (quad1.x * 0.125) + 0.5/512.0 + ((0.125 - 1.0/512.0) * textureColor.r);
    texPos1.y = (quad1.y * 0.125) + 0.5/512.0 + ((0.125 - 1.0/512.0) * textureColor.g);
    vec2 texPos2 = vec2(0.0);
    texPos2.x = (quad2.x * 0.125) + 0.5/512.0 + ((0.125 - 1.0/512.0) * textureColor.r);
    texPos2.y = (quad2.y * 0.125) + 0.5/512.0 + ((0.125 - 1.0/512.0) * textureColor.g);
    vec3 newColor1 = texture2D(lookupTable, texPos1).rgb;
    vec3 newColor2 = texture2D(lookupTable, texPos2).rgb;
    vec3 newColor = mix(newColor1, newColor2, fract(blueColor));
    return newColor;
}
//
vec3 getLut (vec3 textureColor) {
    return getLut(textureColor, u_lut);
}

void main() {
    vec3 normal = vec3(0.,0.,1.);
    vec4 color = vec4(0.,0.,0.,1.);


    color = texture2D(u_tex0,v_texcoord.xy);

color.rgb = mix(color.rgb,
                getLut(color.rgb),
                LUT_AMOUNT);
    gl_FragColor = color;
}