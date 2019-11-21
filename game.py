import field
import pacman
import ghosts
import time
from tkinter import *


class Game:
    def __init__(self):
        self.canvas = None
        self.root = None
        self.geometry = [700, 700]
        self.fps = 25

        self.level_number = 1
        self.level = None

    def init_graphics(self):
        self.root = Tk()
        self.root.geometry("{0}x{1}".format(self.geometry[0], self.geometry[1]))

        self.canvas = Canvas(self.root, bg='blue')
        self.canvas.pack(expand=True, fill=BOTH)

    def stabilizer(self, launch_time):
        end_time = launch_time + self.fps ** (-1)
        if time.time() > end_time + 0.001:
            self.fps -= 1
        else:
            time.sleep(end_time - time.time())

    def level_processing(self):
        level_config = {'number': self.level_number}
        self.level = Level(self, level_config)
        #self.level.launch()

        self.root.mainloop()




class Level:
    def __init__(self, game, args):
        self.game = game
        self.canvas = game.canvas
        self.root = game.root

        self.time = 0
        self.field = None
        self.ghosts = None
        self.pacman = None

    def launch(self):
        self.field = field.Field(self.canvas)
        self.field.get_graph()

        self.pacman = pacman.Pacman(self.canvas, self.field)
        self.ghosts = ghosts.Ghosts(self.canvas, self.field)

    def move(self):
        self.pacman.move(self.game.fps ** -1)
        self.ghosts.move(self.game.fps ** -1)

    def play(self):
        pass


if __name__ == '__main__':
    test_game = Game()
    test_game.init_graphics()
    test_game.level_processing()
