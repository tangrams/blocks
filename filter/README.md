

### [filter-grain](https://github.com/tangrams/blocks/blob/gh-pages/filter/grain.yaml)

Apply a lens grain effect to the scene.
The amount can be set by the GRAIN_AMOUNT define [0.0~1.0]

This provides the following blocks:

- **filter**:

```glsl
// Apply the grain in the amount defined on GRAIN_AMOUNT
color.rgb -= grain()*GRAIN_AMOUNT;

```


- **global**:

This blocks have the following defines you can use or tweak:
 - **GRAIN_AMOUNT**: ```0.3```


Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./filter./filter/grain.yaml
```




### [filter-hatch](https://github.com/tangrams/blocks/blob/gh-pages/filter/hatch.yaml)

Hatching filter based on [Jaume's Sanchez](https://twitter.com/thespite?lang=en) [Cross-hatching GLSL shader](https://www.clicktorelease.com/code/cross-hatching/). 
Giving a brightness level it provides a fragment of the following table of textures:
![](https://cdn.rawgit.com/tangrams/blocks/gh-pages/filter/imgs/hatch.png)

This provides the following blocks:

- **global**:

Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./filter./filter/hatch.yaml
```




### [filter-height](https://github.com/tangrams/blocks/blob/gh-pages/filter/height.yaml)

This provides the following blocks:

- **color**:

```glsl
color.rgb *= min((worldPosition().z*.001 + .5),1.);
```



Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./filter./filter/height.yaml
```




### [filter-lut](https://github.com/tangrams/blocks/blob/gh-pages/filter/lut.yaml)

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

Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./filter./filter/lut.yaml
```




### [filter-tv](https://github.com/tangrams/blocks/blob/gh-pages/filter/tv.yaml)

This provides the following blocks:

- **filter**:

```glsl
color *= abs(cos((gl_FragCoord.y*TV_FREQ+u_time*5.)));

```



This blocks have the following defines you can use or tweak:
 - **TV_FREQ**: ```1.2```


Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./filter./filter/tv.yaml
```


