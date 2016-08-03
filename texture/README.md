

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
 + `vec4 NonRepetitiveTexture (sampler2D tex, vec2 x, float v) `

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
 + `vec4 TileTexture (sampler2D tex, float scale) `

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/crosshatch.yaml&lines=76" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/crosshatch.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/pericoli.yaml&lines=121" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/pericoli.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
