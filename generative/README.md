

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

- **fbm_float_5oct** ( mean: 0.0336908917327 median: 0.033696 ):


```glsl
color += fbm(v_texcoord.x);
```


- **fbm_vec2_5oct** ( mean: 0.203022174284 median: 0.203059 ):


```glsl
color += fbm(v_texcoord);
```


- **fbm_vec3_5oct** ( mean: 0.257110042869 median: 0.237755 ):


```glsl
color += fbm(vec3(v_texcoord,u_time));
```


- **fbm_float_8oct** ( mean: 0.079127012571 median: 0.079134 ):


```glsl
color += fbm(v_texcoord.x);
```


- **fbm_vec3_8oct** ( mean: 0.279172775066 median: 0.00129 ):


```glsl
color += fbm(vec3(v_texcoord,u_time));
```


- **fbm_float_3oct** ( mean: 0.0212405672609 median: 0.021245 ):


```glsl
color += fbm(v_texcoord.x);
```


- **fbm_vec2_3oct** ( mean: 0.110890893017 median: 0.110911 ):


```glsl
color += fbm(v_texcoord);
```


- **fbm_vec3_3oct** ( mean: 0.115624434633 median: 0.115654 ):


```glsl
color += fbm(vec3(v_texcoord,u_time));
```


- **fbm_vec2_8oct** ( mean: 0.317204595403 median: 0.001329 ):


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

- **getCaustic_3iter** ( mean: 0.0696100020309 median: 0.069609 ):


```glsl
color.rgb += getCaustic(v_texcoord);
```


- **getCaustic_5iter** ( mean: 0.110268591426 median: 0.110257 ):


```glsl
color.rgb += getCaustic(v_texcoord);
```


- **getCaustic_4iter** ( mean: 0.0902682538133 median: 0.090259 ):


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

- **noise_float** ( mean: 0.00917584567388 median: 0.009174 ):


```glsl
color += noise(v_texcoord.x);
```


- **noise_vec2** ( mean: 0.0306955224994 median: 0.030737 ):


```glsl
color += noise(v_texcoord.xy);
```


- **snoise_vec3** ( mean: 0.0269340193957 median: 0.026935 ):


```glsl
color += snoise(vec3(v_texcoord.xy,u_time));
```


- **noise_vec3** ( mean: 0.0270204386821 median: 0.027022 ):


```glsl
color += noise(vec3(v_texcoord.xy,u_time));
```


- **snoise_vec2** ( mean: 0.0215113619805 median: 0.021511 ):


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

- **voronoi** ( mean: 0.0855091167853 median: 0.085535 ):


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

- **random_vec3** ( mean: 0.00743001829897 median: 0.007413 ):


```glsl
color.rgb += random(vec3(v_texcoord.xy,u_time));
```


- **random_vec2** ( mean: 0.00874655187587 median: 0.008372 ):


```glsl
color.rgb += random(v_texcoord.xy);
```


- **random3_vec2_t** ( mean: 0.0063473914012 median: 0.005726 ):


```glsl
color.rgb += random3(v_texcoord.xy);
```


- **random_float** ( mean: 0.0074499586153 median: 0.007399 ):


```glsl
color.rgb += random(v_texcoord.x);
```


- **random2_vec2** ( mean: 0.00844278848125 median: 0.008433 ):


```glsl
color.rg += random2(v_texcoord.xy);
```


- **random3_vec3** ( mean: 0.00821318774244 median: 0.008193 ):


```glsl
color.rgb += random3(vec3(v_texcoord.xy,u_time));
```


- **random3_vec2** ( mean: 0.0130702410415 median: 0.013069 ):


```glsl
color.rgb += random3(v_texcoord.xy);
```

