

#### [filter-grain](http://tangrams.github.io/blocks/#filter-grain) <a href="https://github.com/tangrams/blocks/blob/gh-pages/filter/grain.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a lens grain effect to the scene.
The amount can be set by the GRAIN_AMOUNT define [0.0~1.0]



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


This blocks use a custom **shader**.These are the defaults **defines**:
 - **GRAIN_AMOUNT**: ```0.3```

These are the **shader blocks**:

- **global**:
 + `float grain () `
- **filter**:

```glsl
// Apply the grain in the amount defined on GRAIN_AMOUNT
color.rgb -= grain()*GRAIN_AMOUNT;

```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/grain.yaml&lines=29" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/grain.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [filter-grid](http://tangrams.github.io/blocks/#filter-grid) <a href="https://github.com/tangrams/blocks/blob/gh-pages/filter/grid.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a grid filter to they syle
<p>The amount can be set by the GRID_AMOUNT define [0.0~1.0]</p>
<p>Then you should choose between the modes: ```GRID_ADD```, ```GRID_SUBSTRACT``` and ```GRID_MULTIPLY```</p>



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


This blocks use a custom **shader**.These are the defaults **defines**:
 - **GRID_AMOUNT**: ```0.2```
 - **GRID_SUBSTRACT**: ```False```
 - **GRID_ADD**: ```True```
 - **GRID_MULTIPLY**: ```False```

These are the **shader blocks**:

- **filter**:

```glsl
#ifdef GRID_ADD
color.rgb += tileGrid()*GRID_AMOUNT;
#endif
#ifdef GRID_SUBSTRACT
color.rgb -= tileGrid()*GRID_AMOUNT;
#endif
#ifdef GRID_MULTIPLY
color.rgb *= tileGrid()*GRID_AMOUNT;
#endif

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


This blocks use a custom **shader**.This are the **uniforms**:
 - **u_hatchmap**: ```imgs/hatch.png```

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

Adds a dark gradiant to the geometries conform they aproach to height 0.



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


This blocks use a custom **shader**.These are the **shader blocks**:

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

Add a look up table filter defined on the uniform ```u_lut``` to the current style. This look up tables are hable to produce similar effect to instagram filters.



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


This blocks use a custom **shader**.This are the **uniforms**:
 - **u_lut**: ```imgs/lut-0001.png```

These are the **shader blocks**:

- **global**:
 + `vec4 getLut (vec3 textureColor, sampler2D lookupTable) `
 + `vec4 getLut (vec3 textureColor) `
 + `vec4 getLut (vec4 textureColor, sampler2D lookupTable) `
 + `vec4 getLut (vec4 textureColor) `
- **filter**:

```glsl
color = getLut(color);
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/sandbox-lut.yaml" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/sandbox-lut.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [filter-tv](http://tangrams.github.io/blocks/#filter-tv) <a href="https://github.com/tangrams/blocks/blob/gh-pages/filter/tv.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a old TV effect to the style.



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


This blocks use a custom **shader**.These are the defaults **defines**:
 - **TV_FREQ**: ```1.2```

These are the **shader blocks**:

- **filter**:

```glsl
color *= abs(cos((gl_FragCoord.y*TV_FREQ+u_time*5.)));

```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/9845C.yaml" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/9845C.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
