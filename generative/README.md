

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

- **fbm_float_5oct** ( mean: 0.00843543722155 median: 0.008447 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/fbm-fbm_float_5oct.frag"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_float_5oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += fbm(v_texcoord.x);
```


- **fbm_vec2_5oct** ( mean: 0.0510610432411 median: 0.051074 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec2_5oct.frag"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec2_5oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += fbm(v_texcoord);
```


- **fbm_vec3_5oct** ( mean: 0.0574625950982 median: 0.057435 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec3_5oct.frag"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec3_5oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += fbm(vec3(v_texcoord,u_time));
```


- **fbm_float_8oct** ( mean: 0.0198344518668 median: 0.019838 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/fbm-fbm_float_8oct.frag"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_float_8oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define NUM_OCTAVES 8
...
// Color:
    color.rgb += fbm(v_texcoord.x);
```


- **fbm_vec3_8oct** ( mean: 0.140089968883 median: 0.134088 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec3_8oct.frag"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec3_8oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define NUM_OCTAVES 8
...
// Color:
    color.rgb += fbm(vec3(v_texcoord,u_time));
```


- **fbm_float_3oct** ( mean: 0.00532545727015 median: 0.00534 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/fbm-fbm_float_3oct.frag"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_float_3oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define NUM_OCTAVES 3
...
// Color:
    color.rgb += fbm(v_texcoord.x);
```


- **fbm_vec2_3oct** ( mean: 0.0277975055679 median: 0.027812 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec2_3oct.frag"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec2_3oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define NUM_OCTAVES 3
...
// Color:
    color.rgb += fbm(v_texcoord);
```


- **fbm_vec3_3oct** ( mean: 0.0287937845561 median: 0.028803 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec3_3oct.frag"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec3_3oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define NUM_OCTAVES 3
...
// Color:
    color.rgb += fbm(vec3(v_texcoord,u_time));
```


- **fbm_vec2_8oct** ( mean: 0.131822992102 median: 0.130721 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec2_8oct.frag"><img src="http://tangrams.github.io/blocks/./generative/test/fbm-fbm_vec2_8oct.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define NUM_OCTAVES 8
...
// Color:
    color.rgb += fbm(v_texcoord);
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
[![](http://tangrams.github.io/blocks/./generative/test/generative-caustic.png)](http://tangrams.github.io/blocks/test.html?test=./generative/test/generative-caustic.json)

- **getCaustic_3iter** ( mean: 0.0175578070531 median: 0.017577 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/caustics-getCaustic_3iter.frag"><img src="http://tangrams.github.io/blocks/./generative/test/caustics-getCaustic_3iter.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += getCaustic(v_texcoord);
```


- **getCaustic_5iter** ( mean: 0.0275885850051 median: 0.027595 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/caustics-getCaustic_5iter.frag"><img src="http://tangrams.github.io/blocks/./generative/test/caustics-getCaustic_5iter.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define CAUSTIC_ITERATIONS 5
...
// Color:
    color.rgb += getCaustic(v_texcoord);
```


- **getCaustic_4iter** ( mean: 0.022532501015 median: 0.022574 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/caustics-getCaustic_4iter.frag"><img src="http://tangrams.github.io/blocks/./generative/test/caustics-getCaustic_4iter.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define CAUSTIC_ITERATIONS 4
...
// Color:
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
 + `float gnoise (in vec2 p)`
 + `float gnoise (in vec3 p)`
 + `vec3 mod289(vec3 x)`
 + `vec2 mod289(vec2 x)`
 + `vec3 permute(vec3 x)`
 + `float snoise(vec2 v)`
 + `float snoise (vec3 p)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./generative/test/generative-noise.png)](http://tangrams.github.io/blocks/test.html?test=./generative/test/generative-noise.json)

- **snoise_vec3** ( mean: 0.00677372446072 median: 0.006808 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/noise-snoise_vec3.frag"><img src="http://tangrams.github.io/blocks/./generative/test/noise-snoise_vec3.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += snoise(vec3(v_texcoord.xy*2.,u_time));
```


- **snoise_vec2** ( mean: 0.00451638136797 median: 0.004538 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/noise-snoise_vec2.frag"><img src="http://tangrams.github.io/blocks/./generative/test/noise-snoise_vec2.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += snoise(v_texcoord.xy*2.);
```


- **gnoise_vec3** ( mean: 0.0141895265936 median: 0.014205 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/noise-gnoise_vec3.frag"><img src="http://tangrams.github.io/blocks/./generative/test/noise-gnoise_vec3.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += gnoise(vec3(v_texcoord.xy*2.,u_time));
```


- **gnoise_vec2** ( mean: 0.00689842558376 median: 0.006905 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/noise-gnoise_vec2.frag"><img src="http://tangrams.github.io/blocks/./generative/test/noise-gnoise_vec2.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += gnoise(v_texcoord.xy*2.);
```


- **noise_float** ( mean: 0.00232499366053 median: 0.002328 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/noise-noise_float.frag"><img src="http://tangrams.github.io/blocks/./generative/test/noise-noise_float.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += noise(v_texcoord.x*2.);
```


- **noise_float_t** ( mean: 0.00177410478548 median: 0.001546 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/noise-noise_float_t.frag"><img src="http://tangrams.github.io/blocks/./generative/test/noise-noise_float_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define NOISE_TEXSAMPLE 1
...
// Color:
    color.rgb += noise(v_texcoord.x*2.);
```


- **noise_vec3_t** ( mean: 0.00191383052225 median: 0.001828 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/noise-noise_vec3_t.frag"><img src="http://tangrams.github.io/blocks/./generative/test/noise-noise_vec3_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define NOISE_TEXSAMPLE 1
...
// Color:
    color.rgb += noise(vec3(v_texcoord.xy,u_time)*2.);
```


- **noise_vec3** ( mean: 0.00675933225086 median: 0.006781 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/noise-noise_vec3.frag"><img src="http://tangrams.github.io/blocks/./generative/test/noise-noise_vec3.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += noise(vec3(v_texcoord.xy*2.,u_time));
```


- **noise_vec2** ( mean: 0.00642775015235 median: 0.006456 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/noise-noise_vec2.frag"><img src="http://tangrams.github.io/blocks/./generative/test/noise-noise_vec2.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += noise(v_texcoord.xy*2.);
```


- **noise_vec2_t** ( mean: 0.00173221588595 median: 0.001506 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/noise-noise_vec2_t.frag"><img src="http://tangrams.github.io/blocks/./generative/test/noise-noise_vec2_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define NOISE_TEXSAMPLE 1
...
// Color:
    color.rgb += noise(v_texcoord.xy*2.);
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

- **voronoi** ( mean: 0.021461264855 median: 0.021467 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/voronoi-voronoi.frag"><img src="http://tangrams.github.io/blocks/./generative/test/voronoi-voronoi.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
color.rgb = voronoi(v_texcoord*2.);
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

- **random3_vec3_t** ( mean: 0.00270945480514 median: 0.00272 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/random-random3_vec3_t.frag"><img src="http://tangrams.github.io/blocks/./generative/test/random-random3_vec3_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define RANDOM_TEXSAMPLE 1
...
// Color:
    color.rgb += random3(vec3(v_texcoord.xy*2.,u_time));
```


- **random_vec3** ( mean: 0.00172030091743 median: 0.001564 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/random-random_vec3.frag"><img src="http://tangrams.github.io/blocks/./generative/test/random-random_vec3.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += random(vec3(v_texcoord.xy*2.,u_time));
```


- **random_vec2** ( mean: 0.00206787708588 median: 0.00205 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/random-random_vec2.frag"><img src="http://tangrams.github.io/blocks/./generative/test/random-random_vec2.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += random(v_texcoord.xy*2.);
```


- **random3_vec2_t** ( mean: 0.00273615463076 median: 0.002735 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/random-random3_vec2_t.frag"><img src="http://tangrams.github.io/blocks/./generative/test/random-random3_vec2_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define RANDOM_TEXSAMPLE 1
...
// Color:
    color.rgb += random3(v_texcoord.xy*2.);
```


- **random_vec2_t** ( mean: 0.00275891369414 median: 0.002734 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/random-random_vec2_t.frag"><img src="http://tangrams.github.io/blocks/./generative/test/random-random_vec2_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define RANDOM_TEXSAMPLE 1
...
// Color:
    color.rgb += random(v_texcoord.xy*2.);
```


- **random_float_t** ( mean: 0.00170052665853 median: 0.001498 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/random-random_float_t.frag"><img src="http://tangrams.github.io/blocks/./generative/test/random-random_float_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define RANDOM_TEXSAMPLE 1
...
// Color:
    color.rgb += random(v_texcoord.x*2.);
```


- **random_vec3_t** ( mean: 0.00273784700348 median: 0.00272 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/random-random_vec3_t.frag"><img src="http://tangrams.github.io/blocks/./generative/test/random-random_vec3_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define RANDOM_TEXSAMPLE 1
...
// Color:
    color.rgb += random(vec3(v_texcoord.xy*2.,u_time));
```


- **random2_vec2_t** ( mean: 0.00272712119976 median: 0.002734 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/random-random2_vec2_t.frag"><img src="http://tangrams.github.io/blocks/./generative/test/random-random2_vec2_t.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
#define RANDOM_TEXSAMPLE 1
...
// Color:
    color.rg += random2(v_texcoord.xy*2.);
```


- **random_float** ( mean: 0.00183072934938 median: 0.001528 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/random-random_float.frag"><img src="http://tangrams.github.io/blocks/./generative/test/random-random_float.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += random(v_texcoord.x*2.);
```


- **random2_vec2** ( mean: 0.00215338416124 median: 0.00213 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/random-random2_vec2.frag"><img src="http://tangrams.github.io/blocks/./generative/test/random-random2_vec2.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rg += random2(v_texcoord.xy*2.);
```


- **random3_vec3** ( mean: 0.00185836615134 median: 0.001753 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/random-random3_vec3.frag"><img src="http://tangrams.github.io/blocks/./generative/test/random-random3_vec3.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += random3(vec3(v_texcoord.xy*2.,u_time));
```


- **random3_vec2** ( mean: 0.00281683506838 median: 0.002758 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./generative/test/random-random3_vec2.frag"><img src="http://tangrams.github.io/blocks/./generative/test/random-random3_vec2.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += random3(v_texcoord.xy*2.);
```

