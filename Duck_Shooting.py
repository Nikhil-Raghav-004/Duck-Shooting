import pygame


pygame.init()

width = 1000
height = 600
Score = 0

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
Target.topleft = (100,360)
Speed = 3

Shot_rect = Ducky_Shot.get_rect()

RIFLEE = pygame.image.load("assets/Objects/rifle.png")
RIFLEE = pygame.transform.scale(RIFLEE,(90,150))

RIFLEE_rect = RIFLEE.get_rect()
clock = pygame.time.Clock()


Cloud1 = pygame.image.load("assets/Stall/cloud2.png").convert_alpha()
Cloud1 = pygame.transform.scale(Cloud1,(90,50))
Cloud1.set_alpha(200)

bullet_list = []

# global Bullet_rect
# Bullet_rect = Bullet
running = True
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
                Bullet_rect = Bullet.get_rect()
                Bullet_rect.midbottom = RIFLEE_rect.midtop
                bullet_list.append(Bullet_rect)


    screen.blit(Bg,(0,0))

    Target.x += Speed
    if Target.right >= width or Target.left <= 0:
        Speed*= -1
    Target2.x += speed
    if Target2.right >= width or Target2.left <= 0:
        speed *= -1


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
    for b in bullet_list[:]:
        b.y -= 3

        if b.colliderect(Target):
            bullet_list.remove(b)
            Shot_rect.center = Target.center
            screen.blit(Ducky_Shot, Shot_rect)
            Score += 1

        if b.colliderect(Target2):
            bullet_list.remove(b)
            Shot_rect.center = Target2.center
            screen.blit(Ducky_Shot, Shot_rect)
            Score += 3





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


    text = font.render(f"Score : {Score}", True,'white')
    screen.blit(text,(0,0))

    for i in bullet_list:
        screen.blit(Bullet,i)
    clock.tick(60)
    pygame.display.flip()
