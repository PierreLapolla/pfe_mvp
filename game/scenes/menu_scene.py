from .base_scene import BaseScene
import pygame
from ..utils.assets_manager import assets


class MenuScene(BaseScene):
    def __init__(self):
        self.font = assets.get("gameon")
        self.options = ["Start", "Quit"]
        self.selected_index = 0

    def handle_events(self, event: pygame.event.Event) -> bool:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.selected_index = (self.selected_index + 1) % len(self.options)
            elif event.key == pygame.K_UP:
                self.selected_index = (self.selected_index - 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                if self.selected_index == 0:
                    return False
                elif self.selected_index == 1:
                    pygame.quit()
                    exit()
        return True

    def update(self) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        screen.fill((0, 0, 0))
        for idx, option in enumerate(self.options):
            color = (255, 255, 255) if idx == self.selected_index else (100, 100, 100)
            text_surface = self.font.render(option, True, color)
            screen.blit(text_surface, (100, 100 + idx * 40))
