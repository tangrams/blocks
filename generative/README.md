

#### [generative-fbm](http://tangrams.github.io/blocks/#generative-fbm) <a href="https://github.com/tangrams/blocks/blob/gh-pages/generative/fbm.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Set of Fractal Brownian Motion functions.
For more information on this theme read [this chapter of The Book of Shaders about fractal Brownian Motion](http://thebookofshaders.com/13/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/fbm.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/fbm-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **NUM_OCTAVES**:  The *default value* is ```5```. 

These are the **shader blocks**:

- **global**:
 + `float fbm (in float x)`
 + `float fbm (in vec2 xy)`
 + `float fbm (in vec3 xyz)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
![](http://tangrams.github.io/blocks/./generative/generative-fbm.png)

- **fbm_float_5oct** ( mean: 0.0129786044136 median: 0.012977 ):


```glsl
color += fbm(v_texcoord.x);
```


- **fbm_vec2_5oct** ( mean: 0.0797156163074 median: 0.079713 ):


```glsl
color += fbm(v_texcoord);
```


- **fbm_vec3_5oct** ( mean: 0.0918465875438 median: 0.091821 ):


```glsl
color += fbm(vec3(v_texcoord,u_time));
```


- **fbm_float_8oct** ( mean: 0.036561471747 median: 0.036585 ):


```glsl
color += fbm(v_texcoord.x);
```


- **fbm_vec3_8oct** ( mean: 0.253147785452 median: 0.213681 ):


```glsl
color += fbm(vec3(v_texcoord,u_time));
```


- **fbm_float_3oct** ( mean: 0.0082190238837 median: 0.008214 ):


```glsl
color += fbm(v_texcoord.x);
```


- **fbm_vec2_3oct** ( mean: 0.0427192917853 median: 0.042711 ):


```glsl
color += fbm(v_texcoord);
```


- **fbm_vec3_3oct** ( mean: 0.0445404752999 median: 0.044535 ):


```glsl
color += fbm(vec3(v_texcoord,u_time));
```


- **fbm_vec2_8oct** ( mean: 0.241552287655 median: 0.204608 ):


```glsl
color += fbm(v_texcoord);
```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [generative-caustic](http://tangrams.github.io/blocks/#generative-caustic) <a href="https://github.com/tangrams/blocks/blob/gh-pages/generative/caustics.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Caustic generative texture inspired on <https://www.shadertoy.com/view/MdlXz8> by David Hoskins



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/caustics.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/caustics-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **TAU**:  The *default value* is ```6.28318530718```. 
 -  **CAUSTIC_ITERATIONS**:  The *default value* is ```3```. 

These are the **shader blocks**:

- **global**:
 + `vec3 getCaustic (vec2 uv)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
![](http://tangrams.github.io/blocks/./generative/generative-caustic.png)

- **getCaustic_3iter** ( mean: 0.0268119082978 median: 0.026815 ):


```glsl
color.rgb += getCaustic(v_texcoord);
```


- **getCaustic_5iter** ( mean: 0.0424732053934 median: 0.042478 ):


```glsl
color.rgb += getCaustic(v_texcoord);
```


- **getCaustic_4iter** ( mean: 0.0347584188312 median: 0.034755 ):


```glsl
color.rgb += getCaustic(v_texcoord);
```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [generative-noise](http://tangrams.github.io/blocks/#generative-noise) <a href="https://github.com/tangrams/blocks/blob/gh-pages/generative/noise.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Set of Noise functions.
For more information on this theme read [this chapter of The Book of Shaders about Noise](http://thebookofshaders.com/11/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/noise.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/noise-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float noise (in float x)`
 + `float noise (vec2 xy)`
 + `float noise (vec3 xyz)`
 + `vec3 mod289(vec3 x)`
 + `vec2 mod289(vec2 x)`
 + `vec3 permute(vec3 x)`
 + `float snoise(vec2 v)`
 + `float snoise (vec3 p)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
![](http://tangrams.github.io/blocks/./generative/generative-noise.png)

- **noise_float** ( mean: 0.003561023355 median: 0.003563 ):


```glsl
color += noise(v_texcoord.x);
```


- **noise_vec2** ( mean: 0.00991735265406 median: 0.009915 ):


```glsl
color += noise(v_texcoord.xy);
```


- **snoise_vec3** ( mean: 0.012500758665 median: 0.012504 ):


```glsl
color += snoise(vec3(v_texcoord.xy,u_time));
```


- **noise_vec3** ( mean: 0.0104708118912 median: 0.01047 ):


```glsl
color += noise(vec3(v_texcoord.xy,u_time));
```


- **snoise_vec2** ( mean: 0.00696662253005 median: 0.006966 ):


```glsl
color += snoise(v_texcoord.xy);
```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [generative-voronoi](http://tangrams.github.io/blocks/#generative-voronoi) <a href="https://github.com/tangrams/blocks/blob/gh-pages/generative/voronoi.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Set of Voronoi functions.
For more information on this theme read [this chapter of The Book of Shaders about Cellular Noise and Voronoi](http://thebookofshaders.com/12/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/voronoi.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/voronoi-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `vec3 voronoi (vec2 st)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
![](http://tangrams.github.io/blocks/./generative/generative-voronoi.png)

- **voronoi** ( mean: 0.0329303864778 median: 0.032942 ):


```glsl
color.rgb = voronoi(v_texcoord);
```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [generative-random](http://tangrams.github.io/blocks/#generative-random) <a href="https://github.com/tangrams/blocks/blob/gh-pages/generative/random.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Set of functions about random.
For more information on this theme read [this chapter of The Book of Shaders about Random](http://thebookofshaders.com/10/).



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/random.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/generative/random-full.yaml
```


These blocks uses a custom **shader**.
These are the **uniforms**:
 -  **u_random**:  The *default value* is ```https://tangrams.github.io/blocks/generative/imgs/tex16.png```. 

These are the **shader blocks**:

- **global**:
 + `float random (float x)`
 + `float random (vec2 p)`
 + `float random (vec3 p)`
 + `vec2 random2 (vec2 xy)`
 + `vec3 random3 (vec2 xy)`
 + `vec3 random3 (vec3 c)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
![](http://tangrams.github.io/blocks/./generative/generative-random.png)

- **random_vec3** ( mean: 0.0023659912227 median: 0.002364 ):


```glsl
color.rgb += random(vec3(v_texcoord.xy,u_time));
```


- **random_vec2** ( mean: 0.00311012685807 median: 0.00311 ):


```glsl
color.rgb += random(v_texcoord.xy);
```


- **random3_vec2_t** ( mean: 0.00198231552007 median: 0.001965 ):


```glsl
color.rgb += random3(v_texcoord.xy);
```


- **random_float** ( mean: 0.00223235727403 median: 0.002227 ):


```glsl
color.rgb += random(v_texcoord.x);
```


- **random2_vec2** ( mean: 0.00325916375102 median: 0.003262 ):


```glsl
color.rg += random2(v_texcoord.xy);
```


- **random3_vec3** ( mean: 0.00267978437373 median: 0.002678 ):


```glsl
color.rgb += random3(vec3(v_texcoord.xy,u_time));
```


- **random3_vec2** ( mean: 0.00420477196954 median: 0.004213 ):


```glsl
color.rgb += random3(v_texcoord.xy);
```

