

#### generative-caustic [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//generative/caustics.yaml)
This provides the following blocks:

- **global**:
 + `vec3 getCaustic (vec2 uv) `
 + `int n = 0; n < int(CAUSTIC_ITERATIONS); n++) `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **TAU**: ```6.28318530718```
 - **CAUSTIC_ITERATIONS**: ```3```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/caustics.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/caustics-full.yaml
```




#### generative-fbm [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//generative/fbm.yaml)
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




#### generative-noise [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//generative/noise.yaml)
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




#### generative-random [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//generative/random.yaml)
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




#### generative-voronoi [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//generative/voronoi.yaml)
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


