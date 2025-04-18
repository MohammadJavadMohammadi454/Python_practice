import pygame
import math
import random
import sys

# تنظیمات اولیه
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("شلیک تیر")

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

# موقعیت‌های اولیه
shooter_pos = (100, 500)
target_pos = [random.randint(500, 750), random.randint(100, 500)]
bullet_radius = 5
bullet_speed = 10  # سرعت تیر
radius_limit = 100  # شعاع محدودکننده بردار موس

# تابع برای رسم آدمک تفنگ‌دار
def draw_shooter(pos):
    pygame.draw.circle(screen, BLACK, (pos[0], pos[1] - 20), 10)
    pygame.draw.line(screen, BLACK, (pos[0], pos[1] - 10), (pos[0], pos[1] + 30), 2)
    pygame.draw.line(screen, BLACK, (pos[0], pos[1] - 5), (pos[0] + 20, pos[1] - 15), 2)
    pygame.draw.line(screen, BLACK, (pos[0], pos[1] - 5), (pos[0] - 20, pos[1] - 15), 2)
    pygame.draw.line(screen, BLACK, (pos[0], pos[1] + 30), (pos[0] - 20, pos[1] + 50), 2)
    pygame.draw.line(screen, BLACK, (pos[0], pos[1] + 30), (pos[0] + 20, pos[1] + 50), 2)
    pygame.draw.rect(screen, BLACK, (pos[0] + 20, pos[1] - 15, 20, 5))
    pygame.draw.line(screen, BLACK, (pos[0] + 40, pos[1] - 12), (pos[0] + 50, pos[1] - 10), 2)

# تابع بررسی برخورد تیر
def check_collision(bullet, target):
    distance = math.hypot(bullet[0] - target[0], bullet[1] - target[1])
    return distance < 20

# تابع محدود کردن بردار موس به داخل شعاع دایره
def get_limited_mouse_vector(center, mouse_pos, max_radius):
    dx = mouse_pos[0] - center[0]
    dy = mouse_pos[1] - center[1]
    distance = math.hypot(dx, dy)

    if distance > max_radius:
        scale = max_radius / distance
        dx *= scale
        dy *= scale

    limited_x = center[0] + dx
    limited_y = center[1] + dy
    angle_deg = math.degrees(math.atan2(dy, dx))

    return angle_deg, (limited_x, limited_y)

# تابع شلیک تیر
def shoot(angle_deg):
    angle_rad = math.radians(angle_deg)
    vx = bullet_speed * math.cos(angle_rad)
    vy = bullet_speed * math.sin(angle_rad)
    bullet_pos = list(shooter_pos)

    while 0 < bullet_pos[0] < WIDTH and 0 < bullet_pos[1] < HEIGHT:
        bullet_pos[0] += vx
        bullet_pos[1] += vy

        if check_collision(bullet_pos, target_pos):
            print("تیر به هدف خورد!")
            return True, bullet_pos

        screen.fill(WHITE)
        draw_shooter(shooter_pos)
        pygame.draw.circle(screen, RED, (int(target_pos[0]), int(target_pos[1])), 20)
        pygame.draw.circle(screen, RED, (int(bullet_pos[0]), int(bullet_pos[1])), bullet_radius)
        pygame.display.update()
        pygame.time.delay(10)

    return False, bullet_pos

# حلقه اصلی بازی
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # گرفتن موقعیت موس و محدودسازی
    mouse_pos = pygame.mouse.get_pos()
    angle, limited_mouse = get_limited_mouse_vector(shooter_pos, mouse_pos, radius_limit)

    # رسم شعاع دایره تعیین زاویه
    pygame.draw.circle(screen, GRAY, shooter_pos, radius_limit, 1)

    # رسم خط جهت شلیک
    pygame.draw.line(screen, RED, shooter_pos, limited_mouse, 2)

    # رسم هدف
    pygame.draw.circle(screen, RED, (int(target_pos[0]), int(target_pos[1])), 20)

    # رسم آدمک
    draw_shooter(shooter_pos)

    # نمایش زاویه
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"زاویه: {int(angle)} درجه", True, BLACK)
    screen.blit(text, (WIDTH - 220, 50))

    # شلیک در صورت کلیک
    if pygame.mouse.get_pressed()[0]:
        hit, bullet_pos = shoot(angle)
        if hit:
            pygame.time.delay(500)
            target_pos = [random.randint(500, 750), random.randint(100, 500)]

    pygame.display.update()