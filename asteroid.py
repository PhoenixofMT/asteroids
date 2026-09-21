import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        deflection = random.uniform(20, 50)
        a1_velocity = self.velocity.rotate(deflection) * 1.2
        a2_velocity = self.velocity.rotate(-deflection) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        x, y = self.position

        a1 = Asteroid(x, y, new_radius)
        a2 = Asteroid(x, y, new_radius)

        a1.velocity = a1_velocity
        a2.velocity = a2_velocity
