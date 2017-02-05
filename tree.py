import sdl2.ext

from fractal import FractalApp, Recursor
from fractal.geometry import Line, Transform
from math import sqrt,pi


BLACK = sdl2.ext.Color(50,150,50)
base_diagram = [Line((0,0),1,pi/2,BLACK),]

recrule = [Transform((0,1),-6*pi/10,'hue',hue_shift=30),
           Transform((0,1),-2*pi/10,'hue',hue_shift=30),
           Transform((0,1),2*pi/10,'hue',hue_shift=30),
           Transform((0,1),6*pi/10,'hue',hue_shift=30)]

rec = Recursor(base_diagram,recrule,1./2,'add')

arrangement = [Transform((0,0),0)]

my_app = FractalApp()
renderer = my_app.renderer

lines = rec.generate(7)
for a in arrangement:
    renderer.lines.extend(a.modify_lines(lines,1))

renderer.save_svg('tree.svg',1000)

my_app.run()
