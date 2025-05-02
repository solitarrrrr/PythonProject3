import cv2
import numpy as np
img = cv2.imread('ylsssss.webp',cv2.IMREAD_COLOR)
print(img.shape)
print(img.size)
#img=cv2.flip(img,-1)
y,x,z=img.shape
output=np.zeros((y,x,z),dtype='uint8')
img_resized=cv2.resize(img,(960,540))
output[0:540,0:960]=img_resized
output_1=cv2.flip(img_resized,1) # Horizontal Flip
output_2 = cv2.flip(img_resized, 0)  # Vertical Flip
output_3 = cv2.flip(img_resized, -1) # Horizontal and Vertical Flip

# Placement
output[0:540, 960:1920] = output_1      # Top-Right
output[540:1080, 0:960] = output_2      # Bottom-Left
output[540:1080, 960:1920] = output_3   # Bottom-Right

cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('test1.jpg',img)