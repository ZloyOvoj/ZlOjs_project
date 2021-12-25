import pygame
import random
import sys

blokBot = True
blok = True
blok2 = False
blok3 = False
blok4 = True
blok5 = False
blok6 = False
blok7 = False

Menu = True

ms = 101
sec = 30

# Рандом
ran = random.randint(0, 1)
ran2 = random.randint(0, 1)

# Экран
sc = pygame.display.set_mode((600, 515))

# Щёчики
betaS = 0
betaS2 = 0

# Очки
score = 0
score2 = 0

# Я
y = 150
x = 30

# Бот
y2 = 149
x2 = 570

# Мяч
y3 = 200
x3 = 300
bx = -1
by = 1

special = pygame.image.load("image/kulak.jpg")
scale = pygame.transform.scale(special, (special.get_width() // 13, special.get_height() // 13))

Game = False

pygame.font.init()
f1 = pygame.font.Font(None, 30)
f2 = pygame.font.Font(None, 90)
f3 = pygame.font.Font(None, 40)
f4 = pygame.font.Font(None, 130)
f5 = pygame.font.Font(None, 30)


def button(x, y, hight, top, R, G, B, ff, texttext, razmer, nadpis, R2, G2, B2, x2, y2):
    pygame.draw.rect((R, G, B), (x, y, hight, top))
    ff = pygame.font.Font(None, razmer)
    texttext = ff.render(nadpis, False, (R2, G2, B2))
    sc.blit(texttext, (x2, y2))

while Menu:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        Menu = False
        Game = True

    pygame.display.update()
    pygame.time.delay(3)

while Game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= 1
    if keys[pygame.K_s]:
        y += 1
    if blok2:
        if keys[pygame.K_f]:
            blok3 = True

    ms -= 1

    if blok:
        if ms == 0:
            sec -= 1
            ms = 101

    sc.fill((0, 0, 0))

    # Счёт
    text1 = f1.render(str(score), False, (130, 125, 125))
    text2 = f1.render(":", False, (130, 125, 125))
    text3 = f1.render(str(score2), False, (130, 125, 125))
    sc.blit(text1, (270, 12))
    sc.blit(text2, (290, 10))
    sc.blit(text3, (310, 12))

    # Коллизия движ. объектов
    aColl = pygame.Rect((x2, y2), (10, 100))
    bColl = pygame.Rect((x3, y3), (5, 5))
    cColl = pygame.Rect((x, y), (10, 100))

    # Коллизия стен
    wallColl1 = pygame.Rect((0, -100), (600, 100))
    wallColl2 = pygame.Rect((0, 400), (600, 100))
    wallColl3 = pygame.Rect((-1, -10), (1, 410))
    wallColl4 = pygame.Rect((600, 0), (10, 400))

    # Движ. объекты
    pygame.draw.rect(sc, (255, 255, 255), (x3, y3, 5, 5))
    pygame.draw.rect(sc, (255, 255, 255), (x2, y2, 10, 100))
    pygame.draw.rect(sc, (255, 255, 255), (x, y, 10, 100))

    if blok3:
        pygame.draw.rect(sc, (0, 0, 255), (x + 10, y, 5, 100))
        specialColl = pygame.Rect((x + 10, y), (5, 100))
        collS = bColl.colliderect(specialColl)
        if collS == 1:
            bx = bx * -1
            bx = bx * 4
            by = by * 4
            blok4 = False
            blok6 = True

    # Недвиж. объекты
    pygame.draw.rect(sc, (130, 125, 125), (0, 400, 600, 15))
    pygame.draw.rect(sc, (30, 30, 30), (250, 415, 100, 100))
    pygame.draw.rect(sc, (0, 0, 0), (265, 430, 70, 70))

    text4 = f2.render(str(sec), False, (30, 30, 30))
    text5 = f3.render("F", False, (0, 0, 0))
    sc.blit(text4, (265, 435))

    if sec == 0:
        blok = False
        sc.blit(scale, (265, 430))
        pygame.draw.rect(sc, (255, 255, 255), (365, 445, 40, 40))
        sc.blit(text5, (370, 450))
        blok2 = True

    # Все коллизии
    Coll1 = bColl.colliderect(aColl)
    Coll2 = bColl.colliderect(cColl)
    Coll3 = cColl.colliderect(wallColl1)
    Coll4 = cColl.colliderect(wallColl2)
    Coll5 = bColl.colliderect(wallColl3)
    Coll6 = bColl.colliderect(wallColl4)
    Coll7 = bColl.colliderect(wallColl1)
    Coll8 = bColl.colliderect(wallColl2)

    if blok4:
        y2 = y3 - 50

    if not blok4:
        if blokBot:
            y2 += 1
        if y2 == 300:
            blokBot = False
        if not blokBot:
            y2 -= 1
        if y2 == 0:
            blokBot = True

    if Coll3 == 1:
        y = 0

    if Coll4 == 1:
        y = 300

    if Coll2 == 1:
        bx = bx * -1
        if y >= 200:
            bx = 1
            by = -1
        if y < 200:
            bx = 1
            by = 1

        if by >= -0.2 and by <= 0.2:
            by = random.randint(-1, 1)

    if Coll7 == 1:

        rikoshet = random.randint(0, 2)

        if rikoshet == 0:
            by = by * -1
            bx = bx * 2

        if rikoshet == 1:
            by = by * -1

        if rikoshet == 2:
            by = by * -2

    if Coll8 == 1:

        rikoshet2 = random.randint(0, 2)

        if rikoshet2 == 0:
            by = by * -1
            bx = bx * 2

        if rikoshet2 == 1:
            by = by * -1

        if rikoshet2 == 2:
            by = by * -2

    if Coll1 == 1:
        bx = bx * -1
        blokBot = True
        blok = True
        blok2 = False
        blok3 = False
        blok4 = True
        if y2 >= 200:
            bx = 1
            by = -1
        if y2 < 200:
            bx = 1
            by = 1
        if blok6:
            sec = 30
            ms = 101
            blok6 = False
        bx = -1
        by = 1

    if Coll6 == 1:
        blokBot = True
        blok = True
        blok2 = False
        blok3 = False
        blok4 = True
        bx = -1
        by = 1
        y3 = 200
        x3 = 300
        y = 150
        x = 30
        sec = 30
        ms = 101
        blok6 = False
        score += 1

    if Coll5 == 1:
        y3 = 200
        x3 = 300
        y = 150
        x = 30
        bx = -1
        by = 1
        sec = 30
        ms = 101
        score2 += 1

    if score2 == 10:
        Game = False

    if score == 10:
        Game = False

    x3 += bx
    y3 += by

    pygame.display.update()
    pygame.time.delay(3)
