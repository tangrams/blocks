

#### [tiling-brick](https://github.com/tangrams/blocks/blob/gh-pages/tiling/brick.yaml)



Import using:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/brick.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `vec2 brick (vec2 st, float zoom) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [tiling-simplex](https://github.com/tangrams/blocks/blob/gh-pages/tiling/simplex.yaml)



Import using:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/simplex.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `vec2 simplex (vec2 st) `
 + `vec2 unsimplex (vec2 st) `
 + `vec3 simplexGrid (vec2 st) `
 + `vec3 simplexRotatedGrid (vec2 st) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [tiling-tile](https://github.com/tangrams/blocks/blob/gh-pages/tiling/tile.yaml)



Import using:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/tile.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `vec2 tile (vec2 st, float zoom) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [tiling-truchet](https://github.com/tangrams/blocks/blob/gh-pages/tiling/truchet.yaml)



Import using:

```yaml
import:
    - https://tangrams.github.io/blocks/tiling/truchet.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **PI**: ```3.14159265359```

These are the **shader blocks**:

- **global**:
 + `vec2 truchetMirror (vec2 st) `
 + `vec2 truchetRotate (vec2 st) `
