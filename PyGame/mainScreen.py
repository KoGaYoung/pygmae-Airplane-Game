import pygame, sys
import math
from pygame.locals import *
from random import *
from ball import *
from player import *

SCREEN_WIDTH = 300
SCREEN_HEIGHT= 300

pygame.init()
pygame.display.set_caption('Main_Screen')
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#프레임마다 몇 밀리세컨 걸렸는지 계산하는 시계
clock = pygame.time.Clock()

def main():
    player = Player()
    numBall=5
    ballList = []
    for i in range(numBall):
        ballList.append(Ball())
    saveKey = [False, False, False, False]
#    score = 0

 # main game loop
    while True:
        elapsed = clock.tick(30)
        #score += elapsed

        #키가 눌려있을 때 동시키 입력할 수 있도록
        for event in pygame.event.get():
            if(event.type == KEYDOWN):
                if event.key == K_a:
                    saveKey[0] = True
                if event.key == K_d:
                    saveKey[1] = True
                if event.key == K_w:
                    saveKey[2] = True
                if event.key == K_s:
                    saveKey[3] = True
            elif(event.type == KEYUP):
                if event.key == K_a:
                    saveKey[0] = False
                if event.key == K_d:
                    saveKey[1] = False
                if event.key == K_w:
                    saveKey[2] = False
                if event.key == K_s:
                    saveKey[3] = False


        min = 10000
        ball = ballList[0]
        a = 0
        b = 0
        for i in range (5) :
            a = player.x - ballList[i].x
            b = player.y - ballList[i].y
            c = math.sqrt((a * a ) + (b * b)) #제곱근구하기
            if( c < min ):
                min = c
                ball = ballList[i]


        saveKey[0] = ball.x > player.x
        saveKey[1] = ball.x < player.x
        saveKey[2] = ball.y < player.y
        saveKey[3] = ball.y > player.y

        #눌린 키에 따라 비행기 이동
        # true IF condition ELSE false
        if (saveKey[0]) :
            player.x = player.x - 5 if player.x - 5 > 0 else player.x
        elif (saveKey[1]) :
            player.x = player.x + 5 if player.x + 5 < SCREEN_WIDTH else player.x
        if (saveKey[2]) :
            player.y = player.y - 5 if player.y - 5 > 0 else player.y
        elif (saveKey[3]) :
            player.y = player.y + 5 if player.y + 5 < SCREEN_HEIGHT else player.y;


        #게임종료
        if event.type == pygame.QUIT:
            sys.exit()

        #화면 초기화
        screen.fill((0,0,0))
        player.draw(screen)
        for i in range(numBall):
            ballList[i].draw(screen)
        #text = str(score)
        #label = pygame.font.Font(None, 64).render(text, 1, (0, 0, 250))
        #screen.blit(label, (100, 100))
        pygame.display.update()

if __name__ == "__main__":
    main()
