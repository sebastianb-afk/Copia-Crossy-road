import pygame
import random

class Car:
    def __init__(self,x,y,w,h,s):
        self.rect = pygame.Rect(x,y,w,h)
        self.speed = s
        self.direction = random.choice([-1,1])
        azules = [(173, 216, 230), (0, 0, 255), (0, 0, 139)]
        self.color = random.choice(azules)
    def move(self,a,u):
        self.rect.x += self.speed*self.direction
        if self.rect.left <= 0:
            self.direction = 1  
        elif self.rect.right >= a:
            self.direction = -1
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Solid_object:
    def __init__(self,x,y,w,h):
        self.rect = pygame.Rect(x,y,w,h)
        colores = [(192, 192, 192), (128, 128, 128), (95, 95, 95)]
        self.color = random.choice(colores)
    def draw(self,surface):
        pygame.draw.rect(surface, self.color, self.rect)

def cars_generator(w,h,u,s):
    v_p = []
    h_p = []
    obs = []
    for i in range(h-2):
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

pygame.init()

stocky = 'C:/Users/jsbui/Documents/Visual_Python/Proyecto_Kod/stocky.ttf'
size = 800, 600
initial_bg_values = (0, 0, 0)
grid_color = (50, 50, 50)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Crossy Road")

clock = pygame.time.Clock()
font = pygame.font.Font(stocky, 26)

run = True
Menu_Status = True
Settings_Status = False
Game_Status = False

Setter  = True
typoc = True
typo = True
speedo = True
speedoc = True
move = True
goalr = False

