from PIL import Image 
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

df = pd.read_csv("data/image_metadata.csv")

img1 = df[df["name"] == "Chungthang Dam Pre GLOF 2022.jpg"].iloc[0]['name']
img2 = df[df["name"] == "Chungthang Dam Post GLOF 2026.jpg"].iloc[0]['name']
print(img1)

img1_path = Path("data/raw") / img1 
img2_path = Path("data/raw") / img2

# with Image.open(img1_path) as img_1:
#     plt.imshow(img_1)
#     plt.title("Chungthang Dam - Pre-GLOF (2022)")
#     plt.axis("off")
#     plt.show()

with Image.open(img1_path) as img_1, Image.open(img2_path) as img_2:
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    axes[0].imshow(img_1)
    axes[1].imshow(img_2)

    axes[0].set_title("Pre-GLOF (2022)")
    axes[1].set_title("Post-GLOF (2026)")

    axes[0].axis('off')
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()
    


