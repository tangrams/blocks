

#### [fx-water](http://tangrams.github.io/blocks/#fx-water) <a href="https://github.com/tangrams/blocks/blob/gh-pages/fx/water.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Water effect, made by altering the normal map of a surface and applying a sky spherical map to the surface. 
The result looks like moving water.



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/fx/water.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/fx/water-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **normal**:

```glsl
normal += snoise(vec3(worldPosition().xy*0.08,u_time*.5))*0.02;
```



Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/sandbox.yaml" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/sandbox.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
