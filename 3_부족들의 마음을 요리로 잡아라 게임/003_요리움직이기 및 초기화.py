import pygame as pg


def 스프라이트생성(이미지, 위치):
    스프라이트 = pg.sprite.Sprite()
    스프라이트.image = 이미지
    스프라이트.rect = 스프라이트.image.get_rect()
    스프라이트.rect.x, 스프라이트.rect.y = 위치[0], 위치[1]
    return 스프라이트


pg.init()

실행여부 = True
화면가로길이, 화면세로길이 = 874, 800
화면 = pg.display.set_mode([화면가로길이, 화면세로길이])
pg.display.set_caption('부족들의 마음을 요리로 사로잡아라!')

# 색지정
흰색 = (255, 255, 255)
검은색 = (0, 0, 0)

# 글꼴 설정
글꼴 = pg.font.SysFont('malgungothic', 25)

# 게임 요소 초기화
경과시간 = 0
점수 = 0
시계 = pg.time.Clock()
현재챕터 = 1
최종챕터 = 10

자바독상태 = "기본자세"
자바독인덱스 = 0
자바독움직임흐름 = 1
자바독요리가능여부 = True
현재요리 = "사료"
현재요리상태 = '전'
요리움직임여부 = False
이미지마우스위치 = [0, 0]

요리초기위치 = [424, 248]
요리위치 = [요리초기위치[0] - 53, 요리초기위치[1] - 60]

손님가로숫자, 손님세로숫자 = 4, 2

요리상태리스트 = ['전', '후']
요리리스트 = ['사료', '뼈다귀', '물']

배경이미지 = pg.image.load('3_부족들의 마음을 요리로 잡아라 게임/img/배경.png')
배경이미지 = pg.transform.scale(배경이미지, (화면가로길이, 화면세로길이))

챕터바이미지크기 = (358, 61)
챕터바이미지 = pg.image.load('3_부족들의 마음을 요리로 잡아라 게임/img/챕터바.png')
챕터바이미지 = pg.transform.scale(챕터바이미지, 챕터바이미지크기)

자바독이미지크기 = (238, 238)
자바독이미지딕셔너리 = {}
자바독이미지딕셔너리['기본자세'] = pg.image.load('3_부족들의 마음을 요리로 잡아라 게임/img/자바독_기본자세.png')
자바독이미지딕셔너리['기본자세'] = pg.transform.scale(자바독이미지딕셔너리['기본자세'], 자바독이미지크기)

for 요리 in 요리리스트:
    자바독이미지딕셔너리[요리] = []
    for 인덱스 in range(3):
        자바독요리중이미지 = pg.image.load(
            f'3_부족들의 마음을 요리로 잡아라 게임/img/자바독_{요리}_요리중_{인덱스+1}.png')
        자바독요리중이미지 = pg.transform.scale(자바독요리중이미지, 자바독이미지크기)
        자바독이미지딕셔너리[요리].append(자바독요리중이미지)

주방테이블이미지크기 = (668, 173)
주방테이블이미지 = pg.image.load('3_부족들의 마음을 요리로 잡아라 게임/img/주방-테이블.png')
주방테이블이미지 = pg.transform.scale(주방테이블이미지, 주방테이블이미지크기)

요리이미지크기딕셔너리 = {'사료': (106, 61), '뼈다귀': (106, 61), '물': (106, 61)}
요리이미지딕셔너리 = {}

for 요리상태 in 요리상태리스트:
    요리이미지딕셔너리[요리상태] = {}
    for 요리 in 요리리스트:
        요리이미지딕셔너리[요리상태][요리] = pg.image.load(
            f'3_부족들의 마음을 요리로 잡아라 게임/img/{요리}_요리{요리상태}.png')
        요리이미지딕셔너리[요리상태][요리] = pg.transform.scale(
            요리이미지딕셔너리[요리상태][요리], 요리이미지크기딕셔너리[요리])

요리스프라이트 = 스프라이트생성(요리이미지딕셔너리['전'][현재요리], 요리위치)

동족이미지크기 = (185, 265)
동족음식생각중이미지 = pg.image.load('3_부족들의 마음을 요리로 잡아라 게임/img/동족_음식-생각-중.png')
동족음식생각중이미지 = pg.transform.scale(동족음식생각중이미지, 동족이미지크기)

동족스프라이트리스트 = [스프라이트생성(동족음식생각중이미지, (85+동족이미지크기[0]*j, 320+동족이미지크기[1]*i))
              for i in range(손님세로숫자) for j in range(손님가로숫자)]

