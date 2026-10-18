from PIL import Image
from pathlib import Path
import pandas as pd

folder = Path("data/raw")

if not folder.exists():
    raise FileNotFoundError("Input folder does not exist.")

k = folder.glob("*.jpg")

details = []

k = list(folder.glob("*.jpg"))

if not k:
    raise FileNotFoundError(
        f"No .jpg images found in {folder.resolve()}"
    )

for i in k:
    with Image.open(i) as img:
        name = i.name
        width, height = img.size # i is the file path
        formati = img.format #img is the image
        mode = img.mode

        d = {
            "name": name, 
            "width": width,
            "height": height,
            "format": formati,
            "mode": mode
        }
        details.append(d)

# for i in details:
#     print(i)
    
df = pd.DataFrame(details)
# print(df.to_string(index=False))
print(df)
df.to_csv("data/image_metadata.csv", index=False)



