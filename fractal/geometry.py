import sdl2.ext
from math import sin, cos, pi

__all__ = ['Line', 'Grid','Transform']

class Line:
    '''
    Defines one line drawn on the Canvas

    Args:
        pos: Tuple of position of starting point of line in grid coordinates
        length: length of line in grid coordinate scale
        angle: angle of rotation from x-axis in radians
        color: sdl2.ext.Color object representing color of line

    Methods:
        plot(surface): plot this line on the surface
    '''

    def __init__(self, pos, length, angle, color,width=1):
        self.pos = pos
        self.length = length
        self.angle = angle
        self.color = color
        self.width = width

    def plot(self, surface, grid):
        x1,y1 = self.pos

        x2,y2 = grid.get_pixel_pos(
                    (x1+cos(self.angle)*self.length,
                     y1+sin(self.angle)*self.length))

        x1,y1 = grid.get_pixel_pos(self.pos)

        sdl2.ext.line(surface,self.color,(x1,y1,x2,y2),self.width)

    @property
    def p1(self):
        return self.pos

    @property
    def p2(self):
        x1, y1 = self.pos
        x,y = (x1+cos(self.angle)*self.length,
               y1+sin(self.angle)*self.length)

        return (x,y)


    def __repr__(self):
        x1, y1 = self.pos
        x2, y2 = x1+cos(self.angle)*self.length, y1+sin(self.angle)*self.length
        return '(%f,%f) -> (%f,%f), l:%f' % (x1,y1,x2,y2,self.length)

class Grid:
    '''
    Grid of the Coordinate system followed by the Renderer

    Args:
        origin: Tuple of pixel position of origin on the canvas
        scale: Float representing what one pixel is on the grid coordinates
        window_size: pixel size of the surface window
    '''


    def __init__(self, origin, scale, window_size):
        self.origin = origin
        self.velocity = [0,0]
        self.scale = float(scale)
        self.window_size = window_size

    def get_pixel_pos(self,pos):
        x,y = pos
        ox,oy = self.origin
        s = self.scale
        px = int(x*s + ox)
        py = int(oy - y*s)

        if px < 0:
            px = 0
        if px > self.window_size[0]:
            px = self.window_size[0]
        if py < 0:
            py = 0
        if py > self.window_size[1]:
            py = self.window_size[1]

        return (px,py)

    def plot(self, surface):
        wx, wy = self.window_size
        ox, oy = self.origin
        ox += self.velocity[0]
        oy += self.velocity[1]
        self.origin = (ox,oy)


        if oy > 0 and oy < wy: # x axis
            sdl2.ext.line(surface, sdl2.ext.Color(255,50,50), (0,oy,wx,oy))
        if ox > 0 and ox < wx: # y axis
            sdl2.ext.line(surface, sdl2.ext.Color(255,50,50), (ox,0,ox,wy))


class Transform:
    def __init__(self, offset, angle, color_transform=None, hue_shift=0, sat_scale=1):
        self.offset = offset
        self.angle = angle
        self.color_transform = color_transform
        self.hue_shift = hue_shift
        self.sat_scale = sat_scale

    def modify_color(self, color):
        ret = sdl2.ext.Color(0,0,0)
        if self.color_transform == 'hue':
            H = self.hue_shift

            U = cos(H*pi/180);
            W = sin(H*pi/180);

            ret.r = max(min(
                    int((.299+.701*U+.168*W)*color.r
                        + (.587-.587*U+.330*W)*color.g
                        + (.114-.114*U-.497*W)*color.b),255),0)
            ret.g = max(min(
                    int((.299-.299*U-.328*W)*color.r
                        + (.587+.413*U+.035*W)*color.g
                        + (.114-.114*U+.292*W)*color.b),255),0)
            ret.b = max(min(
                    int((.299-.3*U+1.25*W)*color.r
                        + (.587-.588*U-1.05*W)*color.g
                        + (.114+.886*U-.203*W)*color.b),255),0)
        elif self.color_transform == 'sat':
            s = self.sat_scale

            ret.r = min(int(color.r*s),255)
            ret.g = min(int(color.g*s),255)
            ret.b = min(int(color.b*s),255)
        else:
            ret = color

        return ret


    def modify_lines(self, lines, scale):
        nl = []
        ox,oy = self.offset
        s,c = sin(self.angle),cos(self.angle)

        for l in lines:
            nlength = l.length*scale
            x, y = l.pos[0]*scale, l.pos[1]*scale
            npos = c*x-s*y+ox,s*x+c*y+oy
            nangle = l.angle + self.angle
            nl.append(Line(npos, nlength, nangle, self.modify_color(l.color)))

        return nl
