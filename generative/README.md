

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
[![](http://tangrams.github.io/blocks/./generative/test/generative-caustic.png)](http://tangrams.github.io/blocks/test.html?test=./generative/test/generative-caustic.json)

- **getCaustic_3iter** ( mean: 0.0174673326526 median: 0.01747 )

<a href="http://tangrams.github.io/blocks/./generative/test/caustics-getCaustic_3iter.png"><img src="http://tangrams.github.io/blocks/./generative/test/caustics-getCaustic_3iter.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rgb += getCaustic(v_texcoord);
```


- **getCaustic_5iter** ( mean: 0.027666305584 median: 0.027669 )

<a href="http://tangrams.github.io/blocks/./generative/test/caustics-getCaustic_5iter.png"><img src="http://tangrams.github.io/blocks/./generative/test/caustics-getCaustic_5iter.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rgb += getCaustic(v_texcoord);
```


- **getCaustic_4iter** ( mean: 0.0226411856385 median: 0.022645 )

<a href="http://tangrams.github.io/blocks/./generative/test/caustics-getCaustic_4iter.png"><img src="http://tangrams.github.io/blocks/./generative/test/caustics-getCaustic_4iter.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rgb += getCaustic(v_texcoord);
```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


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
[![](http://tangrams.github.io/blocks/./generative/test/generative-fbm.png)](http://tangrams.github.io/blocks/test.html?test=./generative/test/generative-fbm.json)

- **fbm_float_5oct** ( mean: 0.00846323069085 median: 0.008465 )

<a href="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_float_5oct.png"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_float_5oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += fbm(v_texcoord.x);
```


- **fbm_vec2_5oct** ( mean: 0.0631883174797 median: 0.063202 )

<a href="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec2_5oct.png"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec2_5oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += fbm(v_texcoord);
```


- **fbm_vec3_5oct** ( mean: 0.065993688049 median: 0.066001 )

<a href="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec3_5oct.png"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec3_5oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += fbm(vec3(v_texcoord,u_time));
```


- **fbm_float_8oct** ( mean: 0.0198538417193 median: 0.019859 )

<a href="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_float_8oct.png"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_float_8oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += fbm(v_texcoord.x);
```


- **fbm_vec3_8oct** ( mean: 0.138257784005 median: 0.136402 )

<a href="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec3_8oct.png"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec3_8oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += fbm(vec3(v_texcoord,u_time));
```


- **fbm_float_3oct** ( mean: 0.00639378294574 median: 0.006415 )

<a href="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_float_3oct.png"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_float_3oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += fbm(v_texcoord.x);
```


- **fbm_vec2_3oct** ( mean: 0.0278312615887 median: 0.027835 )

<a href="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec2_3oct.png"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec2_3oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += fbm(v_texcoord);
```


- **fbm_vec3_3oct** ( mean: 0.0290181930218 median: 0.029026 )

<a href="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec3_3oct.png"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec3_3oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += fbm(vec3(v_texcoord,u_time));
```


- **fbm_vec2_8oct** ( mean: 0.130762226438 median: 0.130807 )

<a href="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec2_8oct.png"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec2_8oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += fbm(v_texcoord);
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
[![](http://tangrams.github.io/blocks/./generative/test/generative-noise.png)](http://tangrams.github.io/blocks/test.html?test=./generative/test/generative-noise.json)

- **snoise_vec3** ( mean: 0.00681053334697 median: 0.006827 )

<a href="http://tangrams.github.io/blocks/./generative/test/noise-snoise_vec3.png"><img src="http://tangrams.github.io/blocks/./generative/test/noise-snoise_vec3.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += snoise(vec3(v_texcoord.xy,u_time)*2.);
```


- **snoise_vec2** ( mean: 0.00453934683027 median: 0.004552 )

<a href="http://tangrams.github.io/blocks/./generative/test/noise-snoise_vec2.png"><img src="http://tangrams.github.io/blocks/./generative/test/noise-snoise_vec2.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += snoise(v_texcoord.xy*2.);
```


- **snoise_vec2_t** ( mean: 0.00455094120049 median: 0.004553 )

<a href="http://tangrams.github.io/blocks/./generative/test/noise-snoise_vec2_t.png"><img src="http://tangrams.github.io/blocks/./generative/test/noise-snoise_vec2_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += snoise(v_texcoord.xy*2.);
```


- **noise_float** ( mean: 0.00234074574882 median: 0.002343 )

<a href="http://tangrams.github.io/blocks/./generative/test/noise-noise_float.png"><img src="http://tangrams.github.io/blocks/./generative/test/noise-noise_float.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += noise(v_texcoord.x*2.);
```


- **noise_float_t** ( mean: 0.00159413216855 median: 0.00153 )

<a href="http://tangrams.github.io/blocks/./generative/test/noise-noise_float_t.png"><img src="http://tangrams.github.io/blocks/./generative/test/noise-noise_float_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += noise(v_texcoord.x*2.);
```


- **snoise_vec3_t** ( mean: 0.00682556567103 median: 0.006828 )

<a href="http://tangrams.github.io/blocks/./generative/test/noise-snoise_vec3_t.png"><img src="http://tangrams.github.io/blocks/./generative/test/noise-snoise_vec3_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += snoise(vec3(v_texcoord.xy,u_time)*2.);
```


- **noise_vec3_t** ( mean: 0.00187612970195 median: 0.001841 )

<a href="http://tangrams.github.io/blocks/./generative/test/noise-noise_vec3_t.png"><img src="http://tangrams.github.io/blocks/./generative/test/noise-noise_vec3_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += noise(vec3(v_texcoord.xy,u_time)*2.);
```


- **noise_vec3** ( mean: 0.00675546924177 median: 0.006802 )

<a href="http://tangrams.github.io/blocks/./generative/test/noise-noise_vec3.png"><img src="http://tangrams.github.io/blocks/./generative/test/noise-noise_vec3.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += noise(vec3(v_texcoord.xy,u_time)*2.);
```


- **noise_vec2** ( mean: 0.00643759367347 median: 0.006474 )

<a href="http://tangrams.github.io/blocks/./generative/test/noise-noise_vec2.png"><img src="http://tangrams.github.io/blocks/./generative/test/noise-noise_vec2.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += noise(v_texcoord.xy*2.);
```


- **noise_vec2_t** ( mean: 0.00159965077399 median: 0.001535 )

<a href="http://tangrams.github.io/blocks/./generative/test/noise-noise_vec2_t.png"><img src="http://tangrams.github.io/blocks/./generative/test/noise-noise_vec2_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color += noise(v_texcoord.xy*2.);
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
[![](http://tangrams.github.io/blocks/./generative/test/generative-random.png)](http://tangrams.github.io/blocks/test.html?test=./generative/test/generative-random.json)

- **random3_vec3_t** ( mean: 0.00309042102469 median: 0.003074 )

<a href="http://tangrams.github.io/blocks/./generative/test/random-random3_vec3_t.png"><img src="http://tangrams.github.io/blocks/./generative/test/random-random3_vec3_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rgb += random3(vec3(v_texcoord.xy,u_time)*2.);
```


- **random_vec3** ( mean: 0.00176138404855 median: 0.001587 )

<a href="http://tangrams.github.io/blocks/./generative/test/random-random_vec3.png"><img src="http://tangrams.github.io/blocks/./generative/test/random-random_vec3.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rgb += random(vec3(v_texcoord.xy,u_time)*2.);
```


- **random_vec2** ( mean: 0.00226536647128 median: 0.002361 )

<a href="http://tangrams.github.io/blocks/./generative/test/random-random_vec2.png"><img src="http://tangrams.github.io/blocks/./generative/test/random-random_vec2.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rgb += random(v_texcoord.xy*2.);
```


- **random3_vec2_t** ( mean: 0.00273990486953 median: 0.002739 )

<a href="http://tangrams.github.io/blocks/./generative/test/random-random3_vec2_t.png"><img src="http://tangrams.github.io/blocks/./generative/test/random-random3_vec2_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rgb += random3(v_texcoord.xy*2.);
```


- **random_vec2_t** ( mean: 0.00309059064786 median: 0.003085 )

<a href="http://tangrams.github.io/blocks/./generative/test/random-random_vec2_t.png"><img src="http://tangrams.github.io/blocks/./generative/test/random-random_vec2_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rgb += random(v_texcoord.xy*2.);
```


- **random_float_t** ( mean: 0.00246076509015 median: 0.002309 )

<a href="http://tangrams.github.io/blocks/./generative/test/random-random_float_t.png"><img src="http://tangrams.github.io/blocks/./generative/test/random-random_float_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rgb += random(v_texcoord.x*2.);
```


- **random_vec3_t** ( mean: 0.00307390621735 median: 0.003076 )

<a href="http://tangrams.github.io/blocks/./generative/test/random-random_vec3_t.png"><img src="http://tangrams.github.io/blocks/./generative/test/random-random_vec3_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rgb += random(vec3(v_texcoord.xy,u_time)*2.);
```


- **random2_vec2_t** ( mean: 0.00273658259617 median: 0.002738 )

<a href="http://tangrams.github.io/blocks/./generative/test/random-random2_vec2_t.png"><img src="http://tangrams.github.io/blocks/./generative/test/random-random2_vec2_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rg += random2(v_texcoord.xy*2.);
```


- **random_float** ( mean: 0.00162598687987 median: 0.001528 )

<a href="http://tangrams.github.io/blocks/./generative/test/random-random_float.png"><img src="http://tangrams.github.io/blocks/./generative/test/random-random_float.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rgb += random(v_texcoord.x*2.);
```


- **random2_vec2** ( mean: 0.00213150593379 median: 0.00213 )

<a href="http://tangrams.github.io/blocks/./generative/test/random-random2_vec2.png"><img src="http://tangrams.github.io/blocks/./generative/test/random-random2_vec2.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rg += random2(v_texcoord.xy*2.);
```


- **random3_vec3** ( mean: 0.00236377609167 median: 0.002294 )

<a href="http://tangrams.github.io/blocks/./generative/test/random-random3_vec3.png"><img src="http://tangrams.github.io/blocks/./generative/test/random-random3_vec3.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rgb += random3(vec3(v_texcoord.xy,u_time)*2.);
```


- **random3_vec2** ( mean: 0.00275828962418 median: 0.002759 )

<a href="http://tangrams.github.io/blocks/./generative/test/random-random3_vec2.png"><img src="http://tangrams.github.io/blocks/./generative/test/random-random3_vec2.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rgb += random3(v_texcoord.xy*2.);
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
[![](http://tangrams.github.io/blocks/./generative/test/generative-voronoi.png)](http://tangrams.github.io/blocks/test.html?test=./generative/test/generative-voronoi.json)

- **voronoi** ( mean: 0.0214618096307 median: 0.021465 )

<a href="http://tangrams.github.io/blocks/./generative/test/voronoi-voronoi.png"><img src="http://tangrams.github.io/blocks/./generative/test/voronoi-voronoi.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rgb = voronoi(v_texcoord*2.);
```


- **voronoi_t** ( mean: 0.00495028410718 median: 0.004964 )

<a href="http://tangrams.github.io/blocks/./generative/test/voronoi-voronoi_t.png"><img src="http://tangrams.github.io/blocks/./generative/test/voronoi-voronoi_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
color.rgb = voronoi(v_texcoord*2.);
```

