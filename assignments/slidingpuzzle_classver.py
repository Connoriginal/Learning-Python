#Class version sliding puzzle

class Reader:
    @staticmethod
    def get_number(size):
        num = input("Type the number you want to move (Type 0 to quit): ")
        while not (num.isdigit() and 0 <= int(num) <= size*size -1):
            num = input("Type the number you want to move (Type 0 to quit): ")
        return int(num)


class SlidingBoard:

    @staticmethod
    def creat_init_board(size):
        import random
        pocket = []
        init_board = []
        count = size * size
        for s in range(count):
            pocket.append(s)
        for i in range(size):
            row = []
            for j in range(size):
                k = pocket[random.randint(0,count-1)]
                row.append(k)
                pocket.remove(k)
                count = count - 1
            init_board.append(row)
        return init_board

    @staticmethod
    def set_goal_board(size):
        goal_board = []
        count = 0
        for board in range(0,size):
            board = []
            for i in range(0,size):
                i = int(i)
                board.append(i+size*count)
            goal_board.append(board)
            count = count + 1
        return goal_board

    def __init__(self,size):
        self.__board = SlidingBoard.creat_init_board(size)
        self.__empty = self.find_position(0)

    @property
    def board(self):
        return self.__board

    def find_position(self, num):
        for i in range(len(self.__board)):
            for j in range(len(self.__board)):
                if num == self.__board[i][j]:
                    return (i,j)

    def move(self,pos):
        posx = pos[0]
        posy = pos[1]
        empx = self.__empty[0]
        empy = self.__empty[1]

        if (empx == posx -1 and empy == posy) or \
        (empx == posx+1 and empy == posy) or \
        (empx == posx and empy == posy -1) or \
        (empx == posx and empy == posy +1):
            self.__board[empx][empy],self.__board[posx][posy] =\
            self.__board[posx][posy],self.__board[empx][empy]
            self.__empty = pos
        else:
            print("Can't move: Try again.")

    def print_board(self):
        for row in self.__board:
            for num in row:
                if num == 0:
                    print("  ",end = " ")
                else:
                    print(str(num).rjust(2),end = " ")
            print()

class SlidingPuzzleController:

    def __init__(self,size):
        self.__slider = SlidingBoard(size)
        self.__goal = SlidingBoard.set_goal_board(size)
        self.__size = size

    def play(self):
        while True:
            self.__slider.print_board()
            if self.__slider.board == self.__goal:
                print("Congratulations!")
                break
            num = Reader.get_number(self.__size)
            if num == 0:
                break
            pos = self.__slider.find_position(num)
            self.__slider.move(pos)
        print("Please come again.")

def main():
    import sys
    size = sys.argv[1]
    if size.isdigit() and int(size) > 1:
        SlidingPuzzleController(int(size)).play()
    else:
        print("Not a proper system argument.")
main()
