import pygame

from .base_scene import BaseScene
from ..utils.button import Button
from ..utils.config_loader import config


class MenuScene(BaseScene):
    def __init__(self) -> None:
        super().__init__()
        x_center = config.screen.width // 2
        y_center = config.screen.height // 2
        self.buttons: list[Button] = [
            Button("Show image", "gameon", 24, (x_center, 200), (200, 50), self.show_image),
            Button("Quit", "gameon", 24, (x_center, 300), (200, 50), self.quit_game),
        ]

    def show_image(self):
        return "image"

    def quit_game(self):
        return False

    def handle_events(self, event: pygame.event.Event):
        for button in self.buttons:
            result = button.handle_event(event)
            if result is not True:
                return result

        return True

    def update(self) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        for button in self.buttons:
            button.draw(screen)
