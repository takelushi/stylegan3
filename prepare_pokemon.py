
import shutil
from pathlib import Path

from PIL import Image

SRC_PATH_STR = "data/pokemon"
DST_PATH_STR = "data/pokemon_no_alpha"

SRC_PATH = Path(SRC_PATH_STR)
DST_PATH = Path(DST_PATH_STR)

CLEAR_DST = True


def prepare_pokemon(image):
    # ARGB -> RGB
    image = image.convert("RGB")

    # 画像を128x128にクロップ
    image = image.crop((-4, -4, 124, 124))
    return image


def main():
    if CLEAR_DST:
        shutil.rmtree(DST_PATH, ignore_errors=True)

    DST_PATH.mkdir(parents=True, exist_ok=True)

    for file in SRC_PATH.iterdir():
        if file.name.endswith(".png"):
            image = prepare_pokemon(Image.open(file))
            image.save(DST_PATH / file.name)


if __name__ == '__main__':
    main()
