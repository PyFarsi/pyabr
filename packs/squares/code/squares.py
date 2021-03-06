import pygame, sys, random, time
from pygame.locals import *
from pygame import mixer
from libabr import Res, Control, Files, System,App

res = Res()
control = Control()
files = Files()
pygame.init()
app = App()
app.start('squares')
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption(res.get('@string/app_name'))
clock = pygame.time.Clock()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
p_pos = [370, 500]
e_pos = [random.randint(0, 740), 0]
enemy_l = [e_pos]
speed = 30
speed_e = 5
fps = 60
game_over = False
font = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 80)
score = 0


def collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    if (p_x <= e_x < (p_x + 60)) or (e_x <= p_x < (e_x + 60)):
        if (p_y <= e_y < (p_y + 60)) or (e_y <= p_y < (e_y + 60)):
            return True
    else:
        return False


def enemies(enemy_list):
    a = random.randint(0, 10)
    if len(enemy_list) <= 10 and a < 1:
        x_pos = random.randint(0, 740)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])


def draw_enemies(enemy_list):
    for enemy in enemy_list:
        pygame.draw.rect(win, red, (enemy[0], enemy[1], 60, 60))


def enemy_pos_update(enemy_list, score):
    for index, enemy_pos in enumerate(enemy_list):
        if 0 <= enemy_pos[1] <= 600:
            enemy_pos[1] += speed_e
        else:
            enemy_list.pop(index)
            score += 1
    return score


def level(scr, spd):
    if scr <= 10:
        spd = 2
    elif scr <= 20:
        spd = 4
    elif scr <= 50:
        spd = 6
    elif scr <= 100:
        spd = 8
    else:
        spd = 10
    return spd


def check_collision(enemy_list, player_pos):
    for enemy in enemy_list:
        if collision(enemy, player_pos):
            return True
    return False


def game_opening():
    font3 = pygame.font.Font(None, 500)
    text_s = font3.render("3", True, red)
    win.blit(text_s, (300, 150))
    pygame.display.update()
    time.sleep(1)
    win.fill(black)
    text_s = font3.render("2", True, (255, 201, 14))
    win.blit(text_s, (300, 150))
    pygame.display.update()
    time.sleep(1)
    win.fill(black)
    text_s = font3.render("1", True, green)
    win.blit(text_s, (300, 150))
    pygame.display.update()
    time.sleep(1)
    win.fill(black)
    text_s = font3.render("GO", True, green)
    win.blit(text_s, (150, 150))
    pygame.display.update()
    time.sleep(1)
    win.fill(blue)


game_opening()

while not game_over:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                p_pos[0] += speed

            if event.key == K_LEFT:
                p_pos[0] -= speed

    # if collision(p_pos, e_pos):
    #     game_over = True
    #     break
    if check_collision(enemy_l, p_pos):
        t_s2 = font2.render('Game Over', True, (0, 255, 255))
        win.blit(t_s2, (270, 270))
        t_s = font.render("Your score is : " + str(score), True, (0, 255, 0))
        win.blit(t_s, (270, 320))
        pygame.display.update()
        time.sleep(3)
        game_over = True
        break
    if p_pos[0] <= 0:
        p_pos[0] = 0
    if p_pos[0] >= 740:
        p_pos[0] = 740
    # if (e_pos[1] >= 0) and (e_pos[1] <= 600):
    #     e_pos[1] += speed_e
    # else:
    #     e_pos[1] = 0
    #     e_pos[0] = random.randint(0, 740)
    win.fill(blue)
    enemies(enemy_l)
    draw_enemies(enemy_l)
    score = enemy_pos_update(enemy_l, score)
    t_s = font.render("score : " + str(score), True, (0, 255, 0))
    win.blit(t_s, (20, 20))
    speed_e = level(score, speed_e)

    img1 = pygame.image.load(res.get("@icon/catball"))
    img1 = pygame.transform.scale(img1, (60, 60))
    win.blit(img1, (p_pos[0], p_pos[1], 60, 60))

    clock.tick(fps)
    pygame.display.update()