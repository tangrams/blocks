

#### [geometry-dynamic-height](http://tangrams.github.io/blocks/#geometry-dynamic-height) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/dynamic-height.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Scale geometries in `z` acording to the zoom level



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/dynamic-height.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/dynamic-height-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **ZOOM_START**:  The *default value* is ```15.0```. 
 -  **ZOOM_END**:  The *default value* is ```20.0```. 
 -  **HEIGHT_MAX**:  The *default value* is ```2.5```. 
 -  **HEIGHT_MIN**:  The *default value* is ```1.0```. 
 -  **HEIGHT**:  The *default value* is ```zoom()```. 

These are the **shader blocks**:

- **position**:

```glsl
position.z *= max(HEIGHT_MIN,HEIGHT_MAX*HEIGHT);
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [geometry-dynamic-width](http://tangrams.github.io/blocks/#geometry-dynamic-width) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/dynamic-width.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Change the width of a line acording to the altitud



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/dynamic-width.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/dynamic-width-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **WIDTH_MIN**:  The *default value* is ```0.2```. 
 -  **WIDTH_Z_SCALE**:  The *default value* is ```0.006```. 
 -  **WIDTH_MAX**:  The *default value* is ```1.0```. 

These are the **shader blocks**:

- **width**:

```glsl
width *= min(WIDTH_MIN+(position.z*WIDTH_Z_SCALE)*(position.z*WIDTH_Z_SCALE),WIDTH_MAX);
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/blueprint.yaml&lines=7-28" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/blueprint.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [geometry-matrices](http://tangrams.github.io/blocks/#geometry-matrices) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/matrices.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Useful set of functions to construct scale, rotation and translation of 2, 3 or 4 dimensions. For more information about matrices read [this chapter from The Book of Shaders](http://thebookofshaders.com/08/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/matrices.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/matrices-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `mat2 rotate2D (float angle) `
 + `mat3 rotateX3D (float phi) `
 + `mat4 rotateX4D (float phi) `
 + `mat3 rotateY3D (float theta) `
 + `mat4 rotateY4D (float theta) `
 + `mat3 rotateZ3D (float psi) `
 + `mat4 rotateZ4D (float psi) `
 + `mat4 scale4D (float x, float y, float z) `
 + `mat4 translate4D (float x, float y, float z) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [geometry-normal](http://tangrams.github.io/blocks/#geometry-normal) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/normal.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Functions to detect if the surface is a wall (`bool isWall()`) or a roof ('bool isRoof()') based on the normals



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/normal.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/normal-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `bool isWall () `
 + `bool isRoof () `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [geometry-projections](http://tangrams.github.io/blocks/#geometry-projections) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/projections.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to do different geometry projections



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/projections.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/projections-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **EARTH_RADIUS**:  The *default value* is ```6378137.0```. 

These are the **shader blocks**:

- **global**:
 + `float y2lat_d (float y) `
 + `float x2lon_d (float x) `
 + `float lat2y_d (float lat) `
 + `float lon2x_d (float lon) `
 + `float y2lat_m (float y) `
 + `float x2lon_m (float x) `
 + `float lat2y_m (float lat) `
 + `float lon2x_m (float lon) `
 + `vec2 latlon2albers (float lat, float lon, float lat0, float lng0, float phi1, float phi2 ) `
 + `vec2 latlon2albers (float lat, float lon, float delta_phi1, float delta_phi2) `
 + `vec2 latlon2albers (float lat, float lon, float width) `
 + `vec2 latlon2albers (float lat, float lon) `
 + `vec2 latlon2USalbers (float lat, float lon) `
 + `vec2 latlon2azimuthal (float lat, float lon, float phi1, float lambda0) `
 + `vec2 azimuthal(float lat, float lon) `
 + `vec2 azimuthalNorth(float lat, float lon) `
 + `vec2 azimuthalSouth(float lat, float lon) `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [geometry-rotation](http://tangrams.github.io/blocks/#geometry-rotation) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/rotation.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Allows to rotate the camera while zooming between `ROTATION_IN` and `ROTATION_OUT`.



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/rotation.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/rotation-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **ROTATION**:  The *default value* is ```sin(u_time*ROTATION_SPEED)*ROTATION_RANGE```. 
 -  **ROTATION_SPEED**:  The *default value* is ```0.1```. 
 -  **ROTATION_RANGE**:  The *default value* is ```PI```. 

These are the **shader blocks**:

- **position**:

```glsl
position.xyz = rotateZ3D(ROTATION) * position.xyz;

```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/tilt.yaml&lines=13-19" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/tilt.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/oblivion.yaml&lines=88-94" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/oblivion.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [geometry-tilt](http://tangrams.github.io/blocks/#geometry-tilt) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/tilt.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Allows to TILT the camera while zooming between `TILT_IN` and `TILT_OUT`.



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/tilt.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/tilt-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **TILT**:  The *default value* is ```0```. 

These are the **shader blocks**:

- **position**:

```glsl
position.xyz = rotateX3D(TILT) * position.xyz;
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/tilt.yaml&lines=7-28" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/tilt.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/oblivion.yaml" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/oblivion.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
