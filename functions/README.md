

#### [functions-aastep](http://tangrams.github.io/blocks/#functions-aastep) <a href="https://github.com/tangrams/blocks/blob/gh-pages/functions/aastep.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

AnitAliased ```step()``` function implemented by [Matt DesLauriers](https://twitter.com/mattdesl) in this module <https://github.com/stackgl/glsl-aastep>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/aastep.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/aastep-full.yaml
```


These blocks uses a custom **shader**. These are the **shader blocks**:

- **global**:
 + `float aastep(float threshold, float value) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [functions-easing](http://tangrams.github.io/blocks/#functions-easing) <a href="https://github.com/tangrams/blocks/blob/gh-pages/functions/easing.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Easing functions originally develop by Robert Penner's and transformed to GLSL by [StackGL](http://stack.gl/) in this repo: <https://github.com/stackgl/glsl-easings>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/easing.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/easing-full.yaml
```


These blocks uses a custom **shader**. These are the defaults **defines**:
 - **HALF_PI**: ```1.57079632679```
 - **PI**: ```3.14159265359```

These are the **shader blocks**:

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

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [functions-map](http://tangrams.github.io/blocks/#functions-map) <a href="https://github.com/tangrams/blocks/blob/gh-pages/functions/map.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

This function helps you to interpolate a `value` between an IN range (`inputMin` to `inputMax`) to a OUT range (`outputMin` to `outputMax`). 



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/map.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/map-full.yaml
```


These blocks uses a custom **shader**. These are the defaults **defines**:
 - **EPSILON**: ```1e-07```

These are the **shader blocks**:

- **global**:
 + `float map (in float value, in float inputMin, in float inputMax, in float outputMin, in float outputMax, bool clamp) `
 + `float map (in float value, in float inputMin, in float inputMax, in float outputMin, in float outputMax) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [functions-pulse](http://tangrams.github.io/blocks/#functions-pulse) <a href="https://github.com/tangrams/blocks/blob/gh-pages/functions/pulse.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/pulse.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/pulse-full.yaml
```


These blocks uses a custom **shader**. These are the **shader blocks**:

- **global**:
 + `float pulse (float x, float peak, float width) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [functions-zoom](http://tangrams.github.io/blocks/#functions-zoom) <a href="https://github.com/tangrams/blocks/blob/gh-pages/functions/zoom.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/zoom.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/functions/zoom-full.yaml
```


These blocks uses a custom **shader**. These are the defaults **defines**:
 - **ZOOM_END**: ```20.0```
 - **ZOOM_MAX**: ```max(ZOOM_START, ZOOM_END)```
 - **ZOOM_IN**: ```0.0```
 - **ZOOM_OUT**: ```1.0```
 - **ZOOM_START**: ```14.0```
 - **ZOOM**: ```linear```

These are the **shader blocks**:

- **global**:
 + `float zoom() `
