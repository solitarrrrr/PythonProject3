import time
import pyautogui
from pynput.keyboard import Key, Controller
import cv2
import mss
import numpy

# use browser to visit https://fivesjs.skipser.com/trex-game1/
# put the browser to the left side and run the programme

key = Controller()

tree1 = cv2.imread('t rex/treesmall.png', 0)
tw, th = tree1.shape[::-1]

tree4 = cv2.imread('t rex/treebig.png', 0)
tw4, th4 = tree4.shape[::-1]

birdie = cv2.imread('t rex/birdie.png', 0)
nw, nh = birdie.shape[::-1]

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

        res2 = cv2.matchTemplate(img_gray, tree1, cv2.TM_CCOEFF_NORMED)
        res5 = cv2.matchTemplate(img_gray, tree4, cv2.TM_CCOEFF_NORMED)
        res3 = cv2.matchTemplate(img_gray, birdie, cv2.TM_CCOEFF_NORMED)

        threshold = 0.65

        loc2 = numpy.where(res2 >= threshold)
        for pt in zip(*loc2[::-1]):
            cv2.rectangle(img, pt, (pt[0] + tw, pt[1] + th), (0, 0, 255), 2)
            if pt[0] + tw < 150:
                jump()
                break


        loc3 = numpy.where(res3 >= threshold)
        for pt in zip(*loc2[::-1]):
            cv2.rectangle(img, pt, (pt[0] + nw, pt[1] + nh), (0, 0, 255), 2)
            print("{0},{1}".format(pt[0], pt[1]))
            if pt[0] + nw < 150:
                jump()
                break


        loc5 = numpy.where(res5 >= threshold)
        for pt in zip(*loc5[::- 1]):
            cv2.rectangle(img, pt, (pt[0] + tw4, pt[1] + th4), (0, 0, 255), 2)
            if pt[0] + tw4 < 150:
                jump()
                break



        # Display the picture
        cv2.imshow('OpenCV/Numpy normal', img)

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break