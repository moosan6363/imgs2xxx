import argparse
import os

from PIL import Image

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--indir", type=str, help="Directory containing images")
    parser.add_argument(
        "--outdir", type=str, help="Output directory for converted images"
    )
    args = parser.parse_args()

    in_exts = [".jpg", ".png", ".jpeg", ".webp"]
    out_ext = ".png"

    # Get the file paths in the directory
    img_paths = [
        os.path.join(args.indir, filename)
        for filename in os.listdir(args.indir)
        if os.path.splitext(filename)[1].lower() in in_exts
    ]
    img_paths.sort()

    for img_path in img_paths:
        try:
            # Open the WebP image
            with Image.open(img_path) as img:
                # Convert the image to PNG format
                output_file = os.path.join(
                    args.outdir,
                    os.path.splitext(os.path.basename(img_path))[0] + out_ext,
                )
                img.save(output_file, "png")
            print(f"Conversion successful: {img_path} -> {output_file}")
        except Exception as e:
            print(f"Error converting WebP to PNG: {e}")

    print("Conversion complete!")
