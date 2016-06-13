

#### [points-cross](https://github.com/tangrams/blocks/blob/gh-pages/points/cross.yaml)

This provides the following blocks:

- **color**:

```glsl
color.a = clamp(cross(v_texcoord.xy,vec2(2.,.5)),0.,1.)*CROSS_ALPHA;

```



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **CROSS_ALPHA**: ```0.75```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/points/cross.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/points/cross-full.yaml
```




#### [points-shape](https://github.com/tangrams/blocks/blob/gh-pages/points/shape.yaml)

This provides the following blocks:

- **color**:

```glsl
float df = shapeDF(vec2(v_texcoord.x,1.-v_texcoord.y),int(SHAPE_SIDES));
color.rgb = mix(color.rgb,
                SHAPE_BORDER_COLOR,
                aastep(SHAPE_SIZE*.5-SHAPE_BORDER_WIDTH,df));
color.a = (1.-aastep(SHAPE_SIZE*.5,df))*SHAPE_ALPHA;
```



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **SHAPE_ALPHA**: ```1.0```
 - **SHAPE_BORDER_WIDTH**: ```0.15```
 - **SHAPE_SIDES**: ```3```
 - **SHAPE_BORDER_COLOR**: ```vec3(1.)```
 - **SHAPE_SIZE**: ```1.0```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/points/shape.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/points/shape-full.yaml
```


