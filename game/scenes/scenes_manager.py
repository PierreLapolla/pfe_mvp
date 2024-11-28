from typing import Optional

from .base_scene import BaseScene
from .image_scene import ImageScene
from .menu_scene import MenuScene
from ..utils.logger import log


class ScenesManager:
    def __init__(self):
        self.scenes = {}

        self.register_scene("menu", MenuScene())
        self.register_scene("image", ImageScene())

        self.current_scene_key = "menu"

    def register_scene(self, key: str, scene: BaseScene) -> None:
        """
        Register a scene with a specific key.

        :param key: Identifier for the scene.
        :param scene: The scene object.
        """
        self.scenes[key] = scene

    def switch_scene(self, key: str) -> None:
        """
        Switch to a different scene by key.

        :param key: Identifier of the scene to switch to.
        """
        if key in self.scenes:
            self.current_scene_key = key
        else:
            log.error(f"scene with key '{key}' not found.")
            raise KeyError(f"Scene with key '{key}' not found.")

    def get_current_scene(self) -> Optional[BaseScene]:
        """
        Get the current active scene.

        :return: The current scene or None if no scene is active.
        """
        return self.scenes.get(self.current_scene_key, None)
