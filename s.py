import random
import time
import os

# Constants for the game
WIDTH, HEIGHT = 15, 225
EMPTY_CELL, FILLED_CELL = ' ', '█'

# Define the shapes of the Tetris pieces
SHAPES = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1], [1, 1]],
    'T': [[0, 1, 0], [1, 1, 1]],
    'S': [[0, 1, 1], [1, 1, 0]],
    'Z': [[1, 1, 0], [0, 1, 1]],
    'J': [[1, 0, 0], [1, 1, 1]],
    'L': [[0, 0, 1], [1, 1, 1]]
}

class Tetris:
    def __init__(self):
        self.grid = [[EMPTY_CELL] * WIDTH for _ in range(HEIGHT)]
        self.current_piece = self.new_piece()
        self.piece_x, self.piece_y = 0, 0

    def new_piece(self):
        shape = random.choice(list(SHAPES.keys()))
        return SHAPES[shape]

    def can_move(self, dx, dy):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    new_x, new_y = self.piece_x + x + dx, self.piece_y + y + dy
                    if new_x < 0 or new_x >= WIDTH or new_y < 0 or new_y >= HEIGHT:
                        return False
                    if new_y >= 0 and self.grid[new_y][new_x] != EMPTY_CELL:
                        return False
        return True

    def move_piece(self, dx, dy):
        if self.can_move(dx, dy):
            self.piece_x += dx
            self.piece_y += dy
            return True
        return False

    def freeze_piece(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.piece_y + y][self.piece_x + x] = FILLED_CELL
        self.current_piece = self.new_piece()
        self.piece_x, self.piece_y = 0, 0

    def clear_lines(self):
        self.grid = [row for row in self.grid if any(cell == EMPTY_CELL for cell in row)]
        while len(self.grid) < HEIGHT:
            self.grid.insert(0, [EMPTY_CELL] * WIDTH)

    def render(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        display_grid = [row[:] for row in self.grid]
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    display_grid[self.piece_y + y][self.piece_x + x] = FILLED_CELL
        for row in display_grid:
            print(''.join(row))
        print('\nControls: q - quit')

    def play(self):
        while True:
            self.render()
            time.sleep(0.5)
            if not self.move_piece(0, 1):
                self.freeze_piece()
                self.clear_lines()

if __name__ == "__main__":
    game = Tetris()
    game.play()
