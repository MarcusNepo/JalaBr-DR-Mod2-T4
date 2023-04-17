import pygame
from random import randint

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleManage:
    def __init__(self,):
        self.obstacles = []
        

    def update(self, game):
        Obstacle_type = [
            Cactus(),
            Bird(),
        ]
        if len(self.obstacles) == 0:
            self.obstacles.append(Obstacle_type[randint(0,1)])
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                self.obstacles.remove(obstacle)
                pygame.time.delay(200)
                game.playing = False

    def reset_obstacles(self):    
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)