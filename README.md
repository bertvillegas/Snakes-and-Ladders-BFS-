# Snakes-and-Ladders-BFS-
BFS Project that focuses on the popular game, Snakes and Ladders

Given a particular Snakes and Ladders board, determine the minimum number of rolls needed to win the game.

# Background
Snakes and Ladders is a board game in which players roll a 6-sided die to determine how many squares forward they move on their turn, in a race to the finish. Some special squares are the start of ladders, and if a player ends on that square they move forward to the end of the ladder; other squares are the start of snakes, and if a player ends on that square they move back to the end of the snake.

# Function specs
Write a function called minimum_moves that takes:

A 1d list of ints called board
And returns:

An int, the minimum number of rolls needed to get to the final space on the board. Return -1 if it's not possible to win.

# Assumptions
The given board has at least 1 space
The player begins at 0
The player ends at n-1, where n is the length of board
If a ladder/snake ends at the start of another ladder/snake, you do not automatically take the second ladder/snake (i.e. no combos)

# Example 
minimum_moves([-1, -1, -1, 7, -1, -1, -1, -1])
should return 1, since rolling a 3 would allow the player to use a ladder to get to the space 7.

minimum_moves([-1, -1, -1, -1, -1, -1, -1, -1])
should return 2, since an extra roll is required to get to space 7 when there's no ladder. A valid winning combo would be 6, 1.
