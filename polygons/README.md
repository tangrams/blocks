

#### [polygons-diagonal-grid](http://tangrams.github.io/blocks/#polygons-diagonal-grid) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/diagonal-grid.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/diagonal-grid.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/diagonal-grid-full.yaml
```


These blocks uses a custom **shader**. These are the defaults **defines**:
 - **GRID_SCALE**: ```20.0```
 - **GRID_WIDTH**: ```0.05```

These are the **shader blocks**:

- **color**:

```glsl
color -= diagonalGrid(fract(getTileCoords()*GRID_SCALE),0.001+GRID_WIDTH);
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [polygons-diagonal-stripes](http://tangrams.github.io/blocks/#polygons-diagonal-stripes) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/diagonal-stripes.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/diagonal-stripes.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/diagonal-stripes-full.yaml
```


These blocks uses a custom **shader**. These are the defaults **defines**:
 - **STRIPES_MAX**: ```-.2```
 - **STRIPES_SCALE**: ```2.0```
 - **STRIPES_MAX_ZOOM**: ```20.0```
 - **STRIPES_OUT**: ```16.0```
 - **STRIPES_ALPHA**: ```0.5```
 - **STRIPES_MIN**: ```0.9```
 - **STRIPES_IN**: ```3.0```

These are the **shader blocks**:

- **color**:

```glsl
color.a = diagonalStripes(  (getTileCoords()*0.707)*(STRIPES_SCALE), 
                            mix(STRIPES_MIN,
                                STRIPES_MAX,
                                clamp( smoothstep(  STRIPES_IN/STRIPES_MAX_ZOOM, 
                                                    STRIPES_OUT/STRIPES_MAX_ZOOM, 
                                                    max(u_map_position.z/STRIPES_MAX_ZOOM, 0.) * 0.9), 
                                        0., 1.))) * STRIPES_ALPHA;
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [polygons-dots](http://tangrams.github.io/blocks/#polygons-dots) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/dots.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/dots.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/dots-full.yaml
```


These blocks uses a custom **shader**. These are the defaults **defines**:
 - **DOTS_SIZE**: ```0.41```
 - **DOTS_SCALE**: ```10.0```
 - **DOTS_COLOR**: ```vec3(0.212,0.302,0.431)```

These are the **shader blocks**:

- **color**:

```glsl
color.rgb = mix(color.rgb, DOTS_COLOR, TileDots(DOTS_SCALE, DOTS_SIZE));
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [polygons-glass-walls](http://tangrams.github.io/blocks/#polygons-glass-walls) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/glass-walls.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a glass walls to the sides of a geometry



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/glass-walls.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/glass-walls-full.yaml
```


These blocks uses a custom **shader**. These are the **shader blocks**:

- **color**:

```glsl
color.rgb *= vec3(min((worldPosition().z*.001 + .5),1.));

if (isWall()) {
    vec2 st = vec2(v_texcoord.x*10.,worldPosition().z*0.2);
    vec2 ipos = floor(st);
    vec2 fpos = fract(st);
    if ( step(0.01,fpos.x)*step(0.1,fpos.y) > 0.0 ){
        material.specular = vec4(1.) * max( 1.-(worldPosition().z*.001 + .5), 0. );
        material.emission = vec4(0.957,0.988,0.976,1.0) * step(.5,random(ipos*vec2(0.0000001,0.01)+floor(worldNormal().xy*10.0)));
        material.emission *= vec4(0.988,0.983,0.880,1.0) * step(.5,random(ipos));
    }
}

```


- **filter**:

```glsl
color.rgb += vec3(1.)* min( 1.-(worldPosition().z*.001 + .7) , 0.5 );
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/gotham.yaml&lines=131" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/gotham.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [polygons-pixelate](http://tangrams.github.io/blocks/#polygons-pixelate) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/pixelate.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/pixelate.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/pixelate-full.yaml
```


These blocks uses a custom **shader**. These are the **shader blocks**:

- **filter**:

```glsl
float gridSize = 40.;
float gradDarker = .7;
color.rgb = mix(color.rgb,
                color.rgb*gradDarker,
                random(floor(getTileCoords()*gridSize)));
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [polygons-shimmering](http://tangrams.github.io/blocks/#polygons-shimmering) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/shimmering.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/shimmering.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/shimmering-full.yaml
```


These blocks uses a custom **shader**. These are the defaults **defines**:
 - **SHIMMERING_OUT**: ```20.0```
 - **SHIMMERING_SPEED**: ```0.1```
 - **SHIMMERING_MAX_ZOOM**: ```20.0```
 - **SHIMMERING_SCALE_IN**: ```10.0```
 - **SHIMMERING_SCALE_OUT**: ```10.0```
 - **SHIMMERING_IN**: ```14.0```
 - **SHIMMERING_BACKGROUND**: ```vec3(0.000,0.00,0.94)```

These are the **shader blocks**:

- **color**:

```glsl
float z = clamp(smoothstep(SHIMMERING_IN/SHIMMERING_MAX_ZOOM, SHIMMERING_OUT/SHIMMERING_MAX_ZOOM, max(u_map_position.z/SHIMMERING_MAX_ZOOM,0.)*0.9), 0., 1.);
float scale = mix(SHIMMERING_SCALE_IN, SHIMMERING_SCALE_OUT, z);
/*
vec2 st = gl_FragCoord.xy/u_resolution.xy;
st = (st-.5)*scale+ .5;
if (u_resolution.y > u_resolution.x ) {
    st.y *= u_resolution.y/u_resolution.x;
} else {
    st.x *= u_resolution.x/u_resolution.y;
}
*/
vec2 st = getConstantCoords()*scale;

vec2 s = skew(st);
vec2 s_f = fract(s);
float n = snoise(vec3(floor(s+step(s_f.x,s_f.y)*5.),u_time*SHIMMERING_SPEED));
color.rgb = mix(color.rgb,
                mix(SHIMMERING_BACKGROUND,color.rgb,n),
                z);
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [polygons-stripes](http://tangrams.github.io/blocks/#polygons-stripes) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/stripes.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/stripes.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/stripes-full.yaml
```


These blocks uses a custom **shader**. These are the defaults **defines**:
 - **STRIPES_SCALE**: ```2.0```
 - **STRIPES_OUT**: ```16.0```
 - **STRIPES_ALPHA**: ```0.5```
 - **STRIPES_MIN**: ```0.9```
 - **STRIPES_MAX**: ```-.2```
 - **STRIPES_MAX_ZOOM**: ```20.0```
 - **STRIPES_IN**: ```3.0```
 - **STRIPES_ANGLE**: ```0.25```

These are the **shader blocks**:

- **color**:

```glsl
color.a = stripes(  getTileCoords()*STRIPES_SCALE, 
                    mix(STRIPES_MIN,
                        STRIPES_MAX,
                        clamp(smoothstep(STRIPES_IN/STRIPES_MAX_ZOOM, STRIPES_OUT/STRIPES_MAX_ZOOM, max(u_map_position.z/STRIPES_MAX_ZOOM,0.)*0.9), 0., 1.)), 
                  PI*STRIPES_ANGLE)*STRIPES_ALPHA;
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [polygons-windows](http://tangrams.github.io/blocks/#polygons-windows) <a href="https://github.com/tangrams/blocks/blob/gh-pages/polygons/windows.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a windows patterns on the walls of a geometry



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/windows.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/polygons/windows-full.yaml
```


These blocks uses a custom **shader**. These are the **shader blocks**:

- **color**:

```glsl
color.rgb *= vec3(min((worldPosition().z*.001 + .5),1.));
float t = 0.5;
if (isWall()) {
    vec2 st = vec2(v_texcoord.x*10.,worldPosition().z*0.2);
    vec2 ipos = floor(st);
    vec2 fpos = fract(st);
    if ( step(0.6,fpos.x)*step(0.4,fpos.y) > 0.0 ){
        material.specular = vec4(1.) * max( 1.-(worldPosition().z*.001 + .5), 0. );
        material.emission = vec4(0.988,0.983,0.880,1.0) * step(.5,random(ipos+floor(worldNormal().xy*10.0)+t));
    }
}

```


- **filter**:

```glsl
color.rgb += vec3(1.)* min( 1.-(worldPosition().z*.001 + .7) , 0.5 );
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/gotham.yaml&lines=128" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/gotham.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
