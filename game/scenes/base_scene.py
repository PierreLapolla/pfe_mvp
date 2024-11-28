# game/scenes/base_scene.py
from abc import ABC, abstractmethod

import pygame


class BaseScene(ABC):
    @abstractmethod
    def handle_events(self, event: pygame.event.Event) -> bool:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def render(self, screen: pygame.Surface) -> None:
        pass
