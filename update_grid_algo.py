from game_objects import Grid


def update_grid(grid):
    for i in range(grid.n):
        for j in range(grid.n):
            cell = grid.__getitem__(i, j)
            neighbors = find_neighbors(i, j, grid)
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
            if cell.state:
                if live_neighbors != 2 and live_neighbors != 3:
                    cell.change_state()
            else:
                if live_neighbors == 3:
                    cell.change_state()



def find_neighbors(i, j, grid):
    neighbors = []
    neighbors.append(grid.__getitem__(i - 1, j - 1))
    neighbors.append(grid.__getitem__(i - 1, j))
    neighbors.append(grid.__getitem__(i, j - 1))
    neighbors.append(grid.__getitem__(i + 1, j - 1))
    neighbors.append(grid.__getitem__(i - 1, j + 1))
    neighbors.append(grid.__getitem__(i, j + 1))
    neighbors.append(grid.__getitem__(i + 1, j))
    neighbors.append(grid.__getitem__(i + 1, j + 1))
    return neighbors
