import pygame
def inter(x1,y1,x2,y2,db1,db2):
    if x1>x2-db1 and x1 < x2+db2 and y1 > y2-db1 and y1 <y2+db2:
        return 1
    else:
        return 0
pygame.init()
window=pygame.display.set_mode((400,400))
screen=pygame.Surface((400,400))
player=pygame.Surface((40,40))
zet=pygame.Surface((40,40))
arrow=pygame.Surface((40,40))
count=0
player.set_colorkey((0,0,0))
arrow.set_colorkey((0,0,0))
zet.set_colorkey((0,0,0))
img_a=pygame.image.load('src/a.png')
img_b=pygame.image.load('src/b.png')
img_p=pygame.image.load('src/p.png')
myfont=pygame.font.SysFont('monospase', 15)
a_x=1000
a_y=1000
strike=False
z_x=0
z_y=0
x_p=0
y_p=360
right=True
done=False
while done==False:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            done=True
        if e.type==pygame.KEYDOWN and e.key==pygame.K_s:
            y_p+=4
        if e.type==pygame.KEYDOWN and e.key==pygame.K_w:
            y_p-=4
        if e.type==pygame.KEYDOWN and e.key==pygame.K_a:
            x_p-=4
        if e.type==pygame.KEYDOWN and e.key==pygame.K_d:
            x_p+=4
        if e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE:
            if strike == False:
                strike = True
                a_x = x_p
                a_y = y_p - 40
    if strike:
        a_y-=0.5
        if a_y < 0:
            strike=False
            a_y=1000
            a_x=1000
    if inter(a_x,a_y,z_x,z_y,20,1):
        count+=1
        strike=False
        a_y=1000
        a_x=1000
    if right:
        z_x+=0.1
        if z_x > 400:
            z_x -= 1
            right=False
    else:
        z_x-=0.07
        if z_x < 0:
            z_x+=1
            right=True
    string=myfont.render('Очков: '+str(count),0,(255,0,0))
    screen.fill((0,255,0))
    arrow.blit(img_a,(0,0))
    player.blit(img_p,(0,0))
    zet.blit(img_b,(0,0))
    screen.blit(string,(0,50))
    screen.blit(arrow,(a_x,a_y))
    screen.blit(zet,(z_x,z_y))
    screen.blit(player,(x_p,y_p))
    window.blit(screen,(0,0))
    pygame.display.update()
pygame.quit()
