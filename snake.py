import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

class Player():
    def __init__(self, x, y):
        self.rect = pygame.rect.Rect(x, y, 20, 20)
        self.LEFT = False
        self.RIGHT = False
        self.UP = False
        self.DOWN = False
        self.prev_pos = [self.rect.x, self.rect.y]
        self.tail = []

    def update(self, surface):
        global SCORE
        if self.UP:
            self.prev_pos = [self.rect.x, self.rect.y]
            self.rect.y -= 20
        if self.DOWN:
            self.prev_pos = [self.rect.x, self.rect.y]
            self.rect.y += 20
        if self.LEFT:
            self.prev_pos = [self.rect.x, self.rect.y]
            self.rect.x -= 20
        if self.RIGHT:
            self.prev_pos = [self.rect.x, self.rect.y]
            self.rect.x += 20
        
        self.prev_rect = pygame.rect.Rect(self.prev_pos[0], self.prev_pos[1], 20, 20)

        for t in self.tail:
            t.update(screen)
            if t.rect.colliderect(self.rect):
                print("score:",SCORE)
                pygame.quit()
                sys.exit()

        if self.rect.right<0 or self.rect.left>600 or self.rect.bottom<0 or self.rect.top>600:
            print("score:",SCORE)
            pygame.quit()
            sys.exit()
        


        pygame.draw.rect(screen, (0,255,0), self.rect)
        # pygame.draw.rect(screen, (0,255,0), self.prev_rect)

class Tail():
    def __init__(self, parent, x, y):
        self.rect = pygame.rect.Rect(x, y, 20, 20)
        self.LEFT = False
        self.RIGHT = False
        self.UP = False
        self.DOWN = False
        self.prev_pos = [self.rect.x, self.rect.y]
        self.parent = parent
    
    def update(self, surface):
        self.prev_pos = [self.rect.x,self.rect.y]
        self.rect.x = self.parent.prev_pos[0]
        self.rect.y = self.parent.prev_pos[1]
        pygame.draw.rect(screen, (0,255,0), self.rect, 2)

class Apple():
    def __init__(self, x, y):
        self.rect = pygame.rect.Rect(x, y, 20, 20)
    
    def update(self, surface):
        global SCORE
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 0)
        if self.rect.colliderect(p.rect):
            SCORE += 1
            if len(p.tail)==0:
                p.tail.append(Tail(p,0,0))
            else:
                p.tail.append(Tail(p.tail[len(p.tail)-1],0,0))
            aGroup.append(Apple(randint(0,29)*20,randint(0,29)*20))
            if SCORE >= 10:
                aGroup.append(Apple(randint(0,20)*20,randint(0,20)*20))
            if SCORE >= 20:
                aGroup.append(Apple(randint(0,20)*20,randint(0,20)*20))
            if SCORE >= 30:
                aGroup.append(Apple(randint(0,20)*20,randint(0,20)*20))

            aGroup.remove(self)

SCORE = 0

def main():
    global SCORE
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_a] or key[pygame.K_LEFT]:
                p.LEFT = True
                p.RIGHT = False
                p.UP = False
                p.DOWN = False
            if key[pygame.K_d] or key[pygame.K_RIGHT]:
                p.LEFT = False
                p.RIGHT = True
                p.UP = False
                p.DOWN = False
            if key[pygame.K_w] or key[pygame.K_UP]:
                p.LEFT = False
                p.RIGHT = False
                p.UP = True
                p.DOWN = False
            if key[pygame.K_s] or key[pygame.K_DOWN]:
                p.LEFT = False
                p.RIGHT = False
                p.UP = False
                p.DOWN = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
    
    screen.fill((20,20,20))


    for a in aGroup:
        a.update(screen)

    p.update(screen)
    
    pygame.display.update()

eGroup = []
aGroup = []
p = Player(60,60)
a = Apple(randint(0,20)*20,randint(0,20)*20)
aGroup.append(a)

while True:
    main()
    clock.tick(10)
    pygame.display.set_caption(f"SCORE: {SCORE}")