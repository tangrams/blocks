

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


