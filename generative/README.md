

### [generative-fbm](https://github.com/tangrams/blocks/blob/gh-pages/generative/fbm.yaml)

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
    - http://tangrams.github.io/blocks/generative/fbm.yaml
```




### [generative-noise](https://github.com/tangrams/blocks/blob/gh-pages/generative/noise.yaml)

This provides the following blocks:

- **global**:
 + `float noise (in float x) `
 + `float noise (vec2 xy) `
 + `float noise (vec3 xyz) `
 + `float snoise (vec3 p) `

Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/generative/noise.yaml
```




### [generative-random](https://github.com/tangrams/blocks/blob/gh-pages/generative/random.yaml)

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
    - http://tangrams.github.io/blocks/generative/random.yaml
```




### [generative-voronoi](https://github.com/tangrams/blocks/blob/gh-pages/generative/voronoi.yaml)

This provides the following blocks:

- **global**:
 + `vec3 voronoi (vec2 st) `

Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/generative/voronoi.yaml
```


