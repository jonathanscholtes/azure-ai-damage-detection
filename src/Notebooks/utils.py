import base64
import json
import cv2
import numpy as np
import re
from semantic_kernel.contents import ChatHistory, ChatMessageContent, ImageContent, TextContent

def encode_image(path):
    """Load image and return base64 string."""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
    

def fill_prompt(template, before_image, after_image ):
    return template.replace("{{before_image}}", before_image)\
                   .replace("{{after_image}}", after_image)



def build_damage_chat_with_image_examples(
    before_image: str,
    after_image: str,
    img_width: int,
    img_height: int,
    example_pairs: list
):
    """
    Build a ChatHistory that includes few-shot visual examples before the real comparison.
    example_pairs: list of tuples [(before_path, after_path, example_json), ...]
    """
    chat_history = ChatHistory()

    # Few-shot visual examples
    for i, (ex_before, ex_after, size, ex_json) in enumerate(example_pairs, start=1):
        chat_history.add_message(
            ChatMessageContent(
                role="user",
                items=[
                    TextContent(
                        text=(
                            f"Example {i}:\n"
                            f"Here are BEFORE and AFTER images of a damaged vehicle.\n"
                            f"Each image is {size[0]}px wide and {size[1]}px tall.\n"
                            f"Below is the correct analysis JSON for this pair:\n\n"
                            f"{json.dumps(ex_json, indent=2)}"
                        )
                    ),
                    ImageContent.from_image_file(ex_before),
                    ImageContent.from_image_file(ex_after)
                ]
            )
        )

    # The actual query
    chat_history.add_message(
        ChatMessageContent(
            role="user",
            items=[
                TextContent(
                    text=(
                        f"Now analyze the following images in the same way.\n"
                        f"The first image is BEFORE and the second is AFTER.\n"
                        f"relative to the AFTER image dimensions (width={img_width}, height={img_height}). \n "
                        f"Return ONLY valid JSON using pixel coordinates (not normalized).\n"
                        f"Use integer values for coordinates and double quotes for all strings.\n"
                        f"The origin (0,0) is the top-left corner of the image. \n "
                        f"Do not include markdown, explanations, or text outside the JSON.\n\n"
                    )
                ),
                ImageContent.from_image_file(before_image),
                ImageContent.from_image_file(after_image)
            ]
        )
    )

    return chat_history

def parse_damage_json(raw_text: str) -> dict:
    
    
    cleaned = re.sub(r"^```json\s*|```$", "", raw_text.strip(), flags=re.MULTILINE)
    
    # Remove any leading/trailing whitespace
    cleaned = cleaned.strip()
    
    return json.loads(cleaned)



def draw_damage_boxes(image_path: str, damage_data: dict) -> np.ndarray:
    """
    Draw bounding boxes (pixel coordinates only) from damage JSON on the image
    and return the annotated image as RGB.

    Expected JSON format:
    {
        "damage_summary": "...",
        "damage_locations": [
            {
                "type": "dent",
                "severity": "medium",
                "confidence": 0.95,
                "bounding_box": {
                    "x_min": 420,
                    "y_min": 280,
                    "x_max": 520,
                    "y_max": 360
                }
            },
            ...
        ]
    }
    """
    import cv2
    import numpy as np

    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_height, img_width = img.shape[:2]

    for damage in damage_data.get("damage_locations", []):
        box = damage["bounding_box"]

        # --- Expect absolute pixel coordinates ---
        x1, y1, x2, y2 = map(int, (box["x_min"], box["y_min"], box["x_max"], box["y_max"]))

        # Clamp values to image boundaries
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(img_width - 1, x2), min(img_height - 1, y2)

        # Draw rectangle
        color = (255, 0, 0)  # Red
        cv2.rectangle(img_rgb, (x1, y1), (x2, y2), color, 2)

        # Add label
        label = f"{damage.get('type', 'damage')} ({damage.get('severity', '?')})"
        cv2.putText(
            img_rgb,
            label,
            (x1, max(20, y1 - 10)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2,
        )

    return img_rgb
