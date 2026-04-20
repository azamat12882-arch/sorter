import os
import sys
import pygame
from pathlib import Path
import getpass
import shutil

# Инициализация
pygame.init()

# Настройки окна
WIDTH = 400
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sorter")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
BLUE = (0, 150, 255)
DARK_BLUE = (0, 100, 200)
GREEN = (0, 255, 0)

# Шрифт
font = pygame.font.Font(None, 30)

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.is_hovered = False
    
    def draw(self, screen):
        # Меняем цвет при наведении
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)  # рамка
        
        # Рисуем текст
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            # Проверяем наведение
            self.is_hovered = self.rect.collidepoint(event.pos)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                if self.rect.collidepoint(event.pos):
                    if self.action:
                        self.action()

def button1_action():
    with open('config.txt', 'r') as f:
        sorting_path = f.read()
    
    for item in os.listdir(sorting_path):
        source = os.path.join(sorting_path, item)
        if not os.path.isfile(source):
            continue  # пропускаем папки
        
        ext = os.path.splitext(item)[1].lower()  # получаем расширение в нижнем регистре
        
        # Текстовые файлы
        if ext in [".txt", ".md"]:
            dest_folder = sorting_path + "text/"
            shutil.move(source, dest_folder)
            
        # Документы
        elif ext in [".docx", ".pptx", ".xlsx", ".doc", ".ppt", ".xls", ".pdf", ".drawio", ".rtf", ".vsd", ".vsdx", ".vsdm", ".vstx", ".vssx"]:
            dest_folder = sorting_path + "documents/"
            shutil.move(source, dest_folder)
            
        # Изображения
        elif ext in [".png", ".jpeg", ".jpg", ".webp", ".gif", ".svg", ".avif", ".tiff", ".tif", ".bmp", ".heic", ".eps", ".ai", ".cdr", ".dng", ".cr2", ".cr3", ".nef", ".arw", ".raf", ".psd", ".ico", ".icns", ".exr"]:
            dest_folder = sorting_path + "images/"
            shutil.move(source, dest_folder)

        # Видео
        elif ext in [".mp4", ".avi", ".mov", ".mkv", ".webm", ".flv", ".f4v", ".mts", ".m2ts", ".3gp", ".3g2", ".vob", ".ifo"]:
            dest_folder = sorting_path + "video/"
            shutil.move(source, dest_folder)
        
        # Архивы
        elif ext in [".zip", ".rar", ".7z", ".tar", ".tar.gz", ".tgz", ".tar.xz", "gz", ".bz2", ".cab", "iso", ".zst"]:
            dest_folder = sorting_path + "archives/"
            shutil.move(source, dest_folder)

        # Аудио
        elif ext in [".mp3", ".aac", ".ogg", ".opus", ".wma", ".flac", ".alac", ".m4a", ".wav", ".aiff", ".dff", ".dsf", ".mid", ".midi"]:
            dest_folder = sorting_path + "audio/"
            shutil.move(source, dest_folder)

        # Шрифты
        elif ext in [".ttf", ".otf", ".woff", ".woff2", ".eot", ".pfa", ".pfb", ".fon", ".bdf", ".pcf", ".ttc"]:
            dest_folder = sorting_path + "fonts/"
            shutil.move(source, dest_folder)

        # Торренты
        elif ext in [".torrent"]:
            dest_folder = sorting_path + "torrents/"
            shutil.move(source, dest_folder)

# Создаём кнопки
button1 = Button(70, 120, 270, 50, "запустить сортировку", BLUE, DARK_BLUE, button1_action)

buttons = [button1]

# Главный цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Передаём события всем кнопкам
        for button in buttons:
            button.handle_event(event)
    
    # Отрисовка
    screen.fill(DARK_GRAY)
    
    for button in buttons:
        button.draw(screen)
    
    pygame.display.flip()

pygame.quit()
sys.exit()