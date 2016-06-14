

#### [generative-caustic](https://github.com/tangrams/blocks/blob/gh-pages/generative/caustics.yaml)

Caustic generative texture inspired on <https://www.shadertoy.com/view/MdlXz8> by David Hoskins



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/caustics.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **TAU**: ```6.28318530718```
 - **CAUSTIC_ITERATIONS**: ```3```

These are the **shader blocks**:

- **global**:
 + `vec3 getCaustic (vec2 uv) `
 + `int n = 0; n < int(CAUSTIC_ITERATIONS); n++) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [generative-fbm](https://github.com/tangrams/blocks/blob/gh-pages/generative/fbm.yaml)

Set of Fractal Brownian Motion functions.
For more information on this theme read [this chapter of The Book of Shaders about fractal Brownian Motion](http://thebookofshaders.com/13/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/fbm.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **NUM_OCTAVES**: ```5```

These are the **shader blocks**:

- **global**:
 + `float fbm (in float x) `
 + `int i = 0; i < int(NUM_OCTAVES); ++i) `
 + `float fbm (in vec2 xy) `
 + `int i = 0; i < int(NUM_OCTAVES); ++i) `
 + `float fbm (in vec3 xyz) `
 + `int i = 0; i < int(NUM_OCTAVES); ++i) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [generative-noise](https://github.com/tangrams/blocks/blob/gh-pages/generative/noise.yaml)

Set of Noise functions.
For more information on this theme read [this chapter of The Book of Shaders about Noise](http://thebookofshaders.com/11/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/noise.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `float noise (in float x) `
 + `float noise (vec2 xy) `
 + `float noise (vec3 xyz) `
 + `float snoise (vec3 p) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [generative-random](https://github.com/tangrams/blocks/blob/gh-pages/generative/random.yaml)

Set of functions about random.
For more information on this theme read [this chapter of The Book of Shaders about Random](http://thebookofshaders.com/10/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/random.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `float random (float x) `
 + `float random (vec2 p) `
 + `float random (vec3 p) `
 + `vec2 random2 (vec2 xy) `
 + `vec3 random3 (vec2 xy) `
 + `vec3 random3 (vec3 c) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [generative-voronoi](https://github.com/tangrams/blocks/blob/gh-pages/generative/voronoi.yaml)

Set of Voronoi functions.
For more information on this theme read [this chapter of The Book of Shaders about Cellular Noise and Voronoi](http://thebookofshaders.com/12/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/voronoi.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `vec3 voronoi (vec2 st) `
