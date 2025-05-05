from pygame import *

back = (161, 48, 48)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
#classes
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#sprites
racket1 = Player('racket.png', 30, 200, 50, 150, 4)
racket2 = Player('badminton.png', 620, 200, 50, 150, 4)
ball = GameSprite('ball_802340.png', 325, 225, 50, 50, 1)

#fonts
font.init()
font = font.SysFont('arial', 35)
lose1 = font.render('PLAYER1 LOSED!!!', True, (222, 225, 60))
lose2 = font.render('PLAYER2 LOSED!!!', True, (119, 117, 255))

game = True
finish = False
clock = time.Clock()
FPS = 60
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_left()
        racket2.update_right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True 
            window.blit(lose1, (225, 250))
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (225, 250))

        racket1.reset()
        racket2.reset()
        ball.reset()
        
    display.update()
    clock.tick(FPS)    
