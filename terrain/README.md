

#### [terrain-base](https://github.com/tangrams/blocks/blob/gh-pages/terrain/base.yaml)



Import using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/base.yaml
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrain-geometry](https://github.com/tangrams/blocks/blob/gh-pages/terrain/geometry.yaml)



Import using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/geometry.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **TERRAIN_TEXTURE_INDEX**: ```0```
 - **TERRAIN_ZOFFSET**: ```0.0```

These are the **shader blocks**:

- **global**:
 + `float getHeight() `
- **position**:

```glsl
position.z += TERRAIN_ZOFFSET*u_meters_per_pixel;
position.z += getHeight();
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrain-lines](https://github.com/tangrams/blocks/blob/gh-pages/terrain/lines.yaml)



Import using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/lines.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **TERRAIN_ZOFFSET**: ```1.5```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrain-polygons](https://github.com/tangrams/blocks/blob/gh-pages/terrain/polygons.yaml)



Import using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/polygons.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **TERRAIN_ZOFFSET**: ```1.0```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrain-terrain](https://github.com/tangrams/blocks/blob/gh-pages/terrain/terrain.yaml)



Import using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/terrain.yaml
```


