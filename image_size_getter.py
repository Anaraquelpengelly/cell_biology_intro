#%%
import numpy as np
from PIL import Image
import os
#%% Get the images in the forlder
files = os.listdir()
images=[f for f in files if ('.png' in f )|('.jpeg' in f)|('.tiff' in f)]


#%%
f=open('image_sizes.txt', 'w')
for i in images:
    img = Image.open(i)
    s= img.size
    img.close()
    f.write(f'the width and height of {i} is {s}\n')
f.close()