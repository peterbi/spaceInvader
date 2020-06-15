import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")

playerImg = pygame.image.load("space-invaders.png")
playerX = 370.
playerY = 480.

alienImg = pygame.image.load("alien.png")

alienX = random.randint(0, 736)
alienY = random.randint(50, 150)
alienX_change = 0.3
alienY_change = 0.3

bulletImg = pygame.image.load("bullet.png")
bulletX = 370.
bulletY = 480.
bulletX_change = 0
bulletY_change = 4
bullet_state = False

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


def alien(x, y):
    screen.blit(alienImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = True
    screen.blit(bulletImg, (x + 16, y + 10))

def is_collision(bulletX, bulletY, alienX, alienY):
    return True if (bulletX - alienX)**2 + (bulletY - alienY)**2 <= 500 else False

running = True
i = 0
inc = 1
playerX_change = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check key input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -.3
            if event.key == pygame.K_RIGHT:
                playerX_change = .3
            if event.key == pygame.K_SPACE:
                if not bullet_state:
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    if i == 225:
        inc = -1
    elif i == 0:
        inc = 1
    i += inc
    # Move alien
    if alienX <= 0:
        alienX_change = 0.3
        alienY += 40
    elif alienX >= 736:
        alienX_change = -0.3
        alienY += 40




    screen.fill((255, 127, i))
    playerX += playerX_change
    playerX = max(0, min(736, playerX))
    player(playerX, playerY)
    alienX += alienX_change

    alien(alienX, alienY)
    # move bullet
    if bullet_state:
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        if bulletY <= 0:
            bullet_state = False
            bulletY = 480

    # collision
    if is_collision(bulletX, bulletY, alienX, alienY):
        bulletY = 480
        bullet_state = False
        score += 1
        print(score)
        alienX = random.randint(0, 736)
        alienY = random.randint(50, 150)

    pygame.display.update()
# icon comes from https://www. tourbuzz.net/1615984?idx=1
# Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="https://www.flaticon.com/authors/those-icons" title="Those Icons">Those Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>