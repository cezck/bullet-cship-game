import pygame
import random



class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # наследуем свойства родителя
        self.image = pygame.image.load(f'image/enemy1.png')  # импортируе картику
        self.image = pygame.transform.rotozoom(self.image, 1, 0.09)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(1, 800)
        self.rect.centery = 0
        self.speedy = 3
        self. speedx = 0

    def update(self):
        self.move()
        if self.rect.bottom > 900:
            self.kill()

    def move(self):
        self.rect.y += self.speedy
