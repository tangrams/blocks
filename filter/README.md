

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