이미지움직임최대시간 = 0.2
이미지움직임시간 = 0
움직임최대횟수 = 3
움직임횟수 = 0

while 실행여부:
    if 현재챕터 <= 최종챕터:
        화면.blit(배경이미지, (0, 0))
        흐른시간 = 시계.tick(60) / 1000
        경과시간 += 흐른시간
        시간문자열 = '%02d:%02d' % (경과시간/60, 경과시간 % 60)
        경과시간글자 = 글꼴.render(시간문자열, True, 검은색)
        화면.blit(챕터바이미지, (화면가로길이 - 챕터바이미지크기[0] * 1.7, 7))
        화면.blit(경과시간글자, (20, 20))

        챕터문자열 = f'{현재챕터}챕터'
        챕터글자 = 글꼴.render(챕터문자열, True, 흰색)
        화면.blit(챕터글자, ((화면가로길이 - 14 * len(챕터문자열)) // 2 - 19, 20))

        점수문자열 = f'{점수}챕터'
        점수글자 = 글꼴.render(점수문자열, True, 검은색)
        화면.blit(점수글자, ((화면가로길이 - 14 * len(점수문자열)) - 30, 20))

        if 자바독상태 == '기본자세':
            화면.blit(자바독이미지딕셔너리[자바독상태], (321, 55))
        else:
            화면.blit(자바독이미지딕셔너리[자바독상태][자바독인덱스], (321, 55))

        화면.blit(주방테이블이미지, (100, 162))

        for 동족스프라이트 in 동족스프라이트리스트:
            화면.blit(동족스프라이트.image, 동족스프라이트.rect)

        요청요리리스트 = {}

        for 인덱스, 요리 in enumerate(요리리스트):
            요청요리리스트[요리] = 화면.blit(요리이미지딕셔너리['후'][요리], (460 + 90 * 인덱스,
                                                       250 - 요리이미지딕셔너리["후"][요리].get_height()))

        요리스프라이트.image = 요리이미지딕셔너리[현재요리상태][현재요리]

        if 자바독요리가능여부:
            요리위치 = [요리초기위치[0] - 요리스프라이트.image.get_width() // 2,
                    요리초기위치[1] - 요리스프라이트.image.get_height() // 1.05]
        요리스프라이트.rect.x, 요리스프라이트.rect.y = 요리위치[0], 요리위치[1]
        진행중인요리 = 화면.blit(요리스프라이트.image, 요리스프라이트.rect)

        if 요리움직임여부:
            마우스위치 = pg.mouse.get_pos()
            요리위치 = [마우스위치[0] + 이미지마우스위치[0], 마우스위치[1] + 이미지마우스위치[1]]

    else:
        화면.fill(흰색)

    pg.display.update()

    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            실행여부 = False
        elif 이벤트.type == pg.MOUSEBUTTONDOWN:
            클릭위치 = pg.mouse.get_pos()
            if 진행중인요리.collidepoint(클릭위치):
                요리움직임여부 = True
                자바독요리가능여부 = False
                이미지마우스위치 = [요리위치[0] - 클릭위치[0], 요리위치[1] - 클릭위치[1]]

            for 요리 in 요리리스트:
                if 요청요리리스트[요리].collidepoint(클릭위치):
                    현재요리 = 요리
                    현재요리상태 = '전'
                    자바독요리가능여부 = True
        elif 이벤트.type == pg.MOUSEBUTTONUP:
            요리움직임여부 = False

    keys = pg.key.get_pressed()

    if keys[pg.K_SPACE] and 자바독요리가능여부:
        if 자바독상태 == "기본자세":
            자바독상태 = 현재요리
        else:
            이미지움직임시간 += 흐른시간
            if 이미지움직임시간 >= 이미지움직임최대시간:
                이미지움직임시간 = 0
                자바독인덱스 += 자바독움직임흐름
                if 자바독인덱스 == 0 or 자바독인덱스 == len(자바독이미지딕셔너리[자바독상태]) - 1:
                    자바독움직임흐름 *= -1
                    움직임횟수 += 1
                    if 움직임횟수 >= 움직임최대횟수:
                        현재요리상태 = '후'
    else:
        이미지움직임시간 = 0
        자바독상태 = "기본자세"
        자바독인덱스 = 0
        자바독움직임흐름 = 1
        움직임횟수 = 0


pg.display.quit()
