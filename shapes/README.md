

### [shapes-circle](https://github.com/tangrams/blocks/blob/gh-pages/shapes/circle.yaml)

This provides the following blocks:

- **global**:
 + `float circleDF (vec2 st) `
 + `float circle (vec2 st, float radius) `

This blocks have the following defines you can use or tweak:
 - **PI**: ```3.14159265359```


Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./shapes./shapes/circle.yaml
```




### [shapes-cross](https://github.com/tangrams/blocks/blob/gh-pages/shapes/cross.yaml)

This provides the following blocks:

- **global**:
 + `float cross (vec2 st, float size, float width) `

Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./shapes./shapes/cross.yaml
```




### [shapes-digits](https://github.com/tangrams/blocks/blob/gh-pages/shapes/digits.yaml)

This provides the following blocks:

- **global**:
 + `float SampleDigit(const in float fDigit, const in vec2 vUV) `
 + `float PrintValue(const in vec2 vStringCharCoords, const in float fValue, const in float fMaxDigits, const in float fDecimalPlaces) `

This blocks have the following defines you can use or tweak:
 - **CHAR_DECIMAL_POINT**: ```10.0```
 - **CHAR_MINUS**: ```11.0```
 - **CHAR_BLANK**: ```12.0```


Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./shapes./shapes/digits.yaml
```




### [shapes-polygons](https://github.com/tangrams/blocks/blob/gh-pages/shapes/polygons.yaml)

This provides the following blocks:

- **global**:
 + `float shapeDF (vec2 st, int N) `
 + `float shape (vec2 st, int N, float width) `

This blocks have the following defines you can use or tweak:
 - **TWO_PI**: ```6.283185307```
 - **PI**: ```3.14159265359```


Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./shapes./shapes/polygons.yaml
```




### [shapes-rect](https://github.com/tangrams/blocks/blob/gh-pages/shapes/rect.yaml)

This provides the following blocks:

- **global**:
 + `float rectDF(vec2 st, vec2 size) `
 + `float rectDF(vec2 st, float size) `
 + `float rect(vec2 st, vec2 size, float radio) `
 + `float rect(vec2 st, float size, float radio) `

Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./shapes./shapes/rect.yaml
```




### [shapes-simplex](https://github.com/tangrams/blocks/blob/gh-pages/shapes/simplex.yaml)

This provides the following blocks:

- **global**:
 + `float warp (vec3 S) `
 + `float circle (vec3 S) `
 + `float triangle (vec3 S) `
 + `vec3 star (vec3 S) `
 + `vec3 sakura (vec3 S) `
 + `float lotus (vec3 S, float petals_size, float roundness) `

Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./shapes./shapes/simplex.yaml
```


