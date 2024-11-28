from pathlib import Path
from typing import Union, Dict, Any

import pygame
from tqdm import tqdm

from .logger import log


class AssetsManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, assets_dir: Union[str, Path]) -> None:
        """
        Initializes the AssetsManager with the assets directory.

        :param assets_dir: The directory where the assets are stored.
        :return: None
        """
        if not hasattr(self, "initialized"):
            self.assets_dir = Path(assets_dir)
            self.assets: Dict[str, Any] = {}
            self.load_assets()
            self.initialized = True

    def load_assets(self) -> None:
        """
        Loads all the assets from the assets directory recursively.

        :return: None
        """
        for asset_path in tqdm(self.assets_dir.rglob("*"), desc="Loading assets"):
            if asset_path.is_file():
                asset_name = asset_path.stem

                try:
                    if asset_path.suffix in [".png", ".jpg", ".jpeg", ".bmp", ".gif"]:
                        self.assets[asset_name] = pygame.image.load(str(asset_path))
                        log.debug(f"loaded image: {asset_name}")

                    elif asset_path.suffix in [".ttf", ".otf"]:
                        self.assets[asset_name] = str(asset_path)
                        log.debug(f"loaded font: {asset_name}")

                    elif asset_path.suffix in [".wav", ".mp3", ".ogg"]:
                        self.assets[asset_name] = pygame.mixer.Sound(str(asset_path))
                        log.debug(f"loaded sound: {asset_name}")

                    else:
                        log.warning(f"unsupported asset type: {asset_path}")

                except Exception as e:
                    log.error(f"failed to load asset {asset_name}: {e}")

    def get(self, asset_name: str, font_size: int = 24) -> Any:
        """
        Retrieves an asset by its name. If the asset is a font, it can be retrieved with a specific size.

        :param asset_name: The name of the asset (filename without extension).
        :param font_size: The size of the font (only applicable for font assets).
        :return: The loaded asset or None if not found.
        """
        asset = self.assets.get(asset_name)
        if not asset:
            log.error(f"asset '{asset_name}' not found.")
            return None

        if isinstance(asset, str):
            return pygame.font.Font(asset, font_size)

        return asset


assets = AssetsManager(Path(__file__).parent.parent.parent / 'assets')

if __name__ == "__main__":
    img = assets.get("gameon")
    print(img)
