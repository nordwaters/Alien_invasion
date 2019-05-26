import sys
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from button import Button


def run_game():

    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Play")

    # Создание экземпляра для хранения игровой статистики.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Создание корабля, группы пуль и группы пришельцев.
    ship = Ship(ai_settings, screen)

    # Создание группы для хранения пуль.
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # Запуск основного цикла игры.

    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                    aliens, bulletss)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                        bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                        bullets)
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                             play_button)

        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # При каждом проходе цикла перерисовывается экран.
            screen.fill(ai_settings.bg_color)

            ship.blitme()
            # Отображение последнего прорисованного экрана.
            pygame.display.flip()


run_game()

