# Graph Coverage In Random Walks

# Problem Statement
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

# Problem Statement Analysis
Following are a few observations that need to be taken into account for the strategy to be successful:
* Considering that the strategy needs to perform optimally for a general case, and not favor grids where A >> B or B >> A, roughly the same amount of steps needs to be taken horisontally and vertically.
* Since it is at no point known at what position on the A*B grid the snake is positioned, it may seem intuitive to spiral around an anchor point (the starting position), with the hope of avoiding visited tiles. However, while this approach performs optimally on grids where the width and the height are about the same - it plays out poorly on all screens which are significantly taller/wider than wide/tall (A >> B or B >> A).
* Strategies with periodic properties need to be avoided, as they may leed to the snake looping around the grid.
* Additionaly, attempts to avoid periodicity through determining the number of steps in a direction via a growing function can quickly lead to the snake wasting excessive moves in a single row/column. For f(x) = x^2, assuming that S = 1000000, it would take only a 1000 turns for the snake to move over S moves in a single direction, therefore unecessarily retracing old steps. Even f(x) = x performs poorly. If a function is to be used to combat periodicity, it needs to grow slowly, and is likely not monotonous.
  
# Strategy Considerations and Experimental Evaluation
Taking the observations into account, it is reasonable to consider an approach where the snake takes each step in a random direction. 
* Over a large enough number of moves, the snake ends up moving about the same amount vertically and horisontally
* Long strides in a single direction are improbable and therefore rare
* The randomness prevents the snake from moving in patterns

A heuristic improvement that follows naturally is one that allows the snake to move only "up" and "right", in an attempt to eliminate unproductive move sequences such as "up-down" and "left-left-right-right-right-left" (this is made possible by the fact that the map is in actuality a toroidal grid, although being represented as a matrix).

Once both approaches demonstrated themselves successful in preliminary simulations, a larger scale experiment was conducted.

## Experimental Setup and Results

**1. Comparing performance of the random and heuristic random approaches**
We simulated 100 games for every board size between 2x2 and 100x100. This provided insight into how the strategies performed on A >> B, B >> A and B ~ A boards, although on relatively small grids (maximum S was 10^5, compared to the allowed 10^6).

The first plot displays the number of moves used over a certain board size. It is important to note that there was significantly more small grids in the experiment, which is why there are less statistical outliers for bigger boards. This is particulairly noticable for the random method, whoose outliers deviated from the mean more significantly.
![stats](https://github.com/lkuresevic/graph_coverage_with_random_walks/blob/main/Plots/stats.png)
In order to gain better insight into how many moves the snake took to find the apple in the majority of these simulations, we plot the amount of simulations that utilized a certain percentage of moves.
![stats_histogram](https://github.com/lkuresevic/graph_coverage_with_random_walks/blob/main/Plots/stats_distribution.png)
Although the heuristic strategy's superiority is clear, given that all of its runs terminated succesfully, utilizing less then 50% of allowed moves, we notice that even the random approach performs surprisingly well, with the vast majority of its simulations utilizing under 10% of moves.
This is better demonstrated on the following plot, which compares the percentage of succesful runs under a given threshold.
![stats_histogram](https://github.com/lkuresevic/graph_coverage_with_random_walks/blob/main/Plots/stats_histograms.png)
It is appearent that the snake using the heuristic random method finds the apple in under 20% of the allowed moves, and around 97.5% of the times in under 10% of the allowed moves. What is left is to experimentally examine whether the method becomes obsolete when tested on larger grids, where the 35 multiplier means less.
**2. Testing the heuristic random approach on larger grid sizes**

A deterministic strategy that mimics the behaviour of the random approach and conforms to the observations, is one where the snake's movements are decided by a string of ones and zeroes generated by binary (or Gray's) code. While this idea has also proven successful in preliminary simulations, it failed to offer apparent mathematical proofs that would make it 

However, probability theory offers an opportunity to explain the effectiveness of the random approach, and proove it works almost surely.
# Probabilistic basis
The field is given in the form of a grid of dimensions A x B, where the right and left edge, as well as the upper and lower one are connected. We can represent the tiles and their connections as a 4-regular undirected graph. If we can prove that starting from any node we can cover the entire graph with high probability in under 35S turns - by making a random step toward one of the adjacent nodes each turn - we have proof that the snake will have almost certainly reached the apple before running out of moves to make.
We can define the problem as a Markov Chain, where each node of the graph corresponds to a state. Transitions (steps) between states (nodes) are random, and have equal probability of 0.25 each. 
Since our 4-regular graph is connected and there exists a path between every two nodes, the Markov Chain represented by it is irreducible (all states can be reached from all other states).
We can also prove that this Markov Chain is aperiodic. A period *d* of a state *i* is defined as:
* *d(i) = gcd{n|P^n(i,i)>0}*,

where *P^n(i,i)* is the probability of returning to state *i* after *n* steps (in our case, a state *i* corresponds to a node in the graph which represents the matrix AxB; each state *i* represents an element of the AxB matrix with coordinates (a,b), 1 < a < A, 1 < b < B). Since the chain is irreducible, and transitions are random, it is possible to return to state *i* after 1, 2, 3, or any number of steps *n*. The greates common denominator of a set that contains all such *n* (defined with *d(i) = gcd{n|P^n(i,i)>0}*) is 1, hence the Markov Chain is aperiodic. It is also positively recurrent, since the AxB grid it represents is finite.

Having established that our Markov Chain is irreducible, aperiodic and positively recurrent, we know it is also **ergodic** (Markov chains modeling finite-state systems with random transitions, as ours is, are well known to be ergodic, but it may have been useful to proove so step by step). This provides us with a key property - **stationary distribution** (a distribution towards which the chain converges to over time, regardless of the starting state). Specifically, given that all nodes are equally accessible and symmetric in the random walk's structure, the stationary distribution is **uniform**, meaning that in the long run, the random walk will visit all nodes with equal probability. For a finite graph with S nodes (representing S tiles of the AxB grid), the probability of being at any specific node converges to 1/S.
