import cv2
#import the opencv module

img=cv2.imread('Samples 1/flower.jpg')
#reading the image in the given path

img[100:150,100:150]=[0,0,0]

cv2.imshow('IMG',img)
#parameters -name of the window,source image
