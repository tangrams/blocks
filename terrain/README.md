

#### terrain-base [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//terrain/base.yaml)


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/base.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/base-full.yaml
```




#### terrain-geometry [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//terrain/geometry.yaml)
This provides the following blocks:

- **position**:

```glsl
position.z += TERRAIN_ZOFFSET*u_meters_per_pixel;
position.z += getHeight();
```


- **global**:
 + `float getHeight() `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **TERRAIN_TEXTURE_INDEX**: ```0```
 - **TERRAIN_ZOFFSET**: ```0.0```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/geometry.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/geometry-full.yaml
```




#### terrain-lines [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//terrain/lines.yaml)


This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **TERRAIN_ZOFFSET**: ```1.5```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/lines.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/lines-full.yaml
```




#### terrain-polygons [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//terrain/polygons.yaml)


This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **TERRAIN_ZOFFSET**: ```1.0```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/polygons.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/polygons-full.yaml
```




#### terrain-terrain [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//terrain/terrain.yaml)


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/terrain.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/terrain-full.yaml
```


