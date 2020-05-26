#importing modules
from tkinter import *
from PIL import Image, ImageTk
import re

#main class
class Game():
    def __init__(self, title, width=100, height=100, bg="lightblue"):
        self.screen = Tk()
        self.title = title
        self.bg = bg
        self.width = width
        self.height = height
        self.screen.title(title)
        self.canvas = Canvas(self.screen, width=self.with, height=self.height)
        self.canvas.pack()
        self.canvas.bind_all("<Key>", self.react_to_key)
        
        self.characters = []
        self.blocks = []
        self.running = False
    
    def title(self, screentitle):
        if screentitle:
            self.title = screentitle
            return self.screen.title(screentitle)
    
    def update(self):
        self.screen.update()
    
    def add(self, object):
        if isInstance(object, Character):
            object.canvas = self.canvas
            self.characters.append(object)
        elif isInstance(object, Block):
            object.canvas = self.canvas
            self.blocks.append(object)
    
    def run(self):
        for character in self.characters:
            character.draw()
        for block in self.blocks:
            block.draw()
        self.running = True
        while self.running:
            self.canvas.update()
    
    #when key is pressed
    def react_to_key(self, event):
        key = event.keysym
        if key == "Left":
            self.onkeyleft()
        elif key == "Right":
            self.onkeyright()
        elif key == "Up":
            self.onkeyup()
    
    #keybinds
    def onkeyleft(self):
        pass
    def onkeyright(self):
        pass
    def onkeyup(self):
        pass
    
    @classmethod
    def createCharacter(src):
        return Character(src)
    
    #decorator
    def onkeypress(self, key):
        def bind(func):
            if key == "left":
                self.onkeyleft = func
            elif key == "right":
                self.onkeyright = func
            elif key == "up":
                self.onkeyup = func
            else:
                raise ModuleError("Python2d doesn't support the key: " + key)
            return func
        return bind

#character class
class Character():
    def __init__(self, path, type="static"):
        self.x = 0
        self.y = 0
        self.canvas = None
        if type == "static":
            if re.matches(r".*\.(png|jpg)", path):
                self.path = path
                self.img = Image.open(self.path)
                self.tatras = ImageTk.PhotoImage(self.img)
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
    
    def move(self, moveX, moveY):
        if self.canvas:
            self.canvas.move(self.image, moveX, moveY)
    
    def draw(self):
        if self.canvas:
            self.image = self.canvas.create_image(self.x, self.y, anchor=NW, image=self.tatras)

#block class
class Block():
    def __init__(self, **kwargs):
        try:
            self.color = kwargs["color"]
        except KeyError:
            self.color = "black"
        try:
            self.width = kwargs["width"]
        except KeyError:
            self.width = 100
        try:
            self.height = kwargs["height"]
        except KeyError:
            self.height = 100
        self.x = 0
        self.y = 0
        self.canvas = None
    
    def place(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def draw(self):
        if self.canvas:
            self.graph = self.canvas.create_rectangle(self.x, self.y, self.width, self.height, fill=self.color)
