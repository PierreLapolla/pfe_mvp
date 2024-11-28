from pathlib import Path
from typing import Any, Union

import yaml
from box import Box

from .logger import log


class ConfigLoader:
    _instance = None

    def __new__(cls, file_path: Union[str, Path]) -> 'ConfigLoader':
        """
        Implement Singleton pattern to ensure a single global instance.

        :param file_path: The path to the configuration YAML file.
        :return: The singleton instance of ConfigLoader.
        """
        if cls._instance is None:
            cls._instance = super(ConfigLoader, cls).__new__(cls)

            file_path = Path(file_path)
            if not file_path.exists():
                log.error(f"config file '{file_path}' not found.")
                raise FileNotFoundError(f"Config file '{file_path}' not found.")

            with open(file_path, 'r') as file:
                cls._instance._config = Box(yaml.safe_load(file) or {})
                log.debug(f"config: {cls._instance._config}")

        return cls._instance

    def __getattr__(self, item) -> Any:
        """
        Allow direct attribute access through dot notation.

        :param item: The configuration key.
        :return: The configuration value.
        """
        if item in self._config:
            return getattr(self._config, item)

        log.error(f"config key '{item}' not found")
        raise AttributeError(f"'ConfigLoader' object has no attribute '{item}'")


config = ConfigLoader(Path(__file__).parent.parent.parent / 'config.yaml')

if __name__ == '__main__':
    print(config.screen.width)
