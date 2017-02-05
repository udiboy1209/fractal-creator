import sdl2
import sdl2.ext
from fractal.geometry import Grid
import svgwrite

class Renderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        wx, wy = window.size
        self.grid = Grid((int(wx/2),int(5*wy/6)), 200, window.size)
        self.lines = []

        super(Renderer, self).__init__(window)

    def render(self, components):
        sdl2.ext.fill(self.surface, sdl2.ext.Color(255,255,255))

        # self.grid.plot(self.surface)

        for l in self.lines:
            l.plot(self.surface, self.grid)

        super(Renderer, self).render(components)

    def save_svg(self, filename, scale):
        dwg = svgwrite.Drawing(filename, profile='tiny')

        for l in self.lines:
            p1 = l.p1
            p2 = l.p2

            p1 = (p1[0]*scale, p1[1]*scale)
            p2 = (p2[0]*scale, p2[1]*scale)

            dwg.add(dwg.line(p1,p2,stroke=svgwrite.rgb(l.color.r,l.color.g,l.color.b)))

        dwg.save()
