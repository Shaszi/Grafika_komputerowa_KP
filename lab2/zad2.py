import pygame as pg

pg.init()

WIDTH, HEIGHT = 600, 600
win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Zielona figura")

green = (0, 255, 0)
white = (255, 255, 255)

def draw_shape(surface):
    size = 200
    x, y = (WIDTH - size) // 2, (HEIGHT - size) // 2

    pg.draw.rect(surface, green, (x, y, size, size))

    triangle_points = [
        (x + size // 2, y + size // 2),
        (x, y + size),
        (x + size, y + size)
    ]

    pg.draw.polygon(surface, white, triangle_points)

run = True
while run:
    win.fill(white)

    draw_shape(win)

    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

pg.quit()