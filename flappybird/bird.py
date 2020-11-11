import pygame

class Bird(pygame.sprite.Sprite):
   def __init__(self, screen):
      super().__init__()
      self.downflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-downflap.png'))
      self.midflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png'))
      self.upflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-upflap.png'))
      self.birdframes = [self.downflap, self.midflap, self.upflap]
      self.birdindex = 0

      self.surface = self.birdframes[self.birdindex]
    
      self.rect = self.surface.get_rect(center = (100,200))
      self.gravity = 0.25
      self.movement = 0
      self.screen = screen

   def rotate(self):
      return pygame.transform.rotozoom(self.surface, -self.movement*3, 1)

   def update(self):
         self.movement += self.gravity
         self.rect.y+=self.movement
         rotated = self.rotate()
         self.screen.blit(rotated,(self.rect))
   
   def flap(self):
      # self.birdindex +=1 if self.birdindex <= 2 else 0

      if self.birdindex < 2: self.birdindex+=1
      else: self.birdindex = 0

      print(self.birdindex)
      self.surface = self.birdframes[self.birdindex]
