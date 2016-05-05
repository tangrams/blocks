![](blocks.jpg)

# Tangram Blocks

Set of reusable building blocks for Tangram to make beatifull maps. Is in esence a library of our own Tangram recipes. A simpler way to add new GSLS Shaders features into your maps.

## How to use them?

In your style add a path to it, like this:

```yaml
import:
    - http://tangrams.github.io/blocks/filter/grain.yaml
```

Then ```mix``` it with your custom styles like this:

```yaml
styles:
    buildings:
        base: polygons
        mix: [filter-grain]
```

This will add all the functions defined on that **Tangram Block** to your current custom style (in this case ```buildings```). Note that some of this modules have some values on the ````defines``` that can be tweaked. For example in the above example we can increase the detail and amount of the grain by modifying this two defines:

```yaml
styles:
    buildings:
        base: polygons
        mix: [filter-grain]
        shaders:
            defines:
                GRAIN_AMOUNT: .4
                NUM_OCTAVES: 3
```

## Blocks


### [color-conversion](https://github.com/tangrams/blocks/blob/gh-pages/color/conversion.yaml)

Set of functions to convert colors between color systems/spaces

Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./color./color/conversion.yaml
```

Provides the following blocks:

- **global**:
 + `vec3 rgb2hsb (vec3 c) `
 + `vec3 rgb2hsb (vec4 c) `
 + `vec3 hsb2rgb (vec3 c) `


### [color-palette](https://github.com/tangrams/blocks/blob/gh-pages/color/palette.yaml)

Provides the following blocks:

- **global**:
 + `vec3 palette (float t, vec3 a, vec3 b, vec3 c, vec3 d) `


### [color-tools](https://github.com/tangrams/blocks/blob/gh-pages/color/tools.yaml)

Provides the following blocks:

- **global**:
 + `float getIntensity (vec3 c) `
 + `float getIntensity (vec4 c) `
 + `float getBrightness (vec3 c) `
 + `float getBrightness (vec4 c) `


### [filter-grain](https://github.com/tangrams/blocks/blob/gh-pages/filter/grain.yaml)

Provides the following blocks:

- **filter**:

```glsl
// Apply the grain in the amount defined on GRAIN_AMOUNT
color.rgb -= grain()*GRAIN_AMOUNT;
```


- **global**:


### [filter-hatch](https://github.com/tangrams/blocks/blob/gh-pages/filter/hatch.yaml)

Provides the following blocks:

- **global**:


### [filter-height](https://github.com/tangrams/blocks/blob/gh-pages/filter/height.yaml)

Provides the following blocks:

- **color**:

```glsl
color.rgb *= min((worldPosition().z*.001 + .5),1.);```




### [filter-lut](https://github.com/tangrams/blocks/blob/gh-pages/filter/lut.yaml)

Provides the following blocks:

- **filter**:

```glsl
color = getLut(color);```


- **global**:
 + `vec4 getLut (vec3 textureColor, sampler2D lookupTable) `
 + `vec4 getLut (vec3 textureColor) `
 + `vec4 getLut (vec4 textureColor, sampler2D lookupTable) `
 + `vec4 getLut (vec4 textureColor) `


### [filter-tv](https://github.com/tangrams/blocks/blob/gh-pages/filter/tv.yaml)

Provides the following blocks:

- **filter**:

```glsl
color *= abs(cos((gl_FragCoord.y*TV_FREQ+u_time*5.)));
```




### [functions-aastep](https://github.com/tangrams/blocks/blob/gh-pages/functions/aastep.yaml)

Provides the following blocks:

- **global**:
 + `float aastep(float threshold, float value) `


### [functions-easing](https://github.com/tangrams/blocks/blob/gh-pages/functions/easing.yaml)

Provides the following blocks:

- **global**:
 + `float linear(float t) `
 + `float exponentialIn(float t) `
 + `float exponentialOut(float t) `
 + `float exponentialInOut(float t) `
 + `float sineIn(float t) `
 + `float sineOut(float t) `
 + `float sineInOut(float t) `
 + `float qinticIn(float t) `
 + `float qinticOut(float t) `
 + `float qinticInOut(float t) `
 + `float quarticIn(float t) `
 + `float quarticOut(float t) `
 + `float quarticInOut(float t) `
 + `float quadraticInOut(float t) `
 + `float quadraticIn(float t) `
 + `float quadraticOut(float t) `
 + `float cubicIn(float t) `
 + `float cubicOut(float t) `
 + `float cubicInOut(float t) `
 + `float elasticIn(float t) `
 + `float elasticOut(float t) `
 + `float elasticInOut(float t) `
 + `float circularIn(float t) `
 + `float circularOut(float t) `
 + `float circularInOut(float t) `
 + `float bounceOut(float t) `
 + `float bounceIn(float t) `
 + `float bounceInOut(float t) `
 + `float backIn(float t) `
 + `float backOut(float t) `
 + `float backInOut(float t) `


