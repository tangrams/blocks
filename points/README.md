

#### [points-cross](http://tangrams.github.io/blocks/#points-cross) <a href="https://github.com/tangrams/blocks/blob/gh-pages/points/cross.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Draws a '+' shape in each point. To learn more about shapes on shaders read [this chapter from The Nook of Shader](http://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/points/cross.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/points/cross-full.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **CROSS_ALPHA**: ```0.75```

These are the **shader blocks**:

- **color**:

```glsl
color.a = clamp(cross(v_texcoord.xy,vec2(2.,.5)),0.,1.)*CROSS_ALPHA;

```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/callejas.yaml&lines=96-99" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/callejas.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [points-shape](http://tangrams.github.io/blocks/#points-shape) <a href="https://github.com/tangrams/blocks/blob/gh-pages/points/shape.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Draws shape with N amount of sides (`SHAPE_SIDES`), a colored border (`SHAPE_BORDER_WIDTH` & `SHAPE_BORDER_COLOR`). To learn more about shapes on shaders read [this chapter from The Nook of Shader](http://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/points/shape.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/points/shape-full.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **SHAPE_ALPHA**: ```1.0```
 - **SHAPE_BORDER_WIDTH**: ```0.15```
 - **SHAPE_SIDES**: ```3```
 - **SHAPE_BORDER_COLOR**: ```vec3(1.)```
 - **SHAPE_SIZE**: ```1.0```

These are the **shader blocks**:

- **color**:

```glsl
float df = shapeDF(vec2(v_texcoord.x,1.-v_texcoord.y),int(SHAPE_SIDES));
color.rgb = mix(color.rgb,
                SHAPE_BORDER_COLOR,
                aastep(SHAPE_SIZE*.5-SHAPE_BORDER_WIDTH,df));
color.a = (1.-aastep(SHAPE_SIZE*.5,df))*SHAPE_ALPHA;
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/elevation-places.yaml&lines=29-36" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/elevation-places.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
