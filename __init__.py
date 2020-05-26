#importing modules
from tkinter import *

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
