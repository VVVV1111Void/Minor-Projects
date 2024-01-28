"""Import pygame and pygame locals for handling player movement"""
import pygame.locals as pyl
from pygame.sprite import Sprite, Group
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.surface import Surface

class ScoreHandler(object):
    def __init__(self, topleft, font, color=(255, 255, 255)) -> None:
        self.score = 0
        self.topleft = topleft
        self.font_color = color
        self.font = font

    def add_score(self):
        self.score += 1

    def reset(self):
        self.score = 0

    def render(self, screen):
        rendered_score = self.font.render(
            f'Points: {self.score}', True, self.font_color)
        screen.blit(rendered_score, self.topleft)


class Bullet(Sprite):
    def __init__(self, image: Surface, speed: int = 3, *groups) -> None:
        super().__init__(*groups)
        self.SPEED: int = speed
        self.image: Surface = image
        self.firing: bool = False
        self.rect: Rect = image.get_rect(topleft=(3000, 3000))

    def update(self, ) -> None:
        if self.firing:
            self.rect.move_ip(0, -self.SPEED)  # Move inplace
    
    """Puts the bullet in a position where it was fired from"""
    def fire(self, location) -> None:
        self.firing = True
        self.rect.midbottom = location

    def reset(self) -> None:
        self.rect.topleft = (3000, 3000)  # Place offscreen
        self.firing = False

class Enemy(Sprite):
    def __init__(self, image: Surface, centerx: int, centery: int, speed: float, *groups) -> None:
        super().__init__(*groups)
        self.image: Surface = image
        self.rect: Rect = image.get_rect(center=(centerx, centery))
        self.velocity = Vector2(0, speed)
        # Temporary Vector to hold float values

    def update(self, ) -> None:
        self.rect.move_ip(self.velocity[0], self.velocity[1])
        # self.pos += self.velocity
        # # Rect will round the float values of the vector
        # self.rect.center = (round(self.pos.x), round(self.pos.y))


class Player(Sprite):
    def __init__(self, image: Surface, centerx, centery, speed: float = 0.25, MAX_SPEED: float = 0.5, *groups) -> None:
        super().__init__(*groups)
        self.change_x = 0
        self.SPEED = speed
        self.MAX_SPEED = MAX_SPEED
        self.image = image
        self.rect: Rect = image.get_rect(
            center=(centerx, centery))  # type: ignore
        self.bullets = Group()
        self.cooldown = 100
        self.last = 0

    def update_position(self, rect, tick) -> None:
        self.rect.move_ip(self.change_x*tick, 0)  # Move inplace
        self.rect.clamp_ip(rect.get_rect())  # puts the object inside the rect
        """Move the player according to velocity
        """

    def fire_bullet(self, now) -> None:
        if now - self.last >= self.cooldown:
            self.last = now
            for bullet in self.bullets:
                if not bullet.firing:
                    bullet.fire(self.rect.midtop)
                    break
        """Looks for a free bullet and fires it
        """

    def take_input(self, keys_pressed, time) -> None:
        if keys_pressed[pyl.K_SPACE]:
            self.fire_bullet(time)

        # Movement
        if keys_pressed[pyl.K_RIGHT] and keys_pressed[pyl.K_LEFT]:  # ??
            self.decellerate()
            return
        elif keys_pressed[pyl.K_RIGHT] and self.change_x < self.MAX_SPEED:  # move towards right
            self.change_x += self.SPEED
            return
        elif keys_pressed[pyl.K_LEFT] and self.change_x > -self.MAX_SPEED:
            self.change_x += -self.SPEED
            return
        self.decellerate()
        """Moves the player based on user input and if its less than max velocity
        """

    def decellerate(self):
        if self.change_x > 0.1:
            self.change_x = self.change_x - 0.1
        elif self.change_x < -0.1:
            self.change_x = self.change_x + 0.1



