import cv2
import numpy as np

def apply_contrast(image):
  img = cv2.imread(image, 0)
  
  histeq = cv2.equalizeHist(img)
  #cv2.imshow('Input', img)
  #cv2.imshow('Histogram equalized', histeq)
  #cv2.waitKey(0)
  return img , histeq

