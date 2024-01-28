from config import WIDTH, PLAYER_POS, OBSTACLE_SPRITE, NORM_Y, MIN_SPAWN, MAX_SPAWN
from pygame.sprite import Group, Sprite
from pygame import Rect, Surface, transform
import pygame
import time
import random

class Player(Sprite):
    def __init__(self, frames: list[Surface], *groups: Group) -> None:
        super().__init__(*groups)
        self.frames: list[Surface] = frames
        self.state = "RUN"
        self.frame_states = {"DEFAULT": (0, 4, 5), "RUN": (4, 10, 10)}
        self.frame_index = 0
        self.start = time.time()
        self.velocity_y = 0
        self.JUMP_VEL = -31

        self.x, self.y = PLAYER_POS
        self.width, self.height = self.frames[0].get_size()
        self.rect = Rect(self.x, self.y, self.width, self.height)

    @property
    def image(self):
        img = self.frames[self.frame_index]
        return img

    def render(self, display: Surface):
        display.blit(self.image, self.rect.topleft)

    def update(self, delta):  # Delta not used since it's too fast
        subgroup_start, subgroup_end, fps = self.frame_states[self.state]
        subgroup_size = subgroup_end - subgroup_start
        # Simpler solution that has independent delta
        self.frame_index = subgroup_start + \
            int((time.time() - self.start) * fps % subgroup_size)
        
        # Correct the position incase the player is below the ground
        self.velocity_y += 2.8
        self.rect.move_ip(0, self.velocity_y)
        if self.rect.top > NORM_Y:
            self.rect.top = NORM_Y
            self.velocity_y = 0

    def try_jump(self):
        if self.rect.top == NORM_Y:
            self.velocity_y = self.JUMP_VEL
             

class Obstacle(Sprite):
    image = transform.scale(pygame.image.load(OBSTACLE_SPRITE), (64, 64))
    size = image.get_size()

    def __init__(self, *groups: Group) -> None:
        super().__init__(*groups) # Join group
        self.x = int(WIDTH)
        self.y = int(NORM_Y)
        self.width, self.height = int(Obstacle.size[0]*0.75), int(Obstacle.size[1]*0.75)
        self.moving = True
        self.speed = 10.0
        self.rect = Rect(self.x, self.y, self.width, self.height)

    def render(self, display: Surface):
        display.blit(Obstacle.image, self.rect.topleft)

    def update(self, delta):
        if self.moving:
            # Move left
            self.rect.move_ip(-self.speed, 0)


class Entity_Factory():
    """This class handles the spawning of objects and entities in the game."""

    def __init__(self) -> None:
        self.timer_float: int = 0

    def spawn_player(self, *groups: list[Group]):
        return Player(self.load_dino_sprites(0, 17), *groups)

    def spawn_enemy(self, delta, *groups: list[Group]):
        if self.timer_float <= 0:
            self.timer_float = random.randint(MIN_SPAWN, MAX_SPAWN)
            Obstacle(*groups)
        self.timer_float = self.timer_float - (1*delta*1000)

    def load_dino_sprites(self, start, end):
        frames = []
        for i in range(start, end):
            img = (pygame.image.load(f"Vita/{i+1}.bmp").convert_alpha())
            img = transform.scale(img, (64, 64))
            frames.append(img)
        return frames
