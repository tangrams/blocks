

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
 + `float linear (in float t) `
 + `float exponentialIn (in float t) `
 + `float exponentialOut (in float t) `
 + `float exponentialInOut (in float t) `
 + `float sineIn (in float t) `
 + `float sineOut (in float t) `
 + `float sineInOut (in float t) `
 + `float qinticIn (in float t) `
 + `float qinticOut (in float t) `
 + `float qinticInOut (in float t) `
 + `float quarticIn (in float t) `
 + `float quarticOut (in float t) `
 + `float quarticInOut (in float t) `
 + `float quadraticInOut (in float t) `
 + `float quadraticIn (in float t) `
 + `float quadraticOut (in float t) `
 + `float cubicIn (in float t) `
 + `float cubicOut (in float t) `
 + `float cubicInOut (in float t) `
 + `float elasticIn (in float t) `
 + `float elasticOut (in float t) `
 + `float elasticInOut (in float t) `
 + `float circularIn (in float t) `
 + `float circularOut (in float t) `
 + `float circularInOut (in float t) `
 + `float bounceOut (in float t) `
 + `float bounceIn (in float t) `
 + `float bounceInOut (in float t) `
 + `float backIn (in float t) `
 + `float backOut (in float t) `
 + `float backInOut (in float t) `

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

This one dimensional shaping function made by Inigo Quiles in [this article](http://www.iquilezles.org/www/articles/functions/functions.htm).



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

How it works?
Well, you add it like any other block, by `import`ing it and then `mix`ing it to the style.
Then you set the zooms wher should **start** and **end** the interpolation, setting the `defines`: `ZOOM_START` and `ZOOM_END`.
Then you use the `zoom()` function... by default this function gives a number between 0 and 1. But you can change it to interpolate any thing (`floats`, `vec2`, `vec3`, `vec4` and even other functions). For that you Just need to change de `defines`: `ZOOM_IN`, and `ZOOM_OUT`.
Another thing that can be change is the type of interpolation, de default is `linear`, but can be any of the [easing functions](#functions-easing). For it you need to change the s`define` of this block like this: `ZOOM: quadraticInOut`



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
 - **ZOOM_FNC**: ```linear```

These are the **shader blocks**:

- **global**:
 + `float zoom() `
