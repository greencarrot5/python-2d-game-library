# python2d documentation

This is a guide that lists up the possibilities with python2d.

# introduction

Python2d is an open source library for creating 2d games in python. It only has a few function, but new will come as soon as possible.
You can already create simple games with python2d. Here is the minimum code:
```python
from python2d import *

game = Game("Title")

game.run()
```
The code does the following:

- Python2d is imported
- An instance of Game is created. Its title is set to "Title"
- The game loop starts

If you use this script, the game loop's only function is to update the screen repeatedly. Nothing will change, no matter how long you wait.
For change, we need characters.

## characters

You can easily create characters with this line of code:
```python
character = Game.createCharacter("image.png")
```
Mention that Game is the name of the class, and not the name of the object.
To let this work without errors, you need an image called "image.png" in the folder where your game file is.
You can let them move with character.move(x, y).

## key events

Coming soon!
