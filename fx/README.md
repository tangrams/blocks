

#### [fx-water](https://github.com/tangrams/blocks/blob/gh-pages/fx/water.yaml)

Water effect, made by altering the normal map of a surface and applying a sky spherical map to the surface. 
The result looks like moving water.



Import using:

```yaml
import:
    - https://tangrams.github.io/blocks/fx/water.yaml
```


This blocks use a custom **shader**.These are the **shader blocks**:

- **normal**:

```glsl
normal += snoise(vec3(worldPosition().xy*0.08,u_time*.5))*0.02;
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/sandbox.yaml" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/sandbox.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