while run:

    if typo:
        unit = 25
        width = 32
        height = 24

    if not typo:
        unit = 50
        width = 16
        height = 12

    if speedo:
        dif = 2
    if not speedo:
        dif = 4    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if Menu_Status:

        lila1 = (200, 162, 200)
        lila2 = (220, 190, 220)

        tile = 10

        a, l = size[1], size[0]

        screen.fill(initial_bg_values)

        for row in range(0, a // tile):
            for col in range(0, l // tile):
                if (row + col) % 2 == 0:
                    color = lila1
                else:
                    color = lila2

                pygame.draw.rect(screen, color, (col * tile, row * tile, tile, tile))

        title_font = pygame.font.Font(stocky, 72)
        text_Menu = title_font.render("Escape!", True, (0, 0, 0))
        text_rect = text_Menu.get_rect(center=(screen.get_width() // 2, 150))
        screen.blit(text_Menu, text_rect)

        font_options = pygame.font.Font(stocky, 48)
        text_options = font_options.render("O - Opciones", True, (0, 0, 0))
        text_options_rect = text_options.get_rect(center=(screen.get_width() // 2, 350))
        screen.blit(text_options, text_options_rect)

        text_play = font_options.render("P - Jugar", True, (0, 0, 0))
        text_play_rect = text_play.get_rect(center=(screen.get_width() // 2, 300))
        screen.blit(text_play, text_play_rect)

        keym = pygame.key.get_pressed()
        if keym[pygame.K_o]:
            Menu_Status = False
            Settings_Status = True
        if keym[pygame.K_p]:
            Menu_Status = False
            Game_Status = True

    if Settings_Status:

        lila3 = (75, 0, 130)
        lila4 = (102, 51, 153)

        tile = 10

        a, l = size[1], size[0]

        screen.fill(initial_bg_values)

        for row in range(0, a // tile):
            for col in range(0, l // tile):
                if (row + col) % 2 == 0:
                    color = lila3
                else:
                    color = lila4

                pygame.draw.rect(screen, color, (col * tile, row * tile, tile, tile))

        if typo:
            tipo_size = 25
        if not typo:
            tipo_size = 50
        if speedo:
            speed_text = "I"
        if not speedo:
            speed_text = "III"

        text_tipo = font.render(f"Bloque actual:", True, (255, 255, 255))
        text_rect_tipo = text_tipo.get_rect(x=25, y=200)
        screen.blit(text_tipo, text_rect_tipo)

        square_color = (255, 0, 0)
        pygame.draw.rect(screen, square_color, (245, 190, tipo_size, tipo_size))

        text_button = font.render("Para cambiar tamaño: C", True, (255, 255, 255))
        text_rect_button = text_button.get_rect(x=300, y=200)
        screen.blit(text_button, text_rect_button)

        text_speed = font.render(f"Velocidad actual: {speed_text}", True, (255, 255, 255))
        text_rect_speed = text_speed.get_rect(x=25, y=250)
        screen.blit(text_speed, text_rect_speed)

        text_button1 = font.render("Para cambiar velocidad: V", True, (255, 255, 255))
        text_rect_button1 = text_button1.get_rect(x=340, y=250)
        screen.blit(text_button1, text_rect_button1)

        text_back = font.render("Presione X para volver al menu", True, (255, 255, 255))
        text_rect_back = text_back.get_rect(x=100, y=400)
        screen.blit(text_back, text_rect_back)

        keys = pygame.key.get_pressed()
        if not keys[pygame.K_c]:
            typoc = True
        if typoc:
            if keys[pygame.K_c]:
                typo = not typo
                typoc = False
        if not keys[pygame.K_v]:
            speedoc = True
        if speedoc:
            if keys[pygame.K_v]:
                speedo = not speedo
                speedoc = False
        if keys[pygame.K_x]:
            Settings_Status = False
            Menu_Status = True

    if Game_Status:

        if Setter:
            player_dimensions = (0, 0, unit, unit)
            goal_dimensions = (0, unit*(height-1), width * unit, unit)
            player = pygame.Rect(player_dimensions)
            goal = pygame.Rect(goal_dimensions)
            cars = cars_generator(width,height,unit,dif)
            objs = objects_generator(width,height,unit)
            Setter = False

        if goalr:

            screen.fill(initial_bg_values)

            lila5 = (106, 90, 205)
            lila6 = (72, 61, 139)

            tile = 10

            a, l = size[1], size[0]

            screen.fill(initial_bg_values)

            for row in range(0, a // tile):
                for col in range(0, l // tile):
                    if (row + col) % 2 == 0:
                        color = lila5
                    else:
                        color = lila6

                    pygame.draw.rect(screen, color, (col * tile, row * tile, tile, tile))

            for x in range(0, width*unit, unit):
                pygame.draw.line(screen, grid_color, (x, 0), (x, height*unit))
            for y in range(0, height*unit, unit):
                pygame.draw.line(screen, grid_color, (0, y), (width*unit, y))

            title_font = pygame.font.Font(stocky, 72)
            text_Menu = title_font.render("Victoria!", True, (0, 0, 0))
            text_rect = text_Menu.get_rect(x=25,y=20)
            screen.blit(text_Menu, text_rect)

            text_speed = font.render(f"Salir: Q", True, (0, 0, 0))
            text_rect_speed = text_speed.get_rect(x=50, y=125)
            screen.blit(text_speed, text_rect_speed)

            text_button1 = font.render("Menu: M", True, (0, 0, 0))
            text_rect_button1 = text_button1.get_rect(x=50, y=175)
            screen.blit(text_button1, text_rect_button1)

            text_back = font.render("Reset: R", True, (0, 0, 0))
            text_rect_back = text_back.get_rect(x=50, y=225)
            screen.blit(text_back, text_rect_back)

            pygame.display.update()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                player.topleft = (0, 0)
                goalr = False
            if keys[pygame.K_q]:
                run = False
            if keys[pygame.K_m]:
                player.topleft = (0, 0)
                goalr = False
                Setter = True
                Game_Status = False
                Menu_Status = True

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
            obj.draw(screen)

        for car in cars:
            car.draw(screen)
            car.move(width*unit, unit)

        pygame.draw.rect(screen, (0,255,0), player)

        pygame.draw.rect(screen, (255,255,255), goal)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()