

#### [lines-chevron](https://github.com/tangrams/blocks/blob/gh-pages/lines/chevron.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/chevron.yaml
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


#### [lines-dash](https://github.com/tangrams/blocks/blob/gh-pages/lines/dash.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dash.yaml
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



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-dots](https://github.com/tangrams/blocks/blob/gh-pages/lines/dots.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/dots.yaml
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


#### [lines-outline](https://github.com/tangrams/blocks/blob/gh-pages/lines/outline.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/outline.yaml
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



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-stripes](https://github.com/tangrams/blocks/blob/gh-pages/lines/rainbow.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/rainbow.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **color**:

```glsl
color.rgb = hsb2rgb(vec3(v_texcoord.x,1.,1.));
```



![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [lines-stripes](https://github.com/tangrams/blocks/blob/gh-pages/lines/stripes.yaml)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/lines/stripes.yaml
```


This blocks use a custom **shader**.These are the defaults **defines**:
 - **STRIPES_INTENSITY**: ```0.1```
 - **STRIPES_WIDTH**: ```0.1```

These are the **shader blocks**:

- **color**:

```glsl
color.rgb += step(STRIPES_WIDTH, sin((fract(v_texcoord).x+fract(v_texcoord).y) * 6.283)) * STRIPES_INTENSITY;
```


