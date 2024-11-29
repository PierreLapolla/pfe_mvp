from typing import Callable, Tuple, Optional, Dict, Any, Union

import pygame

from .assets_manager import assets


class Button:
    def __init__(
            self,
            text: str,
            font: str,
            font_size: int,
            position: Tuple[int, int],
            size: Tuple[int, int],
            callback: Callable[[], Any],
            colors: Optional[Dict[str, Tuple[int, int, int]]] = None
    ) -> None:
        """
        Initialize the button.

        :param text: The text to display on the button.
        :param font: The pygame.font.Font object for rendering text.
        :param position: Tuple (x, y) for the center of the button.
        :param size: Tuple (width, height) for button size.
        :param callback: Function to call when the button is clicked.
        :param colors: Dictionary with keys "normal", "hover", and "clicked" for button colors.
        """
        self.text = text
        self.font = assets.get(font, font_size=font_size)
        self.position = position
        self.size = size
        self.callback = callback
        self.colors = colors or {
            "normal": (100, 100, 100),
            "hover": (150, 150, 150),
            "clicked": (200, 200, 200),
        }
        self.rect = pygame.Rect(0, 0, *self.size)
        self.rect.center = self.position
        self.hovered = False
        self.clicked = False

        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def handle_event(self, event: pygame.event.Event) -> Union[bool, str]:
        """
        Handle mouse events for the button.
        """
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered:
                self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.hovered:
                return self.callback()
            self.clicked = False

        return True


    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw the button on the screen.
        """
        color = (
            self.colors["clicked"] if self.clicked else
            self.colors["hover"] if self.hovered else
            self.colors["normal"]
        )
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
        screen.blit(self.text_surface, self.text_rect)
