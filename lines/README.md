

#### [lines-chevron](http://tangrams.github.io/blocks/#lines-chevron) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/chevron.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a chevron pattern to a line



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/chevron.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/chevron-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **CHEVRON_SIZE**:  number between ```0.0``` and ```10.0``` that control the *size*. The *default value* is ```1.0```. 
 -  **CHEVRON_COLOR**:  The *default value* is ```color.rgb*.5```. 
 -  **CHEVRON_ALPHA**:  number between ```0.0``` and ```1.0``` that control the *alpha*. The *default value* is ```1.0```. 
 -  **CHEVRON_SCALE**:  number between ```0.0``` and ```10.0``` that control the *scale*. The *default value* is ```1.0```. 
 -  **CHEVRON_BACKGROUND_COLOR**:  The *default value* is ```color.rgb```. 
 -  **CHEVRON_BACKGROUND_ALPHA**:  number between ```0.0``` and ```1.0``` that control the *background alpha*. The *default value* is ```color.a```. 

These are the **shader blocks**:

- **color**:

```glsl
color = mix(vec4(CHEVRON_BACKGROUND_COLOR, CHEVRON_BACKGROUND_ALPHA),
            vec4(CHEVRON_COLOR, CHEVRON_ALPHA),
            step(.5,fract((v_texcoord.y+abs(v_texcoord.x-.5)) * CHEVRON_SCALE)*CHEVRON_SIZE));
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-dash](http://tangrams.github.io/blocks/#lines-dash) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/dash.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a stripe pattern to a line



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dash.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dash-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **DASH_SIZE**:  number between ```0.0``` and ```1.0``` that control the *size*. The *default value* is ```0.5```. 
 -  **DASH_SCALE**:  number between ```1.0``` and ```1000.0``` that control the *scale*. The *default value* is ```0.1```. 

These are the **shader blocks**:

- **filter**:

```glsl
if ( step(DASH_SIZE,fract(v_texcoord.y*DASH_SCALE)) == 0.){
    discard;
}
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/elevation.yaml&lines=59-63" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/elevation.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-datastream](http://tangrams.github.io/blocks/#lines-datastream) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/datastream.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply some stream of random lines to your lines



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/datastream.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/datastream-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **DATASTREAM_SPEED**:  number between ```0.0``` and ```1000.0``` that control the *speed*. The *default value* is ```20.0```. 
 -  **DATASTREAM_MARGIN**:  number between ```0.0``` and ```1.0``` that control the *lines margins*. The *default value* is ```0.4```. 
 -  **DATASTREAM_AMOUNT**:  number between ```0.0``` and ```1.0``` that control the *amount*. The *default value* is ```0.8```. 
 -  **DATASTREAM_ROADS**:  number between ```0.0``` and ```10.0``` that control the *number of roads*. The *default value* is ```5.0```. 
 -  **DATASTREAM_COLOR**:  The *default value* is ```vec3(1.)```. 
 -  **DATASTREAM_BACKGROUND_COLOR**:  The *default value* is ```color.rgb```. 

These are the **shader blocks**:

- **global**:
 + `float datastream_pattern(vec2 st, float v, float t) `
- **color**:

