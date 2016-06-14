

#### [color-conversion](https://github.com/tangrams/blocks/blob/gh-pages/color/conversion.yaml)

Set of functions to convert colors between color systems/spaces.
For more information on this theme read [this chapter of The Book of Shaders about color](http://thebookofshaders.com/06/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/color/conversion.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `vec3 rgb2hsb (vec3 c) `
 + `vec3 rgb2hsb (vec4 c) `
 + `vec3 hsb2rgb (vec3 c) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [color-palette](https://github.com/tangrams/blocks/blob/gh-pages/color/palette.yaml)

Procedural generation of color paletters implemented by [Inigo Quiles](https://twitter.com/iquilezles) (1999) explained in [this article](http://www.iquilezles.org/www/articles/palettes/palettes.htm)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/color/palette.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `vec3 palette (float t, vec3 a, vec3 b, vec3 c, vec3 d) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [color-tools](https://github.com/tangrams/blocks/blob/gh-pages/color/tools.yaml)

Set of color tools to get the **intensity** and **brightness** of a color.
For more information on this theme read [this chapter of The Book of Shaders about color](http://thebookofshaders.com/06/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/color/tools.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `float getIntensity (vec3 c) `
 + `float getIntensity (vec4 c) `
 + `float getBrightness (vec3 c) `
 + `float getBrightness (vec4 c) `
