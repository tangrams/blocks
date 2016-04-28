![](blocks.jpg)

## Tangram Blocks

Set of reusable building blocks for Tangram to make beatifull maps. Is in esence a library of our own Tangram recipes. A simpler way to add new GSLS Shaders features into your maps.

### Inventory

* color
    * conversion
    * palette
    * tools

* filter
    * grain
    * hatch
    * lut
    * tv

* functions
    * aastep
    * easing
    * map
    * pulse

* generative
    * random
    * noise
    * fbm
    * voronoi

* geometry
    * matrices
    * normal
    * projections
    * tilt
    * dynamic-height
    * dynamic-width

* grids
    * grid
    * tile

* patterns
    * dots
    * stripes
    * waves
    * zigzag

* shapes
    * circle
    * cross
    * digits
    * polygons
    * rect
    * simplex

* space
    * constant
    * screen
    * tex
    * tile
    * uz

* tiling
    * tile
    * brick
    * truchet
    * simplex
    * texture
        * non-repetitive
        * zoom-fade

### How to use them?

In your style add a path to it, like this:

```yaml
import:
    - http://tangrams.github.io/blocks/filter/grain.yaml
```

Then ```mix``` it with your custom styles like this:

```yaml
styles:
    buildings:
        base: polygons
        mix: [filter-grain]
```

This will add all the functions defined on that **Tangram Block** to your current custom style (in this case ```buildings```). Note that some of this modules have some values on the ````defines``` that can be tweaked. For example in the above example we can increase the detail and amount of the grain by modifying this two defines:

```yaml
styles:
    buildings:
        base: polygons
        mix: [filter-grain]
        shaders:
            defines:
                GRAIN_AMOUNT: .4
                NUM_OCTAVES: 3
```
