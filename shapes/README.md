

#### [shapes-circle](https://github.com/tangrams/blocks/blob/gh-pages/shapes/circle.yaml)



Import using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/circle.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **PI**: ```3.14159265359```

These are the **shader blocks**:

- **global**:
 + `float circleDF (vec2 st) `
 + `float circle (vec2 st, float radius) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-cross](https://github.com/tangrams/blocks/blob/gh-pages/shapes/cross.yaml)



Import using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/cross.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `float cross (vec2 st, float size, float width) `
 + `float cross (in vec2 st, float _size) `
 + `float cross (in vec2 st, vec2 _size) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-digits](https://github.com/tangrams/blocks/blob/gh-pages/shapes/digits.yaml)



Import using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/digits.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **CHAR_DECIMAL_POINT**: ```10.0```
 - **CHAR_MINUS**: ```11.0```
 - **CHAR_BLANK**: ```12.0```

These are the **shader blocks**:

- **global**:
 + `float SampleDigit (const in float fDigit, const in vec2 vUV) `
 + `float PrintValue (const in vec2 vStringCharCoords, const in float fValue, const in float fMaxDigits, const in float fDecimalPlaces) `
 + `float PrintValue (in vec2 fragCoord, const in vec2 vPixelCoords, const in vec2 vFontSize, const in float fValue, const in float fMaxDigits, const in float fDecimalPlaces) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-polygons](https://github.com/tangrams/blocks/blob/gh-pages/shapes/polygons.yaml)



Import using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/polygons.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **TWO_PI**: ```6.283185307```
 - **PI**: ```3.14159265359```

These are the **shader blocks**:

- **global**:
 + `float shapeDF (vec2 st, int N) `
 + `float shape (vec2 st, int N, float width) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-rect](https://github.com/tangrams/blocks/blob/gh-pages/shapes/rect.yaml)



Import using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/rect.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `float rectDF (vec2 st, vec2 size) `
 + `float rectDF (vec2 st, float size) `
 + `float rect (vec2 st, vec2 size, float radio) `
 + `float rect (vec2 st, float size, float radio) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-simplex](https://github.com/tangrams/blocks/blob/gh-pages/shapes/simplex.yaml)



Import using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/simplex.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `float warp (vec3 S) `
 + `float circle (vec3 S) `
 + `float triangle (vec3 S) `
 + `vec3 star (vec3 S) `
 + `vec3 sakura (vec3 S) `
 + `float lotus (vec3 S, float petals_size, float roundness) `
