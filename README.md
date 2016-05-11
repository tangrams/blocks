# Tangram Blocks

Set of reusable building blocks for Tangram to make beatifull maps. Is in esence a library of our own Tangram recipes. A simpler way to add new GSLS Shaders features into your maps.

![](blocks.jpg)

## How to use them?
<hr>

In your style add a path to it, like this:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/grain.yaml
```

Then ```mix``` it with your custom styles like this:

```yaml
styles:
    buildings:
        base: polygons
        mix: [filter-grain]
```

This will add all the functions defined on that **Tangram Block** to your current custom style (in this case ```buildings```). Note that some of this modules have some values on the ```defines``` that can be tweaked. For example in the above example we can increase the detail and amount of the grain by modifying this two defines:

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

## Blocks Index
<hr>
- [Shapes](https://github.com/tangrams/blocks/tree/gh-pages/shapes)
  - [Shapes-Digits](https://github.com/tangrams/blocks/tree/gh-pages/shapes/digits.yaml)

  - [Shapes-Simplex](https://github.com/tangrams/blocks/tree/gh-pages/shapes/simplex.yaml)

  - [Shapes-Cross](https://github.com/tangrams/blocks/tree/gh-pages/shapes/cross.yaml)

  - [Shapes-Rect](https://github.com/tangrams/blocks/tree/gh-pages/shapes/rect.yaml)

  - [Shapes-Polygons](https://github.com/tangrams/blocks/tree/gh-pages/shapes/polygons.yaml)

- [Functions](https://github.com/tangrams/blocks/tree/gh-pages/functions)
  - [Functions-Easing](https://github.com/tangrams/blocks/tree/gh-pages/functions/easing.yaml)

  - [Functions-Pulse](https://github.com/tangrams/blocks/tree/gh-pages/functions/pulse.yaml)

  - [Functions-Map](https://github.com/tangrams/blocks/tree/gh-pages/functions/map.yaml)

- [Patterns](https://github.com/tangrams/blocks/tree/gh-pages/patterns)
  - [Patterns-Grid](https://github.com/tangrams/blocks/tree/gh-pages/patterns/grid.yaml)

  - [Patterns-Stripes](https://github.com/tangrams/blocks/tree/gh-pages/patterns/stripes.yaml)

  - [Patterns-Zigzag](https://github.com/tangrams/blocks/tree/gh-pages/patterns/zigzag.yaml)

  - [Patterns-Waves](https://github.com/tangrams/blocks/tree/gh-pages/patterns/waves.yaml)

- [Color](https://github.com/tangrams/blocks/tree/gh-pages/color)
  - [Color-Palette](https://github.com/tangrams/blocks/tree/gh-pages/color/palette.yaml)

  - [Color-Tools](https://github.com/tangrams/blocks/tree/gh-pages/color/tools.yaml)

- [Space](https://github.com/tangrams/blocks/tree/gh-pages/space)
  - [Space-Tex](https://github.com/tangrams/blocks/tree/gh-pages/space/tex.yaml)

  - [Space-Tile](https://github.com/tangrams/blocks/tree/gh-pages/space/tile.yaml)

  - [Space-Screen](https://github.com/tangrams/blocks/tree/gh-pages/space/screen.yaml)

  - [Space-Uz](https://github.com/tangrams/blocks/tree/gh-pages/space/uz.yaml)

- [Lines](https://github.com/tangrams/blocks/tree/gh-pages/lines)
  - [Lines-Dash](https://github.com/tangrams/blocks/tree/gh-pages/lines/dash.yaml)

  - [Lines-Dots](https://github.com/tangrams/blocks/tree/gh-pages/lines/dots.yaml)

  - [Lines-Outline](https://github.com/tangrams/blocks/tree/gh-pages/lines/outline.yaml)

  - [Lines-Stripes](https://github.com/tangrams/blocks/tree/gh-pages/lines/stripes.yaml)

- [Texture](https://github.com/tangrams/blocks/tree/gh-pages/texture)
  - [Texture-Zoom-Fade](https://github.com/tangrams/blocks/tree/gh-pages/texture/zoom-fade.yaml)

- [Filter](https://github.com/tangrams/blocks/tree/gh-pages/filter)
  - [Filter-Tv](https://github.com/tangrams/blocks/tree/gh-pages/filter/tv.yaml)

  - [Filter-Height](https://github.com/tangrams/blocks/tree/gh-pages/filter/height.yaml)

  - [Filter-Lut](https://github.com/tangrams/blocks/tree/gh-pages/filter/lut.yaml)

  - [Filter-Hatch](https://github.com/tangrams/blocks/tree/gh-pages/filter/hatch.yaml)

- [Geometry](https://github.com/tangrams/blocks/tree/gh-pages/geometry)
  - [Geometry-Normal](https://github.com/tangrams/blocks/tree/gh-pages/geometry/normal.yaml)

  - [Geometry-Tilt](https://github.com/tangrams/blocks/tree/gh-pages/geometry/tilt.yaml)

  - [Geometry-Terrarium](https://github.com/tangrams/blocks/tree/gh-pages/geometry/terrarium.yaml)

  - [Geometry-Projections](https://github.com/tangrams/blocks/tree/gh-pages/geometry/projections.yaml)

  - [Geometry-Matrices](https://github.com/tangrams/blocks/tree/gh-pages/geometry/matrices.yaml)

  - [Geometry-Dynamic-Width](https://github.com/tangrams/blocks/tree/gh-pages/geometry/dynamic-width.yaml)

- [Points](https://github.com/tangrams/blocks/tree/gh-pages/points)
  - [Points-Shape](https://github.com/tangrams/blocks/tree/gh-pages/points/shape.yaml)

- [Generative](https://github.com/tangrams/blocks/tree/gh-pages/generative)
  - [Generative-Random](https://github.com/tangrams/blocks/tree/gh-pages/generative/random.yaml)

  - [Generative-Voronoi](https://github.com/tangrams/blocks/tree/gh-pages/generative/voronoi.yaml)

  - [Generative-Noise](https://github.com/tangrams/blocks/tree/gh-pages/generative/noise.yaml)

- [Tiling](https://github.com/tangrams/blocks/tree/gh-pages/tiling)
  - [Tiling-Tile](https://github.com/tangrams/blocks/tree/gh-pages/tiling/tile.yaml)

  - [Tiling-Truchet](https://github.com/tangrams/blocks/tree/gh-pages/tiling/truchet.yaml)

  - [Tiling-Simplex](https://github.com/tangrams/blocks/tree/gh-pages/tiling/simplex.yaml)


## Blocks description

<hr>


### [COLOR](https://github.com/tangrams/blocks/tree/gh-pages/color)

#### [color-conversion](https://github.com/tangrams/blocks/blob/gh-pages/color/conversion.yaml)

Set of functions to convert colors between color systems/spaces.
For more information on this theme read [this chapter of The Book of Shaders about color](http://thebookofshaders.com/06/).

This provides the following blocks:

- **global**:
 + `vec3 rgb2hsb (vec3 c) `
 + `vec3 rgb2hsb (vec4 c) `
 + `vec3 hsb2rgb (vec3 c) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/color/conversion.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/color/conversion-full.yaml
