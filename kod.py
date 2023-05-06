from pygame import*

wind_h = 500
wind_w = 700

wind = display.set_mode((wind_w,wind_h))
timer = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
 
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        wind.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < wind_w - 80:
            self.rect.y += self.speed


    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < wind_w - 80:
            self.rect.y += self.speed

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

