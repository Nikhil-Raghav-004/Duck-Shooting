import pygame
import time

pygame.init()

width = 1000
height = 600
Score = 0
Life =  3
Bullet_No = 10
font = pygame.font.SysFont('Papyrus',50)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame basics")

Bg = pygame.image.load("assets/Stall/bg_wood.png")
Bg = pygame.transform.scale(Bg,(width,height))

Curtain1 =  pygame.image.load("assets/Stall/curtain.png")
Curtain1 = pygame.transform.scale(Curtain1,(100,500))

Curtain2 = pygame.transform.flip(Curtain1,True,False)
Curtain_Top = pygame.image.load("assets/Stall/curtain_straight.png")

Water = pygame.image.load("assets/Stall/water1.png")
Water_2 = pygame.image.load("assets/Stall/water2.png")

Ducky1 = pygame.image.load("assets/Objects/duck_yellow.png")
Ducky1 = pygame.transform.scale(Ducky1,(60,60))

Ducky2 = pygame.image.load("assets/Objects/duck_white.png")
Ducky2 = pygame.transform.scale(Ducky2,(30,30))

Life_Less_Duck = pygame.image.load("assets/Objects/duck_brown.png")
Life_Less_Duck = pygame.transform.scale(Life_Less_Duck,(80,80))

Ducky_Shot = pygame.image.load("assets/Objects/shot_yellow_large.png")
Ducky_Shot = pygame.transform.scale(Ducky_Shot,(10,10))

Shot_Brown = pygame.image.load("assets/Objects/shot_brown_large.png")
Shot_Brown = pygame.transform.scale(Shot_Brown,(20,20))

Bullet = pygame.image.load("assets/HUD/icon_bullet_gold_short.png")
Bullet = pygame.transform.scale(Bullet,(10,20))



Target2 = Ducky2.get_rect()
Target2.topleft = (100,450)
speed = 5
Target = Ducky1.get_rect()
Target.topleft = (100,300)
Speed = 3

Target_Life = Life_Less_Duck.get_rect()
Target_Life.topleft = (100,360)
speeed = 8

Shot_rect = Ducky_Shot.get_rect()

Score_New = pygame.image.load("assets/HUD/text_score_small.png")
# Score_New = pygame.transform.scale(Score_New)

Colon = pygame.image.load("assets/HUD/text_dots_small.png")

RIFLEE = pygame.image.load("assets/Objects/rifle.png")
RIFLEE = pygame.transform.scale(RIFLEE,(90,150))

RIFLEE_rect = RIFLEE.get_rect()
clock = pygame.time.Clock()

Score_NoLis = ["text_0_small.png","text_1_small.png","text_2_small.png","text_3_small.png","text_4_small.png","text_5_small.png","text_6_small.png","text_7_small.png","text_8_small.png","text_9_small.png"]



Cloud1 = pygame.image.load("assets/Stall/cloud2.png").convert_alpha()
Cloud1 = pygame.transform.scale(Cloud1,(90,50))
Cloud1.set_alpha(200)

bullet_list = []

# global Bullet_rect
# Bullet_rect = Bullet
running = True

def Score_Plus(No_Up):
    Path = "assets/HUD/" + Score_NoLis[No_Up]
    Img = pygame.image.load(Path)
    No = pygame.image.load("assets/HUD/text_plus_small.png")
    screen.blit(No,(290,23))
    screen.blit(Img,(310,23))
    # time.sleep(2)

def Display_Life(Life):
    font = pygame.font.SysFont("Papyrus",50)
    font.set_bold(True)
    text = font.render(f'Lives: {Life}',True,'#B8AFC7')
    screen.blit(text,(820,2))



def Display_Score(Score):
    screen.blit(Score_New,(58,25))
    screen.blit(Colon,(170,30))
    Digits = str(Score)
    Space = 190
    for i in Digits:
        Path = "assets/HUD/" + Score_NoLis[int(i)]
        Img = pygame.image.load(Path)
        screen.blit(Img,(Space,25))
        Space += 25

def Display_Gameover():
    Game_Over = pygame.image.load("assets/HUD/text_gameover.png")
    Game_Over = pygame.transform.scale(Game_Over,(200,100))
    screen.blit(Game_Over,(400,250))

while running:
    RIFLEE_rect.midbottom = (461,680)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         Bullet_rect = Bullet.get_rect()
        #         Bullet_rect.midbottom = RIFLEE_rect.midtop
        #         bullet_list.append(Bullet_rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 :
                Bullet_No -= 1
                Bullet_rect = Bullet.get_rect()
                Bullet_rect.midbottom = RIFLEE_rect.midtop
                if len(bullet_list) <= Bullet_No+6:
                    bullet_list.append(Bullet_rect)


    screen.blit(Bg,(0,0))

    Target.x += Speed
    if Target.right >= width or Target.left <= 0:
        Speed*= -1
    Target2.x += speed
    if Target2.right >= width or Target2.left <= 0:
        speed *= -1
    Target_Life.x += speeed
    if Target_Life.right >= width or Target_Life.left <= 0:
        speeed*= -1


    b = 40
    for j in range(8):
        screen.blit(Water_2, (b, 350))
        b = b + 132
    b = 0
    for j in range(8):
        screen.blit(Water, (b, 400))
        b = b+132

    screen.blit(Curtain1,(0,0))
    screen.blit(Curtain2, (900, 0))
    # screen.blit(Curtain_Top,(0,0))

    a =0
    for i in range(4):
        screen.blit(Curtain_Top,(a,0))
        a = a+256
    screen.blit(Ducky1, Target)
    screen.blit(Ducky2,Target2)
    screen.blit(Life_Less_Duck,Target_Life)
    for b in bullet_list[:]:
        b.y -= 3

        if b.colliderect(Target):
            bullet_list.remove(b)
            Shot_rect.center = Target.center
            screen.blit(Ducky_Shot, Shot_rect)
            Score += 1
            Score_Plus(1)

        if b.colliderect(Target2):
            bullet_list.remove(b)
            Shot_rect.center = Target2.center
            screen.blit(Ducky_Shot, Shot_rect)
            Score += 3
            Score_Plus(3)

        if b.colliderect(Target_Life):
            bullet_list.remove(b)
            Shot_rect.center = Target_Life.center
            screen.blit(Ducky_Shot, Shot_rect)
            Life -= 1
            if Life == 0:
                Display_Gameover()
                pygame.time.wait(3000)
                running = False




    # screen.blit(Ducky_Shot, Shot_rect)


    screen.blit(RIFLEE,(450,500))

    screen.blit(Cloud1, (100, 100))
    screen.blit(Cloud1, (200, 140))
    screen.blit(Cloud1, (300, 100))
    screen.blit(Cloud1, (430, 200))
    screen.blit(Cloud1, (430, 110))
    screen.blit(Cloud1, (540, 120))
    screen.blit(Cloud1, (650, 60))
    screen.blit(Cloud1, (650, 140))
    screen.blit(Cloud1, (760, 100))
    screen.blit(Cloud1, (850, 110))


    text = font.render(f"Score : ", True,'white')

    # screen.blit(text,(0,0))
    Display_Score(Score)
    Display_Life(Life)

    for i in bullet_list:
        screen.blit(Bullet,i)
    clock.tick(60)
    pygame.display.flip()
