

#### [fx-water](https://github.com/tangrams/blocks/blob/gh-pages/fx/water.yaml)

This provides the following blocks:

- **normal**:

```glsl
normal += snoise(vec3(worldPosition().xy*0.08,u_time*.5))*0.02;
```



Import it using:

```yaml
import:
    - https://tangrams.github.io/blocks/fx/water.yaml
```




If you want to import this block with dependences included try this:

```yaml
import:
    - https://tangrams.github.io/blocks/fx/water-full.yaml
```


