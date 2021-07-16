import pygame as pg
import random


def draw_gametable():
    if len(total_fish) == 0:
        for width in range(70, 520, 90):
            pg.draw.line(display, (255, 255, 255), (width, 370),
                         (width, display_height-30), 3)
            for height in range(370, display_height-30, 80):
                pg.draw.line(display, (255, 255, 255),
                             (70, height), (520, height), 3)
                total_fish.append((width+10, height+10))

        pg.draw.line(display, (255, 255, 255), (520, 370),
                     (520, display_height-30), 3)
        pg.draw.line(display, (255, 255, 255), (70, display_height-30),
                     (520, display_height-30), 3)

    else:
        for width in range(70, 520, 90):
            pg.draw.line(display, (255, 255, 255),
                         (width, 370), (width, display_height-30), 3)
            for height in range(370, display_height-30, 80):
                pg.draw.line(display, (255, 255, 255),
                             (70, height), (520, height), 3)

        pg.draw.line(display, (255, 255, 255),
                     (520, 370), (520, display_height-30), 3)
        pg.draw.line(display, (255, 255, 255),
                     (70, display_height-30), (520, display_height-30), 3)


pg.init()

display_width = 600
display_height = 800

display = pg.display.set_mode((display_width, display_height))

pg.display.set_caption('생선잡기_게임')

background_img = pg.image.load("img/배경.png")
background_img = pg.transform.scale(
    background_img, (display_width, display_height))
display.blit(background_img, (0, 0))

fish_img1 = pg.image.load("img/물고기1.png")
fish_img1 = pg.transform.scale(
    fish_img1, (64, 64))

fish_img2 = pg.image.load("img/물고기2.png")
fish_img2 = pg.transform.scale(
    fish_img2, (64, 64))

fish_img3 = pg.image.load("img/물고기3.png")
fish_img3 = pg.transform.scale(
    fish_img3, (64, 64))

fish_img4 = pg.image.load("img/물고기4.png")
fish_img4 = pg.transform.scale(
    fish_img4, (64, 64))

fish_img5 = pg.image.load("img/물고기5.png")
fish_img5 = pg.transform.scale(
    fish_img5, (64, 64))

fish_img6 = pg.image.load("img/물고기6.png")
fish_img6 = pg.transform.scale(
    fish_img6, (64, 64))

apple_img = pg.image.load("img/apple.png")
apple_img = pg.transform.scale(
    apple_img, (64, 64))

bottle_img = pg.image.load("img/bottle.png")
bottle_img = pg.transform.scale(
    bottle_img, (64, 64))

score_bar = pg.image.load("img/스코어바.png")
score_bar = pg.transform.scale(
    score_bar, (250, 74))

time_bar = pg.image.load("img/시간바.png")
time_bar = pg.transform.scale(
    time_bar, (200, 55))

fish = [fish_img1, fish_img2, fish_img3, fish_img4,
        fish_img5, fish_img6]
trash = [apple_img, bottle_img]
total_fish = []
total_trash = []

draw_gametable()

# 랜덤으로 물고기랑 쓰레기 뿌리는 방법에 대해서 연구하기

pg.display.update()


font = pg.font.SysFont("hy얕은샘물m", 30, True)
Start_time = pg.time.get_ticks()
Catched_fish = 0


while True:
    elapsed_time = round((pg.time.get_ticks() - Start_time) / 1000, 1)

    display.blit(score_bar, (350, 2))
    display.blit(time_bar, (0, 10))

    time = font.render(f"{elapsed_time} sec", True, (0, 0, 0))
    display.blit(time, (60, 28))

    fish_score = font.render(f"{Catched_fish} fish", True, (0, 0, 0))
    display.blit(fish_score, (450, 28))

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
