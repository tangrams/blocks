

#### [terrarium-base](#terrarium-base) <a href="https://github.com/tangrams/blocks/blob/gh-pages/terrarium/base.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/base.yaml
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrarium-geometry](#terrarium-geometry) <a href="https://github.com/tangrams/blocks/blob/gh-pages/terrarium/geometry.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



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


#### [terrarium-lines](#terrarium-lines) <a href="https://github.com/tangrams/blocks/blob/gh-pages/terrarium/lines.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/lines.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **TERRARIUM_ZOFFSET**: ```0.2```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrarium-polygons](#terrarium-polygons) <a href="https://github.com/tangrams/blocks/blob/gh-pages/terrarium/polygons.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/polygons.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **TERRARIUM_ZOFFSET**: ```1.0```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrarium-terrain](#terrarium-terrain) <a href="https://github.com/tangrams/blocks/blob/gh-pages/terrarium/terrain.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/terrain.yaml
```


