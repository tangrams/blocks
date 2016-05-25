

#### [terrarium-base](https://github.com/tangrams/blocks/blob/gh-pages/terrarium/base.yaml)

This provides the following blocks:

- **position**:

```glsl
position.z += TERRARIUM_ZOFFSET*u_meters_per_pixel;
extrudeTerrain(position);
```


- **global**:
 + `float getHeight() `
 + `void extrudeTerrain (inout vec4 position) `

This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **TERRARIUM_ZOFFSET**: ```0.0```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/base.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/base-full.yaml
```


