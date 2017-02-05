# Fractal Creator

Python library for creating and viewing geometric fractals.

# Howto

You need a base diagram definition, a recursion rule and an arrangement rule for
your fractal.

Base diagram will be a list of `Line`s. Recursion rule and arrangment rule will be
a list of `Transform`s.

The library will then apply the recursion rule for fixed number of recursions to
the base diagram and finally arrange the fractal using the arrangment rule.

# Features

 - Color changes in the transform to generate colorful fractals
 - SVG output (needs fine-tuning)

### Examples included

 - [Koch snowflake](https://en.wikipedia.org/wiki/Koch_snowflake): `koch.py`
 - [Fractal dragon](https://en.wikipedia.org/wiki/Dragon_curve): `dragon.py`
 - [Serpinksi Triangle](https://en.wikipedia.org/wiki/Sierpinski_triangle): `triangle.py`
 - Tree: `tree.py`

![fractal_tree](/tree_fractal.png)

