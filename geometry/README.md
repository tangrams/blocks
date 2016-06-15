

#### [geometry-dynamic-height](http://tangrams.github.io/blocks/#geometry-dynamic-height) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/dynamic-height.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/dynamic-height.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **ZOOM_LINEAR_FACTOR**: ```2.0```
 - **ZOOM_START**: ```15.0```
 - **ZOOM_END**: ```20.0```

These are the **shader blocks**:

- **position**:

```glsl
float zoom = map(u_map_position.z,ZOOM_START,ZOOM_END,1.,0.);
position.z *= max(1.,.5+ZOOM_LINEAR_FACTOR*zoom);
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [geometry-dynamic-width](http://tangrams.github.io/blocks/#geometry-dynamic-width) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/dynamic-width.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/dynamic-width.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **width**:

```glsl
width *= 0.2+min(pow(position.z*0.006,2.),.6);
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [geometry-matrices](http://tangrams.github.io/blocks/#geometry-matrices) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/matrices.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/matrices.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **HALF_PI**: ```1.57079632679```
 - **TWO_PI**: ```6.28318530718```
 - **PI**: ```3.14159265359```

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



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/normal.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **global**:
 + `bool isWall () `
 + `bool isRoof () `

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [geometry-projections](http://tangrams.github.io/blocks/#geometry-projections) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/projections.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/projections.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **PI**: ```3.14159265359```
 - **HALF_PI**: ```1.57079632679```
 - **EARTH_RADIUS**: ```6378137.0```
 - **deg2rad(d)**: ```(((d)*3.14159265358979323846)/180.0)```
 - **QUATER_PI**: ```0.785398163```
 - **rad2deg(d)**: ```(((d)*180.0)/3.14159265358979323846)```

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


#### [geometry-tilt](http://tangrams.github.io/blocks/#geometry-tilt) <a href="https://github.com/tangrams/blocks/blob/gh-pages/geometry/tilt.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/geometry/tilt.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **TILT_MAX_ZOOM**: ```20.0```
 - **TILT_IN**: ```15.0```
 - **TILT_OUT**: ```20.0```
 - **TILT_ROTATE**: ```True```

These are the **shader blocks**:

- **position**:

```glsl
float t = u_time*0.1; 
float z = clamp(smoothstep(TILT_IN/TILT_MAX_ZOOM, TILT_OUT/TILT_MAX_ZOOM, max(u_map_position.z/TILT_MAX_ZOOM,0.)*0.9), 0., 1.);
#ifdef TILT_ROTATE
position.xyz = rotateX3D(z*HALF_PI) * rotateZ3D(sin(t)*PI*z) * position.xyz;
#else
position.xyz = rotateX3D(z*HALF_PI) * position.xyz;
#endif
```


