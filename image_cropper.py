from PIL import Image, ImageFilter
import pyautogui
import os


im = pyautogui.screenshot(region=(350, 180, 625, 370))
im_left = im.crop((10,210,75,350))
im_right = im.crop((505,200,565,315))
im_left = im_left.rotate(-9.8)
im_right = im_right.rotate(9.2)
im_left_blurred = im_left.filter(filter=ImageFilter.BoxBlur(1))
im_right_blurred = im_right.filter(filter=ImageFilter.BoxBlur(1))
im.paste(im_left_blurred,(10,210))
im.paste(im_right_blurred,(505,200))

im.show()
