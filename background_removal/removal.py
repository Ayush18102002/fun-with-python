from rembg import remove
from PIL import Image

img = Image.open("input-2.jpeg")
output = remove(img)
output.save("output-2.png")