import pygame

from .base_scene import BaseScene
from ..utils.assets_manager import assets
from ..utils.config_loader import config


class ImageScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.img = assets.get("default")

    def handle_events(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return "menu"
        return True

    def update(self) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        screen.fill((0, 0, 0))
        screen.blit(self.img, (config.screen.width // 2 - self.img.get_width() // 2,
                               config.screen.height // 2 - self.img.get_height() // 2))
