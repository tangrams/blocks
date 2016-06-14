

#### [space-constant](https://github.com/tangrams/blocks/blob/gh-pages/space/constant.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/space/constant.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `vec2 getConstantCoords () `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [space-screen](https://github.com/tangrams/blocks/blob/gh-pages/space/screen.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/space/screen.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `vec2 getScreenCoords () `
 + `vec2 getScreenNonStretchCoords () `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [space-tex](https://github.com/tangrams/blocks/blob/gh-pages/space/tex.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/space/tex.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `vec2 getTexCoords () `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [space-tile](https://github.com/tangrams/blocks/blob/gh-pages/space/tile.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/space/tile.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `vec2 getTileCoords() `
- **position**:

```glsl
// Normalize the attribute position of a vertex
v_pos = modelPosition().xyz;
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [space-uz](https://github.com/tangrams/blocks/blob/gh-pages/space/uz.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/space/uz.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `vec2 getUZCoords () `
