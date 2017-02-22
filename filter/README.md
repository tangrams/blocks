

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
 + `float grain ()`
- **filter**:

```glsl
// Apply the grain in the amount defined on GRAIN_AMOUNT
color.rgb = color.rgb GRAIN_BLEND (grain()*GRAIN_AMOUNT);

```



Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./filter/test/filter-grain.png)](http://tangrams.github.io/blocks/test.html?test=./filter/test/filter-grain.json)

- **grain** ( mean: 0.0808475447799 median: 0.080916 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./filter/test/grain-grain.frag"><img src="http://tangrams.github.io/blocks/./filter/test/grain-grain.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color = texture2D(u_tex0,v_texcoord.xy);
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



Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./filter/test/filter-grid.png)](http://tangrams.github.io/blocks/test.html?test=./filter/test/filter-grid.json)

- **grid** ( mean: 0.00300891284167 median: 0.003008 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./filter/test/grid-grid.frag"><img src="http://tangrams.github.io/blocks/./filter/test/grid-grid.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define v_pos v_texcoord
...
// Color:
    color = texture2D(u_tex0,v_texcoord.xy);
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
 -  **u_hatchmap**:  The *default value* is ```https://tangrams.github.io/blocks/filter/imgs/hatch.png```. 

These are the **shader blocks**:

- **global**:
 + `float getHatch (vec2 st, float brightness)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./filter/test/filter-hatch.png)](http://tangrams.github.io/blocks/test.html?test=./filter/test/filter-hatch.json)

- **hatch** ( mean: 0.0125426022875 median: 0.01236 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./filter/test/hatch-hatch.frag"><img src="http://tangrams.github.io/blocks/./filter/test/hatch-hatch.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
float brightness = texture2D(u_tex0,v_texcoord.xy).r;
color.rgb = vec3(1.);
color.rgb -= getHatch(v_texcoord.xy*10., brightness);

```


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
 + `vec3 getLut (vec3 textureColor, sampler2D lookupTable)`
 + `vec3 getLut (vec3 textureColor)`
- **filter**:

```glsl
color.rgb = mix(color.rgb,
                getLut(color.rgb),
                LUT_AMOUNT);
```



Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./filter/test/filter-lut.png)](http://tangrams.github.io/blocks/test.html?test=./filter/test/filter-lut.json)

- **lut** ( mean: 0.00844491654321 median: 0.008673 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./filter/test/lut-lut.frag"><img src="http://tangrams.github.io/blocks/./filter/test/lut-lut.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color = texture2D(u_tex0,v_texcoord.xy);
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



Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./filter/test/filter-tv.png)](http://tangrams.github.io/blocks/test.html?test=./filter/test/filter-tv.json)

- **tv** ( mean: 0.00291611334028 median: 0.002553 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./filter/test/tv-tv.frag"><img src="http://tangrams.github.io/blocks/./filter/test/tv-tv.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color = texture2D(u_tex0,v_texcoord.xy);
```


Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/9845C.yaml" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/9845C.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