```




#### [color-palette](https://github.com/tangrams/blocks/blob/gh-pages/color/palette.yaml)

Procedural generation of color paletters implemented by [Inigo Quiles](https://twitter.com/iquilezles) (1999) explained in [this article](http://www.iquilezles.org/www/articles/palettes/palettes.htm)

This provides the following blocks:

- **global**:
 + `vec3 palette (float t, vec3 a, vec3 b, vec3 c, vec3 d) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/color/palette.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/color/palette-full.yaml
```




#### [color-tools](https://github.com/tangrams/blocks/blob/gh-pages/color/tools.yaml)

Set of color tools to get the **intensity** and **brightness** of a color.
For more information on this theme read [this chapter of The Book of Shaders about color](http://thebookofshaders.com/06/).

This provides the following blocks:

- **global**:
 + `float getIntensity (vec3 c) `
 + `float getIntensity (vec4 c) `
 + `float getBrightness (vec3 c) `
 + `float getBrightness (vec4 c) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/color/tools.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/color/tools-full.yaml
```



<hr>


### [FILTER](https://github.com/tangrams/blocks/tree/gh-pages/filter)

#### [filter-grain](https://github.com/tangrams/blocks/blob/gh-pages/filter/grain.yaml)

Apply a lens grain effect to the scene.
<p>The amount can be set by the GRAIN_AMOUNT define [0.0~1.0]</p>
<p>For example:</p>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/grain.yaml"><div style="background-image: url(http://tangrams.github.io/tangram-sandbox/styles/grain.png); width: 100%; height: 100px; background-position: center center;"></div></a>

This provides the following blocks:

- **filter**:

```glsl
// Apply the grain in the amount defined on GRAIN_AMOUNT
color.rgb -= grain()*GRAIN_AMOUNT;

