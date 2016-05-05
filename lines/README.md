

### [lines-dots](https://github.com/tangrams/blocks/blob/gh-pages/lines/dash.yaml)

Provides the following blocks:

- **color**:

```glsl
color.a = 1.-step(dash_size,fract(v_texcoord.y*dash_scale));
```




### [lines-dots](https://github.com/tangrams/blocks/blob/gh-pages/lines/dots.yaml)

Provides the following blocks:

- **color**:

```glsl
vec2 st = fract(v_texcoord.xy);
st -= .5;
color.a = 1.- step(dotSize, dot(st,st)*2.);
```




### [lines-outline](https://github.com/tangrams/blocks/blob/gh-pages/lines/outline.yaml)

Provides the following blocks:

- **color**:

```glsl
color.rgb = mix(color.rgb,
                outline_color,
                (1.0-(aastep(outline_width,v_texcoord.x)-step(1.0-outline_width,v_texcoord.x))));
```




### [lines-stripes](https://github.com/tangrams/blocks/blob/gh-pages/lines/stripes.yaml)

Provides the following blocks:

- **color**:

```glsl
vec2 st = fract(v_texcoord);
color.rgb += step(.1,sin((st.x+st.y)*6.283))*.1;
```


