

#### [terrarium-base](https://github.com/tangrams/blocks/blob/gh-pages/terrarium/base.yaml)

This provides the following blocks:

- **position**:

```glsl
position.z += TERRARIUM_ZOFFSET*u_meters_per_pixel;
extrudeTerrarium(position);
```


- **global**:
 + `float getHeight() `
 + `void extrudeTerrarium (inout vec4 position) `

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




#### [terrarium-lines](https://github.com/tangrams/blocks/blob/gh-pages/terrarium/lines.yaml)



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **TERRARIUM_ZOFFSET**: ```0.2```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/lines.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/lines-full.yaml
```




#### [terrarium-terrain](https://github.com/tangrams/blocks/blob/gh-pages/terrarium/terrain.yaml)



This block use the following **defines** with the following defaults. Remember you can use or tweak.
 - **TERRARIUM_ZOFFSET**: ```0.0```


Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/terrain.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/terrarium/terrain-full.yaml
```


