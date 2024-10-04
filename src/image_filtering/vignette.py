import cv2
import numpy as np

def apply_vignette(image):
    img = cv2.imread(image)
    rows, cols = img.shape[:2]
    # generating vignette mask using Gaussian kernels
    kernel_x = cv2.getGaussianKernel(cols,200)
    kernel_y = cv2.getGaussianKernel(rows,200)
    kernel = kernel_y * kernel_x.T
    mask = 255 * kernel / np.linalg.norm(kernel)
    output = np.copy(img)
    # applying the mask to each channel in the input image
    for i in range(3):
       output[:,:,i] = output[:,:,i] * mask
       
    return output