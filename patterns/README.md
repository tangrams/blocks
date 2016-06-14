

#### [patterns-dots](https://github.com/tangrams/blocks/blob/gh-pages/patterns/dots.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/dots.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `float TileDots(float scale, float size) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [patterns-grid](https://github.com/tangrams/blocks/blob/gh-pages/patterns/grid.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/grid.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `bool grid (vec2 st, float res, float press) `
 + `bool grid (vec2 st, float res) `
 + `float tileGrid (float res) `
 + `float tileGrid() `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [patterns-stripes](https://github.com/tangrams/blocks/blob/gh-pages/patterns/stripes.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/stripes.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **PI**: ```3.14159265359```
 - **STRIPE_SCALE**: ```28.296```

These are the **shader blocks**:

- **global**:
 + `float stripesDF (vec2 st) `
 + `float stripes (vec2 st, float width) `
 + `float stripes (vec2 st, float width, float angle) `
 + `float diagonalStripes (vec2 st) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [patterns-waves](https://github.com/tangrams/blocks/blob/gh-pages/patterns/waves.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/waves.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `float wavesDF (vec2 st, float freq, float amp) `
 + `float waves (vec2 st, float freq, float amp, float width) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [patterns-zigzag](https://github.com/tangrams/blocks/blob/gh-pages/patterns/zigzag.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/zigzag.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `float zigzagDF (vec2 st, float freq) `
 + `float zigzag (vec2 st, float freq, float width) `
