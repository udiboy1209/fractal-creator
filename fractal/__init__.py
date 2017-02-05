import sdl2
import sdl2.ext

from fractal.renderer import Renderer

__all__ = ['FractalApp','Recursor']

class FractalApp:
    def __init__(self, title="Fractal App"):
        sdl2.ext.init()
        self.window = sdl2.ext.Window(title, size=(800, 600))
        self.world = sdl2.ext.World()
        self.renderer = Renderer(self.window)
        self.world.add_system(self.renderer)

    def run(self):
        self.window.show()

        grid = self.renderer.grid

        running = True
        while running:
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
                if event.type == sdl2.SDL_KEYDOWN:
                    if event.key.keysym.sym == sdl2.SDLK_UP:
                        grid.velocity[1] = -6
                    elif event.key.keysym.sym == sdl2.SDLK_DOWN:
                        grid.velocity[1] = 6
                    elif event.key.keysym.sym == sdl2.SDLK_LEFT:
                        grid.velocity[0] = -6
                    elif event.key.keysym.sym == sdl2.SDLK_RIGHT:
                        grid.velocity[0] = 6
                elif event.type == sdl2.SDL_KEYUP:
                    if event.key.keysym.sym in \
                            (sdl2.SDLK_UP, sdl2.SDLK_DOWN,
                             sdl2.SDLK_LEFT, sdl2.SDLK_RIGHT):
                        grid.velocity = [0,0]
                    elif event.key.keysym.sym == sdl2.SDLK_z:
                        grid.scale += 10
                    elif event.key.keysym.sym == sdl2.SDLK_x:
                        grid.scale -= 10
            self.world.process()
        return 0

class Recursor:
    def __init__(self, base_drawing, recursion_rule, scale, mode='substitute'):
        self.base_drawing = base_drawing
        self.recursion_rule = recursion_rule
        self.scale = scale
        self.mode = mode

    def generate(self,levels):
        lines = []
        if levels == 1:
            lines.extend(self.base_drawing)
            return lines

        if self.mode == 'add':
            lines.extend(self.base_drawing)

        nlevel = self.generate(levels-1)

        for r in self.recursion_rule:
            lines.extend(r.modify_lines(nlevel, self.scale))

        return lines
