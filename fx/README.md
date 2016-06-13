

#### fx-water [<i class='fa fa-github' aria-hidden='true'></i>](https://github.com/tangrams/blocks/tree/gh-pages//fx/water.yaml)
Water effect, made by altering the normal map of a surface and applying a sky spherical map to the surface. The result looks like moving water. <p>See sandbox example:</p>
[ <div style="background-image: url(https://tangrams.github.io/tangram-sandbox/styles/sandbox.png); width: 100%; height: 100px; background-position: center center;"></div> ](https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/sandbox.yaml)
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


