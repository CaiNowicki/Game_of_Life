import pygame
from game_objects.game_objects import Grid, RandomGrid
import time

def iterate_grid(filled_coord_pairs, blank_coord_pairs, grid, grid_dict, pixel_dict, sleep_time=0.5):
    # checking that grid object contains correct state for cells
    for value in filled_coord_pairs:
        x = grid_dict[value[0]]
        y = grid_dict[value[1]]
        cell = grid.__getitem__(x, y)
        if not cell.state:
            cell.change_state()
    for value in blank_coord_pairs:
        x = grid_dict[value[0]]
        y = grid_dict[value[1]]
        cell = grid.__getitem__(x, y)
        if cell.state:
            cell.change_state()
    time.sleep(sleep_time)
    # step to next generation in grid
    grid.update_grid()
    # assign updated cells back to correct list
    filled_coord_pairs = []
    blank_coord_pairs = []
    for i in range(25):
        for j in range(25):
            cell = grid.__getitem__(i, j)
            x = pixel_dict[i]
            y = pixel_dict[j]
            if cell.state:
                filled_coord_pairs.append((x, y))
            else:
                blank_coord_pairs.append((x, y))
    # tick_sound = pygame.mixer.Sound(file="assets/tick.mp3")
    # tick_sound.set_volume(0.5)
    # tick_sound.play(loops=0)
    return filled_coord_pairs, blank_coord_pairs


def show_rules():
    black = (0, 0, 0)
    white = (255, 255, 255)
    # hold this display until X is clicked
    closed = False
    while not closed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # game window closed
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # X button pressed
                x = event.pos[0]
                y = event.pos[1]
                if 1000 < x < 1100 and 10 < y < 50:
                    closed = True
        game_display.fill(white)
        rules_box1 = pygame.font.SysFont("arial", 50)
        rules_text1 = rules_box1.render("Rules of the Game of Life", True, black, white)
        rules_box2 = pygame.font.SysFont("arial", 25)
        rules_text2 = rules_box2.render("A cell can be either dead (white) or alive (black) and has 8 neighbors.", True, black, white)
        rules_box3 = pygame.font.SysFont("arial", 25)
        rules_text3 = rules_box3.render("If a cell is alive and has fewer than 2 living neighbors, it dies.", True,
                                        black, white)
        rules_box4 = pygame.font.SysFont("arial", 25)
        rules_text4 = rules_box4.render("If a cell is alive and has more than 4 living neighbors, it dies.", True,
                                        black, white)
        rules_box5 = pygame.font.SysFont("arial", 25)
        rules_text5 = rules_box5.render("If a cell is dead and has exactly 3 living neighbors, it becomes alive.", True,
                                        black, white)
        rules_box6 = pygame.font.SysFont("arial", 25)
        rules_text6 = rules_box6.render("All cells which do not meet these conditions remain in their current state.",
                                        True, black, white)
        exit_box = pygame.font.SysFont("arial", 70)
        exit_text = exit_box.render("X", True, black, (0, 0, 255))

        game_display.blit(rules_text1, [300, 10])
        game_display.blit(exit_text, [1000, 10])
        game_display.blit(rules_text2, [100, 100])
        game_display.blit(rules_text3, [100, 200])
        game_display.blit(rules_text4, [100, 300])
        game_display.blit(rules_text5, [100, 400])
        game_display.blit(rules_text6, [100, 500])
        pygame.display.update()
    # after escaping while loop by pressing X, go back to game


# creating game instance
pygame.init()
pygame.font.init()
default_font = pygame.font.get_default_font()
display_width = 1125
display_height = 825
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Conway's Game of Life")


# running game

