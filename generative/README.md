

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
![](http://tangrams.github.io/blocks/./generative/test/generative-fbm.png)

- **fbm_float_5oct** ( mean: 0.00846291137431 median: 0.008465 ):


```glsl
color += fbm(v_texcoord.x);
```


- **fbm_vec2_5oct** ( mean: 0.0632879187042 median: 0.063298 ):


```glsl
color += fbm(v_texcoord);
```


- **fbm_vec3_5oct** ( mean: 0.0762683388614 median: 0.080104 ):


```glsl
color += fbm(vec3(v_texcoord,u_time));
```


- **fbm_float_8oct** ( mean: 0.0198570343137 median: 0.019859 ):


```glsl
color += fbm(v_texcoord.x);
```


- **fbm_vec3_8oct** ( mean: 0.138698488202 median: 0.1368 ):


```glsl
color += fbm(vec3(v_texcoord,u_time));
```


- **fbm_float_3oct** ( mean: 0.00535479469388 median: 0.005357 ):


```glsl
color += fbm(v_texcoord.x);
```


- **fbm_vec2_3oct** ( mean: 0.0296593756483 median: 0.027856 ):


```glsl
color += fbm(v_texcoord);
```


- **fbm_vec3_3oct** ( mean: 0.029021972825 median: 0.029026 ):


```glsl
color += fbm(vec3(v_texcoord,u_time));
```


- **fbm_vec2_8oct** ( mean: 0.130543922517 median: 0.130569 ):


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
![](http://tangrams.github.io/blocks/./generative/test/generative-caustic.png)

- **getCaustic_3iter** ( mean: 0.0174631791109 median: 0.017467 ):


```glsl
color.rgb += getCaustic(v_texcoord);
```


- **getCaustic_5iter** ( mean: 0.033190257319 median: 0.0332 ):


```glsl
color.rgb += getCaustic(v_texcoord);
```


- **getCaustic_4iter** ( mean: 0.0226284105327 median: 0.022643 ):


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
These are the **defines**:
 -  **NOISE_TEXSAMPLE_SIZE**:  The *default value* is ```256.0```. 

These are the **shader blocks**:

- **global**:
 + `float noise (in float x)`
 + `float noise (vec2 p)`
 + `float noise (vec3 p)`
 + `vec3 mod289(vec3 x)`
 + `vec2 mod289(vec2 x)`
 + `vec3 permute(vec3 x)`
 + `float snoise(vec2 v)`
 + `float snoise (vec3 p)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
![](http://tangrams.github.io/blocks/./generative/test/generative-noise.png)

- **snoise_vec3** ( mean: 0.00677064722793 median: 0.006774 ):


```glsl
color += snoise(vec3(v_texcoord.xy,u_time));
```


- **snoise_vec2** ( mean: 0.0052441590097 median: 0.005412 ):


```glsl
color += snoise(v_texcoord.xy);
```


- **snoise_vec2_t** ( mean: 0.00541204602288 median: 0.005416 ):


```glsl
color += snoise(v_texcoord.xy);
```


- **noise_float** ( mean: 0.00234710103891 median: 0.002328 ):


```glsl
color += noise(v_texcoord.x);
```


- **noise_float_t** ( mean: 0.00169528271932 median: 0.001615 ):


```glsl
color += noise(v_texcoord.x);
```


- **snoise_vec3_t** ( mean: 0.00677290980949 median: 0.006775 ):


```glsl
color += snoise(vec3(v_texcoord.xy,u_time));
```


- **noise_vec3_t** ( mean: 0.0017634083045 median: 0.001723 ):


```glsl
color += noise(vec3(v_texcoord.xy,u_time));
```


- **noise_vec3** ( mean: 0.00814021793883 median: 0.00816 ):


```glsl
color += noise(vec3(v_texcoord.xy,u_time));
```


- **noise_vec2** ( mean: 0.00756182942058 median: 0.007738 ):


```glsl
color += noise(v_texcoord.xy);
```


- **noise_vec2_t** ( mean: 0.00168515640973 median: 0.001537 ):


```glsl
color += noise(v_texcoord.xy);
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
![](http://tangrams.github.io/blocks/./generative/test/generative-voronoi.png)

- **voronoi** ( mean: 0.0214547701687 median: 0.021459 ):


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
 + `vec3 random3 (vec2 p)`
 + `vec3 random3 (vec3 p)`
 + `vec2 random2 (vec2 p)`
 + `float random (float x)`
 + `float random (vec2 p)`
 + `float random (vec3 p)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
![](http://tangrams.github.io/blocks/./generative/test/generative-random.png)

- **random3_vec3_t** ( mean: 0.00272294387336 median: 0.002719 ):


```glsl
color.rgb += random3(vec3(v_texcoord.xy,u_time)*2.);
```


- **random_vec3** ( mean: 0.00163443861083 median: 0.001578 ):


```glsl
color.rgb += random(vec3(v_texcoord.xy,u_time)*2.);
```


- **random_vec2** ( mean: 0.00205109247136 median: 0.002049 ):


```glsl
color.rgb += random(v_texcoord.xy*2.);
```


- **random3_vec2_t** ( mean: 0.00318851207479 median: 0.00308 ):


```glsl
color.rgb += random3(v_texcoord.xy*2.);
```


- **random_vec2_t** ( mean: 0.00314136791721 median: 0.003081 ):


```glsl
color.rgb += random(v_texcoord.xy*2.);
```


- **random_float_t** ( mean: 0.00162592697893 median: 0.001503 ):


```glsl
color.rgb += random(v_texcoord.x*2.);
```


- **random_vec3_t** ( mean: 0.00313116466283 median: 0.003077 ):


```glsl
color.rgb += random(vec3(v_texcoord.xy,u_time)*2.);
```


- **random2_vec2_t** ( mean: 0.00275288664766 median: 0.002742 ):


```glsl
color.rg += random2(v_texcoord.xy*2.);
```


- **random_float** ( mean: 0.00188097360897 median: 0.001729 ):


```glsl
color.rgb += random(v_texcoord.x*2.);
```


- **random2_vec2** ( mean: 0.00243623400191 median: 0.002492 ):


```glsl
color.rg += random2(v_texcoord.xy*2.);
```


- **random3_vec3** ( mean: 0.00179571800081 median: 0.001781 ):


```glsl
color.rgb += random3(vec3(v_texcoord.xy,u_time)*2.);
```


- **random3_vec2** ( mean: 0.00330146122239 median: 0.003305 ):


```glsl
color.rgb += random3(v_texcoord.xy*2.);
```

