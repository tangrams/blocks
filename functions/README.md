

### [functions-aastep](https://github.com/tangrams/blocks/blob/gh-pages/functions/aastep.yaml)

AnitAliased ```step()``` function implemented by [Matt DesLauriers](https://twitter.com/mattdesl) in this module <https://github.com/stackgl/glsl-aastep>

This provides the following blocks:

- **global**:
 + `float aastep(float threshold, float value) `

Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./functions./functions/aastep.yaml
```




### [functions-easing](https://github.com/tangrams/blocks/blob/gh-pages/functions/easing.yaml)

Easing functions originally develop by Robert Penner's and transformed to GLSL by [StackGL](http://stack.gl/) in this repo: <https://github.com/stackgl/glsl-easings>

This provides the following blocks:

- **global**:
 + `float linear(float t) `
 + `float exponentialIn(float t) `
 + `float exponentialOut(float t) `
 + `float exponentialInOut(float t) `
 + `float sineIn(float t) `
 + `float sineOut(float t) `
 + `float sineInOut(float t) `
 + `float qinticIn(float t) `
 + `float qinticOut(float t) `
 + `float qinticInOut(float t) `
 + `float quarticIn(float t) `
 + `float quarticOut(float t) `
 + `float quarticInOut(float t) `
 + `float quadraticInOut(float t) `
 + `float quadraticIn(float t) `
 + `float quadraticOut(float t) `
 + `float cubicIn(float t) `
 + `float cubicOut(float t) `
 + `float cubicInOut(float t) `
 + `float elasticIn(float t) `
 + `float elasticOut(float t) `
 + `float elasticInOut(float t) `
 + `float circularIn(float t) `
 + `float circularOut(float t) `
 + `float circularInOut(float t) `
 + `float bounceOut(float t) `
 + `float bounceIn(float t) `
 + `float bounceInOut(float t) `
 + `float backIn(float t) `
 + `float backOut(float t) `
 + `float backInOut(float t) `

This blocks have the following defines you can use or tweak:
 - **HALF_PI**: ```1.57079632679```
 - **PI**: ```3.14159265359```


Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./functions./functions/easing.yaml
```




### [functions-map](https://github.com/tangrams/blocks/blob/gh-pages/functions/map.yaml)

This provides the following blocks:

- **global**:
 + `float map (in float value, in float inputMin, in float inputMax, in float outputMin, in float outputMax, bool clamp) `
 + `float map (in float value, in float inputMin, in float inputMax, in float outputMin, in float outputMax) `

This blocks have the following defines you can use or tweak:
 - **EPSILON**: ```1e-07```


Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./functions./functions/map.yaml
```




### [functions-pulse](https://github.com/tangrams/blocks/blob/gh-pages/functions/pulse.yaml)

This provides the following blocks:

- **global**:
 + `float pulse (float x, float p, float w) `

Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./functions./functions/pulse.yaml
```


