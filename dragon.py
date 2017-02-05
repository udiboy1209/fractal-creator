import sdl2.ext

from fractal import FractalApp, Recursor
from fractal.geometry import Line, Transform
from math import sqrt,pi


BLACK = sdl2.ext.Color(0,0,0)
base_diagram = [Line((0,0),1,pi/2,BLACK),
                Line((0,1),1,pi,BLACK)]

recrule = [Transform((0,1),3*pi/4),
           Transform((0,1),pi/4)]

rec = Recursor(base_diagram,recrule,1./sqrt(2))

arrangement = [Transform((0,0),-pi/4)]

my_app = FractalApp()
renderer = my_app.renderer

lines = rec.generate(13)
for a in arrangement:
    renderer.lines.extend(a.modify_lines(lines,1))

renderer.save_svg('dragon.svg',1000)

my_app.run()

