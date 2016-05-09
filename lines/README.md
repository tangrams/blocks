

#### + [lines-dash](https://github.com/tangrams/blocks/blob/gh-pages/lines/dash.yaml)

This provides the following blocks:

- **color**:

```glsl
color.a = 1.-step(DASH_SIZE,fract(v_texcoord.y*DASH_SCALE));
```



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **DASH_SIZE**: ```0.5```
 - **DASH_SCALE**: ```0.1```


Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/lines/dash.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - http://tangrams.github.io/blocks/lines/dash-full.yaml
```




#### + [lines-dots](https://github.com/tangrams/blocks/blob/gh-pages/lines/dots.yaml)

This provides the following blocks:

- **color**:

```glsl
vec2 st = fract(v_texcoord.xy);
st -= .5;
color.a = 1.- step(DOT_SIZE, dot(st,st)*2.);
```



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **DOT_SIZE**: ```0.05```


Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/lines/dots.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - http://tangrams.github.io/blocks/lines/dots-full.yaml
```




#### + [lines-outline](https://github.com/tangrams/blocks/blob/gh-pages/lines/outline.yaml)

This provides the following blocks:

- **color**:

```glsl
color.rgb = mix(color.rgb,
                OUTLINE_COLOR,
                (1.0-(aastep(OUTLINE_WIDTH,v_texcoord.x)-step(1.0-OUTLINE_WIDTH,v_texcoord.x))));
```



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **OUTLINE_WIDTH**: ```0.1```
 - **OUTLINE_COLOR**: ```vec3(1.)```


Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/lines/outline.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - http://tangrams.github.io/blocks/lines/outline-full.yaml
```




#### + [lines-stripes](https://github.com/tangrams/blocks/blob/gh-pages/lines/stripes.yaml)

This provides the following blocks:

- **color**:

```glsl
color.rgb += step(STRIPES_WIDTH, sin((fract(v_texcoord).x+fract(v_texcoord).y) * 6.283)) * STRIPES_INTENSITY;
```



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **STRIPES_INTENSITY**: ```0.1```
 - **STRIPES_WIDTH**: ```0.1```


Import it using:

```yaml
import:
    - http://tangrams.github.io/blocks/lines/stripes.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - http://tangrams.github.io/blocks/lines/stripes-full.yaml
```


