#importing modules
from tkinter import *
import re

#main class
class game():
    def __init__(self, title, width=100, height=100, bg="lightblue"):
        self.screen = Tk()
        self.title = title
        self.bg = bg
        self.width = width
        self.height = height
        self.screen.title(title)
        self.canvas = Canvas(self.screen, width=self.with, height=self.height)
        self.canvas.pack()
    
    def title(self, screentitle):
        if screentitle:
            self.title = screentitle
            return self.screen.title(screentitle)
    
    def update(self):
        self.screen.update()
    
    @classmethod
    def createCharacter(src):
        return Character(src)

#character class
class Character():
    def __init__(self, path, type="static"):
        self.x = 0
        self.y = 0
        if type == "static":
            if re.matches(r".*\.(png|jpg)", path):
                self.path = path
            else:
                raise ValueError(path + " is not an image.")
        
    
    def place(self, **kwargs):
        try:
            self.x = kwargs["x"]
        except KeyError:
            pass
        try:
            self.y = kwargs["y"]
        except KeyError:
            pass
