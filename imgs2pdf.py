import argparse
import os

from PIL import Image

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert images to PDF")
    parser.add_argument("--dir", type=str, help="Directory containing images")

    args = parser.parse_args()

    exts = [".jpg", ".png", ".jpeg", ".webp"]

    # Get the file paths in the directory
    img_paths = [
        os.path.join(args.dir, filename)
        for filename in os.listdir(args.dir)
        if os.path.splitext(filename)[1].lower() in exts
    ]

    img_paths.sort()

    images = []
    for img_path in img_paths:
        with Image.open(img_path) as img:
            images.append(img.copy())

    if images:
        images[0].save(
            f"{os.path.basename(args.dir)}.pdf",
            save_all=True,
            append_images=images[1:],
            resolution=100.0,
        )
