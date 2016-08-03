

#### [color-conversion](http://tangrams.github.io/blocks/#color-conversion) <a href="https://github.com/tangrams/blocks/blob/gh-pages/color/conversion.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Set of functions to convert colors between color systems/spaces.
For more information on this theme read [this chapter of The Book of Shaders about color](http://thebookofshaders.com/06/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/color/conversion.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/color/conversion-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec3 rgb2hsb (vec3 c) `
 + `vec3 rgb2hsb (vec4 c) `
 + `vec3 hsb2rgb (vec3 c) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [color-palette](http://tangrams.github.io/blocks/#color-palette) <a href="https://github.com/tangrams/blocks/blob/gh-pages/color/palette.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Procedural generation of color palettes implemented by [Inigo Quiles](https://twitter.com/iquilezles) (1999) explained in [this article](http://www.iquilezles.org/www/articles/palettes/palettes.htm)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/color/palette.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/color/palette-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec3 palette (float t, vec3 a, vec3 b, vec3 c, vec3 d) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [color-tools](http://tangrams.github.io/blocks/#color-tools) <a href="https://github.com/tangrams/blocks/blob/gh-pages/color/tools.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Set of color tools to get the **intensity** and **brightness** of a color.
For more information on this theme read [this chapter of The Book of Shaders about color](http://thebookofshaders.com/06/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/color/tools.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/color/tools-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float getIntensity (vec3 c) `
 + `float getIntensity (vec4 c) `
 + `float getBrightness (vec3 c) `
 + `float getBrightness (vec4 c) `
