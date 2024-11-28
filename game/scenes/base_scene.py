from abc import ABC, abstractmethod


class BaseScene(ABC):
    def __init__(self):
        self.next_scene = self

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass
