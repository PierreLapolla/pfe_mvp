import pygame

from .base_scene import BaseScene
from ..utils.assets_manager import assets
from ..utils.config_loader import config


class ImageScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.img = assets.get("default")
        self.img_pos = (config.screen.width // 2 - self.img.get_width() // 2,
                        config.screen.height // 2 - self.img.get_height() // 2)

    def handle_events(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "menu"

            if event.key == pygame.K_LEFT:
                self.img_pos = (self.img_pos[0] - 10, self.img_pos[1])
            elif event.key == pygame.K_RIGHT:
                self.img_pos = (self.img_pos[0] + 10, self.img_pos[1])
            elif event.key == pygame.K_UP:
                self.img_pos = (self.img_pos[0], self.img_pos[1] - 10)
            elif event.key == pygame.K_DOWN:
                self.img_pos = (self.img_pos[0], self.img_pos[1] + 10)

        return True

    def update(self) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        screen.blit(self.img, self.img_pos)
