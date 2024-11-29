from abc import ABC, abstractmethod
from typing import Union



class BaseScene(ABC):
    def __init__(self):
        self.next_scene = self

    @abstractmethod
    def handle_events(self, events) -> Union[str, bool]:
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass
