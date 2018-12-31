import cv2
import numpy as np

crest = cv2.imread('queens_crest.png', 0)
height, width = crest.shape

scale = float(100/width)

crest_resize = cv2.resize(crest,None,fx=scale,fy=scale)

height_resize, width_resize = crest_resize.shape

print('Height: '+str(height_resize))
print('Width: '+str(width_resize))

cv2.imwrite('crest_resize.png', crest_resize)