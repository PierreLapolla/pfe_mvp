import pygame

from .scenes.base_scene import BaseScene
from .scenes.scenes_manager import ScenesManager
from .utils.config_loader import config


class GameLoop:
    def __init__(self) -> None:
        """
        Initializes the game loop with screen dimensions and title.
        """

        self.screen = pygame.display.set_mode((config.screen.width, config.screen.height))
        pygame.display.set_caption(config.screen.title)
        self.clock = pygame.time.Clock()

        self.scenes_manager = ScenesManager()

        self.running = True
        self.run()

    def handle_events(self, current_scene: BaseScene) -> None:
        """
        Handles the events and delegates to the current scene.

        :param current_scene: The current scene to handle the events.
        :return: None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if not current_scene.handle_events(event):
                self.running = False

    def update(self, current_scene: BaseScene) -> None:
        """
        Updates the current scene logic.

        :param current_scene: The current scene to update.
        :return: None
        """
        current_scene.update()

    def render(self, current_scene: BaseScene) -> None:
        """
        Renders the current scene.

        :param current_scene: The current scene to render.
        :return: None
        """
        current_scene.render(self.screen)
        pygame.display.flip()

    def run(self) -> None:
        """
        Main loop of the game.

        :return: None
        """
        while self.running:
            current_scene = self.scenes_manager.get_current_scene()
            self.handle_events(current_scene)
            self.update(current_scene)
            self.render(current_scene)
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    game = GameLoop()
