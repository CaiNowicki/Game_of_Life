import pygame
from app_scripts.game_objects import Grid

#creating game instance
pygame.init()
grid = Grid(25)
display_width = 1125
display_height = 825
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Conway's Game of Life")

#creating image assets and colors
black = (0,0,0)
white = (255,255,255)
empty_tile = pygame.image.load("assets/blank_grid_tile.png")
black_tile = pygame.image.load("assets/black_tile.png")
start_button = pygame.image.load("assets/start_button.png")
start_button = pygame.transform.scale(start_button, (60,20))
stop_button = pygame.image.load("assets/stop_button.png")
stop_button = pygame.transform.scale(stop_button, (60,20))


clock = pygame.time.Clock()

#setting grid coordinates
x_blank = [x+25 for x in range(0,1000,40)]

blank_coord_pairs = []
for i in range(len(x_blank)):
    for j in range(len(x_blank)):
        blank_coord_pairs.append((x_blank[i],x_blank[j]))

filled_coord_pairs = []


#hard-coding rounding values
rounded_dict = {}
for x in range(1,len(x_blank)):
    for i in range(x_blank[x-1],x_blank[x]):
        rounded_dict.update({i : x_blank[x-1]})


#running game
crashed = False
interactive = True
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        #if a square is clicked, replace it with a black tile
        if event.type == pygame.MOUSEBUTTONDOWN and interactive:
            x = event.pos[0]
            y = event.pos[1]
            try:
                x = rounded_dict[x]
                y = rounded_dict[y]
            except KeyError:
                pass
            if (x,y) in blank_coord_pairs:
                blank_coord_pairs.remove((x,y))
                filled_coord_pairs.append((x,y))
            elif (x,y) in filled_coord_pairs:
                blank_coord_pairs.append((x,y))
                filled_coord_pairs.remove((x,y))
            elif 5 < x < 65 and 5 < y < 25:
                interactive = False
        if event.type == pygame.MOUSEBUTTONDOWN and not interactive:
            x = event.pos[0]
            y = event.pos[1]
            if 70 < x < 130 and 5 < y < 25:
                interactive = True

    game_display.fill(white)
    game_display.blit(start_button, [5,5])
    game_display.blit(stop_button, [70, 5])
    for pair in blank_coord_pairs:
        game_display.blit(empty_tile, [pair[0],pair[1]])
    for pair in filled_coord_pairs:
        game_display.blit(black_tile, [pair[0],pair[1]])
    if not interactive:
        pass
        #filled contains all live cells
        #blank contains all dead cells
        #need to assign to cell x,y in Grid() object according to location on visible grid
        #then update grid
        #assign back to respective filled/blank lists and re-draw without turning interactive back on
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

