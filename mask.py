import	cv2
mask = cv2.imread('mask.png', cv2.IMREAD_COLOR)
print(mask.shape)
print(mask.size)
w = 1280
h = 605
mask_resized = cv2.resize(mask, (w, int (h / 2)))
mask_h,	mask_w, mask_c = mask_resized.shape
for	ht in range(mask_h):
	for wt in range(mask_w):
		if mask_resized [ht, wt][3] != 0:
			frame[y - int (h / 2) + ht, x + wt]= mask_resized[ht, wt][:3]