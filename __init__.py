#importing modules
from tkinter import *

#main class
class game():
    def __init__(self, title, bg="lightblue"):
        self.screen = Tk()
        self.title = title
        self.bg = bg
        self.screen.title(title)
    
    def title(screentitle):
        if screentitle:
            self.title = screentitle
            return self.screen.title(screentitle)
