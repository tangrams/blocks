

#### terrarium-base [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//terrarium/base.yaml)


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/base.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/base-full.yaml
```




#### terrarium-geometry [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//terrarium/geometry.yaml)
This provides the following blocks:

- **position**:

```glsl
position.z += TERRARIUM_ZOFFSET*u_meters_per_pixel;
position.z += getHeight();
```


- **global**:
 + `float getHeight() `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **TERRARIUM_ZOFFSET**: ```0.0```
 - **TERRARIUM_TEXTURE_INDEX**: ```1```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/geometry.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/geometry-full.yaml
```




#### terrarium-lines [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//terrarium/lines.yaml)


This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **TERRARIUM_ZOFFSET**: ```0.2```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/lines.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/lines-full.yaml
```




#### terrarium-polygons [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//terrarium/polygons.yaml)


This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **TERRARIUM_ZOFFSET**: ```1.0```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/polygons.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/polygons-full.yaml
```




#### terrarium-terrain [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//terrarium/terrain.yaml)


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/terrain.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/terrain-full.yaml
```


