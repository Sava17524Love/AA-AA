from email.mime import image

import display as display
import mixer as mixer
from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Maze')
background = transform.scale(image.load('1632448069_21-idei-club-p-psikhbolnitsa-myagkaya-komnata-interer-kra-26 - копия - копия.jpg'), (win_width, win_height))

game = True
clock = time.Clock()
FPS = 60

#mixer.music.load('')
#mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,60))
        self.rect = self.image.get_rect()
        self.speed.x = player_x
        self.speed.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = GameSprite('Penguins-transformed - копия - копия.png', 5, win_height - 80, 4)

monster = GameSprite('Penguins-transformed - копия - копия.png', win_width - 80, 280, 3)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    player.reset()
    display.update()
    clock.tick(FPS)
