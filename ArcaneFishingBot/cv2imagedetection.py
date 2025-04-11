from numpy import asarray
from mss import mss
import cv2
import time
import pyautogui
import imageio.v3 as iio
import random


import cv2

flag_vision = False

def vision():
    cords = (400,100,1300,700)
    
    mark = cv2.imread("D:\\Python\\test\\banana.png")  #r"D:\Python\\New folder\banana.png"
    # cv2.imshow("OpenCV Image",mark) #to show the image
    # cv2.waitKey(0) 
    with mss() as sct:
        #screen size and coverting into numpy arrays
        screenshot = sct.grab(cords)
        image = asarray(screenshot)

        #import image into grayscale
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        mark_gray = cv2.cvtColor(mark, cv2.COLOR_BGR2GRAY)
        mark_w, mark_h = mark_gray.shape[::-1]

        #craeting mini display

        image_mini = cv2.resize(src=image_gray, dsize=(650,450))
        cv2.imshow('Bot Vision', image_mini)
        cv2.waitKey(10) #Refresh Rate lower more  CPU use
        fishing_result =cv2.matchTemplate(
            image= image_gray,
            templ= mark_gray,
            method=cv2.TM_CCOEFF_NORMED
        )

        caught_min_val, caught_max_val, caught_min_loc, caught_max_loc = cv2.minMaxLoc(fishing_result)
        print(str(caught_max_val) + " MATCH ATTEMPT")
        global maxval
        maxval = caught_max_val
        if caught_max_val >= 0.7:
            image = cv2.rectangle(
                img=image_gray,
                pt1=caught_max_loc,
                pt2=(caught_max_loc[0] + mark_w,
                     caught_max_loc[1] + mark_h),
                color=(0, 0, 255),
                thickness=2)
            for i in range(3):
                pyautogui.click(random.randint(4,6))
                time.sleep(0.8)

def timer():
    end = time.time()
    counter = end - start
    print(counter)
    if counter >= 30 and maxval <= 0.7:
        pyautogui.click(clicks=1)
        start = 0


start = time.time()
while True:
   if not flag_vision:
        # prevents function `vision` from running multiple times.
        vision()
        end = time.time()
        counter = end - start
        print(counter)
        if counter >= 30 and maxval <= 0.7:
            pyautogui.click(clicks=1)
            start = time.time()
        run_vision = True
