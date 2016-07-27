

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
 - **GRID_BACKGROUND_COLOR**: ```color.rgb*.5```
 - **GRID_WIDTH**: ```0.05```

These are the **shader blocks**:

- **color**:

```glsl
color.rgb = mix(color.rgb, GRID_BACKGROUND_COLOR, diagonalGrid(  fract(getTileCoords()*GRID_SCALE),
                        GRID_WIDTH));
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
 - **STRIPES_ALPHA**: ```1.0```
 - **STRIPES_SCALE**: ```2.0```
 - **STRIPES_WIDTH**: ```0.5```

These are the **shader blocks**:

- **color**:

```glsl
color.a = diagonalStripes( (getTileCoords()*0.999)*floor(STRIPES_SCALE), 
                            STRIPES_WIDTH) * STRIPES_ALPHA;
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
 - **DOTS_COLOR**: ```color.rgb*.5```

These are the **shader blocks**:

- **color**:

```glsl
color.rgb = mix(color.rgb, 
                DOTS_COLOR, 
                aastep( DOTS_SIZE,
                        circleDF(vec2(0.5)-brick(getTileCoords()*DOTS_SCALE,2.)));
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


These blocks uses a custom **shader**. These are the defaults **defines**:
 - **PIXELATE_BACKGROUND**: ```color.rgb*.5```
 - **PIXELATE_SCALE**: ```40.0```

These are the **shader blocks**:

- **color**:

```glsl
color.rgb = mix(color.rgb,
                PIXELATE_BACKGROUND,
                random(floor(getTileCoords()*PIXELATE_SCALE)));
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
 - **SHIMMERING_ANIMATED**: ```True```
 - **SHIMMERING_SPEED**: ```0.1```
 - **SHIMMERING_SCALE**: ```10.0```
 - **SHIMMERING_BACKGROUND**: ```color.rgb*.5```
 - **SHIMMERING_AMOUNT**: ```1.0```

These are the **shader blocks**:

- **color**:

```glsl
vec2 st = getConstantCoords()*SHIMMERING_SCALE;
vec2 s = skew(st);
vec2 s_f = fract(s);
#ifdef SHIMMERING_ANIMATED
float n = snoise(vec3(floor(s+step(s_f.x,s_f.y)*5.),u_time*SHIMMERING_SPEED));
#else
float n = snoise(floor(s+step(s_f.x,s_f.y)*5.));
#endif
color.rgb = mix(color.rgb,
                mix(SHIMMERING_BACKGROUND,color.rgb,n),
                SHIMMERING_AMOUNT);
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
 - **STRIPES_WIDTH**: ```0.5```
 - **STRIPES_ANGLE**: ```PI*0.25```
 - **STRIPES_SCALE**: ```2.0```
 - **STRIPES_ALPHA**: ```0.5```

These are the **shader blocks**:

- **color**:

```glsl
color.a = stripes(  getTileCoords()*STRIPES_SCALE, 
                    STRIPES_WIDTH, 
                    STRIPES_ANGLE)*STRIPES_ALPHA;
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
