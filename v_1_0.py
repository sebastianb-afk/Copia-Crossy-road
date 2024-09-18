import pygame
import random

class Car:
    def __init__(self,x,y,w,h,s):
        self.rect = pygame.Rect(x,y,w,h)
        self.speed = s
        self.direction = random.choice([-1,1])
    def move(self,a,u):
        self.rect.x += self.speed*self.direction
        if self.rect.left <= 0:
            self.direction = 1  
        elif self.rect.right >= a:
            self.direction = -1
    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)

class Solid_object:
    def __init__(self,x,y,w,h):
        self.rect = pygame.Rect(x,y,w,h)
    def draw(self,surface, color):
        pygame.draw.rect(surface, color, self.rect)

def cars_generator(w,h,u,s):
    v_p = []
    h_p = []
    obs = []
    for i in range(h):
        if i%2 != 0:
            v_p.append(i*u)
    for i in v_p:
        h_p.append(random.randrange(w-1)*u)
    for i in range(len(v_p)):
        obs.append(Car(h_p[i],v_p[i],u,u,s))
    return obs

def objects_generator(w,h,u):
    v_p = []
    h_p = []
    obs = []
    for i in range(h-1):
        if i%2 == 0 and i != 0:
            v_p.append(i*u)
    for i in range(w):
        h_p.append(i*u)
    for i in range(len(v_p)):
        av_pos = h_p[:]
        if len(av_pos) >= 3:
            start_idx = random.randint(0, len(av_pos)-3)
            del av_pos[start_idx:start_idx + 3]
            for j in av_pos:
                obs.append(Solid_object(j, v_p[i], u, u))
    return obs

def no_move():
    keys = pygame.key.get_pressed()
    if not (keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]):
        return True 
    else:
        return False 

typo = False
if typo:
    unit = 25
    dif = 2
    width = 32
    height = 24
if not typo:
    unit = 75
    dif = 2
    width = 16
    height = 12

size = width * unit, height * unit
initial_bg_values = (0, 0, 0)
grid_color = (50, 50, 50)

player_dimensions = (0, 0, unit, unit)
goal_dimensions = (0, unit*(height-1), width * unit, unit)

pygame.init()

screen = pygame.display.set_mode(size)
player = pygame.Rect(player_dimensions)
goal = pygame.Rect(goal_dimensions)
cars = cars_generator(width,height,unit,dif)
objs = objects_generator(width,height,unit)

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

pygame.display.set_caption("Crossy Road")
prev_pos = player.topleft

move = True
run = True
goalr = False

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if goalr:

        screen.fill(initial_bg_values)

        for x in range(0, width*unit, unit):
            pygame.draw.line(screen, grid_color, (x, 0), (x, height*unit))
        for y in range(0, height*unit, unit):
            pygame.draw.line(screen, grid_color, (0, y), (width*unit, y))

        text_WIN = font.render("Q quit R reset M menu", True, (255, 255, 255))
        text_rect = text_WIN.get_rect(x=int(width*unit/2),y=int(height*unit/2))
        screen.blit(text_WIN, text_rect)

        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            player.topleft = (0, 0)
            goalr = False
        if keys[pygame.K_q]:
            run = False

        continue

    if no_move():
            move = True

    key = pygame.key.get_pressed()
    if move:
        if key[pygame.K_a] == True:
            player.x-=unit
            move = False
        if key[pygame.K_d] == True:
            player.x+=unit
            move = False
        if key[pygame.K_w] == True:
            player.y-=unit
            move = False
        if key[pygame.K_s] == True:
            player.y+=unit
            move = False

    player.x = max(0, min(width*unit - player.width, player.x))
    player.y = max(0, min(height*unit - player.height, player.y))

    if not any(player.colliderect(obj.rect) for obj in objs):
        prev_pos = player.topleft
    if any(player.colliderect(obj.rect) for obj in objs):
        player.topleft = prev_pos
    if any(player.colliderect(car.rect) for car in cars):
        player.topleft = (0,0)

    if player.colliderect(goal):
        goalr=True

    screen.fill(initial_bg_values)

    for x in range(0, width*unit, unit):
        pygame.draw.line(screen, grid_color, (x, 0), (x, height*unit))
    for y in range(0, height*unit, unit):
        pygame.draw.line(screen, grid_color, (0, y), (width*unit, y))
        
    for obj in objs:
        obj.draw(screen,(255,0,0))

    for car in cars:
        car.draw(screen,(0,0,255))
        car.move(width*unit, unit)

    pygame.draw.rect(screen, (0,255,0), player)

    pygame.draw.rect(screen, (255,255,255), goal)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
