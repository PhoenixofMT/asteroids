import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    @property
    def off_screen(self) -> bool:
        x, y = self.position
        return (x < 0 or x > SCREEN_WIDTH or
                y < 0 or y > SCREEN_HEIGHT)

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass

    def collides_with(self, other: "CircleShape") -> bool:
        min_distance = self.radius + other.radius
        distance = self.position.distance_to(other.position)
        return distance <= min_distance

    def wrap_screen(self) -> None:
        x, y = self.position

        if x < 0:
            x += SCREEN_WIDTH
        elif x > SCREEN_WIDTH:
            x -= SCREEN_WIDTH

        if y < 0:
            y += SCREEN_HEIGHT
        elif y > SCREEN_HEIGHT:
            y -= SCREEN_HEIGHT

        self.position = pygame.Vector2(x, y)
