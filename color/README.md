

### [color-conversion](https://github.com/tangrams/blocks/blob/gh-pages/color/conversion.yaml)

Set of functions to convert colors between color systems/spaces

Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./color./color/conversion.yaml
```

Provides the following blocks:

- **global**:
 + `vec3 rgb2hsb (vec3 c) `
 + `vec3 rgb2hsb (vec4 c) `
 + `vec3 hsb2rgb (vec3 c) `


### [color-palette](https://github.com/tangrams/blocks/blob/gh-pages/color/palette.yaml)

Provides the following blocks:

- **global**:
 + `vec3 palette (float t, vec3 a, vec3 b, vec3 c, vec3 d) `


### [color-tools](https://github.com/tangrams/blocks/blob/gh-pages/color/tools.yaml)

Provides the following blocks:

- **global**:
 + `float getIntensity (vec3 c) `
 + `float getIntensity (vec4 c) `
 + `float getBrightness (vec3 c) `
 + `float getBrightness (vec4 c) `
