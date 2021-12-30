import numpy as np


test = open("input.txt").read()
t = test
t = t.split("\n\n")
draw_numbers = t[0].split("\n")
result = []
for item in t[1:len(t)]:
    result.append(item.split("\n"))

t1 = []
t2 = []
for item in result:
    count = 0
    for thing in item:
        thing = list(map(int, list(filter(None, thing.split(" ")))))
        t2.append(thing)
        count += 1
        if count == 5:
            t1.append(t2)
            t2 = []

lst_of_boards = t1
num_boards = len(lst_of_boards)
result = []
for matrix in lst_of_boards:
    result.append(np.matrix(matrix))

def checkfinished(board, row, col):
    if(np.sum(board[row, :]) == -5):
        return True
    if(np.sum(board[:,col]) == -5):
        return True
    else:
        return False



finished_boards = []  
the_num = []
counta = []
count = 0
draw_numbers = draw_numbers[0].split(",")
for num in draw_numbers:
    for board in result:
        for i in range(0,5):
            for j in range(0,5):
                if board[i,j] == int(num):
                    board[i,j] = -1
                    count += 1
                    if(checkfinished(board, i, j)):
                        copy = np.copy(board)
                        finished_boards.append(copy)
                        the_num.append(int(num))
                        board[:, :] = -1000
                        counta.append(count)


def calculateSum(board):
    count = 0
    for i in range(0,5):
        for j in range(0,5):
            if board[i, j] == -1:
                count += 1
    return sum(sum(board))+count


print(calculateSum(finished_boards[0])*the_num[0])
print(calculateSum(finished_boards[len(finished_boards)-1])*the_num[len(the_num)-1])

























