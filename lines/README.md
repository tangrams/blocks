

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


This blocks use a custom **shader**.These are the defaults **defines**:
 - **CHEVRON_SIZE**: ```1.0```
 - **CHEVRON_COLOR**: ```vec3(1., 0., 0.)```
 - **CHEVRON_ALPHA**: ```1.0```
 - **CHEVRON_SCALE**: ```1.0```

These are the **shader blocks**:

- **color**:

```glsl
color = mix(color,
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


This blocks use a custom **shader**.These are the defaults **defines**:
 - **DASH_SIZE**: ```0.5```
 - **DASH_SCALE**: ```0.1```

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


This blocks use a custom **shader**.These are the defaults **defines**:
 - **DOT_SIZE**: ```0.05```

These are the **shader blocks**:

- **color**:

```glsl
vec2 st = fract(v_texcoord.xy);
st -= .5;
color.a = 1.- step(DOT_SIZE, dot(st,st)*2.);
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


This blocks use a custom **shader**.These are the defaults **defines**:
 - **OUTLINE_WIDTH**: ```0.1```
 - **OUTLINE_COLOR**: ```vec3(1.)```

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


#### [lines-stripes](http://tangrams.github.io/blocks/#lines-stripes) <a href="https://github.com/tangrams/blocks/blob/gh-pages/lines/rainbow.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

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


This blocks use a custom **shader**.These are the **shader blocks**:

- **color**:

```glsl
color.rgb = hsb2rgb(vec3(v_texcoord.x,1.,1.));
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/crosshatch.yaml&lines=111" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/crosshatch.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/pericoli.yaml&lines=157" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/pericoli.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

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


This blocks use a custom **shader**.These are the defaults **defines**:
 - **STRIPES_INTENSITY**: ```0.1```
 - **STRIPES_WIDTH**: ```0.1```

These are the **shader blocks**:

- **color**:

```glsl
color.rgb += step(STRIPES_WIDTH, sin((fract(v_texcoord).x+fract(v_texcoord).y) * 6.283)) * STRIPES_INTENSITY;
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/grain-roads.yaml&lines=35" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/grain-roads.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
