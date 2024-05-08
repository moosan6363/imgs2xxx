import argparse
import os
from fpdf import FPDF

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert images to PDF")
    parser.add_argument("--dir", type=str, help="Directory containing images")

    args = parser.parse_args()

    exts = [".jpg", ".png", "jpeg", "webp"]

    # Get the file paths in the directory
    img_paths = [
        os.path.join(args.dir, filename)
        for filename in os.listdir(args.dir)
        if os.path.splitext(filename)[1].lower() in exts
    ]
    # file_paths = [os.path.join(args.dir, filename) for filename in os.listdir(args.dir)]

    # Sort the file paths in alphabetical order
    img_paths.sort()

    # Create a PDF file
    pdf = FPDF()
    for img_path in img_paths:
        pdf.add_page()
        pdf.image(img_path, 0, 0, 210, 297)

    pdf.output("output.pdf", "F")
