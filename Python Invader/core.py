import pygame
import sys
import config as cfg
from classes import ScoreHandler, Player, Enemy, Bullet
from random import randint
from pygame.font import Font
from pygame.sprite import collide_rect


def render(object, screen):
    screen.blit(object.image, (object.rect.topleft[0], object.rect.topleft[1]))


class Entity_Factory:
    def __init__(self) -> None:
        # Load assets
        self.PLAYER_IMAGE = pygame.image.load(
            cfg.PLAYER_IMAGE).convert_alpha()
        self.ENEMY_IMAGE = pygame.image.load(
            cfg.ENEMY_IMAGE).convert_alpha()
        self.BULLET_IMAGE = pygame.image.load(
            cfg.BULLET_IMAGE).convert_alpha()

    def spawn_default_enemy(self, *groups) -> Enemy:
        return Enemy(
            self.ENEMY_IMAGE, randint(cfg.MIN_X, cfg.MAX_X), randint(
                cfg.MIN_Y, cfg.MAX_Y), cfg.DEF_ENEMY_SPEED, *groups
        )

    def spawn_default_player(self):
        return Player(
            self.PLAYER_IMAGE, cfg.WIDTH/2, cfg.HEIGHT - 100
        )

    def spawn_bullets(self, amt=5):
        f = pygame.sprite.Group()
        for i in range(0, amt):
            (Bullet(self.BULLET_IMAGE, 3, f))
        return f


def main():
    # Set Globals
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption(cfg.TITLE)
    DISPLAY = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT))
    BG = pygame.image.load(cfg.BG).convert()

    # Initialize classes
    score = ScoreHandler((0, 10), Font('freesansbold.ttf', 64))
    factory = Entity_Factory()
    enemies = pygame.sprite.Group()
    player = factory.spawn_default_player()
    player.bullets = factory.spawn_bullets(5)
    last_spawn = 0
    while True:  # Entire program
        if score.score < 0:
            enemies.empty()
            player = factory.spawn_default_player()
            player.bullets = factory.spawn_bullets(5)
            score.score = 0

        tick = clock.tick(cfg.FPS)
        DISPLAY.blit(BG, [0, 0])  # Drawing BG
        score.render(DISPLAY)  # Render Score
        # Enemy Spawner
        now = pygame.time.get_ticks()
        if now - last_spawn >= randint(650, 1200):
            last_spawn = now
            factory.spawn_default_enemy(enemies)

        # Event Handling
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        # Render and handle player
        player.take_input(pygame.key.get_pressed(),
                          now)  # Player input
        player.update_position(DISPLAY, tick)
        render(player, DISPLAY)

        for bullet in player.bullets.sprites():
            if bullet.rect.bottomleft[1] < 0:  # Free if outside the screen
                bullet.reset()
            elif bullet.firing:
                for enemy in enemies.sprites():
                    if collide_rect(bullet, enemy):
                        enemy.kill()
                        bullet.reset()
                        score.add_score()
            bullet.update()
            render(bullet, DISPLAY)

        # Handle Enemies
        for enemy in enemies.sprites():
            if enemy.rect.bottomleft[1] > cfg.HEIGHT:  # Below the screen
                score.score -= 1
                enemy.kill()
                continue
            if collide_rect(enemy, player):
                score.score -= 1
            enemy.update()  # Update position
            render(enemy, DISPLAY)

        pygame.display.update()


if __name__ == "__main__":
    main()
