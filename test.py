from pyxelate import Pyxelate
from skimage import io

images = []
for file in ("image2.png",):
    images.append(io.imread(file))

# dither=False, regenerate_palette=False are recommended options for sequences
p = Pyxelate(height=80, width=80, color=15, dither=False, regenerate_palette=False)

i = 1
for img in p.convert_sequence(images):
    # this will load for a while before the first image
    # is desampled and yielded
    io.imsave(f"convert_{i}.png", img)
    i += 1