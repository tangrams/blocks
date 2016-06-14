

#### [terrarium-base](https://github.com/tangrams/blocks/blob/gh-pages/terrarium/base.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/base.yaml
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrarium-geometry](https://github.com/tangrams/blocks/blob/gh-pages/terrarium/geometry.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/geometry.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **TERRARIUM_ZOFFSET**: ```0.0```
 - **TERRARIUM_TEXTURE_INDEX**: ```1```

These are the **shader blocks**:

- **global**:
 + `float getHeight() `
- **position**:

```glsl
position.z += TERRARIUM_ZOFFSET*u_meters_per_pixel;
position.z += getHeight();
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrarium-lines](https://github.com/tangrams/blocks/blob/gh-pages/terrarium/lines.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/lines.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **TERRARIUM_ZOFFSET**: ```0.2```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrarium-polygons](https://github.com/tangrams/blocks/blob/gh-pages/terrarium/polygons.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/polygons.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **TERRARIUM_ZOFFSET**: ```1.0```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrarium-terrain](https://github.com/tangrams/blocks/blob/gh-pages/terrarium/terrain.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/terrain.yaml
```


