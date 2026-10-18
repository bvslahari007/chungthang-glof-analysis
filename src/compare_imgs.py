
from PIL import Image
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

# read image metadata
df = pd.read_csv("data/image_metadata.csv")


def createImageSubPlot(img1_path, img2_path, count):
    with Image.open(img1_path) as img_1, Image.open(img2_path) as img_2:
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        axes[0].imshow(img_1)
        axes[1].imshow(img_2)

        axes[0].set_title("Pre-GLOF (2022)")
        axes[1].set_title("Post-GLOF (2026)")

        axes[0].axis("off")
        axes[1].axis("off")

        fig.tight_layout()

        # save the comparison
        op_dir = Path("outputs/image_comparisons")
        op_path = op_dir / f"Comparison {count}.jpg"

        fig.savefig(op_path, dpi=150, bbox_inches="tight")
        plt.close(fig)


# image pairs: pre-GLOF first, post-GLOF second
image_pairs = [
    (
        "Chungthang Dam Pre GLOF 2022.jpg",
        "Chungthang Dam Post GLOF 2026.jpg",
    ),
    (
        "Chungthang Pre GLOF 2022.jpg",
        "Chungthang Post GLOF 2026.jpg",
    ),
    (
        "Confluence Pre GLOF 2022.jpg",
        "Confluence Post GLOF 2026.jpg",
    ),
]

# generating comparisons here
for count, (pre_name, post_name) in enumerate(image_pairs, start=1):
    pre_row = df.loc[df["name"] == pre_name, "name"]
    post_row = df.loc[df["name"] == post_name, "name"]

    if pre_row.empty or post_row.empty:
        print(f"Skipping pair {count}: filename not found in metadata.")
        continue

    img1_path = Path("data/raw") / pre_row.iloc[0]
    img2_path = Path("data/raw") / post_row.iloc[0]

    createImageSubPlot(img1_path, img2_path, count)

    print(f"Saved comparison {count}")
