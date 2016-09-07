![](blocks.png)

# Tangram Blocks

Gallery of **reusable building blocks for Tangram** to make beautiful maps simpler.

Writing custom styles for [Tangram](https://mapzen.com/projects/tangram/) can be tricky because you need to know some GL Shading Language, but using this 
library for recipes, you can mix and reuse some of the snippets of shader code blocks that flavor our maps.

## How to use them?
<hr>

So first you need to `import` the block to the [YAML scene file](https://mapzen.com/documentation/tangram/Scene-file/) you are working on. That will look something like this:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/grain.yaml
```

Then you need to ```mix``` it with the custom styles of your choise. For example:

```yaml
styles:
    buildings:
        base: polygons
        mix: [filter-grain]
```

Some of the blocks like [points](#points), [lines](#lines), [polygons](#polygons), [fx](#fx) and [filter](#filter) automatically will add the necessary lines to the `normals`, `color` and `filter` blocks to make it work. So you don't have to do anything else other than add it to the `mix:`. Then you can tweak the values from the ```defines``` to your own prefernces. For example in the above example we can increase the detail and amount of the grain by modifying these two defines:

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

The rest of the building blocks just provide reusable GLSL functions into the `global` shader block. 

To learn basic principles about shaders we recomend reading [The Book of shaders](http://thebookofshaders.com/), if you are interested to learn about [shaders inside Tangram read tangram documentation about that subject](https://mapzen.com/documentation/tangram/Shaders-Overview/).

## Want to contribute?

If you have made a nice shader style you are proud of and want to share it, send me an email to <patricio@mapzen.com> or a DM to [@patriciogv](https://twitter.com/patriciogv) and I will be happy to help you make a **block** out of it. 

## Blocks description
<hr>


### [COLOR](http://tangrams.github.io/blocks/#color) <a href="https://github.com/tangrams/blocks/blob/gh-pages/color" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

#### [color-conversion](http://tangrams.github.io/blocks/#color-conversion) <a href="https://github.com/tangrams/blocks/blob/gh-pages/color/conversion.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Set of functions to convert colors between color systems/spaces.
For more information on this theme read [this chapter of The Book of Shaders about color](http://thebookofshaders.com/06/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/color/conversion.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/color/conversion-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec3 rgb2hsb (vec3 c) `
 + `vec3 rgb2hsb (vec4 c) `
 + `vec3 hsb2rgb (vec3 c) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [color-palette](http://tangrams.github.io/blocks/#color-palette) <a href="https://github.com/tangrams/blocks/blob/gh-pages/color/palette.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Procedural generation of color palettes implemented by [Inigo Quiles](https://twitter.com/iquilezles) (1999) explained in [this article](http://www.iquilezles.org/www/articles/palettes/palettes.htm)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/color/palette.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/color/palette-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec3 palette (float t, vec3 a, vec3 b, vec3 c, vec3 d) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [color-tools](http://tangrams.github.io/blocks/#color-tools) <a href="https://github.com/tangrams/blocks/blob/gh-pages/color/tools.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Set of color tools to get the **intensity** and **brightness** of a color.
For more information on this theme read [this chapter of The Book of Shaders about color](http://thebookofshaders.com/06/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/color/tools.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/color/tools-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float getIntensity (vec3 c) `
 + `float getIntensity (vec4 c) `
 + `float getBrightness (vec3 c) `
 + `float getBrightness (vec4 c) `

![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)


### [ELEVATION](http://tangrams.github.io/blocks/#elevation) <a href="https://github.com/tangrams/blocks/blob/gh-pages/elevation" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

#### [elevation-contours](http://tangrams.github.io/blocks/#elevation-contours) <a href="https://github.com/tangrams/blocks/blob/gh-pages/elevation/contours.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/elevation/contours.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/elevation/contours-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **CONTOURS_SCALE**:  The *default value* is ```60.0```. 
 -  **CONTOURS_OFFSET**:  The *default value* is ```u_time*CONTOURS_SPEED```. 
 -  **CONTOURS_ALPHA**:  The *default value* is ```color.a```. 
 -  **CONTOURS_COLOR**:  The *default value* is ```color.rgb```. 
 -  **CONTOURS_BACKGROUND_ALPHA**:  The *default value* is ```1.0```. 
 -  **CONTOURS_BACKGROUND_COLOR**:  The *default value* is ```vec3(0.0)```. 
 -  **CONTOURS_SPEED**:  The *default value* is ```-0.1```. 

These are the **shader blocks**:

- **color**:

```glsl
color = mix(vec4(CONTOURS_BACKGROUND_COLOR,CONTOURS_BACKGROUND_ALPHA),
            vec4(CONTOURS_COLOR,CONTOURS_ALPHA),
            aastep( dot(normal, vec3(0.,0.,1.)),
                    abs(sin((normal_elv_raster.a*PI)*CONTOURS_SCALE+CONTOURS_OFFSET)) ) );
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [elevation-dash](http://tangrams.github.io/blocks/#elevation-dash) <a href="https://github.com/tangrams/blocks/blob/gh-pages/elevation/dash.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Perfect for the `landuse` layer on your elevation maps, the `elevation-dash` modules use the color of the layer to draw a dash pattern that changes width based on the surface of the terrain.



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/elevation/dash.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/elevation/dash-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **NORMAL_TEXTURE_INDEX**:  The *default value* is ```0```. 
 -  **DASH_SIZE**:  The *default value* is ```shade```. 
 -  **DASH_BACKGROUND_COLOR**:  The *default value* is ```color.rgb```. 
 -  **DASH_TYPE**:  The *default value* is ```fill```. 
 -  **DASH_TILE_STYLE**:  The *default value* is ```tile```. 
 -  **DASH_DIR**:  The *default value* is ```vec3(-0.600,-0.420,0.560)```. 
 -  **DASH_SCALE**:  The *default value* is ```10.0```. 
 -  **DASH_MAX_SIZE**:  The *default value* is ```1.0```. 
 -  **DASH_MIN_SIZE**:  The *default value* is ```0.8```. 
 -  **DASH_COLOR**:  The *default value* is ```color.rgb*.5```. 

These are the **shader blocks**:

- **normal**:

```glsl
float shade = dot((sampleRaster(int(NORMAL_TEXTURE_INDEX)).rgb-.5)*2., DASH_DIR);
shade = mix(DASH_MIN_SIZE, DASH_MAX_SIZE, (shade*shade*shade)*4.);
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [elevation-normal](http://tangrams.github.io/blocks/#elevation-normal) <a href="https://github.com/tangrams/blocks/blob/gh-pages/elevation/normal.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

The raster normal map tiles needs to be load like this:
```
    normals-elevation:
        type: Raster
        url: https://s3.amazonaws.com/elevation-tiles-prod/normal/{z}/{x}/{y}.png
        max_zoom: 15
```
A simple way to do it is to import `https://tangrams.github.io/blocks/source-elevation.yaml` and then link the vector tiles to them (see the example).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/elevation/normal.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/elevation/normal-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **NORMAL_TEXTURE_INDEX**:  The *default value* is ```0```. 

These are the **shader blocks**:

- **normal**:

```glsl
vec4 normal_elv_raster = sampleRaster(int(NORMAL_TEXTURE_INDEX));
normal = (normal_elv_raster.rgb-.5)*2.;
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/elevation.yaml&lines=14" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/elevation.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [elevation-rainbow](http://tangrams.github.io/blocks/#elevation-rainbow) <a href="https://github.com/tangrams/blocks/blob/gh-pages/elevation/rainbow.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/elevation/rainbow.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/elevation/rainbow-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **RAINBOW_SPEED**:  The *default value* is ```-0.5```. 

These are the **shader blocks**:

- **color**:

```glsl
color.rgb = palette(0.380+normal_elv_raster.a+u_time*RAINBOW_SPEED,vec3(.5),vec3(.5),vec3(2.,1.,0.),vec3(.5,.2,0.25));
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [elevation-ramp](http://tangrams.github.io/blocks/#elevation-ramp) <a href="https://github.com/tangrams/blocks/blob/gh-pages/elevation/ramp.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Applies a image/texture named `u_ramp` to the height of a terrain. 
The texture is essentially an image of 1 height by N width. 
Add as many pixels as you want, they will get lineraly interpolated 
producing a colorful gradient ramp, that any other way is hard to produce.
For example this is the default ramp texture:
<img style='width: 100%; height: 10px;' src='data:image/png;base64,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'>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/elevation/ramp.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/elevation/ramp-full.yaml
```


These blocks uses a custom **shader**.
These are the **uniforms**:
 -  **u_ramp**:  The *default value* is ```data:image/png;base64,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```. 

These are the **shader blocks**:

- **color**:

```glsl
color = texture2D(u_ramp, vec2((1.-normal_elv_raster.a),.5));
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/elevation-ramp.yaml" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/elevation-ramp.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [elevation-stripes](http://tangrams.github.io/blocks/#elevation-stripes) <a href="https://github.com/tangrams/blocks/blob/gh-pages/elevation/stripes.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Perfect for the `landuse` layer on your elevation maps, the `elevation-stripe` modules use the color of the layer to draw a stripe pattern that changes width based on the surface of the terrain.



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/elevation/stripes.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/elevation/stripes-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **NORMAL_TEXTURE_INDEX**:  The *default value* is ```0```. 
 -  **STRIPES_PCT**:  The *default value* is ```1.8```. 
 -  **STRIPES_SCALE**:  The *default value* is ```20.0```. 
 -  **STRIPES_WIDTH**:  The *default value* is ```dot((sampleRaster(int(NORMAL_TEXTURE_INDEX)).rgb-.5)*2., STRIPES_DIR)*STRIPES_PCT```. 
 -  **STRIPES_ALPHA**:  The *default value* is ```0.5```. 
 -  **STRIPES_DIR**:  The *default value* is ```vec3(-0.600,-0.420,0.600)```. 


Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/elevation-stripes.yaml" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/elevation-stripes.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)


### [FILTER](http://tangrams.github.io/blocks/#filter) <a href="https://github.com/tangrams/blocks/blob/gh-pages/filter" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

#### [filter-grain](http://tangrams.github.io/blocks/#filter-grain) <a href="https://github.com/tangrams/blocks/blob/gh-pages/filter/grain.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a lens grain effect to the scene.



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/grain.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/grain-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **GRAIN_AMOUNT**:  number between ```0.0``` and ```1.0``` that control the *amount*. The *default value* is ```0.3```. 
 -  **GRAIN_BLEND**:  variable that control the *blend mode* with one of the following values: ```ADD, SUBTRACT, MULTIPLY```. The *default value* is ```SUBTRACT```. 

These are the **shader blocks**:

- **global**:
 + `float grain () `
- **filter**:

```glsl
// Apply the grain in the amount defined on GRAIN_AMOUNT
color.rgb = color.rgb GRAIN_BLEND (grain()*GRAIN_AMOUNT);

```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/grain.yaml&lines=29" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/grain.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [filter-grid](http://tangrams.github.io/blocks/#filter-grid) <a href="https://github.com/tangrams/blocks/blob/gh-pages/filter/grid.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a grid filter to the syle.



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/grid.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/grid-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **GRID_AMOUNT**:  number between ```0.0``` and ```1.0``` that control the *amount*. The *default value* is ```0.2```. 
 -  **GRID_BLEND**:  variable that control the *blend mode* with one of the following values: ```ADD, SUBTRACT, MULTIPLY```. The *default value* is ```ADD```. 

These are the **shader blocks**:

- **filter**:

```glsl
color.rgb = color.rgb GRID_BLEND (tileGrid()*GRID_AMOUNT);

```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [filter-hatch](http://tangrams.github.io/blocks/#filter-hatch) <a href="https://github.com/tangrams/blocks/blob/gh-pages/filter/hatch.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Hatching filter based on [Jaume's Sanchez](https://twitter.com/thespite?lang=en) [Cross-hatching GLSL shader](https://www.clicktorelease.com/code/cross-hatching/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/hatch.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/hatch-full.yaml
```


These blocks uses a custom **shader**.
These are the **uniforms**:
 -  **u_hatchmap**:  The *default value* is ```imgs/hatch.png```. 

These are the **shader blocks**:

- **global**:
 + `float getHatch (vec2 st, float brightness) `

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/crosshatch.yaml&lines=111" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/crosshatch.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/pericoli.yaml&lines=157" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/pericoli.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [filter-height](http://tangrams.github.io/blocks/#filter-height) <a href="https://github.com/tangrams/blocks/blob/gh-pages/filter/height.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Adds a dark gradiant to the geometries conform they approach to height 0.



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/height.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/height-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **color**:

```glsl
color.rgb *= min((worldPosition().z*.001 + .5),1.);
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/default.yaml&lines=88" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/default.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [filter-lut](http://tangrams.github.io/blocks/#filter-lut) <a href="https://github.com/tangrams/blocks/blob/gh-pages/filter/lut.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Maybe you don't know what a LUT is but I am sure you have use it. For example in instagram. Look Up Tables is a fast and cheap way to style an image using another image as a reference. Yes, like filters. Like Instagram filters. 
The reference image needs to have a particular structure and is pass as uniform texture (```u_lut```).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/lut.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/lut-full.yaml
```


These blocks uses a custom **shader**.
These are the **uniforms**:
 -  **u_lut**:  variable that control the *filter type* with one of the following values: ```https://tangrams.github.io/blocks/filter/imgs/lut-0005.png``` ( *Nashville* ), ```https://tangrams.github.io/blocks/filter/imgs/lut-0001.png``` ( *XPro* ), ```https://tangrams.github.io/blocks/filter/imgs/lut-0003.png``` ( *Toaster* ), ```https://tangrams.github.io/blocks/filter/imgs/lut-0004.png``` ( *Sutro* ), ```https://tangrams.github.io/blocks/filter/imgs/lut-0009.png``` ( *Hefe* ), ```https://tangrams.github.io/blocks/filter/imgs/lut-0008.png``` ( *InkWell* ), ```https://tangrams.github.io/blocks/filter/imgs/lut-0010.png``` ( *Gotham* ), ```https://tangrams.github.io/blocks/filter/imgs/lut-0002.png``` ( *Walden* ), ```https://tangrams.github.io/blocks/filter/imgs/lut-0013.png``` ( *Brannan* ), ```https://tangrams.github.io/blocks/filter/imgs/lut-0011.png``` ( *EarlyBird* ), ```https://tangrams.github.io/blocks/filter/imgs/lut-0007.png``` ( *LomoFi* ), ```https://tangrams.github.io/blocks/filter/imgs/lut-0006.png``` ( *LordKelvin* ). The *default value* is ```https://tangrams.github.io/blocks/filter/imgs/lut-0001.png```. 

These are the **defines**:
 -  **LUT_AMOUNT**:  number between ```0.0``` and ```1.0``` that control the *amount*. The *default value* is ```0.5```. 

These are the **shader blocks**:

- **global**:
 + `vec3 getLut (vec3 textureColor, sampler2D lookupTable) `
 + `vec3 getLut (vec3 textureColor) `
- **filter**:

```glsl
color.rgb = mix(color.rgb,
                getLut(color.rgb),
                LUT_AMOUNT);
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/sandbox-lut.yaml" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/sandbox-lut.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [filter-tv](http://tangrams.github.io/blocks/#filter-tv) <a href="https://github.com/tangrams/blocks/blob/gh-pages/filter/tv.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply an old TV effect to the style.



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/tv.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/filter/tv-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **TV_FREQ**:  number between ```0.0``` and ```10.0``` that control the *frequency*. The *default value* is ```2.7```. 
 -  **TV_SPEED**:  number between ```0.0``` and ```10.0``` that control the *speed*. The *default value* is ```5.0```. 
 -  **TV_AMOUNT**:  number between ```0.0``` and ```1.0``` that control the *amount*. The *default value* is ```1.0```. 
 -  **TV_BLEND**:  variable that control the *blend mode* with one of the following values: ```ADD, SUBTRACT, MULTIPLY```. The *default value* is ```MULTIPLY```. 

These are the **shader blocks**:

- **filter**:

```glsl
color = color TV_BLEND (abs(cos((gl_FragCoord.y*(TV_FREQ/u_device_pixel_ratio)+u_time*TV_SPEED)))*TV_AMOUNT);

```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/9845C.yaml" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/9845C.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)


### [FUNCTIONS](http://tangrams.github.io/blocks/#functions) <a href="https://github.com/tangrams/blocks/blob/gh-pages/functions" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

#### [functions-aastep](http://tangrams.github.io/blocks/#functions-aastep) <a href="https://github.com/tangrams/blocks/blob/gh-pages/functions/aastep.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

AnitAliased ```step()``` function implemented by [Matt DesLauriers](https://twitter.com/mattdesl) in this module <https://github.com/stackgl/glsl-aastep>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/aastep.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/aastep-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float aastep(float threshold, float value) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [functions-easing](http://tangrams.github.io/blocks/#functions-easing) <a href="https://github.com/tangrams/blocks/blob/gh-pages/functions/easing.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Easing functions originally develop by Robert Penner's and transformed to GLSL by [StackGL](http://stack.gl/) in this repo: <https://github.com/stackgl/glsl-easings>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/easing.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/easing-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **HALF_PI**:  The *default value* is ```1.57079632679```. 
 -  **PI**:  The *default value* is ```3.14159265359```. 

These are the **shader blocks**:

- **global**:
 + `float linear (in float t) `
 + `float exponentialIn (in float t) `
 + `float exponentialOut (in float t) `
 + `float exponentialInOut (in float t) `
 + `float sineIn (in float t) `
 + `float sineOut (in float t) `
 + `float sineInOut (in float t) `
 + `float qinticIn (in float t) `
 + `float qinticOut (in float t) `
 + `float qinticInOut (in float t) `
 + `float quarticIn (in float t) `
 + `float quarticOut (in float t) `
 + `float quarticInOut (in float t) `
 + `float quadraticInOut (in float t) `
 + `float quadraticIn (in float t) `
 + `float quadraticOut (in float t) `
 + `float cubicIn (in float t) `
 + `float cubicOut (in float t) `
 + `float cubicInOut (in float t) `
 + `float elasticIn (in float t) `
 + `float elasticOut (in float t) `
 + `float elasticInOut (in float t) `
 + `float circularIn (in float t) `
 + `float circularOut (in float t) `
 + `float circularInOut (in float t) `
 + `float bounceOut (in float t) `
 + `float bounceIn (in float t) `
 + `float bounceInOut (in float t) `
 + `float backIn (in float t) `
 + `float backOut (in float t) `
 + `float backInOut (in float t) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [functions-map](http://tangrams.github.io/blocks/#functions-map) <a href="https://github.com/tangrams/blocks/blob/gh-pages/functions/map.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

This function helps you to interpolate a `value` between an IN range (`inputMin` to `inputMax`) to a OUT range (`outputMin` to `outputMax`). 



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/map.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/map-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **EPSILON**:  The *default value* is ```1e-07```. 

These are the **shader blocks**:

- **global**:
 + `float map (in float value, in float inputMin, in float inputMax, in float outputMin, in float outputMax, bool clamp) `
 + `float map (in float value, in float inputMin, in float inputMax, in float outputMin, in float outputMax) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [functions-pulse](http://tangrams.github.io/blocks/#functions-pulse) <a href="https://github.com/tangrams/blocks/blob/gh-pages/functions/pulse.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

This one dimensional shaping function made by Inigo Quiles in [this article](http://www.iquilezles.org/www/articles/functions/functions.htm).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/pulse.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/pulse-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float pulse (float x, float peak, float width) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [functions-zoom](http://tangrams.github.io/blocks/#functions-zoom) <a href="https://github.com/tangrams/blocks/blob/gh-pages/functions/zoom.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

when you mix this block to another block you can use the functions `zoom()` or `zoomEase()`. Both will help you to interpolate any values between the zooms `ZOOM_START` and `ZOOM_END`.
By default `zoom()` and `zoomEase()` will return a `float `number between 0 and 1. But you can change it to interpolate any thing! Like `floats`, `vec2`, `vec3`, `vec4` and even other functions! For that you just need to change de `defines`: `ZOOM_IN`, and `ZOOM_OUT` to what ever you want to interpolate.
`zoom()` use the cuadratic interpolation of `smoothstep()` but you can use `zoomEase()` to specify what type of **easing interpolation** you prefere. Just change the default `linear` function for any [easing functions describe here](#functions-easing) in the `ZOOM_FNC` define. Ex: `ZOOM_FNC: quadraticInOut`



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/zoom.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/zoom-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **ZOOM_END**:  The *default value* is ```20.0```. 
 -  **ZOOM_MAX**:  The *default value* is ```max(ZOOM_START, ZOOM_END)```. 
 -  **ZOOM_IN**:  The *default value* is ```0.0```. 
 -  **ZOOM_OUT**:  The *default value* is ```1.0```. 
 -  **ZOOM_START**:  The *default value* is ```14.0```. 
 -  **ZOOM_FNC**:  The *default value* is ```linear```. 

These are the **shader blocks**:

- **global**:
 + `float zoom() `
 + `float zoomEase() `

![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)


### [FX](http://tangrams.github.io/blocks/#fx) <a href="https://github.com/tangrams/blocks/blob/gh-pages/fx" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

#### [fx-water](http://tangrams.github.io/blocks/#fx-water) <a href="https://github.com/tangrams/blocks/blob/gh-pages/fx/water.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Water effect, made by altering the normal map of a surface and applying a sky spherical map to the surface. 
The result looks like moving water.



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/fx/water.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/fx/water-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **normal**:

```glsl
normal += snoise(vec3(worldPosition().xy*0.08,u_time*.5))*0.02;
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/sandbox.yaml" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/sandbox.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)


### [GENERATIVE](http://tangrams.github.io/blocks/#generative) <a href="https://github.com/tangrams/blocks/blob/gh-pages/generative" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

#### [generative-caustic](http://tangrams.github.io/blocks/#generative-caustic) <a href="https://github.com/tangrams/blocks/blob/gh-pages/generative/caustics.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Caustic generative texture inspired on <https://www.shadertoy.com/view/MdlXz8> by David Hoskins



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/caustics.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/caustics-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **TAU**:  The *default value* is ```6.28318530718```. 
 -  **CAUSTIC_ITERATIONS**:  The *default value* is ```3```. 

These are the **shader blocks**:

- **global**:
 + `vec3 getCaustic (vec2 uv) `
 + `int n = 0; n < int(CAUSTIC_ITERATIONS); n++) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [generative-fbm](http://tangrams.github.io/blocks/#generative-fbm) <a href="https://github.com/tangrams/blocks/blob/gh-pages/generative/fbm.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Set of Fractal Brownian Motion functions.
For more information on this theme read [this chapter of The Book of Shaders about fractal Brownian Motion](http://thebookofshaders.com/13/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/fbm.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/fbm-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **NUM_OCTAVES**:  The *default value* is ```5```. 

These are the **shader blocks**:

- **global**:
 + `float fbm (in float x) `
 + `int i = 0; i < int(NUM_OCTAVES); ++i) `
 + `float fbm (in vec2 xy) `
 + `int i = 0; i < int(NUM_OCTAVES); ++i) `
 + `float fbm (in vec3 xyz) `
 + `int i = 0; i < int(NUM_OCTAVES); ++i) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [generative-noise](http://tangrams.github.io/blocks/#generative-noise) <a href="https://github.com/tangrams/blocks/blob/gh-pages/generative/noise.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Set of Noise functions.
For more information on this theme read [this chapter of The Book of Shaders about Noise](http://thebookofshaders.com/11/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/noise.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/noise-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float noise (in float x) `
 + `float noise (vec2 xy) `
 + `float noise (vec3 xyz) `
 + `vec3 mod289(vec3 x) `
 + `vec2 mod289(vec2 x) `
 + `vec3 permute(vec3 x) `
 + `float snoise(vec2 v) `
 + `float snoise (vec3 p) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [generative-random](http://tangrams.github.io/blocks/#generative-random) <a href="https://github.com/tangrams/blocks/blob/gh-pages/generative/random.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Set of functions about random.
For more information on this theme read [this chapter of The Book of Shaders about Random](http://thebookofshaders.com/10/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/random.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/random-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float random (float x) `
 + `float random (vec2 p) `
 + `float random (vec3 p) `
 + `vec2 random2 (vec2 xy) `
 + `vec3 random3 (vec2 xy) `
 + `vec3 random3 (vec3 c) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [generative-voronoi](http://tangrams.github.io/blocks/#generative-voronoi) <a href="https://github.com/tangrams/blocks/blob/gh-pages/generative/voronoi.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Set of Voronoi functions.
For more information on this theme read [this chapter of The Book of Shaders about Cellular Noise and Voronoi](http://thebookofshaders.com/12/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/voronoi.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/voronoi-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec3 voronoi (vec2 st) `

![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)


### [GEOMETRY](http://tangrams.github.io/blocks/#geometry) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

#### [geometry-dynamic-height](http://tangrams.github.io/blocks/#geometry-dynamic-height) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/dynamic-height.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Scale geometries in `z` acording to the zoom level



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/dynamic-height.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/dynamic-height-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **ZOOM_START**:  The *default value* is ```15.0```. 
 -  **ZOOM_END**:  The *default value* is ```20.0```. 
 -  **HEIGHT_MAX**:  The *default value* is ```2.5```. 
 -  **HEIGHT_MIN**:  The *default value* is ```1.0```. 
 -  **HEIGHT**:  The *default value* is ```zoom()```. 

These are the **shader blocks**:

- **position**:

```glsl
position.z *= max(HEIGHT_MIN,HEIGHT_MAX*HEIGHT);
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [geometry-dynamic-width](http://tangrams.github.io/blocks/#geometry-dynamic-width) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/dynamic-width.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Change the width of a line acording to the altitud



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/dynamic-width.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/dynamic-width-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **WIDTH_MIN**:  The *default value* is ```0.2```. 
 -  **WIDTH_Z_SCALE**:  The *default value* is ```0.006```. 
 -  **WIDTH_MAX**:  The *default value* is ```1.0```. 

These are the **shader blocks**:

- **width**:

```glsl
width *= min(WIDTH_MIN+(position.z*WIDTH_Z_SCALE)*(position.z*WIDTH_Z_SCALE),WIDTH_MAX);
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/blueprint.yaml&lines=7-28" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/blueprint.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [geometry-matrices](http://tangrams.github.io/blocks/#geometry-matrices) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/matrices.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Useful set of functions to construct scale, rotation and translation of 2, 3 or 4 dimensions. For more information about matrices read [this chapter from The Book of Shaders](http://thebookofshaders.com/08/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/matrices.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/matrices-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

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

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [geometry-normal](http://tangrams.github.io/blocks/#geometry-normal) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/normal.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Functions to detect if the surface is a wall (`bool isWall()`) or a roof ('bool isRoof()') based on the normals



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/normal.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/normal-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `bool isWall () `
 + `bool isRoof () `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [geometry-projections](http://tangrams.github.io/blocks/#geometry-projections) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/projections.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to do different geometry projections



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/projections.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/projections-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **EARTH_RADIUS**:  The *default value* is ```6378137.0```. 

These are the **shader blocks**:

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

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [geometry-rotation](http://tangrams.github.io/blocks/#geometry-rotation) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/rotation.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Allows to rotate the camera while zooming between `ROTATION_IN` and `ROTATION_OUT`.



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/rotation.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/rotation-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **ROTATION**:  The *default value* is ```sin(u_time*ROTATION_SPEED)*ROTATION_RANGE```. 
 -  **ROTATION_SPEED**:  The *default value* is ```0.1```. 
 -  **ROTATION_RANGE**:  The *default value* is ```PI```. 

These are the **shader blocks**:

- **position**:

```glsl
position.xyz = rotateZ3D(ROTATION) * position.xyz;

```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/tilt.yaml&lines=13-19" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/tilt.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/oblivion.yaml&lines=88-94" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/oblivion.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [geometry-tilt](http://tangrams.github.io/blocks/#geometry-tilt) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/tilt.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Allows to TILT the camera while zooming between `TILT_IN` and `TILT_OUT`.



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/tilt.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/tilt-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **TILT**:  The *default value* is ```0```. 

These are the **shader blocks**:

- **position**:

```glsl
position.xyz = rotateX3D(TILT) * position.xyz;
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/tilt.yaml&lines=7-28" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/tilt.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/oblivion.yaml" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/oblivion.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)


### [LINES](http://tangrams.github.io/blocks/#lines) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

#### [lines-chevron](http://tangrams.github.io/blocks/#lines-chevron) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/chevron.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a chevron pattern to a line



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/chevron.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/chevron-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **CHEVRON_SIZE**:  number between ```0.0``` and ```10.0``` that control the *size*. The *default value* is ```1.0```. 
 -  **CHEVRON_COLOR**:  The *default value* is ```color.rgb*.5```. 
 -  **CHEVRON_ALPHA**:  number between ```0.0``` and ```1.0``` that control the *alpha*. The *default value* is ```1.0```. 
 -  **CHEVRON_SCALE**:  number between ```0.0``` and ```10.0``` that control the *scale*. The *default value* is ```1.0```. 
 -  **CHEVRON_BACKGROUND_COLOR**:  The *default value* is ```color.rgb```. 
 -  **CHEVRON_BACKGROUND_ALPHA**:  number between ```0.0``` and ```1.0``` that control the *background alpha*. The *default value* is ```color.a```. 

These are the **shader blocks**:

- **color**:

```glsl
color = mix(vec4(CHEVRON_BACKGROUND_COLOR, CHEVRON_BACKGROUND_ALPHA),
            vec4(CHEVRON_COLOR, CHEVRON_ALPHA),
            step(.5,fract((v_texcoord.y+abs(v_texcoord.x-.5)) * CHEVRON_SCALE)*CHEVRON_SIZE));
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-dash](http://tangrams.github.io/blocks/#lines-dash) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/dash.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a stripe pattern to a line



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dash.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dash-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **DASH_SIZE**:  number between ```0.0``` and ```1.0``` that control the *size*. The *default value* is ```0.5```. 
 -  **DASH_SCALE**:  number between ```1.0``` and ```1000.0``` that control the *scale*. The *default value* is ```0.1```. 

These are the **shader blocks**:

- **filter**:

```glsl
if ( step(DASH_SIZE,fract(v_texcoord.y*DASH_SCALE)) == 0.){
    discard;
}
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/elevation.yaml&lines=59-63" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/elevation.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-datastream](http://tangrams.github.io/blocks/#lines-datastream) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/datastream.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply some stream of random lines to your lines



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/datastream.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/datastream-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **DATASTREAM_SPEED**:  number between ```0.0``` and ```1000.0``` that control the *speed*. The *default value* is ```20.0```. 
 -  **DATASTREAM_MARGIN**:  number between ```0.0``` and ```1.0``` that control the *lines margins*. The *default value* is ```0.4```. 
 -  **DATASTREAM_AMOUNT**:  number between ```0.0``` and ```1.0``` that control the *amount*. The *default value* is ```0.8```. 
 -  **DATASTREAM_ROADS**:  number between ```0.0``` and ```10.0``` that control the *number of roads*. The *default value* is ```5.0```. 
 -  **DATASTREAM_COLOR**:  The *default value* is ```vec3(1.)```. 
 -  **DATASTREAM_BACKGROUND_COLOR**:  The *default value* is ```color.rgb```. 

These are the **shader blocks**:

- **global**:
 + `float datastream_pattern(vec2 st, float v, float t) `
- **color**:

```glsl
color.rgb = mix(DATASTREAM_BACKGROUND_COLOR,
                DATASTREAM_COLOR,
                datastream_pattern( v_texcoord.xy, 
                                    u_time*(DATASTREAM_SPEED)*(-.5 * random(floor(v_texcoord.x*DATASTREAM_ROADS)) - .5), 
                                    DATASTREAM_AMOUNT )* 
                (step(DATASTREAM_MARGIN,1.-fract(v_texcoord.x*DATASTREAM_ROADS))*
                 step(DATASTREAM_MARGIN,fract(v_texcoord.x*DATASTREAM_ROADS))));
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-dots-glow](http://tangrams.github.io/blocks/#lines-dots-glow) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/dots-glow.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a dot pattern to a line with some glow



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dots-glow.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dots-glow-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **DOTS_SIZE**:  number between ```0.0``` and ```1.0``` that control the *size*. The *default value* is ```0.15```. 
 -  **DOTS_SCALE**:  number between ```0.0``` and ```2.0``` that control the *scale*. The *default value* is ```2.0```. 
 -  **DOTS_GLOW**:  number between ```0.0``` and ```1.0``` that control the *glow amount*. The *default value* is ```0.5```. 

These are the **shader blocks**:

- **color**:

```glsl
vec2 st = (fract(v_texcoord.xy)-.5)*DOTS_SCALE;
float df = dot(st,st);
color.a = 1.-step(DOTS_SIZE, df);
color.a += smoothstep(1.,0.,df)*(DOTS_GLOW);
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-dots](http://tangrams.github.io/blocks/#lines-dots) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/dots.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a dot pattern to a line



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dots.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dots-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **DOTS_SIZE**:  number between ```0.0``` and ```1.0``` that control the *size*. The *default value* is ```0.05```. 

These are the **shader blocks**:

- **color**:

```glsl
vec2 st = fract(v_texcoord.xy)-.5;
color.a = 1.- step(DOTS_SIZE, dot(st,st)*2.);
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-glow](http://tangrams.github.io/blocks/#lines-glow) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/glow.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Add an exciting glow effect to your



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/glow.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/glow-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **GLOW_WIDTH**:  number between ```0.0``` and ```1.0``` that control the *solid width*. The *default value* is ```0.4```. 
 -  **GLOW_BRIGHTNESS**:  number between ```0.0``` and ```1.0``` that control the *glow brightness*. The *default value* is ```0.25```. 

These are the **shader blocks**:

- **color**:

```glsl
vec4 glow_tmp_color = color;
color = glow_tmp_color*(aastep(GLOW_WIDTH,1.-v_texcoord.x)*aastep(GLOW_WIDTH,v_texcoord.x));
color += glow_tmp_color*(sin(v_texcoord.x*PI)*GLOW_BRIGHTNESS);
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-outline](http://tangrams.github.io/blocks/#lines-outline) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/outline.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply an outline to a line



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/outline.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/outline-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **OUTLINE_WIDTH**:  number between ```0.0``` and ```1.0``` that control the *width*. The *default value* is ```0.1```. 
 -  **OUTLINE_COLOR**:  The *default value* is ```color.rgb*.5```. 

These are the **shader blocks**:

- **color**:

```glsl
color.rgb = mix(color.rgb,
                OUTLINE_COLOR,
                (1.0-(aastep(OUTLINE_WIDTH,v_texcoord.x)-step(1.0-OUTLINE_WIDTH,v_texcoord.x))));
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/blueprint.yaml&lines=116-120" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/blueprint.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/callejas.yaml&lines=116" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/callejas.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-rainbow](http://tangrams.github.io/blocks/#lines-rainbow) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/rainbow.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a rainbow color pattern to a line



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/rainbow.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/rainbow-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **color**:

```glsl
color.rgb = hsb2rgb(vec3(v_texcoord.x,1.,1.));
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-stripes](http://tangrams.github.io/blocks/#lines-stripes) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/stripes.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a stripe pattern to a line



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/stripes.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/stripes-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **STRIPES_WIDTH**:  number between ```0.0``` and ```1.0``` that control the *width*. The *default value* is ```0.1```. 
 -  **STRIPES_COLOR**:  The *default value* is ```color.rgb*.5```. 
 -  **STRIPES_BACKGROUND_COLOR**:  The *default value* is ```color.rgb```. 

These are the **shader blocks**:

- **color**:

```glsl
color.rgb = mix(STRIPES_BACKGROUND_COLOR,
                STRIPES_COLOR,
                step(STRIPES_WIDTH, sin((fract(v_texcoord).x+fract(v_texcoord).y) * 6.283)));
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/grain-roads.yaml&lines=35" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/grain-roads.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)


### [PATTERNS](http://tangrams.github.io/blocks/#patterns) <a href="https://github.com/tangrams/blocks/blob/gh-pages/patterns" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

#### [patterns-dots](http://tangrams.github.io/blocks/#patterns-dots) <a href="https://github.com/tangrams/blocks/blob/gh-pages/patterns/dots.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw dot patterns that animate between zoom levels. To learn more about patterns check [this chapter from the Book of Shaders](https://thebookofshaders.com/09/)    



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/dots.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/dots-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float TileDots(float scale, float size) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [patterns-grid](http://tangrams.github.io/blocks/#patterns-grid) <a href="https://github.com/tangrams/blocks/blob/gh-pages/patterns/grid.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw grids. To learn more about patterns check [this chapter from the Book of Shaders](https://thebookofshaders.com/09/)    



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/grid.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/grid-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `bool grid (vec2 st, float res, float press) `
 + `bool grid (vec2 st, float res) `
 + `float tileGrid (float res) `
 + `float tileGrid() `

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/blueprint.yaml&lines=75-76" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/blueprint.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/grain.yaml&lines=15" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/grain.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [patterns-stripes](http://tangrams.github.io/blocks/#patterns-stripes) <a href="https://github.com/tangrams/blocks/blob/gh-pages/patterns/stripes.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw stripes. To learn more about patterns check [this chapter from the Book of Shaders](https://thebookofshaders.com/09/)    



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/stripes.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/stripes-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **PI**:  The *default value* is ```3.14159265359```. 

These are the **shader blocks**:

- **global**:
 + `float stripesDF (vec2 st) `
 + `float stripes (vec2 st, float width) `
 + `float stripes (vec2 st, float width, float angle) `
 + `float diagonalStripes (vec2 st) `
 + `float diagonalStripes (vec2 st, float width) `

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/press.yaml&lines=150" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/press.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/radar.yaml" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/radar.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/grain-area.yaml&lines=26" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/grain-area.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [patterns-waves](http://tangrams.github.io/blocks/#patterns-waves) <a href="https://github.com/tangrams/blocks/blob/gh-pages/patterns/waves.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw wavy stripes. To learn more about patterns check [this chapter from the Book of Shaders](https://thebookofshaders.com/09/) 



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/waves.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/waves-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float wavesDF (vec2 st, float freq, float amp) `
 + `float waves (vec2 st, float freq, float amp, float width) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [patterns-zigzag](http://tangrams.github.io/blocks/#patterns-zigzag) <a href="https://github.com/tangrams/blocks/blob/gh-pages/patterns/zigzag.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw zigzag stripes. To learn more about patterns check [this chapter from the Book of Shaders](https://thebookofshaders.com/09/) 



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/zigzag.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/zigzag-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float zigzagDF (vec2 st, float freq) `
 + `float zigzag (vec2 st, float freq, float width) `

![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)


### [POINTS](http://tangrams.github.io/blocks/#points) <a href="https://github.com/tangrams/blocks/blob/gh-pages/points" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

#### [points-cross](http://tangrams.github.io/blocks/#points-cross) <a href="https://github.com/tangrams/blocks/blob/gh-pages/points/cross.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Draws a '+' shape in each point. To learn more about shapes on shaders read [this chapter from The Nook of Shader](http://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/points/cross.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/points/cross-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **CROSS_ALPHA**:  number between ```0.0``` and ```1.0``` that control the *alpha*. The *default value* is ```0.75```. 

These are the **shader blocks**:

- **color**:

```glsl
color.a = clamp(cross(v_texcoord.xy,vec2(2.,.5)),0.,1.)*CROSS_ALPHA;

```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/callejas.yaml&lines=96-99" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/callejas.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [points-glow](http://tangrams.github.io/blocks/#points-glow) <a href="https://github.com/tangrams/blocks/blob/gh-pages/points/glow.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/points/glow.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/points/glow-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **filter**:

```glsl
float b = getBrightness(color.rgb);
vec2 st = v_texcoord.xy;
color = mix(v_color*color.a,vec4(0.),b*b);
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [points-shape](http://tangrams.github.io/blocks/#points-shape) <a href="https://github.com/tangrams/blocks/blob/gh-pages/points/shape.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Draws shape with N amount of sides (`SHAPE_SIDES`), a colored border (`SHAPE_BORDER_WIDTH` & `SHAPE_BORDER_COLOR`). To learn more about shapes on shaders read [this chapter from The Nook of Shader](http://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/points/shape.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/points/shape-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **SHAPE_ALPHA**:  number between ```0.0``` and ```1.0``` that control the *alpha*. The *default value* is ```1.0```. 
 -  **SHAPE_BORDER_WIDTH**:  number between ```0.0``` and ```1.0``` that control the *size*. The *default value* is ```0.15```. 
 -  **SHAPE_SIDES**:  number between ```1.0``` and ```6.0``` that control the *corners*. The *default value* is ```3```. 
 -  **SHAPE_BORDER_COLOR**:  The *default value* is ```vec3(1.)```. 
 -  **SHAPE_SIZE**:  number between ```0.0``` and ```1.0``` that control the *size*. The *default value* is ```1.0```. 

These are the **shader blocks**:

- **color**:

```glsl
float df = shapeDF(vec2(v_texcoord.x,1.-v_texcoord.y),int(SHAPE_SIDES));
color.rgb = mix(color.rgb,
                SHAPE_BORDER_COLOR,
                aastep(SHAPE_SIZE*.5-SHAPE_BORDER_WIDTH,df));
color.a = (1.-aastep(SHAPE_SIZE*.5,df))*SHAPE_ALPHA;
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/elevation-places.yaml&lines=29-36" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/elevation-places.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)


### [POLYGONS](http://tangrams.github.io/blocks/#polygons) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

#### [polygons-diagonal-dash](http://tangrams.github.io/blocks/#polygons-diagonal-dash) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/diagonal-dash.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a diagonal dash pattern to the polygon style. To learn more about patterns check [this chapter from the Book of Shaders](https://thebookofshaders.com/09/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/diagonal-dash.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/diagonal-dash-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **DASH_SIZE**:  number between ```0.0``` and ```1.0``` that control the *alpha*. The *default value* is ```0.9```. 
 -  **DASH_BACKGROUND_COLOR**:  The *default value* is ```color.rgb```. 
 -  **DASH_SCALE**:  number between ```1.0``` and ```1000.0``` that control the *scale*. The *default value* is ```10.0```. 
 -  **DASH_COLOR**:  The *default value* is ```color.rgb*.5```. 
 -  **DASH_TYPE**:  variable that control the *type* with one of the following values: ```fill, stroke```. The *default value* is ```fill```. 
 -  **DASH_TILE_STYLE**:  variable that control the *tile type* with one of the following values: ```tile, brick```. The *default value* is ```tile```. 

These are the **shader blocks**:

- **global**:
 + `float dashDF(vec2 st) `
- **color**:

```glsl
color.rgb = mix(DASH_BACKGROUND_COLOR, 
                DASH_COLOR, 
                DASH_TYPE( DASH_SIZE, dashDF(DASH_TILE_STYLE(getTileCoords()*DASH_SCALE,3.))) );
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [polygons-diagonal-grid](http://tangrams.github.io/blocks/#polygons-diagonal-grid) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/diagonal-grid.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a diagonal grid pattern to the polygon style. To learn more about patterns check [this chapter from the Book of Shaders](https://thebookofshaders.com/09/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/diagonal-grid.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/diagonal-grid-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **GRID_SCALE**:  number between ```1.0``` and ```1000.0``` that control the *scale*. The *default value* is ```20.0```. 
 -  **GRID_COLOR**:  The *default value* is ```color.rgb```. 
 -  **GRID_BACKGROUND_COLOR**:  The *default value* is ```color.rgb*.5```. 
 -  **GRID_WIDTH**:  number between ```0.0``` and ```1.0``` that control the *width*. The *default value* is ```0.05```. 

These are the **shader blocks**:

- **color**:

```glsl
color.rgb = mix(GRID_COLOR, 
                GRID_BACKGROUND_COLOR, 
                diagonalGrid(   fract(getTileCoords()*GRID_SCALE),
                                GRID_WIDTH));
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [polygons-diagonal-stripes](http://tangrams.github.io/blocks/#polygons-diagonal-stripes) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/diagonal-stripes.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a diagonal stripe pattern to the polygon style. To learn more about patterns check [this chapter from the Book of Shaders](https://thebookofshaders.com/09/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/diagonal-stripes.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/diagonal-stripes-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **STRIPES_ALPHA**:  number between ```0.0``` and ```1.0``` that control the *alpha*. The *default value* is ```1.0```. 
 -  **STRIPES_SCALE**:  number between ```1.0``` and ```1000.0``` that control the *scale*. The *default value* is ```2.0```. 
 -  **STRIPES_WIDTH**:  number between ```0.0``` and ```1.0``` that control the *alpha*. The *default value* is ```0.5```. 

These are the **shader blocks**:

- **color**:

```glsl
color.a = diagonalStripes( (getTileCoords()*0.9999)*floor(STRIPES_SCALE), 
                            STRIPES_WIDTH) * STRIPES_ALPHA;
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [polygons-dots](http://tangrams.github.io/blocks/#polygons-dots) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/dots.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply dot patterns to a polygon. To learn more about patterns check [this chapter from the Book of Shaders](https://thebookofshaders.com/09/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/dots.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/dots-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **DOTS_SIZE**:  number between ```0.0``` and ```1.0``` that control the *size*. The *default value* is ```0.41```. 
 -  **DOTS_TYPE**:  variable that control the *type* with one of the following values: ```fill, stroke```. The *default value* is ```fill```. 
 -  **DOTS_TILE_STYLE**:  variable that control the *tile type* with one of the following values: ```tile, brick```. The *default value* is ```brick```. 
 -  **DOTS_SCALE**:  number between ```1.0``` and ```1000.0``` that control the *scale*. The *default value* is ```10.0```. 
 -  **DOTS_BACKGROUND_COLOR**:  The *default value* is ```color.rgb```. 
 -  **DOTS_COLOR**:  The *default value* is ```color.rgb*.5```. 

These are the **shader blocks**:

- **color**:

```glsl
color.rgb = mix(DOTS_BACKGROUND_COLOR, 
                DOTS_COLOR, 
                DOTS_TYPE( DOTS_SIZE, circleDF(vec2(0.5)-DOTS_TILE_STYLE(getTileCoords()*DOTS_SCALE,2.))) );
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [polygons-glass-walls](http://tangrams.github.io/blocks/#polygons-glass-walls) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/glass-walls.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a glass walls to the sides of a geometry



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/glass-walls.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/glass-walls-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **color**:

```glsl
color.rgb *= vec3(min((worldPosition().z*.001 + .5),1.));

if (isWall()) {
    vec2 st = vec2(v_texcoord.x*10.,worldPosition().z*0.2);
    vec2 ipos = floor(st);
    vec2 fpos = fract(st);
    if ( step(0.01,fpos.x)*step(0.1,fpos.y) > 0.0 ){
        material.specular = vec4(1.) * max( 1.-(worldPosition().z*.001 + .5), 0. );
        material.emission = vec4(0.957,0.988,0.976,1.0) * step(.5,random(ipos*vec2(0.0000001,0.01)+floor(worldNormal().xy*10.0)));
        material.emission *= vec4(0.988,0.983,0.880,1.0) * step(.5,random(ipos));
    }
}

```


- **filter**:

```glsl
color.rgb += vec3(1.)* min( 1.-(worldPosition().z*.001 + .7) , 0.5 );
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/gotham.yaml&lines=131" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/gotham.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [polygons-pixelate](http://tangrams.github.io/blocks/#polygons-pixelate) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/pixelate.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a random pixelated pattern to the polygon style. To learn more about patterns or random check [this chapter](https://thebookofshaders.com/09/) or  [this other chapter from the Book of Shaders](https://thebookofshaders.com/10/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/pixelate.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/pixelate-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **PIXELATE_BACKGROUND_COLOR**:  The *default value* is ```color.rgb```. 
 -  **PIXELATE_SCALE**:  number between ```1.0``` and ```1000.0``` that control the *scale*. The *default value* is ```40.0```. 
 -  **PIXELATE_COLOR**:  The *default value* is ```color.rgb*.5```. 

These are the **shader blocks**:

- **color**:

```glsl
color.rgb = mix(PIXELATE_BACKGROUND_COLOR,
                PIXELATE_COLOR,
                random(floor(getTileCoords()*PIXELATE_SCALE)));
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [polygons-shimmering](http://tangrams.github.io/blocks/#polygons-shimmering) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/shimmering.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a shimmering radom pattern of simplex grid triangles to the polygon style. To learn more about noise and simplex grid check [this chapter from the Book of Shaders](https://thebookofshaders.com/11/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/shimmering.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/shimmering-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **SHIMMERING_SPEED**:  number between ```0.0``` and ```1.0``` that control the *speed*. The *default value* is ```0.1```. 
 -  **SHIMMERING_COLOR**:  The *default value* is ```color.rgb```. 
 -  **SHIMMERING_ANIMATED**:  The *default value* is ```True```. 
 -  **SHIMMERING_SCALE**:  number between ```1.0``` and ```1000.0``` that control the *scale*. The *default value* is ```10.0```. 
 -  **SHIMMERING_BACKGROUND_COLOR**:  The *default value* is ```color.rgb*.5```. 
 -  **SHIMMERING_AMOUNT**:  number between ```0.0``` and ```1.0``` that control the *amount*. The *default value* is ```1.0```. 

These are the **shader blocks**:

- **color**:

```glsl
vec2 st = getConstantCoords()*SHIMMERING_SCALE;
vec2 s = skew(st);
vec2 s_f = fract(s);
#ifdef SHIMMERING_ANIMATED
float n = snoise(vec3(floor(s+step(s_f.x,s_f.y)*5.),u_time*SHIMMERING_SPEED));
#else
float n = snoise(floor(s+step(s_f.x,s_f.y)*5.));
#endif
color.rgb = mix(SHIMMERING_COLOR,
                mix(SHIMMERING_BACKGROUND_COLOR,SHIMMERING_COLOR,n),
                SHIMMERING_AMOUNT);
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [polygons-stripes](http://tangrams.github.io/blocks/#polygons-stripes) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/stripes.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply stripe pattern to the polygon style. To learn more about patterns check [this chapter from the Book of Shaders](https://thebookofshaders.com/09/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/stripes.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/stripes-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **STRIPES_WIDTH**:  number between ```0.0``` and ```1.0``` that control the *width*. The *default value* is ```0.5```. 
 -  **STRIPES_ANGLE**:  number between ```0.0``` and ```3.1415``` that control the *angle (radiants)*. The *default value* is ```PI*0.25```. 
 -  **STRIPES_SCALE**:  number between ```1.0``` and ```1000.0``` that control the *scale*. The *default value* is ```2.0```. 
 -  **STRIPES_ALPHA**:  number between ```0.0``` and ```1.0``` that control the *amount*. The *default value* is ```0.5```. 

These are the **shader blocks**:

- **color**:

```glsl
color.a = stripes(  getTileCoords()*STRIPES_SCALE, 
                    STRIPES_WIDTH, 
                    STRIPES_ANGLE)*STRIPES_ALPHA;
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [polygons-windows](http://tangrams.github.io/blocks/#polygons-windows) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/windows.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a windows patterns on the walls of a geometry



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/windows.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/windows-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **color**:

```glsl
color.rgb *= vec3(min((worldPosition().z*.001 + .5),1.));
float t = 0.5;
if (isWall()) {
    vec2 st = vec2(v_texcoord.x*10.,worldPosition().z*0.2);
    vec2 ipos = floor(st);
    vec2 fpos = fract(st);
    if ( step(0.6,fpos.x)*step(0.4,fpos.y) > 0.0 ){
        material.specular = vec4(1.) * max( 1.-(worldPosition().z*.001 + .5), 0. );
        material.emission = vec4(0.988,0.983,0.880,1.0) * step(.5,random(ipos+floor(worldNormal().xy*10.0)+t));
    }
}

```


- **filter**:

```glsl
color.rgb += vec3(1.)* min( 1.-(worldPosition().z*.001 + .7) , 0.5 );
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/gotham.yaml&lines=128" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/gotham.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)


### [SHAPES](http://tangrams.github.io/blocks/#shapes) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

#### [shapes-circle](http://tangrams.github.io/blocks/#shapes-circle) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/circle.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw circles. To learn more about how to make shapes on shaders go to From check [this chapter about shapes from the Book of Shaders](https://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/circle.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/circle-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float circleDF (vec2 st) `
 + `float circle (vec2 st, float radius) `
 + `float circleBorder (vec2 st, float radius) `

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/patterns.yaml&lines=146" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/patterns.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/nursery.yaml&lines=146" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/nursery.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/lego.yaml&lines=109-110" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/lego.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-cross](http://tangrams.github.io/blocks/#shapes-cross) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/cross.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw crosses. To learn more about how to make shapes on shaders go to From check [this chapter about shapes from the Book of Shaders](https://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/cross.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/cross-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float cross (vec2 st, float size, float width) `
 + `float cross (in vec2 st, float _size) `
 + `float cross (in vec2 st, vec2 _size) `

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/9845C.yaml&lines=181-183" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/9845C.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/oblivion.yaml&lines=155-156" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/oblivion.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/matrix.yaml&lines=101-104" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/matrix.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/tron.yaml&lines=122" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/tron.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-digits](http://tangrams.github.io/blocks/#shapes-digits) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/digits.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw number digits.



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/digits.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/digits-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **CHAR_DECIMAL_POINT**:  The *default value* is ```10.0```. 
 -  **CHAR_MINUS**:  The *default value* is ```11.0```. 
 -  **CHAR_BLANK**:  The *default value* is ```12.0```. 

These are the **shader blocks**:

- **global**:
 + `float SampleDigit (const in float fDigit, const in vec2 vUV) `
 + `float PrintValue (const in vec2 vStringCharCoords, const in float fValue, const in float fMaxDigits, const in float fDecimalPlaces) `
 + `float PrintValue (in vec2 fragCoord, const in vec2 vPixelCoords, const in vec2 vFontSize, const in float fValue, const in float fMaxDigits, const in float fDecimalPlaces) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-polygons](http://tangrams.github.io/blocks/#shapes-polygons) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/polygons.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw polygons. To learn more about how to make shapes on shaders go to From check [this chapter about shapes from the Book of Shaders](https://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/polygons.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/polygons-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float shapeDF (vec2 st, int N) `
 + `float shape (vec2 st, int N, float width) `
 + `float shapeBorder (vec2 st, int N, float width) `

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/9845C.yaml&lines=153" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/9845C.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-rect](http://tangrams.github.io/blocks/#shapes-rect) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/rect.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw rectangles. To learn more about how to make shapes on shaders go to From check [this chapter about shapes from the Book of Shaders](https://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/rect.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/rect-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float rectDF (in vec2 st, in vec2 size) `
 + `float rectDF (in vec2 st, in float size) `
 + `float rect (in vec2 st, in vec2 size, in float radio) `
 + `float rect (vec2 st, float size, float radio) `
 + `float rectBorder (in vec2 st, in vec2 size, in float radio) `
 + `float rectBorder (vec2 st, float size, float radio) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-simplex](http://tangrams.github.io/blocks/#shapes-simplex) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/simplex.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw shapes using a simplex grid. To learn more about simplex grids check [this chapter about noise from the Book of Shaders](https://thebookofshaders.com/11/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/simplex.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/simplex-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float warp (vec3 S) `
 + `float circle (vec3 S) `
 + `float triangle (vec3 S) `
 + `vec3 star (vec3 S) `
 + `vec3 sakura (vec3 S) `
 + `float lotus (vec3 S, float petals_size, float roundness) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-type](http://tangrams.github.io/blocks/#shapes-type) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/type.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

This block provides to functions `fill` and `stroke`. Each one transform a SDF to a fill shape or a stroke shape (border). The stroke width can be control with the define `STROKE`. 
To learn more about how to make shapes on shaders go to From check [this chapter about shapes from the Book of Shaders](https://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/type.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/type-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **STROKE**:  The *default value* is ```0.15```. 

These are the **shader blocks**:

- **global**:
 + `float fill (in float size, in float x) `
 + `float stroke (in float size, in float x) `

![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)


### [SPACE](http://tangrams.github.io/blocks/#space) <a href="https://github.com/tangrams/blocks/blob/gh-pages/space" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

#### [space-constant](http://tangrams.github.io/blocks/#space-constant) <a href="https://github.com/tangrams/blocks/blob/gh-pages/space/constant.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Get the constant coordinates **(warning: could glitch on zooms)**



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/space/constant.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/space/constant-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec2 getConstantCoords () `

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/grain-area.yaml&lines=26" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/grain-area.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [space-screen](http://tangrams.github.io/blocks/#space-screen) <a href="https://github.com/tangrams/blocks/blob/gh-pages/space/screen.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Get the coordinates in screen space streaching the proportion ('vec2 getScreenCoords ()') or non-streatching the proportion ('getScreenNonStretchCoords ()')



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/space/screen.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/space/screen-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec2 getScreenCoords () `
 + `vec2 getScreenNonStretchCoords () `

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/press.yaml&lines=136-145" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/press.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/radar.yaml&lines=0-143" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/radar.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [space-tex](http://tangrams.github.io/blocks/#space-tex) <a href="https://github.com/tangrams/blocks/blob/gh-pages/space/tex.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Get the position on TexCoords



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/space/tex.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/space/tex-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec2 getTexCoords () `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [space-tile](http://tangrams.github.io/blocks/#space-tile) <a href="https://github.com/tangrams/blocks/blob/gh-pages/space/tile.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Get the position on the tile



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/space/tile.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/space/tile-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec2 getTileCoords() `
- **position**:

```glsl
// Normalize the attribute position of a vertex
v_pos = modelPosition().xyz;
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [space-uz](http://tangrams.github.io/blocks/#space-uz) <a href="https://github.com/tangrams/blocks/blob/gh-pages/space/uz.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Get the position on UZ from the TexCoords (on `x`) and the `z` of the World Position



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/space/uz.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/space/uz-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec2 getUZCoords () `

![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)


### [TERRAIN](http://tangrams.github.io/blocks/#terrain) <a href="https://github.com/tangrams/blocks/blob/gh-pages/terrain" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

#### [terrain-base](http://tangrams.github.io/blocks/#terrain-base) <a href="https://github.com/tangrams/blocks/blob/gh-pages/terrain/base.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/base.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/base-full.yaml
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrain-geometry](http://tangrams.github.io/blocks/#terrain-geometry) <a href="https://github.com/tangrams/blocks/blob/gh-pages/terrain/geometry.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/geometry.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/geometry-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **TERRAIN_TEXTURE_INDEX**:  The *default value* is ```0```. 
 -  **TERRAIN_ZOFFSET**:  The *default value* is ```0.0```. 

These are the **shader blocks**:

- **global**:
 + `float getHeight() `
- **position**:

```glsl
position.z += TERRAIN_ZOFFSET*u_meters_per_pixel;
position.z += getHeight();
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrain-lines](http://tangrams.github.io/blocks/#terrain-lines) <a href="https://github.com/tangrams/blocks/blob/gh-pages/terrain/lines.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/lines.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/lines-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **TERRAIN_ZOFFSET**:  The *default value* is ```1.5```. 


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrain-polygons](http://tangrams.github.io/blocks/#terrain-polygons) <a href="https://github.com/tangrams/blocks/blob/gh-pages/terrain/polygons.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/polygons.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/polygons-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **TERRAIN_ZOFFSET**:  The *default value* is ```1.0```. 


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrain-terrain](http://tangrams.github.io/blocks/#terrain-terrain) <a href="https://github.com/tangrams/blocks/blob/gh-pages/terrain/terrain.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/terrain.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/terrain-full.yaml
```



![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)


### [TEXTURE](http://tangrams.github.io/blocks/#texture) <a href="https://github.com/tangrams/blocks/blob/gh-pages/texture" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

#### [texture-non-repetitive](http://tangrams.github.io/blocks/#texture-non-repetitive) <a href="https://github.com/tangrams/blocks/blob/gh-pages/texture/non-repetitive.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/texture/non-repetitive.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/texture/non-repetitive-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec4 NonRepetitiveTexture (sampler2D tex, vec2 x, float v) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [texture-zoom-fade](http://tangrams.github.io/blocks/#texture-zoom-fade) <a href="https://github.com/tangrams/blocks/blob/gh-pages/texture/zoom-fade.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Tile a texture across zoom levels by fading between them



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/texture/zoom-fade.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/texture/zoom-fade-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec4 TileTexture (sampler2D tex, float scale) `

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/crosshatch.yaml&lines=76" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/crosshatch.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/pericoli.yaml&lines=121" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/pericoli.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)


### [TILING](http://tangrams.github.io/blocks/#tiling) <a href="https://github.com/tangrams/blocks/blob/gh-pages/tiling" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

#### [tiling-brick](http://tangrams.github.io/blocks/#tiling-brick) <a href="https://github.com/tangrams/blocks/blob/gh-pages/tiling/brick.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Repeats a coordinate space (`vec2 st`) in diferent brick-like tiles N times (`float zoom`). For more information about tilling patterns read [this chapter of The Book of Shaders](https://thebookofshaders.com/09/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/brick.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/brick-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec2 brick (vec2 st, float zoom) `

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/patterns.yaml&lines=130" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/patterns.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/nursery.yaml&lines=99" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/nursery.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [tiling-simplex](http://tangrams.github.io/blocks/#tiling-simplex) <a href="https://github.com/tangrams/blocks/blob/gh-pages/tiling/simplex.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Repeats a coordinate space (`vec2 st`) in diferent simplex tiles. To learn more about simplex grids check [this chapter about noise from the Book of Shaders](https://thebookofshaders.com/11/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/simplex.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/simplex-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec2 skew (vec2 st) `
 + `vec3 simplexCoord (vec2 st, float td) `
 + `vec3 simplexGrid (vec2 st) `
 + `vec3 simplexRotatedGrid (vec2 st) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [tiling-tile](http://tangrams.github.io/blocks/#tiling-tile) <a href="https://github.com/tangrams/blocks/blob/gh-pages/tiling/tile.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Repeats a coordinate space (`vec2 st`) in diferent brick-like tiles N times (`float zoom`). For more information about tilling patterns read [this chapter of The Book of Shaders](https://thebookofshaders.com/09/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/tile.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/tile-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec2 tile (vec2 st, float zoom) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [tiling-truchet](http://tangrams.github.io/blocks/#tiling-truchet) <a href="https://github.com/tangrams/blocks/blob/gh-pages/tiling/truchet.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Repeats a coordinate space (`vec2 st`) in diferent tiles acording to a Truchet patern.
There is two way to do this: by mirroring the spaces (`vec2 truchetMirror (vec2 st)`) or rotating them ('vec2 truchetRotate (vec2 st)')



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/truchet.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/truchet-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **PI**:  The *default value* is ```3.14159265359```. 

These are the **shader blocks**:

- **global**:
 + `vec2 truchetMirror (vec2 st) `
 + `vec2 truchetRotate (vec2 st) `

![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)
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
