import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

player_width, player_height = 50, 40
player_speed = 5
bullet_width, bullet_height = 5, 10
bullet_speed = 7
block_width, block_height = 50, 30
block_speed = 2 * 0.7  

font = pygame.font.SysFont(None, 36)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((player_width, player_height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10))
    
    def update(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += player_speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((bullet_width, bullet_height))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))
    
    def update(self):
        self.rect.y -= bullet_speed
        if self.rect.bottom < 0:
            self.kill()

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((block_width, block_height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - block_width)
        self.rect.y = random.randint(-150, -block_height)
    
    def update(self):
        global game_over
        self.rect.y += block_speed
        if self.rect.top > HEIGHT:
            game_over = True  
            self.kill()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(topleft=(x, y))
    surface.blit(textobj, textrect)

def main():
    global game_over
    clock = pygame.time.Clock()
    player = Player()
    player_group = pygame.sprite.Group(player)
    bullets = pygame.sprite.Group()
    blocks = pygame.sprite.Group()

    ADD_BLOCK_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_BLOCK_EVENT, 800)

    score = 0
    game_over = False

    while True:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == ADD_BLOCK_EVENT and not game_over:
                block = Block()
                blocks.add(block)

            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    bullets.add(bullet)

        if not game_over:
            player_group.update(keys)
            bullets.update()
            blocks.update()

            collisions = pygame.sprite.groupcollide(bullets, blocks, True, True)
            if collisions:
                score += len(collisions)

            if pygame.sprite.spritecollide(player, blocks, False):
                game_over = True

        screen.fill(BLACK)
        player_group.draw(screen)
        bullets.draw(screen)
        blocks.draw(screen)
        draw_text(f"Score: {score}", font, WHITE, screen, 10, 10)

        if game_over:
            draw_text("GAME OVER", font, RED, screen, WIDTH // 2 - 100, HEIGHT // 2)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    game_over = False
    main()