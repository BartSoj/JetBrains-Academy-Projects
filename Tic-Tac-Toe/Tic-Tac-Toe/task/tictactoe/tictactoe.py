class Board:

    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.cells = "_________"

    def print_board(self):
        print("-" * (3 + self.x_size * 2))  # prints the top horizontal line
        for y_cell in range(self.y_size):
            print("|", end=" ")  # prints the left vertical line
            for x_cell in range(self.x_size):
                print(self.cells[self.x_size * y_cell + x_cell], end=" ")  # prints each cell
            print("|")  # prints the right vertical line
        print("-" * (3 + self.x_size * 2))  # prints the bottom horizontal line

    def check_win(self, mark):
        # checks if all marks in a row are equal to the given mark
        # returns true if so
        for y in range(self.y_size):  # iterates over each column
            for x in range(self.x_size):  # iterates over each row
                # breaks if any cell is not equal to the given mark
                if self.cells[y * self.x_size + x] != mark:
                    break
            else:
                return True

        # checks if all marks in a column are equal to the given mark
        # returns true if so
        for x in range(self.x_size):  # iterates over each row
            for y in range(self.y_size):  # iterates over each column
                # breaks if any cell is not equal to the given mark
                if self.cells[y * self.x_size + x] != mark:
                    break
            else:
                return True

        # checks if all marks in a diagonal are equal to the given mark
        # returns true if so
        if self.x_size == self.y_size:  # The grid must be a square, the rows must be equal to the columns
            # checks the diagonal from top left to bottom right
            for cell in range(0, self.x_size * self.y_size, self.x_size + 1):  # iterates over diagonal
                if self.cells[cell] != mark:  # breaks if any cell is not equal to the given mark
                    break
            else:
                return True

            # checks the diagonal from top right to bottom left
            for cell in range(self.x_size - 1, self.x_size * self.y_size - 1,
                              self.x_size - 1):  # iterates over diagonal
                if self.cells[cell] != mark:  # breaks if any cell is not equal to the given mark
                    break
            else:
                return True

        return False

    def get_state(self):
        x_wins = self.check_win("X")
        o_wins = self.check_win("O")

        if x_wins:
            return "X wins"
        elif o_wins:
            return "O wins"
        elif "_" not in self.cells:
            return "Draw"

    def next_move(self):
        next_move = "O" if self.cells.count("X") > self.cells.count("O") else "X"
        while True:
            x_pos, y_pos = input("Enter the coordinates: ").split()
            if not x_pos.isdigit() or not y_pos.isdigit():
                print("You should enter numbers!")
                return
            x_pos = int(x_pos)
            y_pos = int(y_pos)
            pos = (self.x_size - y_pos) * self.x_size + x_pos - 1
            if x_pos > self.x_size:
                print("Coordinates should be from 1 to {}!".format(self.x_size))
            elif y_pos > self.y_size:
                print("Coordinates should be from 1 to {}!".format(self.y_size))
            elif self.cells[pos] != "_":
                print("This cell is occupied! Choose another one!")
            else:
                self.cells = self.cells[:pos] + next_move + self.cells[pos + 1:]
                return self.cells


board = Board(3, 3)

# starts the game
while True:
    board.print_board()
    state = board.get_state()
    if state:
        print(state)
        break
    board_cells = board.next_move()
