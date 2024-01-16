import pygame
pygame.init()

back = (0, 255, 245)
win = pygame.display.set_mode((500, 500))
win.fill(back)
cloxk = pygame.time.Clock()
pl_x=200
pl_y=330
m_s = 5

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(win, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Picture(Area):
    def __init__(self, filename, x, y, width, height):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

miachik_sp_x=5
miachik_sp_y=5

miachik = Picture("ball_1615463127.png", 160, 200, 50, 50)
platform = Picture("platform.png", pl_x, pl_y, 100, 30)

monster_x=5
monster_y=5
count = 9
monsters = list()

for s in range(3):
    y = monster_y+(55*s)
    x = monster_x+(28*s)
    for i in range(count):
        monster=Picture('659d711a8c3cb.png',x,y,50,50)
        monsters.append(monster)
        x=x+55
    count=count-1


game_over=False
while not game_over:

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform.rect.x>0:
        platform.rect.x-=10
    if keys[pygame.K_RIGHT] and platform.rect.x<400:
        platform.rect.x+=10

    


    miachik.rect.x+=miachik_sp_x
    miachik.rect.y+=miachik_sp_y
    
    if miachik.rect.x <=0 or miachik.rect.x >=500:
        miachik_sp_x = -miachik_sp_x
    if miachik.rect.y  <=0:
        miachik_sp_y = -miachik_sp_y
    
    win.fill(back)

    for m in monsters:
        m.draw()
    for m in monsters:
        if miachik.rect.colliderect(m.rect):
            monsters.remove(m)
            miachik_sp_y *= -1
    
    miachik.draw()
    platform.draw()
    
    if miachik.rect.colliderect(platform.rect):
        miachik_sp_y*=-1

    if miachik.rect.y>500:
        fontb=pygame.font.Font(None, 40)
        tunt=fontb.render('Найс трай',  True,(255, 50,25 ))
        win.blit(tunt,(200, 250))
        pygame.display.update()   
        game_over = True 
    if monsters == []:
        fontb=pygame.font.Font(None, 40)
        tunt=fontb.render('Atata iiiii ta naaa!!!',  True,(255, 50,25 ))
        win.blit(tunt,(200, 250))
        pygame.display.update()
        game_over = True 
    pygame.display.update()
    cloxk.tick(40)
