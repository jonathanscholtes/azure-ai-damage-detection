import cv2
import os
from pathlib import Path

RAW_DIR = Path("../../data/raw")
OUTPUT_DIR = Path("../../data/transformed")
TARGET_SIZE = (1536, 1024)  # width, height

def resize_with_padding(image, target_size):
    """Resize an image to target size while preserving aspect ratio with padding."""
    h, w = image.shape[:2]
    target_w, target_h = target_size

    # Compute scale and padding
    scale = min(target_w / w, target_h / h)
    new_w, new_h = int(w * scale), int(h * scale)
    resized = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)

    # Create new image and center the resized one
    result = cv2.copyMakeBorder(
        resized,
        top=(target_h - new_h) // 2,
        bottom=(target_h - new_h + 1) // 2,
        left=(target_w - new_w) // 2,
        right=(target_w - new_w + 1) // 2,
        borderType=cv2.BORDER_CONSTANT,
        value=[0, 0, 0],  # black padding
    )

    return result


def preprocess_images():
    """Resize all images from data/raw/ into 1536x1024 and save to data/."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    count = 0

    for img_path in RAW_DIR.glob("*.*"):
        if img_path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
            continue

        img = cv2.imread(str(img_path))
        if img is None:
            print(f"⚠️ Skipping unreadable file: {img_path}")
            continue

        processed = resize_with_padding(img, TARGET_SIZE)
        output_path = OUTPUT_DIR / img_path.name
        cv2.imwrite(str(output_path), processed)
        count += 1

        print(f"✅ Saved: {output_path.name} ({TARGET_SIZE[0]}x{TARGET_SIZE[1]})")

    print(f"\n✅ Preprocessing complete — {count} images resized and saved to {OUTPUT_DIR}/")


if __name__ == "__main__":
    preprocess_images()
