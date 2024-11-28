# TODO: check dataclasses and modify this

from dataclasses import dataclass
from pathlib import Path

import pygame


@dataclass
class Card:
    name: str
    image_path: Path
    description: str
    attack: int
    defense: int

    def load_image(self) -> pygame.Surface:
        return pygame.image.load(str(self.image_path))

    def render(self, screen: pygame.Surface, position: pygame.Rect) -> None:
        image = self.load_image()
        screen.blit(image, position)