```glsl
color.rgb = mix(DATASTREAM_BACKGROUND_COLOR,
                DATASTREAM_COLOR,
                datastream_pattern( v_texcoord.xy, 
                                    u_time*(DATASTREAM_SPEED)*(-.5 * random(floor(v_texcoord.x*DATASTREAM_ROADS)) - .5), 
                                    DATASTREAM_AMOUNT )* 
                (step(DATASTREAM_MARGIN,1.-fract(v_texcoord.x*DATASTREAM_ROADS))*
                 step(DATASTREAM_MARGIN,fract(v_texcoord.x*DATASTREAM_ROADS))));
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-dots-glow](http://tangrams.github.io/blocks/#lines-dots-glow) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/dots-glow.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a dot pattern to a line with some glow



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dots-glow.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dots-glow-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **DOTS_SIZE**:  number between ```0.0``` and ```1.0``` that control the *size*. The *default value* is ```0.15```. 
 -  **DOTS_SCALE**:  number between ```0.0``` and ```2.0``` that control the *scale*. The *default value* is ```2.0```. 
 -  **DOTS_GLOW**:  number between ```0.0``` and ```1.0``` that control the *glow amount*. The *default value* is ```0.5```. 

These are the **shader blocks**:

- **color**:

```glsl
vec2 st = (fract(v_texcoord.xy)-.5)*DOTS_SCALE;
float df = dot(st,st);
color.a = 1.-step(DOTS_SIZE, df);
color.a += smoothstep(1.,0.,df)*(DOTS_GLOW);
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-dots](http://tangrams.github.io/blocks/#lines-dots) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/dots.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a dot pattern to a line



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dots.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dots-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **DOTS_SIZE**:  number between ```0.0``` and ```1.0``` that control the *size*. The *default value* is ```0.05```. 

These are the **shader blocks**:

- **color**:

```glsl
vec2 st = fract(v_texcoord.xy)-.5;
color.a = 1.- step(DOTS_SIZE, dot(st,st)*2.);
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-glow](http://tangrams.github.io/blocks/#lines-glow) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/glow.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Add an exciting glow effect to your



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/glow.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/glow-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **GLOW_WIDTH**:  number between ```0.0``` and ```1.0``` that control the *solid width*. The *default value* is ```0.4```. 
 -  **GLOW_BRIGHTNESS**:  number between ```0.0``` and ```1.0``` that control the *glow brightness*. The *default value* is ```0.25```. 

These are the **shader blocks**:

- **color**:

```glsl
vec4 glow_tmp_color = color;
color = glow_tmp_color*(aastep(GLOW_WIDTH,1.-v_texcoord.x)*aastep(GLOW_WIDTH,v_texcoord.x));
color += glow_tmp_color*(sin(v_texcoord.x*PI)*GLOW_BRIGHTNESS);
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-outline](http://tangrams.github.io/blocks/#lines-outline) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/outline.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply an outline to a line



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/outline.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/outline-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **OUTLINE_WIDTH**:  number between ```0.0``` and ```1.0``` that control the *width*. The *default value* is ```0.1```. 
 -  **OUTLINE_COLOR**:  The *default value* is ```color.rgb*.5```. 

These are the **shader blocks**:

- **color**:

```glsl
color.rgb = mix(color.rgb,
                OUTLINE_COLOR,
                (1.0-(aastep(OUTLINE_WIDTH,v_texcoord.x)-step(1.0-OUTLINE_WIDTH,v_texcoord.x))));
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/blueprint.yaml&lines=116-120" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/blueprint.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/callejas.yaml&lines=116" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/callejas.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-rainbow](http://tangrams.github.io/blocks/#lines-rainbow) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/rainbow.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a rainbow color pattern to a line



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/rainbow.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/rainbow-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **color**:

```glsl
color.rgb = hsb2rgb(vec3(v_texcoord.x,1.,1.));
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-stripes](http://tangrams.github.io/blocks/#lines-stripes) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/stripes.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Apply a stripe pattern to a line



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/stripes.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/stripes-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **STRIPES_WIDTH**:  number between ```0.0``` and ```1.0``` that control the *width*. The *default value* is ```0.1```. 
 -  **STRIPES_COLOR**:  The *default value* is ```color.rgb*.5```. 
 -  **STRIPES_BACKGROUND_COLOR**:  The *default value* is ```color.rgb```. 

These are the **shader blocks**:

- **color**:

```glsl
color.rgb = mix(STRIPES_BACKGROUND_COLOR,
                STRIPES_COLOR,
                step(STRIPES_WIDTH, sin((fract(v_texcoord).x+fract(v_texcoord).y) * 6.283)));
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/grain-roads.yaml&lines=35" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/grain-roads.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
