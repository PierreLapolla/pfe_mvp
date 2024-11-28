from typing import Optional
from .base_scene import BaseScene
from .menu_scene import MenuScene

class ScenesManager:
    def __init__(self):
        self.scene_stack = []

        self.push_scene(MenuScene())

    def get_current_scene(self) -> Optional[BaseScene]:
        """
        Returns the current active scene.

        :return: The current scene or None if no scenes exist.
        """
        return self.scene_stack[-1] if self.scene_stack else None

    def push_scene(self, scene: BaseScene) -> None:
        """
        Pushes a new scene onto the stack.

        :param scene: The scene to push.
        :return: None
        """
        self.scene_stack.append(scene)

    def pop_scene(self) -> Optional[BaseScene]:
        """
        Removes the top scene from the stack and returns it.

        :return: The removed scene or None if no scenes exist.
        """
        return self.scene_stack.pop() if self.scene_stack else None

    def switch_scene(self, scene: BaseScene) -> None:
        """
        Replaces the current scene with a new one.

        :param scene: The new scene to switch to.
        :return: None
        """
        if self.scene_stack:
            self.scene_stack.pop()
        self.scene_stack.append(scene)

    def clear_scenes(self) -> None:
        """
        Clears all scenes from the stack.

        :return: None
        """
        self.scene_stack.clear()
