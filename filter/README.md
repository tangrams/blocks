

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
