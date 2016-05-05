

### [shapes-circle](https://github.com/tangrams/blocks/blob/gh-pages/shapes/circle.yaml)

Provides the following blocks:

- **global**:
 + `float circleDF (vec2 st) `
 + `float circle (vec2 st, float radius) `


### [shapes-cross](https://github.com/tangrams/blocks/blob/gh-pages/shapes/cross.yaml)

Provides the following blocks:

- **global**:
 + `float cross (vec2 st, float size, float width) `


### [shapes-digits](https://github.com/tangrams/blocks/blob/gh-pages/shapes/digits.yaml)

Provides the following blocks:

- **global**:
 + `float SampleDigit(const in float fDigit, const in vec2 vUV) `
 + `float PrintValue(const in vec2 vStringCharCoords, const in float fValue, const in float fMaxDigits, const in float fDecimalPlaces) `


### [shapes-polygons](https://github.com/tangrams/blocks/blob/gh-pages/shapes/polygons.yaml)

Provides the following blocks:

- **global**:
 + `float shapeDF (vec2 st, int N) `
 + `float shape (vec2 st, int N, float width) `


### [shapes-rect](https://github.com/tangrams/blocks/blob/gh-pages/shapes/rect.yaml)

Provides the following blocks:

- **global**:
 + `float rectDF(vec2 st, vec2 size) `
 + `float rectDF(vec2 st, float size) `
 + `float rect(vec2 st, vec2 size, float radio) `
 + `float rect(vec2 st, float size, float radio) `


### [shapes-simplex](https://github.com/tangrams/blocks/blob/gh-pages/shapes/simplex.yaml)

Provides the following blocks:

- **global**:
 + `float warp (vec3 S) `
 + `float circle (vec3 S) `
 + `float triangle (vec3 S) `
 + `vec3 star (vec3 S) `
 + `vec3 sakura (vec3 S) `
 + `float lotus (vec3 S, float petals_size, float roundness) `
