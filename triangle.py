import sdl2.ext

from fractal import FractalApp, Recursor
from fractal.geometry import Line, Transform
from math import sqrt,pi

BLACK = sdl2.ext.Color(0,0,0)
base_diagram = [Line((0,0), 1,      0, BLACK),
                Line((1,0), 1, 2*pi/3, BLACK),
                Line((0,0), 1,   pi/3, BLACK)]

recrule = [Transform((   0,        0), 0),
           Transform((0.25,sqrt(3)/4), 0),
           Transform(( 0.5,        0), 0)]

rec = Recursor(base_diagram,recrule,1./2)

my_app = FractalApp()
renderer = my_app.renderer
renderer.lines = rec.generate(8)

renderer.save_svg('triangle.svg',1000)

my_app.run()
