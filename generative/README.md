

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

- **fbm_float_5oct** ( mean: 0.0101560170896 median: 0.010159 ):


```glsl
color += fbm(v_texcoord.x);
```


- **fbm_vec2_5oct** ( mean: 0.0633186991006 median: 0.063297 ):


```glsl
color += fbm(v_texcoord);
```


- **fbm_vec3_5oct** ( mean: 0.065959054999 median: 0.065957 ):


```glsl
color += fbm(vec3(v_texcoord,u_time));
```


- **fbm_float_8oct** ( mean: 0.0198532370945 median: 0.019856 ):


```glsl
color += fbm(v_texcoord.x);
```


- **fbm_vec3_8oct** ( mean: 0.14228288787 median: 0.136532 ):


```glsl
color += fbm(vec3(v_texcoord,u_time));
```


- **fbm_float_3oct** ( mean: 0.0056203610929 median: 0.005361 ):


```glsl
color += fbm(v_texcoord.x);
```


- **fbm_vec2_3oct** ( mean: 0.0285671451276 median: 0.027839 ):


```glsl
color += fbm(v_texcoord);
```


- **fbm_vec3_3oct** ( mean: 0.0290201660232 median: 0.029027 ):


```glsl
color += fbm(vec3(v_texcoord,u_time));
```


- **fbm_vec2_8oct** ( mean: 0.130539330963 median: 0.13056 ):


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

- **getCaustic_3iter** ( mean: 0.017465895486 median: 0.017468 ):


```glsl
color.rgb += getCaustic(v_texcoord);
```


- **getCaustic_5iter** ( mean: 0.0276614688198 median: 0.027672 ):


```glsl
color.rgb += getCaustic(v_texcoord);
```


- **getCaustic_4iter** ( mean: 0.0226451147208 median: 0.022644 ):


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

- **snoise_vec3** ( mean: 0.00675361593317 median: 0.006773 ):


```glsl
color += snoise(vec3(v_texcoord.xy,u_time));
```


- **snoise_vec2** ( mean: 0.00535939131552 median: 0.005427 ):


```glsl
color += snoise(v_texcoord.xy);
```


- **snoise_vec2_t** ( mean: 0.00451479392581 median: 0.004528 ):


```glsl
color += snoise(v_texcoord.xy);
```


- **noise_float** ( mean: 0.00234618509419 median: 0.002329 ):


```glsl
color += noise(v_texcoord.x);
```


- **noise_float_t** ( mean: 0.00168475406128 median: 0.001574 ):


```glsl
color += noise(v_texcoord.x);
```


- **snoise_vec3_t** ( mean: 0.00811956546246 median: 0.008124 ):


```glsl
color += snoise(vec3(v_texcoord.xy,u_time));
```


- **noise_vec3_t** ( mean: 0.0017707605317 median: 0.001723 ):


```glsl
color += noise(vec3(v_texcoord.xy,u_time));
```


- **noise_vec3** ( mean: 0.00815749666324 median: 0.008161 ):


```glsl
color += noise(vec3(v_texcoord.xy,u_time));
```


- **noise_vec2** ( mean: 0.00645566930733 median: 0.006458 ):


```glsl
color += noise(v_texcoord.xy);
```


- **noise_vec2_t** ( mean: 0.0016554771615 median: 0.001573 ):


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

- **voronoi** ( mean: 0.0214548163888 median: 0.021458 ):


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

- **random3_vec3_t** ( mean: 0.00310801605802 median: 0.003077 ):


```glsl
color.rgb += random3(vec3(v_texcoord.xy,u_time)*2.);
```


- **random_vec3** ( mean: 0.00244736054248 median: 0.002344 ):


```glsl
color.rgb += random(vec3(v_texcoord.xy,u_time)*2.);
```


- **random_vec2** ( mean: 0.00246968324742 median: 0.002436 ):


```glsl
color.rgb += random(v_texcoord.xy*2.);
```


- **random3_vec2_t** ( mean: 0.00310175730163 median: 0.003086 ):


```glsl
color.rgb += random3(v_texcoord.xy*2.);
```


- **random_vec2_t** ( mean: 0.00320178657577 median: 0.003121 ):


```glsl
color.rgb += random(v_texcoord.xy*2.);
```


- **random_float_t** ( mean: 0.00253367882079 median: 0.002417 ):


```glsl
color.rgb += random(v_texcoord.x*2.);
```


- **random_vec3_t** ( mean: 0.00274166087316 median: 0.002723 ):


```glsl
color.rgb += random(vec3(v_texcoord.xy,u_time)*2.);
```


- **random2_vec2_t** ( mean: 0.00273252093118 median: 0.002735 ):


```glsl
color.rg += random2(v_texcoord.xy*2.);
```


- **random_float** ( mean: 0.00254539597315 median: 0.002411 ):


```glsl
color.rgb += random(v_texcoord.x*2.);
```


- **random2_vec2** ( mean: 0.00258814510309 median: 0.002533 ):


```glsl
color.rg += random2(v_texcoord.xy*2.);
```


- **random3_vec3** ( mean: 0.00256771376812 median: 0.002323 ):


```glsl
color.rgb += random3(vec3(v_texcoord.xy,u_time)*2.);
```


- **random3_vec2** ( mean: 0.00275763122586 median: 0.002758 ):


```glsl
color.rgb += random3(v_texcoord.xy*2.);
```

