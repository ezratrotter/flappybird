import pygame, random

class Pipe(pygame.sprite.Sprite):
   def __init__(self, screen, height, offset=0, flipped = False):
      super().__init__()
      if flipped == False:
         self.surface = pygame.transform.scale2x(pygame.image.load('assets/pipe-green.png')).convert_alpha()
      else:
         self.surface = pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('assets/pipe-green.png')), False, True)
      self.screen = screen
      self.rect = self.surface.get_rect(midtop = (700,height-offset))
      self.width = self.rect.width
      self.rect.centerx = 512 + self.width 
   
   def update(self):
      self.rect.centerx -= 5
      self.screen.blit(self.surface, (self.rect))

   # def create_pipe ():
   # new_pipe = pipe_surface.get_rect(midtop = (288,512))
   # return new_pipe

   # def move_pipes(pipes):
   #    for pipe in pipes:
         
   #    return pipes

   # def draw_pipes(pipes):
   #    for pipe in pipes:
   #       screen.blit(pipe_surface, pipe)