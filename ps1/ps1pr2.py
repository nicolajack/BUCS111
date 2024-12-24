# 
# ps1pr2.py - Problem Set 1, Problem 2
#
# Indexing and slicing puzzles
#

#
# List puzzles
#

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example puzzle (puzzle 0):
# Creating the list [2, 5, 9] from pi and e
answer0 = [e[0]] + pi[4:]

# Put your solutions to the remaining list puzzles below.

# Puzzle 1:
# Creating the list [2, 7] from pi and e
answer1 = e[0:2]

# Puzzle 2:
# Use pi and/or e to create the list [5, 4, 3]
answer2 = pi[-2::-2]

# Puzzle 3:
# Use pi and/or e to create the list [1, 2, 3, 4, 5]
answer3 = e[::-2] + pi[::2]


#
# String puzzles
#

b = 'boston'
u = 'university'
t = 'terriers'

# Example puzzle (puzzle 4)
# Creating the string 'bossy'
answer4 = b[:3] + t[-1] + u[-1]

# Put your solutions to the remaining string puzzles below.

# Puzzle 5:
# Use b, u, and/or t to create the string 'universe'
answer5 = u[:-3] + t[1]

# Puzzle 6:
# Use b, u, and/or t to create the string 'roster'
answer6 = t[2] + b[1:4] + t[1:3]

# Puzzle 7:
# Use b, u, and/or t to create the string 'yesyesyes'
answer7 = (u[-1:-7:-5] + u[-4]) * 3

# Puzzle 8:
# Use b, u, and/or t to create the string 'trist'
answer8 = t[:5:2] + b[2:4]


# The code below tests the values of your expressions. DO NOT MODIFY IT!
if __name__ == '__main__':    
    for n in range(0, 9):
        answer_var = 'answer' + str(n)
        if answer_var in dir():
            print(answer_var, '=', eval(answer_var))
