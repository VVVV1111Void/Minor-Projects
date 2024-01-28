import pygame
import config
import sys
from math import floor
from entity_classes import Entity_Factory
from pygame.sprite import Group, Sprite
from pygame import Rect, Surface, transform
class Model:
    """Contains all the world data and handles their interactions"""
    def __init__(self) -> None:
        self.renderable_entities = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.temp_entities = pygame.sprite.Group()
        self.last_spawn = 0
        self.factory: Entity_Factory = Entity_Factory()

    def spawn_enemy(self, delta):
        self.factory.spawn_enemy(delta, self.renderable_entities, self.enemies)

    def update():
        pass

    def initialize_world(self):
        self.enemies.empty()
        self.renderable_entities.empty()
        self.last_spawn = 0
        self.player = self.factory.spawn_player(self.renderable_entities)
        return self
    

def main():
    """Function acts as a view and the controller."""
    # Initialization and the main event loop
    pygame.init()
    DISPLAY = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    FONT = pygame.font.SysFont("monospace", 64)
    BG = pygame.image.load(config.BG).convert()
    pygame.display.set_caption(config.TITLE)
    clock = pygame.time.Clock()
    world: Model = Model().initialize_world()
    score = 0
    # Main event loop

    # render text
    while True:
        DISPLAY.blit(BG, [0, 0])

        label = FONT.render(f"SCORE: {int(score)}", 1, (255,255,0))
        DISPLAY.blit(label, ((config.WIDTH/2)-128,  64))

        delta: int = clock.tick(30) / 1000
        # Events and input
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                case pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        world.player.try_jump()
    
        # Enemy handling
        world.spawn_enemy(delta)
        # ROLES: Render sprites and move them
        sprites: list[sprite] = world.renderable_entities.sprites()
        for i in range(0, len(sprites)):
            sprite: sprite = sprites[i]
            sprite.update(delta)
            sprite.render(DISPLAY)
            # Free-up logic
            if sprite.rect.topleft[0] < 0:
                sprite.remove(world.renderable_entities)
        
        # Collision handling and game end
        collide: Sprite = pygame.sprite.spritecollideany(world.player, world.enemies)
        if (collide):
            score = 0
            world.initialize_world()

        score = (delta + score)
        pygame.display.update()
    print("End")