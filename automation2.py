import time
import pyautogui
from pynput.keyboard import Key, Controller
import cv2
import mss
import numpy

# use browser to visit https://fivesjs.skipser.com/trex-game1/
# put the browser to the left side and run the programme

key = Controller()

tree_small = cv2.imread('t rex/treesmall.png', 0)
tw_s, th_s = tree_small.shape[::-1]

tree_big = cv2.imread('t rex/treebig.png', 0)
tw_b, th_b = tree_big.shape[::-1]

birdie = cv2.imread('t rex/birdie.png', 0)
bw, bh = birdie.shape[::-1]

def jump():
    key.press(Key.space)
    time.sleep(0.3)
    key.release(Key.space)



with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {'top':700, 'left': 100, 'width': 300, 'height': 100}

    while 'Screen capturing':

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        res_tree_small = cv2.matchTemplate(img_gray, tree_small, cv2.TM_CCOEFF_NORMED)
        res_tree_big = cv2.matchTemplate(img_gray, tree_big, cv2.TM_CCOEFF_NORMED)
        res_bird = cv2.matchTemplate(img_gray, birdie, cv2.TM_CCOEFF_NORMED)

        threshold = 0.65

        loc_tree_small = numpy.where(res_tree_small >= threshold)
        for pt in zip(*loc_tree_small[::-1]):
            cv2.rectangle(img, pt, (pt[0] + tw_s, pt[1] + th_s), (0, 0, 255), 2)
            if pt[0] + tw_s < 150:
                jump()
                break


        loc_bird = numpy.where(res_bird >= threshold)
        for pt in zip(*loc_bird[::-1]):
            cv2.rectangle(img, pt, (pt[0] + bw, pt[1] + bh), (0, 0, 255), 2)
            print("{0},{1}".format(pt[0], pt[1]))
            if pt[0] + bw < 250:
                jump()
                break


        loc_tree_big = numpy.where(res_tree_big >= threshold)
        for pt in zip(*loc_tree_big[::- 1]):
            cv2.rectangle(img, pt, (pt[0] + tw_b, pt[1] + th_b), (0, 0, 255), 2)
            if pt[0] + tw_b < 200:
                jump()
                break



        # Display the picture
        cv2.imshow('OpenCV/Numpy normal', img)

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


# add time related changes to parameters regulating jump?