### [functions-map](https://github.com/tangrams/blocks/blob/gh-pages/functions/map.yaml)

Provides the following blocks:

- **global**:
 + `float map (in float value, in float inputMin, in float inputMax, in float outputMin, in float outputMax, bool clamp) `
 + `float map (in float value, in float inputMin, in float inputMax, in float outputMin, in float outputMax) `


### [functions-pulse](https://github.com/tangrams/blocks/blob/gh-pages/functions/pulse.yaml)

Provides the following blocks:

- **global**:
 + `float pulse (float x, float p, float w) `


### [generative-fbm](https://github.com/tangrams/blocks/blob/gh-pages/generative/fbm.yaml)

Provides the following blocks:

- **global**:
 + `float fbm (float x) `
 + `int i = 0; i < int(NUM_OCTAVES); ++i) `
 + `float fbm (vec2 xy) `
 + `int i = 0; i < int(NUM_OCTAVES); ++i) `
 + `float fbm ( in vec3 xyz) `


### [generative-noise](https://github.com/tangrams/blocks/blob/gh-pages/generative/noise.yaml)

Provides the following blocks:

- **global**:
 + `float noise (in float x) `
 + `float noise (vec2 xy) `
 + `float noise (vec3 xyz) `
 + `float snoise (vec3 p) `


### [generative-random](https://github.com/tangrams/blocks/blob/gh-pages/generative/random.yaml)

Provides the following blocks:

- **global**:
 + `float random(float x) `
 + `float random(vec2 p) `
 + `float random(vec3 p) `
 + `vec2 random2 (vec2 xy) `
 + `vec3 random3 (vec2 xy) `
 + `vec3 random3 (vec3 c) `


### [generative-voronoi](https://github.com/tangrams/blocks/blob/gh-pages/generative/voronoi.yaml)

Provides the following blocks:

- **global**:
 + `vec3 voronoi (vec2 st) `


### [geometry-dynamic-height](https://github.com/tangrams/blocks/blob/gh-pages/geometry/dynamic-height.yaml)

Provides the following blocks:

- **position**:

```glsl
float zoom = map(u_map_position.z,ZOOM_START,ZOOM_END,1.,0.);
position.z *= max(1.,.5+ZOOM_LINEAR_FACTOR*zoom);```




### [geometry-dynamic-width](https://github.com/tangrams/blocks/blob/gh-pages/geometry/dynamic-width.yaml)

Provides the following blocks:

- **width**:

```glsl
width *= 0.2+min(pow(position.z*0.006,2.),.6);```




### [geometry-matrices](https://github.com/tangrams/blocks/blob/gh-pages/geometry/matrices.yaml)

Provides the following blocks:

- **global**:
 + `mat2 rotate2D (float angle) `
 + `mat3 rotateX3D (float phi) `
 + `mat4 rotateX4D (float phi) `
 + `mat3 rotateY3D (float theta) `
 + `mat4 rotateY4D (float theta) `
 + `mat3 rotateZ3D (float psi) `
 + `mat4 rotateZ4D (float psi) `
 + `mat4 scale4D (float x, float y, float z) `
 + `mat4 translate4D (float x, float y, float z) `


### [geometry-normal](https://github.com/tangrams/blocks/blob/gh-pages/geometry/normal.yaml)

Provides the following blocks:

- **global**:
 + `bool isWall() `
 + `bool isRoof() `


### [geometry-projections](https://github.com/tangrams/blocks/blob/gh-pages/geometry/projections.yaml)

Provides the following blocks:

