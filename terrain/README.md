

#### [terrain-base](http://tangrams.github.io/blocks/#terrain-base) <a href="https://github.com/tangrams/blocks/blob/gh-pages/terrain/base.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/base.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/base-full.yaml
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrain-geometry](http://tangrams.github.io/blocks/#terrain-geometry) <a href="https://github.com/tangrams/blocks/blob/gh-pages/terrain/geometry.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/geometry.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/geometry-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **TERRAIN_TEXTURE_INDEX**:  The *default value* is ```0```. 
 -  **TERRAIN_ZOFFSET**:  The *default value* is ```0.0```. 

These are the **shader blocks**:

- **global**:
 + `float getHeight() `
- **position**:

```glsl
position.z += TERRAIN_ZOFFSET*u_meters_per_pixel;
position.z += getHeight();
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrain-lines](http://tangrams.github.io/blocks/#terrain-lines) <a href="https://github.com/tangrams/blocks/blob/gh-pages/terrain/lines.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/lines.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/lines-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **TERRAIN_ZOFFSET**:  The *default value* is ```1.5```. 


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrain-polygons](http://tangrams.github.io/blocks/#terrain-polygons) <a href="https://github.com/tangrams/blocks/blob/gh-pages/terrain/polygons.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/polygons.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/polygons-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **TERRAIN_ZOFFSET**:  The *default value* is ```1.0```. 


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [terrain-terrain](http://tangrams.github.io/blocks/#terrain-terrain) <a href="https://github.com/tangrams/blocks/blob/gh-pages/terrain/terrain.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/terrain.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/terrain/terrain-full.yaml
```


