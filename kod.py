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

racket1 = Player('racket.png', 30, 200, 50, 150, 4)
racket2 = Player('racket.png', 520, 200, 50, 150, 4)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)

dx = 3
dy = 3

font.init()
font1 = font.Font(None, 70)
lose1 = font1.render('Первый проиграл!', True, (200,200,200))
lose2 = font1.render('Второй проиграл!', True, (200,200,200))

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish == False:
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += dx
        ball.rect.y += dy
        if ball.rect.y<0 or ball.rect.y>=wind_h - 50:
            dy *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            dx *= -1

        wind.fill((255, 255, 255))
        racket1.reset()
        racket2.reset()
        ball.reset()

        if ball.rect.x<=0:
            finish = True
            wind.blit(lose1, (200,200))


        if ball.rect.x>=wind_w - 50:
            finish = True
            wind.blit(lose2, (200,200))

    display.update()
    timer.tick(FPS)