def game_loop():
    grid = Grid(25)
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
    single_forward_button = pygame.image.load("assets/single_forward.png")
    single_forward_button = pygame.transform.scale(single_forward_button, (20, 20))
    double_forward_button = pygame.image.load("assets/double_forward.png")
    double_forward_button = pygame.transform.scale(double_forward_button, (20, 20))
    single_reverse_button = pygame.image.load("assets/single_reverse.png")
    single_reverse_button = pygame.transform.scale(single_reverse_button, (20, 20))
    double_reverse_button = pygame.image.load("assets/double_reverse.png")
    double_reverse_button = pygame.transform.scale(double_reverse_button, (20, 20))

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
    for i in range(985, 1026):
        rounded_dict.update({i: 985})
    for value in x_blank:
        pixel_dict.update({x_blank.index(value): value})
        grid_dict.update({value: x_blank.index(value)})

    crashed = False
    interactive = True
    sleep_time = 0.5
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # this will fire whether or not game is accepting input to the cells
                x = event.pos[0]
                y = event.pos[1]
                if 1050 < x < 1125 and 100 < y < 120:
                    # clicked on rules
                    show_rules()
                elif 1025 < x < 1045 and 220 < y < 240:
                    # clicked on double-slow
                    sleep_time = 1.25
                elif 1050 < x < 1070 and 220 < y < 240:
                    # click on slow
                    sleep_time = 0.75
                elif 1025 < x < 1045 and 250 < y < 270:
                    # clicked on single-fast (same as default)
                    sleep_time = 0.5
                elif 1050 < x < 1070 and 250 < y < 270:
                    # clicked on double-fast
                    sleep_time = 0.075
                elif 1025 < x < 1125 and 300 < y < 320:
                    # clicked on random, create randomized grid and assign filled cells to lists
                    grid = RandomGrid(25)
                    filled_coord_pairs = []
                    blank_coord_pairs = []
                    for i in range(25):
                        for j in range(25):
                            cell = grid.__getitem__(i, j)
                            x = pixel_dict[i]
                            y = pixel_dict[j]
                            if cell.state:
                                filled_coord_pairs.append((x, y))
                            else:
                                blank_coord_pairs.append((x, y))


            # if the mouse is clicked while the game is accepting input
            if event.type == pygame.MOUSEBUTTONDOWN and interactive:
                x = event.pos[0]
                y = event.pos[1]
                try:
                    # if the click is within the grid, assign it to the top left corner of the square it's in
                    x = rounded_dict[x]
                    y = rounded_dict[y]
                except KeyError:
                    pass
                if (x, y) in blank_coord_pairs:
                    # if the square is empty, put it in list for black square
                    blank_coord_pairs.remove((x, y))
                    filled_coord_pairs.append((x, y))
                elif (x, y) in filled_coord_pairs:
                    # if square is filled, put it in list for blank square
                    blank_coord_pairs.append((x, y))
                    filled_coord_pairs.remove((x, y))
                elif 10 < x < 70 and 5 < y < 25:
                    # pressed the start button
                    interactive = False
                elif 205 < x < 265 and 5 < y < 25:
                    # pressed reset button, fill grid with empty squares and reset grid object
                    blank_coord_pairs = reset_coord_pairs.copy()
                    filled_coord_pairs = []
                    interactive = True
                    grid = Grid(25)
                elif 140 < x < 200 and 5 < y < 25:
                    # pressed the next button, iterate just one generation and stop
                    filled_coord_pairs, blank_coord_pairs = iterate_grid(filled_coord_pairs, blank_coord_pairs, grid,
                                                                         grid_dict, pixel_dict, sleep_time)
                    interactive = True

            # if the mouse is clicked while the game is not accepting input
            if event.type == pygame.MOUSEBUTTONDOWN and not interactive:
                x = event.pos[0]
                y = event.pos[1]
                if 75 < x < 135 and 5 < y < 25:
                    # pressed the stop button
                    interactive = True
                elif 205 < x < 265 and 5 < y < 25:
                    # pressed reset button
                    blank_coord_pairs = reset_coord_pairs.copy()
                    filled_coord_pairs = []
                    interactive = True
        if not interactive:
            filled_coord_pairs, blank_coord_pairs = iterate_grid(filled_coord_pairs, blank_coord_pairs, grid, grid_dict,
                                                                 pixel_dict, sleep_time)
            if filled_coord_pairs == []:
                # if grid is empty, stop iterating
                interactive = True

        generations = grid.generation
        live_cells = grid.live_cells()

        # create text boxes
        generations_box = pygame.font.SysFont("arial", 25)
        generations_text = generations_box.render(f"Generations: {generations}", True, black, white)
        live_cells_box = pygame.font.SysFont("arial", 25)
        live_cells_text = generations_box.render(f"Live Cells: {live_cells}", True, black, white)
        rules_box = pygame.font.SysFont("arial", 25)
        rules_text = rules_box.render("Rules", True, black, (0, 0, 255))
        adjust_box = pygame.font.SysFont("arial", 25)
        adjust_text = adjust_box.render("Adjust", True, black, white)
        speed_box = pygame.font.SysFont("arial", 25)
        speed_text = speed_box.render("Speed", True, black, white)
        random_box = pygame.font.SysFont("arial", 25)
        random_text = random_box.render("Random", True, black, (0, 0, 255))

        # arrange buttons, text, and cells on display
        game_display.fill(white)
        game_display.blit(start_button, [10, 5])
        game_display.blit(stop_button, [75, 5])
        game_display.blit(next_button, [140, 5])
        game_display.blit(reset_button, [205, 5])
        game_display.blit(generations_text, [600, 0])
        game_display.blit(live_cells_text, [900, 0])
        game_display.blit(rules_text, [1025, 100])
        game_display.blit(adjust_text, [1025, 160])
        game_display.blit(speed_text, [1025, 185])
        game_display.blit(single_reverse_button, [1050, 220])
        game_display.blit(double_reverse_button, [1025, 220])
        game_display.blit(single_forward_button, [1025, 250])
        game_display.blit(double_forward_button, [1050, 250])
        game_display.blit(random_text, [1025, 300])
        for pair in blank_coord_pairs:
            game_display.blit(empty_tile, [pair[0], pair[1]])
        for pair in filled_coord_pairs:
            game_display.blit(black_tile, [pair[0], pair[1]])

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()

# TODO:
# create method to replace blank grid with randomized grid and/or presets
