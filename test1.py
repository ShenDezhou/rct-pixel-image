from pyxelate import Pyxelate
from skimage import io
import matplotlib.pyplot as plt

img = io.imread("image.jpg")
# generate pixel art that is 1/14 the size
height, width, _ = img.shape
factor = 14
colors = 6
dither = True

p = Pyxelate(height // factor, width // factor, colors, dither)
img_small = p.convert(img)  # convert an image with these settings

_, axes = plt.subplots(1, 2, figsize=(64, 64))
axes[0].imshow(img)
axes[1].imshow(img_small)
plt.show()