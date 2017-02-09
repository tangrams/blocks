

#### [tiling-brick](http://tangrams.github.io/blocks/#tiling-brick) <a href="https://github.com/tangrams/blocks/blob/gh-pages/tiling/brick.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Repeats a coordinate space (`vec2 st`) in diferent brick-like tiles N times (`float zoom`). For more information about tilling patterns read [this chapter of The Book of Shaders](https://thebookofshaders.com/09/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/brick.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/brick-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec2 brick (vec2 st, float zoom)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./tiling/test/tiling-brick.png)](http://tangrams.github.io/blocks/test.html?test=./tiling/test/tiling-brick.json)

- **brick** ( mean: 0.000162631578947 median: 0.000173 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./tiling/test/brick-brick.frag"><img src="http://tangrams.github.io/blocks/./tiling/test/brick-brick.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rg += brick(v_texcoord.xy,5.);
```


Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/patterns.yaml&lines=130" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/patterns.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/nursery.yaml&lines=99" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/nursery.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [tiling-simplex](http://tangrams.github.io/blocks/#tiling-simplex) <a href="https://github.com/tangrams/blocks/blob/gh-pages/tiling/simplex.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Repeats a coordinate space (`vec2 st`) in diferent simplex tiles. To learn more about simplex grids check [this chapter about noise from the Book of Shaders](https://thebookofshaders.com/11/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/simplex.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/simplex-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec2 skew (vec2 st)`
 + `vec3 simplexCoord (vec2 st, float td)`
 + `vec3 simplexGrid (vec2 st)`
 + `vec3 simplexRotatedGrid (vec2 st)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./tiling/test/tiling-simplex.png)](http://tangrams.github.io/blocks/test.html?test=./tiling/test/tiling-simplex.json)

- **simplex** ( mean: 0.000170048777039 median: 0.000173 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./tiling/test/simplex-simplex.frag"><img src="http://tangrams.github.io/blocks/./tiling/test/simplex-simplex.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += simplexGrid(v_texcoord.xy*5.);
```


- **rotatedSimplex** ( mean: 0.000153131889764 median: 0.000173 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./tiling/test/simplex-rotatedSimplex.frag"><img src="http://tangrams.github.io/blocks/./tiling/test/simplex-rotatedSimplex.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += simplexRotatedGrid(v_texcoord.xy*5.);
```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [tiling-tile](http://tangrams.github.io/blocks/#tiling-tile) <a href="https://github.com/tangrams/blocks/blob/gh-pages/tiling/tile.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Repeats a coordinate space (`vec2 st`) in diferent brick-like tiles N times (`float zoom`). For more information about tilling patterns read [this chapter of The Book of Shaders](https://thebookofshaders.com/09/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/tile.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/tile-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec2 tile (vec2 st, float zoom)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./tiling/test/tiling-tile.png)](http://tangrams.github.io/blocks/test.html?test=./tiling/test/tiling-tile.json)

- **tile** ( mean: 0.000150897749648 median: 0.000173 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./tiling/test/tile-tile.frag"><img src="http://tangrams.github.io/blocks/./tiling/test/tile-tile.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rg += tile(v_texcoord.xy,5.);
```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [tiling-truchet](http://tangrams.github.io/blocks/#tiling-truchet) <a href="https://github.com/tangrams/blocks/blob/gh-pages/tiling/truchet.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Repeats a coordinate space (`vec2 st`) in diferent tiles acording to a Truchet patern.
There is two way to do this: by mirroring the spaces (`vec2 truchetMirror (vec2 st)`) or rotating them ('vec2 truchetRotate (vec2 st)')



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/truchet.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/truchet-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **PI**:  The *default value* is ```3.14159265359```. 

These are the **shader blocks**:

- **global**:
 + `vec2 truchetMirror (vec2 st)`
 + `vec2 truchetRotate (vec2 st)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./tiling/test/tiling-truchet.png)](http://tangrams.github.io/blocks/test.html?test=./tiling/test/tiling-truchet.json)

- **rotate** ( mean: 0.000179617003128 median: 0.000175 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./tiling/test/truchet-rotate.frag"><img src="http://tangrams.github.io/blocks/./tiling/test/truchet-rotate.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rg += truchetRotate(v_texcoord.xy);
```


- **mirror** ( mean: 0.00015493387257 median: 0.000174 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./tiling/test/truchet-mirror.frag"><img src="http://tangrams.github.io/blocks/./tiling/test/truchet-mirror.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rg += truchetMirror(v_texcoord.xy);
```

