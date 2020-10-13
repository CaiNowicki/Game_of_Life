import numpy as np


def create_cell():
    cell = Cell()
    return cell


class Grid:
    def __init__(self, n):
        self.grid = np.ndarray((n, n), dtype="object")
        for i in range(n):
            for j in range(n):
                self.grid[i][j] = create_cell()
        self.generation = 0

    def __getitem__(self, i, j):
        return self.grid[i][j]

    def iterate_generation(self):
        self.generation += 1

class Cell:
    def __init__(self):
        self.state = False
        self.color = "white"
        self.clickable = True

    def change_state(self):
        if self.state:
            self.state = False
            self.color = "white"
        else:
            self.state = True
            self.color = "black"

    def change_click(self):
        if self.clickable:
            self.clickable = False
        else:
            self.clickable = True