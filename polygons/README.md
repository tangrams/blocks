

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
