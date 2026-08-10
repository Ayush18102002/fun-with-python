from rembg import remove
from PIL import Image

img = Image.open("test.jpeg")
output = remove(img)
output.save("output-2.png")