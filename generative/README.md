

### [generative-fbm](https://github.com/tangrams/blocks/blob/gh-pages/generative/fbm.yaml)

Provides the following blocks:

- **global**:
 + `float fbm (float x) `
 + `int i = 0; i < int(NUM_OCTAVES); ++i) `
 + `float fbm (vec2 xy) `
 + `int i = 0; i < int(NUM_OCTAVES); ++i) `
 + `float fbm ( in vec3 xyz) `


### [generative-noise](https://github.com/tangrams/blocks/blob/gh-pages/generative/noise.yaml)

Provides the following blocks:

- **global**:
 + `float noise (in float x) `
 + `float noise (vec2 xy) `
 + `float noise (vec3 xyz) `
 + `float snoise (vec3 p) `


### [generative-random](https://github.com/tangrams/blocks/blob/gh-pages/generative/random.yaml)

Provides the following blocks:

- **global**:
 + `float random(float x) `
 + `float random(vec2 p) `
 + `float random(vec3 p) `
 + `vec2 random2 (vec2 xy) `
 + `vec3 random3 (vec2 xy) `
 + `vec3 random3 (vec3 c) `


### [generative-voronoi](https://github.com/tangrams/blocks/blob/gh-pages/generative/voronoi.yaml)

Provides the following blocks:

- **global**:
 + `vec3 voronoi (vec2 st) `
