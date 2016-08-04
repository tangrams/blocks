

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


These blocks uses a custom **shader**.
These are the **defines**:
 -  **CROSS_ALPHA**:  number between ```0.0``` and ```1.0``` that control the *alpha*. The *default value* is ```0.75```. 

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


#### [points-glow](http://tangrams.github.io/blocks/#points-glow) <a href="https://github.com/tangrams/blocks/blob/gh-pages/points/glow.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/points/glow.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/points/glow-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **filter**:

```glsl
float b = getBrightness(color.rgb);
vec2 st = v_texcoord.xy;
color = mix(v_color*color.a,vec4(0.),b*b);
```



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


These blocks uses a custom **shader**.
These are the **defines**:
 -  **SHAPE_ALPHA**:  number between ```0.0``` and ```1.0``` that control the *alpha*. The *default value* is ```1.0```. 
 -  **SHAPE_BORDER_WIDTH**:  number between ```0.0``` and ```1.0``` that control the *size*. The *default value* is ```0.15```. 
 -  **SHAPE_SIDES**:  number between ```1.0``` and ```6.0``` that control the *corners*. The *default value* is ```3```. 
 -  **SHAPE_BORDER_COLOR**:  The *default value* is ```vec3(1.)```. 
 -  **SHAPE_SIZE**:  number between ```0.0``` and ```1.0``` that control the *size*. The *default value* is ```1.0```. 

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
