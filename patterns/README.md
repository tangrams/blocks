

#### [patterns-dots](http://tangrams.github.io/blocks/#patterns-dots) <a href="https://github.com/tangrams/blocks/blob/gh-pages/patterns/dots.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw dot patterns that animate between zoom levels. To learn more about patterns check [this chapter from the Book of Shaders](https://thebookofshaders.com/09/)    



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/dots.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/dots-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float TileDots(float scale, float size) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [patterns-grid](http://tangrams.github.io/blocks/#patterns-grid) <a href="https://github.com/tangrams/blocks/blob/gh-pages/patterns/grid.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw grids. To learn more about patterns check [this chapter from the Book of Shaders](https://thebookofshaders.com/09/)    



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/grid.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/grid-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `bool grid (vec2 st, float res, float press) `
 + `bool grid (vec2 st, float res) `
 + `float tileGrid (float res) `
 + `float tileGrid() `

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/blueprint.yaml&lines=75-76" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/blueprint.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/grain.yaml&lines=15" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/grain.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [patterns-stripes](http://tangrams.github.io/blocks/#patterns-stripes) <a href="https://github.com/tangrams/blocks/blob/gh-pages/patterns/stripes.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw stripes. To learn more about patterns check [this chapter from the Book of Shaders](https://thebookofshaders.com/09/)    



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/stripes.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/stripes-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **PI**:  The *default value* is ```3.14159265359```. 

These are the **shader blocks**:

- **global**:
 + `float stripesDF (vec2 st) `
 + `float stripes (vec2 st, float width) `
 + `float stripes (vec2 st, float width, float angle) `
 + `float diagonalStripes (vec2 st) `
 + `float diagonalStripes (vec2 st, float width) `

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/press.yaml&lines=150" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/press.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/radar.yaml" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/radar.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/grain-area.yaml&lines=26" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/grain-area.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [patterns-waves](http://tangrams.github.io/blocks/#patterns-waves) <a href="https://github.com/tangrams/blocks/blob/gh-pages/patterns/waves.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw wavy stripes. To learn more about patterns check [this chapter from the Book of Shaders](https://thebookofshaders.com/09/) 



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/waves.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/waves-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float wavesDF (vec2 st, float freq, float amp) `
 + `float waves (vec2 st, float freq, float amp, float width) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [patterns-zigzag](http://tangrams.github.io/blocks/#patterns-zigzag) <a href="https://github.com/tangrams/blocks/blob/gh-pages/patterns/zigzag.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw zigzag stripes. To learn more about patterns check [this chapter from the Book of Shaders](https://thebookofshaders.com/09/) 



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/zigzag.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/zigzag-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float zigzagDF (vec2 st, float freq) `
 + `float zigzag (vec2 st, float freq, float width) `
