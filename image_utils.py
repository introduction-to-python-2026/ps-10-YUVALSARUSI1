from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
 image = Image.open(path)
 image_array = np.array(image)
 return image_array

def edge_detection(image):
 gray_image = np.mean(image, axis=2)
 plt.imshow(gray_image,cmap= "gray")
 kernelX = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
 kernelY= np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
 edgeX = convolve2d(gray_image,kernelX, mode="same")
 edgeY = convolve2d(gray_image,kernelX, mode="same")
 edgeMAG = np.sqrt(edgeX**2 + edgeY**2)
 return edgeMAG

from image_utils import load_image, edge_detection
from PIL import Image
from skimage.filters import median
from skimage.morphology import ball
