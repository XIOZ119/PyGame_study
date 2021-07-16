import pygame as pg


def 게임종료():
    화면.blit(배경이미지, (0, 0))
    결과 = 폰트.render(f'Total {잡은물고기} fish Catched!', True, (0, 0, 0))
    게임종료 = 폰트.render(f'Game End!', True, (0, 0, 0))
    화면.blit(게임종료, (230, 400))
    화면.blit(결과, (170, 550))
    pg.display.update()
    pg.time.delay(5000)
    quit()
