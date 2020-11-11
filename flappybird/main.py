import pygame, sys, os, random
from pipe import Pipe
from bird import Bird

# scrx=-1200
# scry=50

# os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (scrx,scry)

pygame.init()

game_font = pygame.font.Font('04B_19.ttf',40)

def score_display():
   score_surface = game_font.render('Score', True, (255,255,255))
   score_rect = score_surface.get_rect(center=(288,100))
   screen.blit(score_surface, score_rect)



def rotate_bird(bird):
   new_bird = pygame.transform.rotozoom(bird, -bird.movement*3, 1)
   return new_bird

def reset_sprites(bird, pipes):
   bird.rect = bird.surface.get_rect(center = (100,200))
   bird.movement = 0
   pipes.empty()

def check_collisions(bird, screen, pipes):
   pipe_collisions = pygame.sprite.spritecollide(bird, pipes, False)
   #check collisions with pipe
   if len(pipe_collisions) > 0   :
      return True
   #check collisions with top of screen
   if bird.rect.top < 0 or bird.rect.bottom >=900:
      return True
   return False

def remove_pipes(pipes):
   for pipe in pipes.copy():
      if pipe.rect.right <= 0:
         pipes.remove(pipe)
         

def draw_floor():
   screen.blit(floor_surface,(floor_x_pos,900))
   screen.blit(floor_surface,(floor_x_pos + 576,900))

screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

#game variables
 
bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird = Bird(screen)

pipes = pygame.sprite.Group()
BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
game_active = True


score = 0
high_score = 0

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            bird.movement = 0
            bird.movement -= 8
            # bird = rotate_bird(bird)
         if event.key == pygame.K_SPACE and game_active == False:
            reset_sprites(bird, pipes)
            game_active = True
      if event.type == SPAWNPIPE:
         height = random.choice([500,600,700])

         bottom_pipe = Pipe(screen,height=height, offset=0, flipped=False)
         top_pipe = Pipe(screen,height=height, offset=900, flipped= True)
         pipes.add(bottom_pipe)
         pipes.add(top_pipe)
      if event.type == BIRDFLAP:
         
         bird.flap()
         
   floor_x_pos-=1
   if floor_x_pos == -576:
      floor_x_pos = 0

   screen.blit(bg_surface,(0,0))

   collisions = check_collisions(bird, screen, pipes)
   if collisions: game_active = False
   if game_active:
      bird.update()
      pipes.update()
   draw_floor()
   remove_pipes(pipes)
   pygame.display.update()
   score_display()
   clock.tick(120)