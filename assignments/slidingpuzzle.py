def sliding_puzzle(size):
    board = create_init_board(size)
    goal = set_goal_board(size)
    empty = find_position(0,board)
    while (True):
        print_board(board)
        if board == goal:
            print("Congratulations!")
            break
        num = get_number(size)
        if num == 0:
            break
        pos = find_position(num,board)
        (empty,board) = move(pos,empty,board)
    print("Please come again.")

def create_init_board(size):
    import random
    num = int(size)**2
    shufflelist = []
    anslist = []
    for i in range(int(size)):
        anslist.append([])
    for i in range(0,num):
        shufflelist += [i]
    random.shuffle(shufflelist)
    k = 0
    for j in anslist:
        for _ in range(int(size)):
            j.append(shufflelist[k])
            k += 1
    return anslist


def set_goal_board(size):
    anslist = []
    for i in range(int(size)):
        anslist.append([])
    k = 1
    for j in anslist:
        for _ in range(int(size)):
            if k == size**2:
                j.append(int(0))
            else:
                j.append(int(k))
                k += 1

    return anslist

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            num = board[i][j]
            if j == len(board[i])-1:
                if (num<10):
                    print(str(num).rjust(2))
                else:
                    print(str(num).rjust(1))
            else:
                if (num<10):
                    print(str(num).rjust(2),end=" ")
                else:
                    print(str(num).rjust(1),end=" ")


def get_number(size):
    num = input("Type the number you want to move (Type 0 to quit):")
    while not(num.isdigit() and 0 <= int(num) < size**2):
        num = input("Type the number you want to move (Type 0 to quit):")
    return int(num)

def find_position(num,board):
    for i in range(int(size)):
        for j in range(int(size)):
            if num == board[i][j]:
                return (i,j)

def move(pos,empty,board):
    (x,y) = pos
    if empty == (x-1,y) or empty == (x+1,y) or \
       empty == (x,y-1) or empty == (x,y+1):
       board[empty[0]][empty[1]] = board[x][y]
       board[x][y] = 0
       return (pos,board)
    else:
        print("Can\'t move: Try again.")
        return (empty,board)

if __name__=="__main__":
    import sys
    size = sys.argv[1]
    if size.isdigit() and int(size) > 1:
        sliding_puzzle(int(size))
    else:
        print("Not a proper system argument.")
