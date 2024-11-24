# Graph Coverage In Random Walks

# Problem statement
Imagine that you are playing a snake game on your old Nokia phone that has a screen that has width A and height B. You have a small 1x1 snake that can move up, dow, left, and right, and you start from some random point on your screen. Also, there is some apple (also sized 1x1) in some other random place on the screen. If you hit the right border of the screen and try to move right, your snake will appear on the left border in a symmetrical position. A similar thing would happen if your hit the top border of the screen (your snake will appear at the bottom), left border of the screen (it will appear on the right), and bottom border (it will teleport to the top). Your goal is to eat the apple as in the usual "Snake" game, BUT there are some important limitations of the game:

You are playing blindly (with closed eyes).
You don't know the size of the screen (A is unknown, B is unknown, and the area S=AB is ALSO unknown).
All you can do is only to send commands to the game by pressing "up", "down", "left", and "right" buttons.
You don't know your initial position.
You don't know your current position in any point in time in the game.
You don't know the position of the apple.
You can't cheat in the game and can't look at the screen at all.
You only know when you find the apple (your snake's position hits the apple's position) -- because your phone would signal a sound (your ears are not closed).
Once you find 1 apple, the game immediately finishes and you win.
If you use more than 35S left/right/up/down commands (where S = A*B -- also UNKNOWN value to you, BUT known to the game engine), you loose the game.
Please note that while you don't know the size of the screen, it can be literally any size, for example: 1x20, 100x1, 5000x5000 -- are all correct screen sizes. The only limitation is that A and B are positive integers.

# Graph representation

# Random walk rationalization

# Probabilistic proof

