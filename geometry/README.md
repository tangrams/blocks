

### [geometry-dynamic-height](https://github.com/tangrams/blocks/blob/gh-pages/geometry/dynamic-height.yaml)

This provides the following blocks:

- **position**:

```glsl
float zoom = map(u_map_position.z,ZOOM_START,ZOOM_END,1.,0.);
position.z *= max(1.,.5+ZOOM_LINEAR_FACTOR*zoom);
```



This blocks have the following defines you can tweak:
 - **ZOOM_LINEAR_FACTOR**: ```2.0```
 - **ZOOM_START**: ```15.0```
 - **ZOOM_END**: ```20.0```


Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./geometry./geometry/dynamic-height.yaml
```




### [geometry-dynamic-width](https://github.com/tangrams/blocks/blob/gh-pages/geometry/dynamic-width.yaml)

This provides the following blocks:

- **width**:

```glsl
width *= 0.2+min(pow(position.z*0.006,2.),.6);
```



Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./geometry./geometry/dynamic-width.yaml
```




### [geometry-matrices](https://github.com/tangrams/blocks/blob/gh-pages/geometry/matrices.yaml)

This provides the following blocks:

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

This blocks have the following defines you can tweak:
 - **HALF_PI**: ```1.57079632679```
 - **TWO_PI**: ```6.28318530718```
 - **PI**: ```3.14159265359```


Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./geometry./geometry/matrices.yaml
```




### [geometry-normal](https://github.com/tangrams/blocks/blob/gh-pages/geometry/normal.yaml)

This provides the following blocks:

- **global**:
 + `bool isWall() `
 + `bool isRoof() `

Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./geometry./geometry/normal.yaml
```




### [geometry-projections](https://github.com/tangrams/blocks/blob/gh-pages/geometry/projections.yaml)

This provides the following blocks:

- **global**:
 + `float y2lat_d (float y) `
 + `float x2lon_d (float x) `
 + `float lat2y_d (float lat) `
 + `float lon2x_d (float lon) `
 + `float y2lat_m (float y) `
 + `float x2lon_m (float x) `
 + `float lat2y_m (float lat) `
 + `float lon2x_m (float lon) `
 + `vec2 latlon2albers(float lat, float lon, float lat0, float lng0, float phi1, float phi2 ) `
 + `vec2 latlon2albers (float lat, float lon, float delta_phi1, float delta_phi2) `
 + `vec2 latlon2albers (float lat, float lon, float width) `
 + `vec2 latlon2azimuthal (float lat, float lon, float phi1, float lambda0) `
 + `vec2 azimuthal(float lat, float lon) `
 + `vec2 azimuthalNorth(float lat, float lon) `
 + `vec2 azimuthalSouth(float lat, float lon) `

This blocks have the following defines you can tweak:
 - **PI**: ```3.14159265359```
 - **HALF_PI**: ```1.57079632679```
 - **EARTH_RADIUS**: ```6378137.0```
 - **deg2rad(d)**: ```(((d)*3.14159265358979323846)/180.0)```
 - **QUATER_PI**: ```0.785398163```
 - **rad2deg(d)**: ```(((d)*180.0)/3.14159265358979323846)```


Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./geometry./geometry/projections.yaml
```




### [geometry-terrarium](https://github.com/tangrams/blocks/blob/gh-pages/geometry/terrarium.yaml)

This provides the following blocks:

- **position**:

```glsl
position.z += ZOFFSET*u_meters_per_pixel;
extrudeTerrain(position);
```


- **global**:
 + `float getHeight() `
 + `void extrudeTerrain(inout vec4 position) `

This blocks have the following defines you can tweak:
 - **ZOFFSET**: ```0.0```


Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./geometry./geometry/terrarium.yaml
```




### [geometry-tilt](https://github.com/tangrams/blocks/blob/gh-pages/geometry/tilt.yaml)

This provides the following blocks:

- **position**:

```glsl
float t = u_time*0.1; 
float z = clamp(smoothstep(TILT_IN/TILT_MAX_ZOOM, TILT_OUT/TILT_MAX_ZOOM, max(u_map_position.z/TILT_MAX_ZOOM,0.)*0.9), 0., 1.);
position.xyz = rotateX3D(z*HALF_PI) * rotateZ3D(sin(t)*PI*z) * position.xyz;
```



This blocks have the following defines you can tweak:
 - **TILT_MAX_ZOOM**: ```20.0```
 - **TILT_IN**: ```15.0```
 - **TILT_OUT**: ```20.0```


Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/./geometry./geometry/tilt.yaml
```

