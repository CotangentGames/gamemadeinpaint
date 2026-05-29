import pygame
import random
import sys
import os
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 8
CELL_SIZE = 60
FPS = 60
OFFSET_X = 35
OFFSET_Y = 65
EMPTY_SPOT = -2
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (255, 255, 0)
UI_BG_COLOR = (50, 50, 50)
GEM_COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 165, 0),
    (128, 0, 128),
]
GEM_IMAGES = []
gem_files = ["sprites/redGem.png", "sprites/greenGem.png", "sprites/blueGem.png", "sprites/orangeGem.png",
             "sprites/purpleGem.png"]
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("game made in paint")
program_icon = pygame.image.load(resource_path("sprites/redGem.png"))
pygame.display.set_icon(program_icon)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 32)
bigfont = pygame.font.Font(None, 67)
HINT_BUTTON_RECT = pygame.Rect(550, 500, 200, 45)
MENU_BUTTON_RECT = pygame.Rect(550, 420, 200, 60)
LAYOUT_SQUARE = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]
LAYOUT_CROSS = [
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
]
LAYOUT_DONUT = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]
LAYOUT_THESSIS = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
]
LAYOUT_DIAMOND = [
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
]
LAYOUT_H = [
    [0, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 1, 0],
]
LAYOUT_HEART = [
    [0, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
LAYOUT_A = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1],
]
ALL_LAYOUTS = [LAYOUT_SQUARE, LAYOUT_CROSS, LAYOUT_DONUT, LAYOUT_THESSIS, LAYOUT_DIAMOND, LAYOUT_H, LAYOUT_HEART, LAYOUT_A]
ALL_BACKGROUNDS = [
    "sprites/Pyramids Somewhere.png",
    "sprites/Where In The World.png",
    "sprites/One For The Erruption.png",
    "sprites/Breath Up.png",
    "sprites/Orange Coast.png",
    "sprites/Far Away.png",
    "sprites/Freezer White.png",
    "sprites/3000.png",
    "sprites/Alone in a Disco.png"
]
class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, action_id=None, image_path=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action_id = action_id
        self.image = None
        if image_path:
            full_path = resource_path(image_path)
            raw_img = pygame.image.load(full_path).convert_alpha()
            target_w = width - 10
            target_h = height - 10
            self.image = pygame.transform.scale(raw_img, (target_w, target_h))
    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.rect.collidepoint(mouse_pos)
        current_color = self.hover_color if is_hovered else self.color
        if self.image:
            s = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
            s.fill((*current_color, 150))
            screen.blit(s, (self.rect.x, self.rect.y))
            img_rect = self.image.get_rect(center=self.rect.center)
            screen.blit(self.image, img_rect)
            pygame.draw.rect(screen, WHITE, self.rect, 3, border_radius=12)
            if self.text:
                shadow_surf = small_font.render(str(self.text), True, BLACK)
                text_surf = small_font.render(str(self.text), True, WHITE)
                text_rect = text_surf.get_rect(center=self.rect.center)
                screen.blit(shadow_surf, (text_rect.x + 2, text_rect.y + 2))
                screen.blit(text_surf, text_rect)
        else:
            pygame.draw.rect(screen, current_color, self.rect, border_radius=12)
            pygame.draw.rect(screen, WHITE, self.rect, 3, border_radius=12)
            if self.text:
                text_surf = small_font.render(str(self.text), True, WHITE)
                text_rect = text_surf.get_rect(center=self.rect.center)
                screen.blit(text_surf, text_rect)
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False
NUM_LEVELS = 9
LEVEL_CONFIG = {
    1: ("sprites/Pyramids Somewhere.png", 1500, LAYOUT_SQUARE, "Pyramids Somewhere"),
    2: ("sprites/Where In The World.png", 1600, LAYOUT_CROSS, "Where in the World"),
    3: ("sprites/One For The Erruption.png", 1100, LAYOUT_DONUT, "One for the Erruption"),
    4: ("sprites/Breath Up.png", 1650, LAYOUT_THESSIS, "Breath Up"),
    5: ("sprites/Orange Coast.png", 2500, LAYOUT_DIAMOND, "Orange Coast"),
    6: ("sprites/Freezer White.png", 2250, LAYOUT_H, "Freezer White"),
    7: ("sprites/3000.png", 2500, LAYOUT_HEART, "The 3000"),
    8: ("sprites/Alone in a Disco.png", 1700, LAYOUT_A, "Alone in a Disco"),
    9: ("sprites/Far Away.png", 5000, LAYOUT_SQUARE, "Far Away")
}
DEFAULT_LEVEL_DATA = ("sprites/Pyramids Somewhere.png", 2000, LAYOUT_SQUARE, "Unknown")
select_sound = pygame.mixer.Sound(resource_path("sounds/click.wav"))
swap_sound = pygame.mixer.Sound(resource_path("sounds/slide.wav"))
match_sound = pygame.mixer.Sound(resource_path("sounds/match.wav"))
select_sound.set_volume(0.5)
swap_sound.set_volume(0.5)
match_sound.set_volume(0.5)
playlist = [
    "sounds/music1.mp3",
    "sounds/music2.mp3",
    "sounds/music3.mp3",
]
chosen_song = random.choice(playlist)
print(f"Playing: {chosen_song}")
pygame.mixer.music.load(resource_path(chosen_song))
pygame.mixer.music.set_volume(.5)
pygame.mixer.music.play(-1)
menu_bg = pygame.image.load(resource_path("sprites/Far Away.png"))
menu_bg = pygame.transform.scale(menu_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load(resource_path("sprites/Pyramids Somewhere.png"))
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
for filename in gem_files:
    img = pygame.image.load(resource_path(filename)).convert_alpha()
    img = pygame.transform.scale(img, (CELL_SIZE - 10, CELL_SIZE - 10))
    GEM_IMAGES.append(img)
def main_menu():
    run_menu = True
    btn_play = Button("PLAY", 10, 200, 200, 60, (0, 128, 0), (0, 200, 0))
    btn_settings = Button("SETTINGS", 10, 280, 200, 60, (0, 128, 0), (0, 200, 0))
    btn_quit = Button("QUIT", 10, 360, 200, 60, (0, 128, 0), (0, 200, 0))
    while run_menu:
        if menu_bg:
            screen.blit(menu_bg, (0, 0))
        else:
            screen.fill((20, 20, 40))
        title_text = font.render("game made in paint", True, HIGHLIGHT)
        screen.blit(title_text, (10, 50))
        dev_text = small_font.render("Cotangent Games, 2026", True, HIGHLIGHT)
        screen.blit(dev_text, (540, 570))
        btn_play.draw(screen)
        btn_settings.draw(screen)
        btn_quit.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if btn_play.is_clicked(event):
                select_sound.play()
                return "LEVEL_SELECT"
            if btn_settings.is_clicked(event):
                select_sound.play()
                return "SETTINGS"
            if btn_quit.is_clicked(event):
                return "QUIT"
def settings_menu():
    run_settings = True
    btn_fullscreen = Button("TOGGLE FULLSCREEN", 250, 150, 300, 60, (0, 100, 200), (0, 150, 255))
    btn_vol_up = Button("VOL +", 500, 250, 100, 60, (0, 128, 0), (0, 200, 0))
    btn_vol_down = Button("VOL -", 200, 250, 100, 60, (128, 0, 0), (200, 0, 0))
    btn_back = Button("BACK", 50, 500, 150, 50, (100, 100, 100), (150, 150, 150))
    while run_settings:
        screen.fill((30, 30, 30))
        title = font.render("SETTINGS", True, WHITE)
        screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, 50)))
        dev_text = small_font.render("Cotangent Games, 2026", True, HIGHLIGHT)
        screen.blit(dev_text, (540, 570))
        current_vol = round(pygame.mixer.music.get_volume() * 100)
        vol_text = small_font.render(f"VOLUME: {current_vol}%", True, WHITE)
        screen.blit(vol_text, vol_text.get_rect(center=(SCREEN_WIDTH // 2, 280)))
        btn_fullscreen.draw(screen)
        btn_vol_up.draw(screen)
        btn_vol_down.draw(screen)
        btn_back.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if btn_fullscreen.is_clicked(event):
                select_sound.play()
                is_fullscreen = pygame.display.get_surface().get_flags() & pygame.FULLSCREEN
                if is_fullscreen:
                    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                else:
                    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
            if btn_vol_up.is_clicked(event):
                new_vol = min(1.0, pygame.mixer.music.get_volume() + 0.1)
                pygame.mixer.music.set_volume(new_vol)
                select_sound.set_volume(new_vol)
                swap_sound.set_volume(new_vol)
                match_sound.set_volume(new_vol)
                select_sound.play()
            if btn_vol_down.is_clicked(event):
                new_vol = max(0.0, pygame.mixer.music.get_volume() - 0.1)
                pygame.mixer.music.set_volume(new_vol)
                select_sound.set_volume(new_vol)
                swap_sound.set_volume(new_vol)
                match_sound.set_volume(new_vol)
                select_sound.play()
            if btn_back.is_clicked(event):
                select_sound.play()
                return "MENU"
def level_select_menu():
    run_levels = True
    level_buttons = []
    cols = 5
    start_x = 50
    start_y = 150
    spacing_x = 140
    spacing_y = 120
    for i in range(1, NUM_LEVELS + 1):
        level_data = LEVEL_CONFIG.get(i, DEFAULT_LEVEL_DATA)
        image_filename = level_data[0]
        col = (i - 1) % cols
        row = (i - 1) // cols
        x = start_x + (col * spacing_x)
        y = start_y + (row * spacing_y)
        btn = Button(text=str(i), x=x, y=y, width=120, height=80, color=(0, 0, 0), hover_color=(50, 50, 50),
                     action_id=i, image_path=image_filename)
        level_buttons.append(btn)
    btn_back = Button("BACK", 50, 500, 150, 50, (100, 100, 100), (150, 150, 150))
    btn_random = Button("GENERATE RANDOM LEVEL", SCREEN_WIDTH - 450, 500, 400, 50, (100, 0, 100), (150, 0, 150))
    while run_levels:
        if menu_bg:
            screen.blit(menu_bg, (0, 0))
        else:
            screen.fill((20, 20, 40))
        title = font.render("SELECT LEVEL", True, WHITE)
        screen.blit(title, (270, 50))
        dev_text = small_font.render("Cotangent Games, 2026", True, HIGHLIGHT)
        screen.blit(dev_text, (540, 570))
        for btn in level_buttons:
            btn.draw(screen)
        btn_back.draw(screen)
        btn_random.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT", None
            if btn_back.is_clicked(event):
                return "MENU", None
            if btn_random.is_clicked(event):
                select_sound.play()
                rnd_bg = random.choice(ALL_BACKGROUNDS)
                rnd_layout = random.choice(ALL_LAYOUTS)
                rnd_score = random.randint(1000, 3500)
                random_level_data = (rnd_bg, rnd_score, rnd_layout, "Random Generated")
                return "GAME", random_level_data
            for btn in level_buttons:
                if btn.is_clicked(event):
                    select_sound.play()
                    return "GAME", btn.action_id
def show_win_screen(score):
    s = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    s.set_alpha(200)
    s.fill((0, 0, 0))
    screen.blit(s, (0, 0))
    title = font.render("LEVEL COMPLETE!", True, HIGHLIGHT)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    click_text = font.render("Click to Continue", True, (200, 200, 200))
    screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)))
    screen.blit(score_text, score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10)))
    screen.blit(click_text, click_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)))
    pygame.display.flip()
    pygame.time.delay(500)
    pygame.event.clear()
    waiting = True
    match_sound.play()
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.MOUSEBUTTONDOWN:
                return "LEVEL_SELECT"
