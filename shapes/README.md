

#### [shapes-circle](http://tangrams.github.io/blocks/#shapes-circle) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/circle.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw circles. To learn more about how to make shapes on shaders go to From check [this chapter about shapes from the Book of Shaders](https://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/circle.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/circle-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float circleDF (vec2 st) `
 + `float circle (vec2 st, float radius) `
 + `float circleBorder (vec2 st, float radius) `

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/patterns.yaml&lines=146" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/patterns.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/nursery.yaml&lines=146" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/nursery.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/lego.yaml&lines=109-110" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/lego.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-cross](http://tangrams.github.io/blocks/#shapes-cross) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/cross.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw crosses. To learn more about how to make shapes on shaders go to From check [this chapter about shapes from the Book of Shaders](https://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/cross.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/cross-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float cross (vec2 st, float size, float width) `
 + `float cross (in vec2 st, float _size) `
 + `float cross (in vec2 st, vec2 _size) `

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/9845C.yaml&lines=181-183" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/9845C.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/oblivion.yaml&lines=155-156" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/oblivion.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/matrix.yaml&lines=101-104" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/matrix.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/tron.yaml&lines=122" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/tron.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-digits](http://tangrams.github.io/blocks/#shapes-digits) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/digits.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw number digits.



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/digits.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/digits-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **CHAR_DECIMAL_POINT**:  The *default value* is ```10.0```. 
 -  **CHAR_MINUS**:  The *default value* is ```11.0```. 
 -  **CHAR_BLANK**:  The *default value* is ```12.0```. 

These are the **shader blocks**:

- **global**:
 + `float SampleDigit (const in float fDigit, const in vec2 vUV) `
 + `float PrintValue (const in vec2 vStringCharCoords, const in float fValue, const in float fMaxDigits, const in float fDecimalPlaces) `
 + `float PrintValue (in vec2 fragCoord, const in vec2 vPixelCoords, const in vec2 vFontSize, const in float fValue, const in float fMaxDigits, const in float fDecimalPlaces) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-polygons](http://tangrams.github.io/blocks/#shapes-polygons) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/polygons.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw polygons. To learn more about how to make shapes on shaders go to From check [this chapter about shapes from the Book of Shaders](https://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/polygons.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/polygons-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float shapeDF (vec2 st, int N) `
 + `float shape (vec2 st, int N, float width) `
 + `float shapeBorder (vec2 st, int N, float width) `

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/9845C.yaml&lines=153" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/9845C.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-rect](http://tangrams.github.io/blocks/#shapes-rect) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/rect.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw rectangles. To learn more about how to make shapes on shaders go to From check [this chapter about shapes from the Book of Shaders](https://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/rect.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/rect-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float rectDF (in vec2 st, in vec2 size) `
 + `float rectDF (in vec2 st, in float size) `
 + `float rect (in vec2 st, in vec2 size, in float radio) `
 + `float rect (vec2 st, float size, float radio) `
 + `float rectBorder (in vec2 st, in vec2 size, in float radio) `
 + `float rectBorder (vec2 st, float size, float radio) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-simplex](http://tangrams.github.io/blocks/#shapes-simplex) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/simplex.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw shapes using a simplex grid. To learn more about simplex grids check [this chapter about noise from the Book of Shaders](https://thebookofshaders.com/11/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/simplex.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/simplex-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float warp (vec3 S) `
 + `float circle (vec3 S) `
 + `float triangle (vec3 S) `
 + `vec3 star (vec3 S) `
 + `vec3 sakura (vec3 S) `
 + `float lotus (vec3 S, float petals_size, float roundness) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-type](http://tangrams.github.io/blocks/#shapes-type) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/type.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

This block provides to functions `fill` and `stroke`. Each one transform a SDF to a fill shape or a stroke shape (border). The stroke width can be control with the define `STROKE`. 
To learn more about how to make shapes on shaders go to From check [this chapter about shapes from the Book of Shaders](https://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/type.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/type-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **STROKE**:  The *default value* is ```0.15```. 

These are the **shader blocks**:

- **global**:
 + `float fill (in float size, in float x) `
 + `float stroke (in float size, in float x) `
