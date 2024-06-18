import pygame as pyg

pyg.init()

# Screen Dimensions and setup
dimensions = [900, 600]
screen = pyg.display.set_mode(dimensions)
caption = "The Break Out"
pyg.display.set_caption(caption)

# Loop, loop vars and fps vars
fps = 60
clock = pyg.time.Clock()

is_running = True

while is_running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            is_running = False
    
    
    screen.fill((255, 255, 255))
    
    pyg.display.update()
    pyg.display.flip()
            
