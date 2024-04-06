import pygame as pg
import random
from bird import Bird
from pipe import Pipe

pg.init()
pg.font.init()
score = 0
back_ground_img = pg.image.load('flappy_bird.png')

back_groud = pg.surface.Surface((back_ground_img.get_width(), 600))
back_groud_x = 0
back_groud_x2 = back_ground_img.get_width()

screen = pg.display.set_mode((600, 600))
font = pg.font.SysFont("None", 100)
clock = pg.time.Clock()

pipes = pg.sprite.Group()
if score <= 10:
    pg.time.set_timer(pg.USEREVENT, 2000)
elif score >= 20:
    pg.time.set_timer(pg.USEREVENT, random.randint(1500, 2000))
elif score >= 30:
    pg.time.set_timer(pg.USEREVENT, random.randint(900, 2000))
elif score >= 30:
    pg.time.set_timer(pg.USEREVENT, random.randint(800, 1800))
elif score >= 40:
    pg.time.set_timer(pg.USEREVENT, random.randint(800, 1500))
bird = Bird(50, 600 // 2)
all_sprite = pg.sprite.Group(bird)
run = True

while run:
    screen.fill("black")
    clock.tick(60)

    back_groud.blit(back_ground_img, (0, 0))
    screen.blit(back_groud, (back_groud_x, 0))
    screen.blit(back_groud, (back_groud_x2, 0))
    back_groud_x -= 1
    back_groud_x2 -=1

    if back_groud_x < -back_ground_img.get_width()-1:
        back_groud_x = back_ground_img.get_width()

    if back_groud_x2 < -back_ground_img.get_width()-1:
        back_groud_x2 = back_ground_img.get_width()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYUP and event.key == pg.K_SPACE:
            bird.jump()
        if event.type == pg.USEREVENT:
            if score <= 10:
                rand_hight = 150 + random.randint(0, 50)
                pipe_up = Pipe(600, 0, 50, rand_hight, (129, 208, 58))
                pipe_down = Pipe(600, rand_hight + random.randint(100, 200), 50, 1000, (129, 208, 58))
                all_sprite.add(pipe_up, pipe_down)
                pipes.add(pipe_up, pipe_down)
                score += 1
            elif score <= 20:
                rand_hight = 150 + random.randint(0, 200)
                pipe_up = Pipe(600, 0, 50, rand_hight, (129, 208, 58))
                pipe_down = Pipe(600, rand_hight + random.randint(100, 150), 50, 1000, (129, 208, 58))
                all_sprite.add(pipe_up, pipe_down)
                pipes.add(pipe_up, pipe_down)
                score += 1
            elif score <= 30:
                rand_hight = 150 + random.randint(0, 300)
                pipe_up = Pipe(600, 0, 50, rand_hight, (129, 208, 58))
                pipe_down = Pipe(600, rand_hight + random.randint(100, 150), 50, 1000, (129, 208, 58))
                all_sprite.add(pipe_up, pipe_down)
                pipes.add(pipe_up, pipe_down)
            elif score <= 40:
                rand_hight = 150 + random.randint(0, 400)
                pipe_up = Pipe(600, 0, 50, rand_hight, (129, 208, 58))
                pipe_down = Pipe(600, rand_hight + random.randint(100, 150), 50, 1000, (129, 208, 58))
                all_sprite.add(pipe_up, pipe_down)
                pipes.add(pipe_up, pipe_down)
    if pg.sprite.spritecollide(bird, pipes, False):
        run = False
    all_sprite.draw(screen)
    all_sprite.update()

    text = font.render(f"{score}", False, 'white')
    screen.blit(text, (600 // 2 - 25, 500))

    pg.display.update()