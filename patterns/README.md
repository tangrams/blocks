

#### [patterns-dots](https://github.com/tangrams/blocks/blob/gh-pages/patterns/dots.yaml)

This provides the following blocks:

- **global**:
 + `float TileDots(float scale, float size) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/dots.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/dots-full.yaml
```




#### [patterns-grid](https://github.com/tangrams/blocks/blob/gh-pages/patterns/grid.yaml)

This provides the following blocks:

- **global**:
 + `bool grid (vec2 st, float res, float press) `
 + `bool grid (vec2 st, float res) `
 + `float tileGrid (float res) `
 + `float tileGrid() `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/grid.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/grid-full.yaml
```




#### [patterns-stripes](https://github.com/tangrams/blocks/blob/gh-pages/patterns/stripes.yaml)

This provides the following blocks:

- **global**:
 + `float stripesDF (vec2 st) `
 + `float stripes (vec2 st, float width) `
 + `float stripes (vec2 st, float width, float angle) `
 + `float diagonalStripes (vec2 st) `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **PI**: ```3.14159265359```
 - **STRIPE_SCALE**: ```28.296```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/stripes.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/stripes-full.yaml
```




#### [patterns-waves](https://github.com/tangrams/blocks/blob/gh-pages/patterns/waves.yaml)

This provides the following blocks:

- **global**:
 + `float wavesDF (vec2 st, float freq, float amp) `
 + `float waves (vec2 st, float freq, float amp, float width) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/waves.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/waves-full.yaml
```




#### [patterns-zigzag](https://github.com/tangrams/blocks/blob/gh-pages/patterns/zigzag.yaml)

This provides the following blocks:

- **global**:
 + `float zigzagDF (vec2 st, float freq) `
 + `float zigzag (vec2 st, float freq, float width) `

Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/zigzag.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/patterns/zigzag-full.yaml
```


