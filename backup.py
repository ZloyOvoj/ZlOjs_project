import pygame
import random
import sys

WIDTH = 1200
HEIGHT = 1080

pygame.init()
menu = True
score = 0
pygame.font.init()
f1 = pygame.font.Font(None, 30)
FPS = 30
PIMAGE = pygame.image.load('smallship1.png')
E1IMAGE = pygame.image.load('enemy1.png')
PJIMAGE = pygame.image.load('blueprojectile.png')
pygame.mixer.music.load("shootsound.mp3")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("smallship1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(self.rect.x, self.rect.y, 150, 130)
        self.rect.center = (950, 1900)
        players.add(self)

    def update(self):
        if self.rect.left > WIDTH:
            self.rect.right = 720
        if self.rect.right < 720:
            self.rect.left = WIDTH
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        self.speedx = 0
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.speedx = -8
        if key_pressed[pygame.K_LEFT] and (key_pressed[pygame.K_LSHIFT] or key_pressed[pygame.K_RSHIFT]):
            self.speedx = -16
        if key_pressed[pygame.K_RIGHT]:
            self.speedx = 8
        if key_pressed[pygame.K_RIGHT] and (key_pressed[pygame.K_LSHIFT] or key_pressed[pygame.K_RSHIFT]):
            self.speedx = 16
        self.rect.x += self.speedx
        self.speedy = 0
        if key_pressed[pygame.K_DOWN]:
            self.speedy = 8
        if key_pressed[pygame.K_DOWN] and (key_pressed[pygame.K_LSHIFT] or key_pressed[pygame.K_RSHIFT]):
            self.speedy = 16
        if key_pressed[pygame.K_UP]:
            self.speedy = -8
        if key_pressed[pygame.K_UP] and (key_pressed[pygame.K_LSHIFT] or key_pressed[pygame.K_RSHIFT]):
            self.speedy = -16
        self.rect.y += self.speedy

    def shoot(self):
        playerprojectile = Playerprojectile(self.rect.centerx, self.rect.top)
        all_sprites.add(playerprojectile)
        projectiles.add(playerprojectile)


class FirstEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice(range(600, 950)), 100)
        self.rect = pygame.Rect(self.rect.x, self.rect.y, 150, 125)
        enemies.add(self)

    def update(self):
        if self.rect.left > WIDTH:
            self.rect.right = 720
        if self.rect.right < 720:
            self.rect.left = WIDTH
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
        self.speedy = 10
        self.rect.y += self.speedy
        FirstEnemy.rect = pygame.Rect(self.rect.x, self.rect.y, 50, 50)
        self.speedy = 20
        self.speedx = 0
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.speedx = -8
        if key_pressed[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        self.speedy = 0
        if key_pressed[pygame.K_DOWN]:
            self.speedy = 8
        if key_pressed[pygame.K_UP]:
            self.speedy = -8
        self.rect.y += self.speedy


class Playerprojectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image = pygame.transform.scale(pygame.image.load("blueprojectile.png").convert_alpha(), (16, 16))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -25
        self.speedx = 0
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.speedx = -10
        if key_pressed[pygame.K_RIGHT]:
            self.speedx = 10
        if key_pressed[pygame.K_LEFT] and (key_pressed[pygame.K_LSHIFT] or key_pressed[pygame.K_RSHIFT]):
            self.speedx = -20
        if key_pressed[pygame.K_RIGHT] and (key_pressed[pygame.K_LSHIFT] or key_pressed[pygame.K_RSHIFT]):
            self.speedx = 20

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()
            FirstEnemy.kill(self)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
quit_button = pygame.draw.rect(screen, (100, 130, 180), (960, 0, 150, WIDTH))
start_button = pygame.draw.rect(screen, (70, 130, 180), (800, 0, 150, WIDTH))
text5 = f1.render("Выход", True, (255, 255, 255))
text6 = f1.render("Старт", True, (255, 255, 255))
screen.blit(text5, (1000, 540))
screen.blit(text6, (840, 540))
pygame.display.flip()
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


while menu:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos() >= (960, 90):
                if pygame.mouse.get_pos() <= (1110, 140):
                    pygame.quit()
            if pygame.mouse.get_pos() >= (800, 90):
                if pygame.mouse.get_pos() <= (950, 140):
                    menu = False
                    running = True


all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
enemies = pygame.sprite.Group()
players = pygame.sprite.Group()
player = Player()
firstenemy = FirstEnemy()
all_sprites.add(player)
all_sprites.add(firstenemy)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_ESCAPE]:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.shoot()
                pygame.mixer.music.play()
    highscore = score
    if score < highscore:
        highscore = highscore
    if score > highscore:
        highscore = score

    pygame.display.update()
    screen.fill(BLACK)
    pygame.draw.rect(screen, (25, 25, 25), (1, 1, 560, 1080))
    pygame.draw.rect(screen, (25, 25, 25), (1350, 1, 1920, 1080))
    all_sprites.update()
    pdhits = pygame.sprite.groupcollide(enemies, players, True, True)
    for hit in pdhits:
        sys.exit()
    edhits = pygame.sprite.groupcollide(enemies, projectiles, True, True)
    for hit in edhits:
        m = FirstEnemy()
        all_sprites.add(m)
        enemies.add(m)
        score += 1
    all_sprites.draw(screen)
    text1 = f1.render(str(score), True, (255, 255, 255))
    text2 = f1.render(str(highscore), True, (255, 255, 255))
    text3 = f1.render("Счёт", True, (255, 255, 255))
    text4 = f1.render("Рекорд", True, (255, 255, 255))
    screen.blit(text1, (270, 12))
    screen.blit(text2, (270, 30))
    screen.blit(text3, (180, 12))
    screen.blit(text4, (180, 30))
    pygame.display.flip()

pygame.quit()
