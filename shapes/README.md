

#### shapes-circle [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//shapes/circle.yaml)
This provides the following blocks:

- **global**:
 + `float circleDF (vec2 st) `
 + `float circle (vec2 st, float radius) `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **PI**: ```3.14159265359```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/circle.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/circle-full.yaml
```




#### shapes-cross [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//shapes/cross.yaml)
This provides the following blocks:

- **global**:
 + `float cross (vec2 st, float size, float width) `
 + `float cross (in vec2 st, float _size) `
 + `float cross (in vec2 st, vec2 _size) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/cross.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/cross-full.yaml
```




#### shapes-digits [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//shapes/digits.yaml)
This provides the following blocks:

- **global**:
 + `float SampleDigit (const in float fDigit, const in vec2 vUV) `
 + `float PrintValue (const in vec2 vStringCharCoords, const in float fValue, const in float fMaxDigits, const in float fDecimalPlaces) `
 + `float PrintValue (in vec2 fragCoord, const in vec2 vPixelCoords, const in vec2 vFontSize, const in float fValue, const in float fMaxDigits, const in float fDecimalPlaces) `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **CHAR_DECIMAL_POINT**: ```10.0```
 - **CHAR_MINUS**: ```11.0```
 - **CHAR_BLANK**: ```12.0```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/digits.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/digits-full.yaml
```




#### shapes-polygons [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//shapes/polygons.yaml)
This provides the following blocks:

- **global**:
 + `float shapeDF (vec2 st, int N) `
 + `float shape (vec2 st, int N, float width) `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **TWO_PI**: ```6.283185307```
 - **PI**: ```3.14159265359```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/polygons.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/polygons-full.yaml
```




#### shapes-rect [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//shapes/rect.yaml)
This provides the following blocks:

- **global**:
 + `float rectDF (vec2 st, vec2 size) `
 + `float rectDF (vec2 st, float size) `
 + `float rect (vec2 st, vec2 size, float radio) `
 + `float rect (vec2 st, float size, float radio) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/rect.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/rect-full.yaml
```




#### shapes-simplex [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//shapes/simplex.yaml)
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
    - https://tangrams.github.io/blocks/shapes/simplex.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/simplex-full.yaml
```