```


- **global**:
 + `float grain () `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **GRAIN_AMOUNT**: ```0.3```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/grain.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/grain-full.yaml
```




#### [filter-hatch](https://github.com/tangrams/blocks/blob/gh-pages/filter/hatch.yaml)

Hatching filter based on [Jaume's Sanchez](https://twitter.com/thespite?lang=en) [Cross-hatching GLSL shader](https://www.clicktorelease.com/code/cross-hatching/). 
<p>Examples:</p>
[ <div style="background-image: url(http://tangrams.github.io/tangram-sandbox/styles/crosshatch.png); width: 100%; height: 100px; background-position: center center;"></div> ](https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/crosshatch.yaml)
[ <div style="background-image: url(http://tangrams.github.io/tangram-sandbox/styles/pericoli.png); width: 100%; height: 100px; background-position: center center;"></div> ](https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/pericoli.yaml)

This provides the following blocks:

- **global**:
 + `float getHatch (vec2 st, float brightness) `

This block use the following **uniforms** with the following defaults. Remember you can use or tweak.
 - **u_hatchmap**: ```imgs/hatch.png```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/hatch.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/hatch-full.yaml
```




#### [filter-height](https://github.com/tangrams/blocks/blob/gh-pages/filter/height.yaml)

Adds a dark gradiant to the geometries conform they aproach to height 0. <p>For example:</p>
[ <div style="background-image: url(http://tangrams.github.io/tangram-sandbox/styles/default.png); width: 100%; height: 100px; background-position: center center;"></div> ](https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/default.yaml)

This provides the following blocks:

- **color**:

```glsl
color.rgb *= min((worldPosition().z*.001 + .5),1.);
```



Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/height.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/height-full.yaml
```




#### [filter-lut](https://github.com/tangrams/blocks/blob/gh-pages/filter/lut.yaml)

Add a look up table filter defined on the uniform ```u_lut``` to the current style. This look up tables are hable to produce similar effect to instagram filters. <p>For example:</p>
[ <div style="background-image: url(http://tangrams.github.io/tangram-sandbox/styles/sandbox-lut.png); width: 100%; height: 100px; background-position: center center;"></div> ](https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/sandbox-lut.yaml)

This provides the following blocks:

- **filter**:

```glsl
color = getLut(color);
```


- **global**:
 + `vec4 getLut (vec3 textureColor, sampler2D lookupTable) `
 + `vec4 getLut (vec3 textureColor) `
 + `vec4 getLut (vec4 textureColor, sampler2D lookupTable) `
 + `vec4 getLut (vec4 textureColor) `

This block use the following **uniforms** with the following defaults. Remember you can use or tweak.
 - **u_lut**: ```imgs/lut-0001.png```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/lut.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/lut-full.yaml
```




#### [filter-tv](https://github.com/tangrams/blocks/blob/gh-pages/filter/tv.yaml)

<p>Apply a TV effect to the style like</p>
[ <div style="background-image: url(http://tangrams.github.io/tangram-sandbox/styles/9845C.png); width: 100%; height: 100px; background-position: center center;"></div> ](https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/9845C.yaml)

This provides the following blocks:

- **filter**:

```glsl
color *= abs(cos((gl_FragCoord.y*TV_FREQ+u_time*5.)));

```



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **TV_FREQ**: ```1.2```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/tv.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/tv-full.yaml
```



<hr>


### [FUNCTIONS](https://github.com/tangrams/blocks/tree/gh-pages/functions)

#### [functions-aastep](https://github.com/tangrams/blocks/blob/gh-pages/functions/aastep.yaml)

AnitAliased ```step()``` function implemented by [Matt DesLauriers](https://twitter.com/mattdesl) in this module <https://github.com/stackgl/glsl-aastep>

This provides the following blocks:

- **global**:
 + `float aastep(float threshold, float value) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/aastep.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/aastep-full.yaml
```




#### [functions-easing](https://github.com/tangrams/blocks/blob/gh-pages/functions/easing.yaml)

Easing functions originally develop by Robert Penner's and transformed to GLSL by [StackGL](http://stack.gl/) in this repo: <https://github.com/stackgl/glsl-easings>

This provides the following blocks:

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

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **HALF_PI**: ```1.57079632679```
 - **PI**: ```3.14159265359```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/easing.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/easing-full.yaml
```




#### [functions-map](https://github.com/tangrams/blocks/blob/gh-pages/functions/map.yaml)

This provides the following blocks:

- **global**:
 + `float map (in float value, in float inputMin, in float inputMax, in float outputMin, in float outputMax, bool clamp) `
 + `float map (in float value, in float inputMin, in float inputMax, in float outputMin, in float outputMax) `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **EPSILON**: ```1e-07```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/map.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/map-full.yaml
```




#### [functions-pulse](https://github.com/tangrams/blocks/blob/gh-pages/functions/pulse.yaml)

This provides the following blocks:

- **global**:
 + `float pulse (float x, float p, float w) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/pulse.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/pulse-full.yaml
```



<hr>


### [GENERATIVE](https://github.com/tangrams/blocks/tree/gh-pages/generative)

#### [generative-fbm](https://github.com/tangrams/blocks/blob/gh-pages/generative/fbm.yaml)

This provides the following blocks:

- **global**:
 + `float fbm (float x) `
 + `int i = 0; i < int(NUM_OCTAVES); ++i) `
 + `float fbm (vec2 xy) `
 + `int i = 0; i < int(NUM_OCTAVES); ++i) `
 + `float fbm ( in vec3 xyz) `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **NUM_OCTAVES**: ```5```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/fbm.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/fbm-full.yaml
```




#### [generative-noise](https://github.com/tangrams/blocks/blob/gh-pages/generative/noise.yaml)

This provides the following blocks:

- **global**:
 + `float noise (in float x) `
 + `float noise (vec2 xy) `
 + `float noise (vec3 xyz) `
 + `float snoise (vec3 p) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/noise.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/noise-full.yaml
```




#### [generative-random](https://github.com/tangrams/blocks/blob/gh-pages/generative/random.yaml)

This provides the following blocks:

- **global**:
 + `float random (float x) `
 + `float random (vec2 p) `
 + `float random (vec3 p) `
 + `vec2 random2 (vec2 xy) `
 + `vec3 random3 (vec2 xy) `
 + `vec3 random3 (vec3 c) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/random.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/random-full.yaml
```




#### [generative-voronoi](https://github.com/tangrams/blocks/blob/gh-pages/generative/voronoi.yaml)

This provides the following blocks:

- **global**:
 + `vec3 voronoi (vec2 st) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/voronoi.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/voronoi-full.yaml
```



<hr>


### [GEOMETRY](https://github.com/tangrams/blocks/tree/gh-pages/geometry)

#### [geometry-dynamic-height](https://github.com/tangrams/blocks/blob/gh-pages/geometry/dynamic-height.yaml)

This provides the following blocks:

- **position**:

```glsl
float zoom = map(u_map_position.z,ZOOM_START,ZOOM_END,1.,0.);
position.z *= max(1.,.5+ZOOM_LINEAR_FACTOR*zoom);
```



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **ZOOM_LINEAR_FACTOR**: ```2.0```
 - **ZOOM_START**: ```15.0```
 - **ZOOM_END**: ```20.0```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/dynamic-height.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/dynamic-height-full.yaml
```




#### [geometry-dynamic-width](https://github.com/tangrams/blocks/blob/gh-pages/geometry/dynamic-width.yaml)

This provides the following blocks:

- **width**:

```glsl
width *= 0.2+min(pow(position.z*0.006,2.),.6);
```



Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/dynamic-width.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/dynamic-width-full.yaml
```




#### [geometry-matrices](https://github.com/tangrams/blocks/blob/gh-pages/geometry/matrices.yaml)

This provides the following blocks:

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

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **HALF_PI**: ```1.57079632679```
 - **TWO_PI**: ```6.28318530718```
 - **PI**: ```3.14159265359```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/matrices.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/matrices-full.yaml
```




#### [geometry-normal](https://github.com/tangrams/blocks/blob/gh-pages/geometry/normal.yaml)

This provides the following blocks:

- **global**:
 + `bool isWall () `
 + `bool isRoof () `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/normal.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/normal-full.yaml
```




#### [geometry-projections](https://github.com/tangrams/blocks/blob/gh-pages/geometry/projections.yaml)

This provides the following blocks:

- **global**:
 + `float y2lat_d (float y) `
 + `float x2lon_d (float x) `
 + `float lat2y_d (float lat) `
 + `float lon2x_d (float lon) `
 + `float y2lat_m (float y) `
 + `float x2lon_m (float x) `
 + `float lat2y_m (float lat) `
 + `float lon2x_m (float lon) `
 + `vec2 latlon2albers (float lat, float lon, float lat0, float lng0, float phi1, float phi2 ) `
 + `vec2 latlon2albers (float lat, float lon, float delta_phi1, float delta_phi2) `
 + `vec2 latlon2albers (float lat, float lon, float width) `
 + `vec2 latlon2albers (float lat, float lon) `
 + `vec2 latlon2USalbers (float lat, float lon) `
 + `vec2 latlon2azimuthal (float lat, float lon, float phi1, float lambda0) `
 + `vec2 azimuthal(float lat, float lon) `
 + `vec2 azimuthalNorth(float lat, float lon) `
 + `vec2 azimuthalSouth(float lat, float lon) `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **PI**: ```3.14159265359```
 - **HALF_PI**: ```1.57079632679```
 - **EARTH_RADIUS**: ```6378137.0```
 - **deg2rad(d)**: ```(((d)*3.14159265358979323846)/180.0)```
 - **QUATER_PI**: ```0.785398163```
 - **rad2deg(d)**: ```(((d)*180.0)/3.14159265358979323846)```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/projections.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/projections-full.yaml
```




#### [geometry-terrarium](https://github.com/tangrams/blocks/blob/gh-pages/geometry/terrarium.yaml)

This provides the following blocks:

- **position**:

```glsl
position.z += ZOFFSET*u_meters_per_pixel;
extrudeTerrain(position);
```


- **global**:
 + `float getHeight() `
 + `void extrudeTerrain (inout vec4 position) `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **ZOFFSET**: ```0.0```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/terrarium.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/terrarium-full.yaml
```




#### [geometry-tilt](https://github.com/tangrams/blocks/blob/gh-pages/geometry/tilt.yaml)

This provides the following blocks:

- **position**:

```glsl
float t = u_time*0.1; 
float z = clamp(smoothstep(TILT_IN/TILT_MAX_ZOOM, TILT_OUT/TILT_MAX_ZOOM, max(u_map_position.z/TILT_MAX_ZOOM,0.)*0.9), 0., 1.);
position.xyz = rotateX3D(z*HALF_PI) * rotateZ3D(sin(t)*PI*z) * position.xyz;
```



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **TILT_MAX_ZOOM**: ```20.0```
 - **TILT_IN**: ```15.0```
 - **TILT_OUT**: ```20.0```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/tilt.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/tilt-full.yaml
```



<hr>


### [LINES](https://github.com/tangrams/blocks/tree/gh-pages/lines)

#### [lines-chevron](https://github.com/tangrams/blocks/blob/gh-pages/lines/chevron.yaml)

This provides the following blocks:

- **color**:

```glsl
color = mix(color,
            vec4(CHEVRON_COLOR, CHEVRON_ALPHA),
            step(.5,fract((v_texcoord.y+abs(v_texcoord.x-.5)) * CHEVRON_SCALE)*CHEVRON_SIZE));
```



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **CHEVRON_SIZE**: ```1.0```
 - **CHEVRON_COLOR**: ```vec3(1., 0., 0.)```
 - **CHEVRON_ALPHA**: ```1.0```
 - **CHEVRON_SCALE**: ```1.0```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/chevron.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/chevron-full.yaml
```




#### [lines-dash](https://github.com/tangrams/blocks/blob/gh-pages/lines/dash.yaml)

This provides the following blocks:

- **color**:

```glsl
color.a = 1.-step(DASH_SIZE,fract(v_texcoord.y*DASH_SCALE));
```



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **DASH_SIZE**: ```0.5```
 - **DASH_SCALE**: ```0.1```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dash.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dash-full.yaml
```




#### [lines-dots](https://github.com/tangrams/blocks/blob/gh-pages/lines/dots.yaml)

This provides the following blocks:

- **color**:

```glsl
vec2 st = fract(v_texcoord.xy);
st -= .5;
color.a = 1.- step(DOT_SIZE, dot(st,st)*2.);
```



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **DOT_SIZE**: ```0.05```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dots.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dots-full.yaml
```




#### [lines-outline](https://github.com/tangrams/blocks/blob/gh-pages/lines/outline.yaml)

This provides the following blocks:

- **color**:

```glsl
color.rgb = mix(color.rgb,
                OUTLINE_COLOR,
                (1.0-(aastep(OUTLINE_WIDTH,v_texcoord.x)-step(1.0-OUTLINE_WIDTH,v_texcoord.x))));
```



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **OUTLINE_WIDTH**: ```0.1```
 - **OUTLINE_COLOR**: ```vec3(1.)```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/outline.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/outline-full.yaml
```




#### [lines-stripes](https://github.com/tangrams/blocks/blob/gh-pages/lines/stripes.yaml)

This provides the following blocks:

- **color**:

```glsl
color.rgb += step(STRIPES_WIDTH, sin((fract(v_texcoord).x+fract(v_texcoord).y) * 6.283)) * STRIPES_INTENSITY;
```



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **STRIPES_INTENSITY**: ```0.1```
 - **STRIPES_WIDTH**: ```0.1```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/stripes.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/stripes-full.yaml
```



<hr>


### [PATTERNS](https://github.com/tangrams/blocks/tree/gh-pages/patterns)

#### [patterns-dots](https://github.com/tangrams/blocks/blob/gh-pages/patterns/dots.yaml)

This provides the following blocks:

- **global**:
 + `float TileDots(float scale, float size) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/dots.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/dots-full.yaml
```




#### [patterns-grid](https://github.com/tangrams/blocks/blob/gh-pages/patterns/grid.yaml)

This provides the following blocks:

- **global**:
 + `bool grid (vec2 st, float res, float press) `
 + `bool grid (vec2 st, float res) `
 + `float tileGrid (float res) `
 + `float tileGrid() `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/grid.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/grid-full.yaml
```




#### [patterns-stripes](https://github.com/tangrams/blocks/blob/gh-pages/patterns/stripes.yaml)

This provides the following blocks:

- **global**:
 + `float stripesDF (vec2 st) `
 + `float stripes (vec2 st, float width) `
 + `float stripes (vec2 st, float width, float angle) `
 + `float diagonalStripes (vec2 st) `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **PI**: ```3.14159265359```
 - **STRIPE_SCALE**: ```28.296```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/stripes.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/stripes-full.yaml
```




#### [patterns-waves](https://github.com/tangrams/blocks/blob/gh-pages/patterns/waves.yaml)

This provides the following blocks:

- **global**:
 + `float wavesDF (vec2 st, float freq, float amp) `
 + `float waves (vec2 st, float freq, float amp, float width) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/waves.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/waves-full.yaml
```




#### [patterns-zigzag](https://github.com/tangrams/blocks/blob/gh-pages/patterns/zigzag.yaml)

This provides the following blocks:

- **global**:
 + `float zigzagDF (vec2 st, float freq) `
 + `float zigzag (vec2 st, float freq, float width) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/zigzag.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/zigzag-full.yaml
```



<hr>


### [POINTS](https://github.com/tangrams/blocks/tree/gh-pages/points)

#### [points-cross](https://github.com/tangrams/blocks/blob/gh-pages/points/cross.yaml)

This provides the following blocks:

- **color**:

```glsl
color.a = clamp(cross(v_texcoord.xy,vec2(2.,.5)),0.,1.)*CROSS_ALPHA;

```



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **CROSS_ALPHA**: ```0.75```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/points/cross.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/points/cross-full.yaml
```




#### [points-shape](https://github.com/tangrams/blocks/blob/gh-pages/points/shape.yaml)

This provides the following blocks:

- **color**:

```glsl
float df = shapeDF(vec2(v_texcoord.x,1.-v_texcoord.y),SHAPE_SIDES);
color.rgb = mix(color.rgb,
                SHAPE_BORDER_COLOR,
                aastep(SHAPE_SIZE*.5-SHAPE_BORDER_WIDTH,df));
color.a = (1.-aastep(SHAPE_SIZE*.5,df))*SHAPE_ALPHA;
```



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **SHAPE_ALPHA**: ```1.0```
 - **SHAPE_BORDER_WIDTH**: ```0.15```
 - **SHAPE_SIDES**: ```3```
 - **SHAPE_BORDER_COLOR**: ```vec3(1.)```
 - **SHAPE_SIZE**: ```1.0```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/points/shape.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/points/shape-full.yaml
```



<hr>


### [SHAPES](https://github.com/tangrams/blocks/tree/gh-pages/shapes)

#### [shapes-circle](https://github.com/tangrams/blocks/blob/gh-pages/shapes/circle.yaml)

This provides the following blocks:

- **global**:
 + `float circleDF (vec2 st) `
 + `float circle (vec2 st, float radius) `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **PI**: ```3.14159265359```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/circle.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/circle-full.yaml
```




#### [shapes-cross](https://github.com/tangrams/blocks/blob/gh-pages/shapes/cross.yaml)

This provides the following blocks:

- **global**:
 + `float cross (vec2 st, float size, float width) `
 + `float cross (in vec2 st, float _size) `
 + `float cross (in vec2 st, vec2 _size) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/cross.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/cross-full.yaml
```




#### [shapes-digits](https://github.com/tangrams/blocks/blob/gh-pages/shapes/digits.yaml)

This provides the following blocks:

- **global**:
 + `float SampleDigit (const in float fDigit, const in vec2 vUV) `
 + `float PrintValue (const in vec2 vStringCharCoords, const in float fValue, const in float fMaxDigits, const in float fDecimalPlaces) `
 + `float PrintValue (in vec2 fragCoord, const in vec2 vPixelCoords, const in vec2 vFontSize, const in float fValue, const in float fMaxDigits, const in float fDecimalPlaces) `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **CHAR_DECIMAL_POINT**: ```10.0```
 - **CHAR_MINUS**: ```11.0```
 - **CHAR_BLANK**: ```12.0```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/digits.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/digits-full.yaml
```




#### [shapes-polygons](https://github.com/tangrams/blocks/blob/gh-pages/shapes/polygons.yaml)

This provides the following blocks:

- **global**:
 + `float shapeDF (vec2 st, int N) `
 + `float shape (vec2 st, int N, float width) `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **TWO_PI**: ```6.283185307```
 - **PI**: ```3.14159265359```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/polygons.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/polygons-full.yaml
```




#### [shapes-rect](https://github.com/tangrams/blocks/blob/gh-pages/shapes/rect.yaml)

This provides the following blocks:

- **global**:
 + `float rectDF (vec2 st, vec2 size) `
 + `float rectDF (vec2 st, float size) `
 + `float rect (vec2 st, vec2 size, float radio) `
 + `float rect (vec2 st, float size, float radio) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/rect.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/rect-full.yaml
```




#### [shapes-simplex](https://github.com/tangrams/blocks/blob/gh-pages/shapes/simplex.yaml)

This provides the following blocks:

- **global**:
 + `float warp (vec3 S) `
 + `float circle (vec3 S) `
 + `float triangle (vec3 S) `
 + `vec3 star (vec3 S) `
 + `vec3 sakura (vec3 S) `
 + `float lotus (vec3 S, float petals_size, float roundness) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/simplex.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/simplex-full.yaml
```



<hr>


### [SPACE](https://github.com/tangrams/blocks/tree/gh-pages/space)

#### [space-constant](https://github.com/tangrams/blocks/blob/gh-pages/space/constant.yaml)

This provides the following blocks:

- **global**:
 + `vec2 getConstantCoords () `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/space/constant.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/space/constant-full.yaml
```




#### [space-screen](https://github.com/tangrams/blocks/blob/gh-pages/space/screen.yaml)

This provides the following blocks:

- **global**:
 + `vec2 getScreenCoords () `
 + `vec2 getScreenNonStretchCoords () `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/space/screen.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/space/screen-full.yaml
```




#### [space-tex](https://github.com/tangrams/blocks/blob/gh-pages/space/tex.yaml)

This provides the following blocks:

- **global**:
 + `vec2 getTexCoords () `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/space/tex.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/space/tex-full.yaml
```




#### [space-tile](https://github.com/tangrams/blocks/blob/gh-pages/space/tile.yaml)

This provides the following blocks:

- **position**:

```glsl
// Normalize the attribute position of a vertex
v_pos = modelPosition().xyz;
```


- **global**:
 + `vec2 getTileCoords() `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/space/tile.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/space/tile-full.yaml
```




#### [space-uz](https://github.com/tangrams/blocks/blob/gh-pages/space/uz.yaml)

This provides the following blocks:

- **global**:
 + `vec2 getUZCoords () `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/space/uz.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/space/uz-full.yaml
```



<hr>


### [TEXTURE](https://github.com/tangrams/blocks/tree/gh-pages/texture)

#### [texture-non-repetitive](https://github.com/tangrams/blocks/blob/gh-pages/texture/non-repetitive.yaml)

This provides the following blocks:

- **global**:
 + `vec4 NonRepetitiveTexture (sampler2D tex, vec2 x, float v) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/texture/non-repetitive.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/texture/non-repetitive-full.yaml
```




#### [texture-zoom-fade](https://github.com/tangrams/blocks/blob/gh-pages/texture/zoom-fade.yaml)

This provides the following blocks:

- **global**:
 + `vec4 TileTexture (sampler2D tex, float scale) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/texture/zoom-fade.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/texture/zoom-fade-full.yaml
```



<hr>


### [TILING](https://github.com/tangrams/blocks/tree/gh-pages/tiling)

#### [tiling-brick](https://github.com/tangrams/blocks/blob/gh-pages/tiling/brick.yaml)

This provides the following blocks:

- **global**:
 + `vec2 brick (vec2 st, float zoom) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/brick.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/brick-full.yaml
```




#### [tiling-simplex](https://github.com/tangrams/blocks/blob/gh-pages/tiling/simplex.yaml)

This provides the following blocks:

- **global**:
 + `vec2 simplex (vec2 st) `
 + `vec2 unsimplex (vec2 st) `
 + `vec3 simplexGrid (vec2 st) `
 + `vec3 simplexRotatedGrid (vec2 st) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/simplex.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/simplex-full.yaml
```




#### [tiling-tile](https://github.com/tangrams/blocks/blob/gh-pages/tiling/tile.yaml)

This provides the following blocks:

- **global**:
 + `vec2 tile (vec2 st, float zoom) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/tile.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/tile-full.yaml
```




#### [tiling-truchet](https://github.com/tangrams/blocks/blob/gh-pages/tiling/truchet.yaml)

This provides the following blocks:

- **global**:
 + `vec2 truchetMirror (vec2 st) `
 + `vec2 truchetRotate (vec2 st) `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **PI**: ```3.14159265359```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/truchet.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/truchet-full.yaml
```



<hr><hr>
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
