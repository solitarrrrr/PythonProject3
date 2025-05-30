#pip install opencv-python
import		cv2
		import numpy as np

		img = cv2.imread('test1.png', cv2.IMREAD_COLOR)
#cv2.IMREAD_COLOR: show the image in color mode,
#cv2.IMREAD_GRAYSCALE: in black and white mode,
#cv2.IMREAD_REDUCED_COLOR_2: in color mode with 1/2 length of each side
print(img.shape)
#print the pixel structure (Y coordinate, X coordinate, 3 if in color mode)
print(img.size)
#print the amount of numbers stored in the image

y, x, z = img.shape
if x % 2 == 1:
	img = cv2.resize(img, (y, x - 1))
	x = x - 1
		if y%2 == 1:
		img = cv2.resize(img, (y - 1, x))
			y = y - 1
#adjust the height and width, eliminate odd numbers

			resized_img = cv2.resize(img, (int (x / 2), int (y / 2)))
#resize the image to half

			output = np.zeros((y, x, z), dtype = 'uint8')
#generate an empty image in black color for output

			output_1 = resized_img
			output_2 = cv2.flip(resized_img, 1)
			output_3 = cv2.flip(resized_img, 0)
			output_4 = cv2.flip(resized_img, -1)
#flip code:
#1 for swap left-right,
#0 for up-down,
#-1 for all the 0 & 1 effects
output[0:int (y / 2), 0:int (x / 2)]= output_1
#left-top corner
output[0:int (y / 2), int (x / 2):x]= output_2
#right-top corner
output[int (y / 2):y, 0:int (x / 2)]= output_3
#left-bottom corner
output[int (y / 2):y, int (x / 2):x]= output_4
#right-bottom corner
#!!output[Y coordinate, X coordinate]
			cv2.imshow('image', output)
#cv2.imshow('window_name',variable img) #open a window for showing image
			cv2.waitKey(0)
#keep showing the image till any_key_pressed
			cv2.destroyAllWindows()
#close all the windows in this code

			cv2.imwrite('output.jpg', output)
#save the edited image by the filename
