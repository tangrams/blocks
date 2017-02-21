

#### [space-tile](http://tangrams.github.io/blocks/#space-tile) <a href="https://github.com/tangrams/blocks/blob/gh-pages/space/tile.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Get the position on the tile



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/space/tile.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/space/tile-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec2 getTileCoords()`
- **position**:

```glsl
// Normalize the attribute position of a vertex
v_pos = modelPosition().xyz;
```



Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./space/test/space-tile.png)](http://tangrams.github.io/blocks/test.html?test=./space/test/space-tile.json)

- **tile** ( mean: 0.00219142321707 median: 0.002065 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./space/test/tile-tile.frag"><img src="http://tangrams.github.io/blocks/./space/test/tile-tile.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define v_pos v_texcoord
...
// Color:
vec2 st = getTileCoords();
color.rg += fract(st*3.);

```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [space-tex](http://tangrams.github.io/blocks/#space-tex) <a href="https://github.com/tangrams/blocks/blob/gh-pages/space/tex.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Get the position on TexCoords



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/space/tex.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/space/tex-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec2 getTexCoords ()`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./space/test/space-tex.png)](http://tangrams.github.io/blocks/test.html?test=./space/test/space-tex.json)

- **tex** ( mean: 0.001643307393 median: 0.00154 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./space/test/tex-tex.frag"><img src="http://tangrams.github.io/blocks/./space/test/tex-tex.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
vec2 st = getTexCoords();
color.rg += fract(st*3.);

```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [space-screen](http://tangrams.github.io/blocks/#space-screen) <a href="https://github.com/tangrams/blocks/blob/gh-pages/space/screen.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Get the coordinates in screen space streaching the proportion ('vec2 getScreenCoords ()') or non-streatching the proportion ('getScreenNonStretchCoords ()')



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/space/screen.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/space/screen-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec2 getScreenCoords ()`
 + `vec2 getScreenNonStretchCoords ()`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./space/test/space-screen.png)](http://tangrams.github.io/blocks/test.html?test=./space/test/space-screen.json)

- **screen** ( mean: 0.0016686483494 median: 0.001539 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./space/test/screen-screen.frag"><img src="http://tangrams.github.io/blocks/./space/test/screen-screen.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
vec2 st = getScreenCoords();
color.rg += fract(st*3.);

```


- **screen_nonstretch** ( mean: 0.00161397358101 median: 0.00154 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./space/test/screen-screen_nonstretch.frag"><img src="http://tangrams.github.io/blocks/./space/test/screen-screen_nonstretch.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
vec2 st = getScreenNonStretchCoords();
color.rg += fract(st*3.);

```


Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/press.yaml&lines=136-145" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/press.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/radar.yaml&lines=0-143" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/radar.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [space-uz](http://tangrams.github.io/blocks/#space-uz) <a href="https://github.com/tangrams/blocks/blob/gh-pages/space/uz.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Get the position on UZ from the TexCoords (on `x`) and the `z` of the World Position



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/space/uz.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/space/uz-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec2 getUZCoords ()`

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [space-constant](http://tangrams.github.io/blocks/#space-constant) <a href="https://github.com/tangrams/blocks/blob/gh-pages/space/constant.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Get the constant coordinates **(warning: could glitch on zooms)**



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/space/constant.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/space/constant-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec2 getConstantCoords ()`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./space/test/space-constant.png)](http://tangrams.github.io/blocks/test.html?test=./space/test/space-constant.json)

- **constant** ( mean: 0.00223160082623 median: 0.002086 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./space/test/constant-constant.frag"><img src="http://tangrams.github.io/blocks/./space/test/constant-constant.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
vec2 st = getConstantCoords();
color.rg += fract(st*3.);

```


Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/grain-area.yaml&lines=26" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/grain-area.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
