import pygame
from app_scripts.game_objects import Grid
import time

# creating game instance
pygame.init()
display_width = 1125
display_height = 825
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Conway's Game of Life")

# creating image assets and colors
black = (0, 0, 0)
white = (255, 255, 255)
empty_tile = pygame.image.load("assets/blank_grid_tile.png")
black_tile = pygame.image.load("assets/black_tile.png")
start_button = pygame.image.load("assets/start_button.png")
start_button = pygame.transform.scale(start_button, (60, 20))
stop_button = pygame.image.load("assets/stop_button.png")
stop_button = pygame.transform.scale(stop_button, (60, 20))
next_button = pygame.image.load("assets/next_button.png")
next_button = pygame.transform.scale(next_button, (60, 20))
reset_button = pygame.image.load("assets/reset_button.png")
reset_button = pygame.transform.scale(reset_button, (60, 20))

clock = pygame.time.Clock()

# setting grid coordinates and creating blank Grid() object
x_blank = [x + 25 for x in range(0, 1000, 40)]

blank_coord_pairs = []
for i in range(len(x_blank)):
    for j in range(len(x_blank)):
        blank_coord_pairs.append((x_blank[i], x_blank[j]))

reset_coord_pairs = blank_coord_pairs.copy()
filled_coord_pairs = []


# hard-coding rounding values and grid locations
rounded_dict = {}
grid_dict = {}
pixel_dict = {}
for x in range(1, len(x_blank)):
    for i in range(x_blank[x - 1], x_blank[x]):
        # used to assign any number in the square 40x40 to the top left corner of that square
        rounded_dict.update({i: x_blank[x - 1]})

for value in x_blank:
    pixel_dict.update({x_blank.index(value): value})
    grid_dict.update({value: x_blank.index(value)})

# running game
crashed = False
interactive = True
grid = Grid(25)
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        # if a square is clicked, replace it with a black tile
        if event.type == pygame.MOUSEBUTTONDOWN and interactive:
            x = event.pos[0]
            y = event.pos[1]
            try:
                x = rounded_dict[x]
                y = rounded_dict[y]
            except KeyError:
                pass
            if (x, y) in blank_coord_pairs:
                blank_coord_pairs.remove((x, y))
                filled_coord_pairs.append((x, y))
            elif (x, y) in filled_coord_pairs:
                blank_coord_pairs.append((x, y))
                filled_coord_pairs.remove((x, y))
            elif 10 < x < 70 and 5 < y < 25:
                # pressed the start button
                interactive = False
            elif 205 < x < 265 and 5 < y < 25:
                # pressed reset button
                blank_coord_pairs = reset_coord_pairs.copy()
                filled_coord_pairs = []
                interactive = True
                grid = Grid(25)
        if event.type == pygame.MOUSEBUTTONDOWN and not interactive:
            x = event.pos[0]
            y = event.pos[1]
            if 75 < x < 135 and 5 < y < 25:
                # pressed the stop button
                interactive = True
            if 140 < x < 200 and 5 < y < 25:
                # pressed the next button
                # single generation iteration
                pass
            elif 205 < x < 265 and 5 < y < 25:
                # pressed reset button
                blank_coord_pairs = reset_coord_pairs.copy()
                filled_coord_pairs = []
                interactive = True
    generations = grid.generation
    if not interactive:
        # coordinates are range(25, 1000, step=40)
        # need to update state of cell x,y in Grid() object according to location on visible grid if in filled list
        # then update grid
        # assign back to respective filled/blank lists and re-draw without turning interactive back on
        #on first iteration, find each live cell in filled list and set to alive
        if generations == 0:
            for value in filled_coord_pairs:
                x = grid_dict[value[0]]
                y = grid_dict[value[1]]
                cell = grid.__getitem__(x,y)
                if not cell.state:
                    cell.change_state()
        time.sleep(0.5)
        #step to next generation in grid
        grid.update_grid()
        #assign updated cells back to correct list
        filled_coord_pairs = []
        blank_coord_pairs = []
        for i in range(25):
            for j in range(25):
                cell = grid.__getitem__(i,j)
                x = pixel_dict[i]
                y = pixel_dict[j]
                if cell.state:
                    filled_coord_pairs.append((x,y))
                else:
                    blank_coord_pairs.append((x,y))


    game_display.fill(white)
    generations_box = pygame.font.Font(None, 35)
    generations_text = generations_box.render(f"Generations: {generations}", True, black, white)

    game_display.blit(start_button, [10, 5])
    game_display.blit(stop_button, [75, 5])
    game_display.blit(next_button, [140, 5])
    game_display.blit(reset_button, [205, 5])
    game_display.blit(generations_text, [900, 5])
    for pair in blank_coord_pairs:
        game_display.blit(empty_tile, [pair[0], pair[1]])
    for pair in filled_coord_pairs:
        game_display.blit(black_tile, [pair[0], pair[1]])

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()