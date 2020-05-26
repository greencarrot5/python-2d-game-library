# python-2d-game-library
A python library that helps making 2d games.
# description
Python already has a great built-in library for graphics, tkinter, but there aren't many tools to create a 2d game. This library will contain functions to write simple games in a few lines of code.
# goal
The goal is to make it easy for everyone to create 2d games in python, without having to calculate everthing yourself, so you have something like this:

```python

from python2d import Game

game = Game("Example game", width=400, height=400)

#creating main character
main = Game.createCharacter("maincharacter.png")
main.place(x=150, y=150)

#handling keypress
@game.onkeypress("left")
def to_left():
    main.move(-5, 0)

@game.onkeypress("right")
def to_right():
    main.move(5, 0)

@game.onkeypress("up")
def jump():
    main.jump()

#adding gravity to the game
game.gravity = 1

#placing block so the character won't fall
block = Game.block(color="brown", width=300, height=50)
block.place(x=50, y=275)

#adding the block and the character to the game
game.add(block)
game.add(main)

#running the game
game.run()
```

So far, the only thing you can find in this project, is the beginning of the game-class.
