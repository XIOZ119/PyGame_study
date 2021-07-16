import pygame as pg 

pg. init()

화면가로길이 = 600
화면세로길이 = 800

화면 = pg.display.set_mode((화면가로길이, 화면세로길이))

pg.display.set_caption('생성잡기_게임')

배경이미지 = pg.image.load("img/배경.png")
배경이미지 = pg.transform.scale(배경이미지, (화면가로길이, 화면세로길이))

화면.blit(배경이미지, (0,0))
pg.display.update()

while True:
    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            quit()