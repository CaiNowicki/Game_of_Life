import numpy as np
import random





class Grid:
    def __init__(self, n):
        self.grid = np.ndarray((n, n), dtype="object")
        for i in range(n):
            for j in range(n):
                self.grid[i][j] = Cell()
        self.generation = 0
        self.n = n

    def __getitem__(self, i, j):
        if i == self.n:
            i = 0
        if j == self.n:
            j = 0
        if i < 0:
            i = self.n - 1
        if j < 0:
            j = self.n - 1
        return self.grid[i][j]

    def update_grid(self):
        self.generation += 1
        cells_to_update = []
        for i in range(self.n):
            for j in range(self.n):
                cell = self.__getitem__(i, j)
                neighbors = self.find_neighbors(i, j)
                live_neighbors = 0
                # count how many live neighbors
                # if alive and 2 or 3 live neighbors, stay alive
                # if alive and <2 live neighbors, die
                # if alive and >3 live neighbors, die
                # if dead and 3 live neighbors, become alive
                # else state remains unchanged
                for neighbor in neighbors:
                    if neighbor.state:
                        live_neighbors += 1
                #if cell is currently alive, it dies with fewer than 2 neighbors or more than 3
                if cell.state:
                    if 2 <= live_neighbors < 4:
                        pass
                    else:
                        cells_to_update.append(cell)
                #if cell is currently dead, it comes alive with exactly 3 neighbors
                else:
                    if live_neighbors == 3:
                        cells_to_update.append(cell)
        for cell in cells_to_update:
            cell.change_state()


    def find_neighbors(self, i, j):
        neighbors = []
        neighbors.append(self.__getitem__(i - 1, j - 1))
        neighbors.append(self.__getitem__(i - 1, j))
        neighbors.append(self.__getitem__(i, j - 1))
        neighbors.append(self.__getitem__(i + 1, j - 1))
        neighbors.append(self.__getitem__(i - 1, j + 1))
        neighbors.append(self.__getitem__(i, j + 1))
        neighbors.append(self.__getitem__(i + 1, j))
        neighbors.append(self.__getitem__(i + 1, j + 1))
        return neighbors

    def live_cells(self):
        live_counter = 0
        for i in range(self.n):
            for j in range(self.n):
                cell = self.__getitem__(i, j)
                if cell.state:
                    live_counter += 1
        return live_counter

class Cell:
    def __init__(self):
        self.state = False
        if self.state:
            self.color = "black"
        else:
            self.color = "white"
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


class RandomGrid(Grid):
    def __init__(self, n):
        super().__init__(n)
        for i in range(n):
            for j in range(n):
                cell = RandomCell()
                self.grid[i][j] = cell
                print(f"Cell {i}, {j} created, is {cell.state}")


class RandomCell(Cell):
    def __init__(self):
        super().__init__()
        self.state = random.choice([True, False])