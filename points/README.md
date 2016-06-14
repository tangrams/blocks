

#### [points-cross](https://github.com/tangrams/blocks/blob/gh-pages/points/cross.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/points/cross.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **CROSS_ALPHA**: ```0.75```

These are the **shader blocks**:

- **color**:

```glsl
color.a = clamp(cross(v_texcoord.xy,vec2(2.,.5)),0.,1.)*CROSS_ALPHA;

```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [points-shape](https://github.com/tangrams/blocks/blob/gh-pages/points/shape.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/points/shape.yaml
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


