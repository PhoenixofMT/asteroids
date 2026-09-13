import pygame as pg
from constants import *
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version {pg.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.fill("black")


        pg.display.flip()

if __name__ == "__main__":
    main()
