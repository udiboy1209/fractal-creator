import sdl2.ext

from fractal import FractalApp, Recursor
from fractal.geometry import Line, Transform
from math import sqrt,pi


BLACK = sdl2.ext.Color(50,50,50)
base_diagram = [Line((0,0),1,0,BLACK),
                Line((1,0),1,pi/3,BLACK),
                Line((1.5,sqrt(3)/2),1,-pi/3,BLACK),
                Line((2,0),1,0,BLACK)]

recrule = [Transform((0,0),0,'sat',sat_scale=1.2),
           Transform((1,0),pi/3,'sat',sat_scale=1.2),
           Transform((1.5,sqrt(3)/2),-pi/3,'sat',sat_scale=1.2),
           Transform((2,0),0,'sat',sat_scale=1.2)]

rec = Recursor(base_diagram,recrule,1./3)

arrangement = [Transform((0,3*sqrt(3)/2), 0),
              Transform((1.5,0),2*pi/3),
              Transform((3,3*sqrt(3)/2), -2*pi/3)]

my_app = FractalApp()
renderer = my_app.renderer

lines = rec.generate(5)
for a in arrangement:
    renderer.lines.extend(a.modify_lines(lines,1))

renderer.save_svg('koch.svg',1000)

my_app.run()