- **global**:
 + `float y2lat_d (float y) `
 + `float x2lon_d (float x) `
 + `float lat2y_d (float lat) `
 + `float lon2x_d (float lon) `
 + `float y2lat_m (float y) `
 + `float x2lon_m (float x) `
 + `float lat2y_m (float lat) `
 + `float lon2x_m (float lon) `
 + `vec2 latlon2albers(float lat, float lon, float lat0, float lng0, float phi1, float phi2 ) `
 + `vec2 latlon2albers (float lat, float lon, float delta_phi1, float delta_phi2) `
 + `vec2 latlon2albers (float lat, float lon, float width) `
 + `vec2 latlon2azimuthal (float lat, float lon, float phi1, float lambda0) `
 + `vec2 azimuthal(float lat, float lon) `
 + `vec2 azimuthalNorth(float lat, float lon) `
 + `vec2 azimuthalSouth(float lat, float lon) `


### [geometry-terrarium](https://github.com/tangrams/blocks/blob/gh-pages/geometry/terrarium.yaml)

Provides the following blocks:

- **position**:

```glsl
position.z += ZOFFSET*u_meters_per_pixel;
extrudeTerrain(position);```


- **global**:
 + `float getHeight() `
 + `void extrudeTerrain(inout vec4 position) `


### [geometry-tilt](https://github.com/tangrams/blocks/blob/gh-pages/geometry/tilt.yaml)

Provides the following blocks:

- **position**:

```glsl
float t = u_time*0.1; 
float z = clamp(smoothstep(TILT_IN/TILT_MAX_ZOOM, TILT_OUT/TILT_MAX_ZOOM, max(u_map_position.z/TILT_MAX_ZOOM,0.)*0.9), 0., 1.);
position.xyz = rotateX3D(z*HALF_PI) * rotateZ3D(sin(t)*PI*z) * position.xyz;```




### [lines-dots](https://github.com/tangrams/blocks/blob/gh-pages/lines/dash.yaml)

Provides the following blocks:

- **color**:

```glsl
color.a = 1.-step(dash_size,fract(v_texcoord.y*dash_scale));```




### [lines-dots](https://github.com/tangrams/blocks/blob/gh-pages/lines/dots.yaml)

Provides the following blocks:

- **color**:

```glsl
vec2 st = fract(v_texcoord.xy);
st -= .5;
color.a = 1.- step(dotSize, dot(st,st)*2.);```




### [lines-outline](https://github.com/tangrams/blocks/blob/gh-pages/lines/outline.yaml)

Provides the following blocks:

- **color**:

```glsl
color.rgb = mix(color.rgb,
                outline_color,
                (1.0-(aastep(outline_width,v_texcoord.x)-step(1.0-outline_width,v_texcoord.x))));```




### [lines-stripes](https://github.com/tangrams/blocks/blob/gh-pages/lines/stripes.yaml)

Provides the following blocks:

- **color**:

```glsl
vec2 st = fract(v_texcoord);
color.rgb += step(.1,sin((st.x+st.y)*6.283))*.1;```




### [patterns-dots](https://github.com/tangrams/blocks/blob/gh-pages/patterns/dots.yaml)

Provides the following blocks:

- **global**:
 + `float TileDots(float scale, float size) `


### [patterns-grid](https://github.com/tangrams/blocks/blob/gh-pages/patterns/grid.yaml)

Provides the following blocks:

- **global**:


### [patterns-stripes](https://github.com/tangrams/blocks/blob/gh-pages/patterns/stripes.yaml)

Provides the following blocks:

- **global**:
 + `float stripesDF (vec2 st) `
 + `float stripes (vec2 st, float width) `
 + `float diagonalStripes (vec2 st) `


### [patterns-waves](https://github.com/tangrams/blocks/blob/gh-pages/patterns/waves.yaml)

Provides the following blocks:

- **global**:
 + `float wavesDF (vec2 st, float freq, float amp) `
 + `float waves (vec2 st, float freq, float amp, float width) `


### [patterns-zigzag](https://github.com/tangrams/blocks/blob/gh-pages/patterns/zigzag.yaml)

Provides the following blocks:

- **global**:
 + `float zigzagDF (vec2 st, float freq) `
 + `float zigzag (vec2 st, float freq, float width) `


### [shapes-circle](https://github.com/tangrams/blocks/blob/gh-pages/shapes/circle.yaml)

Provides the following blocks:

- **global**:
 + `float circleDF (vec2 st) `
 + `float circle (vec2 st, float radius) `


### [shapes-cross](https://github.com/tangrams/blocks/blob/gh-pages/shapes/cross.yaml)

