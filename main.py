import image_utils
import numpy as np # Import for array type conversion
import matplotlib.pyplot as plt # Import for plotting


original_image = image_utils.load_image('lena.jpg') # Corrected image path and assignment

from skimage.filters import median
from skimage.morphology import ball


clean_image = median(original_image, ball(3)) 


edge_mag_image = image_utils.edge_detection(clean_image) 

plt.figure(figsize=(5,5))
plt.imshow(edge_mag_image, cmap='gray') 
plt.show() 


binary_image = edge_mag_image > 50 # Now edge_mag_image is defined

from PIL import Image

edge_image = Image.fromarray(binary_image.astype(np.uint8) * 255) 
edge_image.save('my_edges.png')