def run_game(level_input, DEFAULT_LEVEL_DATA):
    if isinstance(level_input, tuple):
        filename = level_input[0]
        target_score = level_input[1]
        level_layout = level_input[2]
        level_text = level_input[3]
        print(f"DEBUG: Loading Random Level: {filename}, Score: {target_score}")
    else:
        level_id = level_input
        level_data = LEVEL_CONFIG.get(level_id, DEFAULT_LEVEL_DATA)
        filename = level_data[0]
        target_score = level_data[1]
        level_layout = level_data[2]
        level_text = level_data[3] if len(level_data) > 3 else "Unknown Level"
        print(f"DEBUG: Loading Level {level_id} using image: {filename}")
    current_bg = None
    current_bg = pygame.image.load(resource_path(filename)).convert()
    current_bg = pygame.transform.scale(current_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    grid = create_grid(level_layout)
    selected = None
    matched_cells = find_matches(grid)
    score = 0
    active_hint = None
    no_moves_timer = 0
    btn_back = Button("MENU", 10, 10, 100, 40, (100, 100, 100), (150, 150, 150))
    while True:
        matches = find_matches(grid)
        if not matches: break
        score += len(matches) * 10
        match_sound.play()
        draw_grid(grid, selected, matches, score, target_score, current_bg, active_hint, level_text)
        pygame.display.flip()
        pygame.time.delay(300)
        delete_matches(grid, matches)
        draw_grid(grid, selected, set(), score, target_score, current_bg, active_hint, level_text)
        pygame.display.flip()
        pygame.time.delay(100)
        apply_gravity(grid)
        draw_grid(grid, selected, set(), score, target_score, current_bg, active_hint, level_text)
        pygame.display.flip()
        pygame.time.delay(200)
        if score >= target_score:
            pygame.time.delay(500)
            return show_win_screen(score)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if btn_back.is_clicked(event):
                select_sound.play()
                return "LEVEL_SELECT"
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if MENU_BUTTON_RECT.collidepoint(mouse_pos):
                    select_sound.play()
                    return "LEVEL_SELECT"
                elif HINT_BUTTON_RECT.collidepoint(mouse_pos):
                    possible_move = find_possible_move(grid)
                    if possible_move:
                        active_hint = possible_move
                        select_sound.play()
                    else:
                        no_moves_timer = pygame.time.get_ticks() + 2000
                        print("No moves! Show warning.")
                    select_sound.play()
                else:
                    clicked_row, clicked_col = get_grid_pos(mouse_pos)
                    if 0 <= clicked_row < GRID_SIZE and 0 <= clicked_col < GRID_SIZE:
                        if active_hint: active_hint = None
                        if grid[clicked_row][clicked_col] == -1:
                            pass
                        elif selected is None:
                            selected = (clicked_row, clicked_col)
                            select_sound.play()
                        else:
                            row1, col1 = selected
                            row2, col2 = clicked_row, clicked_col
                            if (row1, col1) == (row2, col2):
                                selected = None
                            elif abs(row1 - row2) + abs(col1 - col2) == 1:
                                grid[row1][col1], grid[row2][col2] = grid[row2][col2], grid[row1][col1]
                                swap_sound.play()
                                selected = None
                                draw_grid(grid, selected, matched_cells, score, target_score, current_bg, active_hint,
                                          level_text)
                                pygame.display.flip()
                                pygame.time.delay(250)
                                matches = find_matches(grid)
                                if not matches:
                                    grid[row1][col1], grid[row2][col2] = grid[row2][col2], grid[row1][col1]
                                    swap_sound.play()
                                else:
                                    while True:
                                        matches = find_matches(grid)
                                        if not matches: break
                                        points = len(matches) * 10
                                        if len(matches) >= 4: points += 20
                                        if len(matches) >= 5: points += 50
                                        score += points
                                        if score >= target_score:
                                            draw_grid(grid, selected, matched_cells, score, target_score, current_bg,
                                                      active_hint, level_text)
                                            pygame.display.flip()
                                            pygame.time.delay(500)
                                            return show_win_screen(score)
                                        match_sound.play()
                                        draw_grid(grid, selected, matched_cells, score, target_score, current_bg,
                                                  active_hint, level_text)
                                        pygame.display.flip()
                                        pygame.time.delay(300)
                                        delete_matches(grid, matches)
                                        draw_grid(grid, selected, matched_cells, score, target_score, current_bg,
                                                  active_hint, level_text)
                                        pygame.display.flip()
                                        pygame.time.delay(100)
                                        apply_gravity(grid)
                                        draw_grid(grid, selected, matched_cells, score, target_score, current_bg,
                                                  active_hint, level_text)
                                        pygame.display.flip()
                                        pygame.time.delay(200)
                            else:
                                selected = (clicked_row, clicked_col)
                                select_sound.play()
        draw_grid(grid, selected, matched_cells, score, target_score, current_bg, active_hint, level_text)
        current_time = pygame.time.get_ticks()
        if no_moves_timer > 0 and current_time < no_moves_timer:
            s = pygame.Surface((400, 120))
            s.set_alpha(220)
            s.fill((0, 0, 0))
            screen.blit(s, ((SCREEN_WIDTH // 2) - 200, (SCREEN_HEIGHT // 2) - 60))
            warn_text = bigfont.render("NO MOVES LEFT!", True, (255, 50, 50))
            warn_rect = warn_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
            screen.blit(warn_text, warn_rect)
            sub_text = small_font.render("Please Restart the Level", True, (255, 255, 255))
            sub_rect = sub_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25))
            screen.blit(sub_text, sub_rect)
            pygame.draw.rect(screen, (255, 255, 255), ((SCREEN_WIDTH // 2) - 200, (SCREEN_HEIGHT // 2) - 60, 400, 120),
                             3)
        if score >= target_score:
            result = show_win_screen(score)
            return result
        pygame.display.flip()
def create_grid(layout=None):
    if layout is None:
        layout = LAYOUT_SQUARE
    new_grid = []
    for row in range(GRID_SIZE):
        grid_row = []
        for col in range(GRID_SIZE):
            if layout[row][col] == 0:
                grid_row.append(-1)
                continue
            while True:
                gem = random.randint(0, len(GEM_IMAGES) - 1)
                if col >= 2:
                    if gem == grid_row[col - 1] and gem == grid_row[col - 2]:
                        continue
                if row >= 2:
                    if gem == new_grid[row - 1][col] and gem == new_grid[row - 2][col]:
                        continue
                grid_row.append(gem)
                break
        new_grid.append(grid_row)
    return new_grid
def draw_grid(grid, selected_cell, matched_cells, score, target_score, bg_image, hint_moves=None, level_text="Unknown"):
    if bg_image:
        screen.blit(bg_image, (0, 0))
    else:
        screen.fill(BLACK)
    if hint_moves:
        (r1, c1), (r2, c2) = hint_moves
        rect1 = pygame.Rect((c1 * CELL_SIZE) + OFFSET_X, (r1 * CELL_SIZE) + OFFSET_Y, CELL_SIZE, CELL_SIZE)
        rect2 = pygame.Rect((c2 * CELL_SIZE) + OFFSET_X, (r2 * CELL_SIZE) + OFFSET_Y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (255, 255, 255), rect1, 4, border_radius=10)
        pygame.draw.rect(screen, (255, 255, 255), rect2, 4, border_radius=10)
    selected_draw_info = None
    score_box_x = 550
    score_box_y = 65
    score_box_width = 200
    score_box_height = 80
    score_surface = pygame.Surface((score_box_width, score_box_height))
    score_surface.set_alpha(150)
    score_surface.fill((0, 0, 0))
    screen.blit(score_surface, (score_box_x, score_box_y))
    pygame.draw.rect(screen, WHITE, (score_box_x, score_box_y, score_box_width, score_box_height), 2)
    score_text = small_font.render(f"Score: {score} / {target_score}", True, WHITE)
    text_rect = score_text.get_rect(center=(score_box_x + score_box_width // 2, score_box_y + score_box_height // 2))
    screen.blit(score_text, text_rect)
    board_width = GRID_SIZE * CELL_SIZE
    board_height = GRID_SIZE * CELL_SIZE
    board_surface = pygame.Surface((board_width, board_height))
    board_surface.set_alpha(150)
    board_surface.fill((0, 0, 0))
    screen.blit(board_surface, (OFFSET_X, OFFSET_Y))
    pygame.draw.rect(screen, WHITE, (OFFSET_X, OFFSET_Y, board_width, board_height), 3)
    s_menu = pygame.Surface((MENU_BUTTON_RECT.width, MENU_BUTTON_RECT.height))
    s_menu.set_alpha(150)
    s_menu.fill((0, 0, 0))
    screen.blit(s_menu, (MENU_BUTTON_RECT.x, MENU_BUTTON_RECT.y))
    pygame.draw.rect(screen, WHITE, MENU_BUTTON_RECT, 2)
    text_menu = font.render("MENU", True, WHITE)
    text_rect_menu = text_menu.get_rect(center=MENU_BUTTON_RECT.center)
    screen.blit(text_menu, text_rect_menu)
    s = pygame.Surface((HINT_BUTTON_RECT.width, HINT_BUTTON_RECT.height))
    s.set_alpha(150)
    s.fill((0, 0, 0))
    screen.blit(s, (HINT_BUTTON_RECT.x, HINT_BUTTON_RECT.y))
    pygame.draw.rect(screen, WHITE, HINT_BUTTON_RECT, 2)
    text = font.render("HINT", True, WHITE)
    text_rect = text.get_rect(center=HINT_BUTTON_RECT.center)
    screen.blit(text, text_rect)
    s = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    s.set_alpha(89)
    s.fill((0, 0, 0))
    screen.blit(s, (0, 0))
    shadow_surf = small_font.render(level_text, True, BLACK)
    screen.blit(shadow_surf, (22, SCREEN_HEIGHT - 40 + 2))
    text_surf = small_font.render(level_text, True, WHITE)
    screen.blit(text_surf, (20, SCREEN_HEIGHT - 40))
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            gem_value = grid[row][col]
            if gem_value == -1 or gem_value == EMPTY_SPOT:
                continue
            x = (col * CELL_SIZE) + OFFSET_X
            y = (row * CELL_SIZE) + OFFSET_Y
            if selected_cell == (row, col):
                selected_draw_info = (gem_value, x, y)
                continue
            if 0 <= gem_value < len(GEM_IMAGES):
                gem_sprite = GEM_IMAGES[gem_value]
                screen.blit(gem_sprite, (x + 5, y + 5))
                if (row, col) in matched_cells:
                    gem_rect = pygame.Rect(x + 5, y + 5, CELL_SIZE - 10, CELL_SIZE - 10)
                    pygame.draw.rect(screen, WHITE, gem_rect, 5, border_radius=10)
    if selected_draw_info:
        val, sx, sy = selected_draw_info
        normal_rect = pygame.Rect(sx + 5, sy + 5, CELL_SIZE - 10, CELL_SIZE - 10)
        pygame.draw.rect(screen, HIGHLIGHT, normal_rect, 4, border_radius=10)
        if 0 <= val < len(GEM_IMAGES):
            original_img = GEM_IMAGES[val]
            scale_factor = 1.25
            new_width = int(original_img.get_width() * scale_factor)
            new_height = int(original_img.get_height() * scale_factor)
            big_img = pygame.transform.scale(original_img, (new_width, new_height))
            center_x = sx + (CELL_SIZE // 2)
            center_y = sy + (CELL_SIZE // 2)
            big_rect = big_img.get_rect(center=(center_x, center_y))
            screen.blit(big_img, big_rect)
def get_grid_pos(mouse_pos):
    mx, my = mouse_pos
    mx -= OFFSET_X
    my -= OFFSET_Y
    if mx < 0 or my < 0:
        return -1, -1
    row = my // CELL_SIZE
    col = mx // CELL_SIZE
    if row >= GRID_SIZE or col >= GRID_SIZE:
        return -1, -1
    return row, col
def find_matches(grid):
    matches = set()
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE - 2):
            if grid[r][c] >= 0:
                if grid[r][c] == grid[r][c + 1] == grid[r][c + 2]:
                    matches.add((r, c))
                    matches.add((r, c + 1))
                    matches.add((r, c + 2))
    for c in range(GRID_SIZE):
        for r in range(GRID_SIZE - 2):
            if grid[r][c] >= 0:
                if grid[r][c] == grid[r + 1][c] == grid[r + 2][c]:
                    matches.add((r, c))
                    matches.add((r + 1, c))
                    matches.add((r + 2, c))
    return matches
def delete_matches(grid, matches):
    for (row, col) in matches:
        grid[row][col] = EMPTY_SPOT
def apply_gravity(grid):
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE - 1, -1, -1):
            if grid[row][col] == -1:
                continue
            if grid[row][col] == EMPTY_SPOT:
                fill_val = EMPTY_SPOT
                for k in range(row - 1, -1, -1):
                    if grid[k][col] == -1:
                        break
                    if grid[k][col] >= 0:
                        fill_val = grid[k][col]
                        grid[k][col] = EMPTY_SPOT
                        break
                grid[row][col] = fill_val
    for col in range(GRID_SIZE):
        start_row = 0
        while start_row < GRID_SIZE and grid[start_row][col] == -1:
            start_row += 1
        for row in range(start_row, GRID_SIZE):
            if grid[row][col] == -1:
                continue
            if grid[row][col] == EMPTY_SPOT:
                grid[row][col] = random.randint(0, len(GEM_IMAGES) - 1)
def find_possible_move(grid):
    def check_swap(r, c, dr, dc):
        val1 = grid[r][c]
        val2 = grid[r + dr][c + dc]
        if val1 < 0 or val2 < 0:
            return None
        grid[r][c], grid[r + dr][c + dc] = grid[r + dr][c + dc], grid[r][c]
        matches = find_matches(grid)
        grid[r][c], grid[r + dr][c + dc] = grid[r + dr][c + dc], grid[r][c]
        if matches:
            return ((r, c), (r + dr, c + dc))
        return None
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if c < GRID_SIZE - 1:
                move = check_swap(r, c, 0, 1)
                if move: return move
            if r < GRID_SIZE - 1:
                move = check_swap(r, c, 1, 0)
                if move: return move
    return None
if __name__ == "__main__":
    current_state = "MENU"
    selected_level = 1
    while current_state != "QUIT":
        if current_state == "MENU":
            current_state = main_menu()
        elif current_state == "SETTINGS":
            current_state = settings_menu()
        elif current_state == "LEVEL_SELECT":
            result = level_select_menu()
            if isinstance(result, tuple):
                current_state, level_choice = result
                if level_choice:
                    selected_level = level_choice
                    print(f"DEBUG: Level selected: {selected_level}")
            else:
                current_state = result
        elif current_state == "GAME":
            current_state = run_game(selected_level, DEFAULT_LEVEL_DATA)
    pygame.quit()
