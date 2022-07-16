import sys
import pygame
import random
from pygame.locals import QUIT , Rect , KEYDOWN ,\
    K_LEFT , K_RIGHT , K_UP , K_DOWN
 


pygame.init()
pygame.key.set_repeat(5,5)
배경 = pygame.display.set_mode((600,600))   # 화면 크기 
클릭 = pygame.time.Clock()
font = pygame.font.SysFont("arrial",30,True,True)
over_text = font.render("game over", True, (255,255,255))
clear_text = font.render("game clear", True, (255,255,255))
foods = []
def 먹이만들기():
    while True:
        pos = [random.randint(0,10) , random.randint(0.,10)]
        if pos in foods:
            continue
        foods.append(pos)
        break

def 먹이그리기():
    for i in foods:
        pygame.draw.rect(배경, (255,200,200), (i[0]*30, i[1]*30,30,30))


earthworms = [[10,10]]
def 지렁이그리기():
    for i in earthworms:
        pygame.draw.rect(배경 , (0,200,200), (i[0]*30,i[1]*30,30,30))


def 라인그리기():
    for x in range(0,20):
        pygame.draw.line(배경 , (255, 255 , 255) , (x*30,0) , (x*30,600) , 3)
    pygame.draw.line(배경 , (255, 255 , 255) , (0,30) , (600,30) , 3)
    for y in range(0,20):
        pygame.draw.line(배경 , (255, 255 , 255) , (0,y*30) , (600,y*30) , 3)

def main():
    for i in range(400):
        먹이만들기()



def main():
    key = K_DOWN
    for i in range(10):
        먹이만들기()
    while True:
        배경.fill((0,0,0))      # 배경색에 대한 변경(빨강,초록,파랑 순)
        for event in pygame.event.get():      #여러가지 이벤트들
            if event.type == QUIT:            # 이벤트의 종류가 종료라면 파이게임을 그만두고 sys(시스템) 종료
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key           # KEYDOWN 이벤트 == 아래


        if key == K_DOWN:
            head = [earthworms[0][0] ,earthworms[0][1]+1]  # 만약  a = [23,21] 23을 부르고 싶다면 0번째 칸 안에 있는 첫번째 [0][1]이 된다.
        elif key == K_UP:
            head = [earthworms[0][0],earthworms[0][1]-1]
        elif key == K_LEFT:
            head = [earthworms[0][0]-1,earthworms[0][1] ]
        elif key == K_RIGHT:
            head = [earthworms[0][0]+1,earthworms[0][1] ]

        
        earthworms.insert(0,head)
        if not head in foods:
            earthworms.pop()
        else:
            del foods[foods.index(head)]
            먹이만들기()
            if len(earthworms) == 20:
                배경.blit(clear_text, (250,300))
                pygame.display.update()
                pygame.time.delay(2000)
                pygame.quit()
                sys.exit()
        
        if head[0] < 0 or head[0] > 20 or head[1] < 0 or head[1] > 20:
            배경.blit(over_text, (250,300))
            pygame.display.update()
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()

        먹이그리기()
        라인그리기()    # 지렁이의 몸통(선) 내려가야 y좌표가 커진다.
        지렁이그리기()

        pygame.display.update()
        클릭.tick(5)

main()