

#### [texture-non-repetitive](http://tangrams.github.io/blocks/#texture-non-repetitive) <a href="https://github.com/tangrams/blocks/blob/gh-pages/texture/non-repetitive.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/texture/non-repetitive.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/texture/non-repetitive-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec4 NonRepetitiveTexture (sampler2D tex, vec2 xy, float v)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./texture/test/texture-non-repetitive.png)](http://tangrams.github.io/blocks/test.html?test=./texture/test/texture-non-repetitive.json)

- **repete_texture** ( mean: 0.0805862656693 median: 0.080419 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./texture/test/non-repetitive-repete_texture.frag"><img src="http://tangrams.github.io/blocks/./texture/test/non-repetitive-repete_texture.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
color.rgb = vec3(1.);
color.rgb -= NonRepetitiveTexture(u_tex0, v_texcoord.xy*10., 1.).a;

```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [texture-zoom-fade](http://tangrams.github.io/blocks/#texture-zoom-fade) <a href="https://github.com/tangrams/blocks/blob/gh-pages/texture/zoom-fade.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Tile a texture across zoom levels by fading between them



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/texture/zoom-fade.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/texture/zoom-fade-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec4 TileTexture (sampler2D tex, float scale)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./texture/test/texture-zoom-fade.png)](http://tangrams.github.io/blocks/test.html?test=./texture/test/texture-zoom-fade.json)

- **zoom_fade** ( mean: 0.00272985063752 median: 0.002456 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./texture/test/zoom-fade-zoom_fade.frag"><img src="http://tangrams.github.io/blocks/./texture/test/zoom-fade-zoom_fade.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define v_pos v_texcoord
...
// Color:
color.rgb = vec3(1.);
color.rgb -= TileTexture(u_tex0,1.).a;

```


Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/crosshatch.yaml&lines=76" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/crosshatch.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/pericoli.yaml&lines=121" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/pericoli.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