Provides the following blocks:

- **global**:
 + `float cross (vec2 st, float size, float width) `


### [shapes-digits](https://github.com/tangrams/blocks/blob/gh-pages/shapes/digits.yaml)

Provides the following blocks:

- **global**:
 + `float SampleDigit(const in float fDigit, const in vec2 vUV) `
 + `float PrintValue(const in vec2 vStringCharCoords, const in float fValue, const in float fMaxDigits, const in float fDecimalPlaces) `


### [shapes-polygons](https://github.com/tangrams/blocks/blob/gh-pages/shapes/polygons.yaml)

Provides the following blocks:

- **global**:
 + `float shapeDF (vec2 st, int N) `
 + `float shape (vec2 st, int N, float width) `


### [shapes-rect](https://github.com/tangrams/blocks/blob/gh-pages/shapes/rect.yaml)

Provides the following blocks:

- **global**:
 + `float rectDF(vec2 st, vec2 size) `
 + `float rectDF(vec2 st, float size) `
 + `float rect(vec2 st, vec2 size, float radio) `
 + `float rect(vec2 st, float size, float radio) `


### [shapes-simplex](https://github.com/tangrams/blocks/blob/gh-pages/shapes/simplex.yaml)

Provides the following blocks:

- **global**:
 + `float warp (vec3 S) `
 + `float circle (vec3 S) `
 + `float triangle (vec3 S) `
 + `vec3 star (vec3 S) `
 + `vec3 sakura (vec3 S) `
 + `float lotus (vec3 S, float petals_size, float roundness) `


### [space-constant](https://github.com/tangrams/blocks/blob/gh-pages/space/constant.yaml)

Provides the following blocks:

- **global**:
 + `vec2 getConstantCoords () `


### [space-screen](https://github.com/tangrams/blocks/blob/gh-pages/space/screen.yaml)

Provides the following blocks:

- **global**:
 + `vec2 getScreenCoords () `
 + `vec2 getScreenNonStretchCoords () `


### [space-tex](https://github.com/tangrams/blocks/blob/gh-pages/space/tex.yaml)

Provides the following blocks:

- **global**:
 + `vec2 getTexCoords () `


### [space-tile](https://github.com/tangrams/blocks/blob/gh-pages/space/tile.yaml)

Provides the following blocks:

- **position**:

```glsl
// Normalize the attribute position of a vertex
v_pos = modelPosition().xyz;```


- **global**:
 + `vec2 getTileCoords() `


### [space-uz](https://github.com/tangrams/blocks/blob/gh-pages/space/uz.yaml)

Provides the following blocks:

- **global**:
 + `vec2 getUZCoords () `


### [texture-non-repetitive](https://github.com/tangrams/blocks/blob/gh-pages/texture/non-repetitive.yaml)

Provides the following blocks:

- **global**:
 + `vec4 NonRepetitiveTexture(sampler2D tex, vec2 x, float v) `


### [texture-zoom-fade](https://github.com/tangrams/blocks/blob/gh-pages/texture/zoom-fade.yaml)

Provides the following blocks:

- **global**:
 + `vec4 TileTexture (sampler2D tex, float scale) `


### [tiling-brick](https://github.com/tangrams/blocks/blob/gh-pages/tiling/brick.yaml)

Provides the following blocks:

- **global**:
 + `vec2 brick (vec2 st, float zoom) `


### [tiling-simplex](https://github.com/tangrams/blocks/blob/gh-pages/tiling/simplex.yaml)

Provides the following blocks:

- **global**:
 + `vec2 simplex (vec2 st) `
 + `vec2 unsimplex (vec2 st) `
 + `vec3 simplexGrid (vec2 st) `
 + `vec3 simplexRotatedGrid (vec2 st) `


### [tiling-tile](https://github.com/tangrams/blocks/blob/gh-pages/tiling/tile.yaml)

Provides the following blocks:

- **global**:
 + `vec2 tile (vec2 st, float zoom) `


### [tiling-truchet](https://github.com/tangrams/blocks/blob/gh-pages/tiling/truchet.yaml)

Provides the following blocks:

- **global**:
 + `vec2 truchetMirror (vec2 st) `
 + `vec2 truchetRotate (vec2 st) `

## License
### The MIT License (MIT)

*Copyright (c) 2016 [Mapzen](http://mapzen.com/)*

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
