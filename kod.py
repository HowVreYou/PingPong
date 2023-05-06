from pygame import*

wind_h = 500
wind_w = 700

wind = display.set_mode((wind_w,wind_h))
timer = time.Clock()
FPS = 60

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    timer.tick(FPS)
    wind.fill((255, 255, 255))

    display.update()
    timer.tick(FPS)


