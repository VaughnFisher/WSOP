from PIL import Image, ImageFilter
from imagesearch import imagesearch_from_folder, screenshotter, imagesearcharea
from best_hand import separate, rank
import pyautogui, sys
import re
import random
import time
from datetime import datetime

def play():
  startTime = datetime.now()
  print(startTime)
  results = imagesearch_from_folder("./dbcards/", 0.95) #0.95
  print(datetime.now() - startTime)
  print()
  if(len(results)<=7):
    print("TRYING AGAIN!")
    play()
    return

  print(len(results), "cards found on screen: ")
  for card, pos in results.items():
    print("  ",card,pos)
  hands = separate(results)
  left = rank(hands[0])
  right = rank(hands[1])
  print(datetime.now() - startTime)

  print("%-25s %-20s %s" % ("HAND", "CATEGORY", "TIE-BREAKER"))
  print("%-25r %-20s %r" % (hands[0], left[0], left[1]))
  print("%-25r %-20s %r" % (hands[1], right[0], right[1]))
  print()


  rep = {"10": "a", "J": "b", "Q": "c", "K": "d", "A": "e"}

  str1 = " "
  str1 = str1.join(left[1])

  rep1 = dict((re.escape(k), v) for k, v in rep.items()) 
  pattern = re.compile("|".join(rep1.keys()))
  r_left = pattern.sub(lambda m: rep1[re.escape(m.group(0))], str1)
  r_left = r_left.split(" ")

  str2 = " "
  str2 = str2.join(right[1])

  rep2 = dict((re.escape(k), v) for k, v in rep.items()) 
  pattern2 = re.compile("|".join(rep2.keys()))
  r_right = pattern2.sub(lambda m: rep2[re.escape(m.group(0))], str2)
  r_right = r_right.split(" ")

  rand = random.randint(-10,10)

  print(datetime.now() - startTime)

  if(left[0] > right[0]):
    print("*** LEFT WINS ***")
    pyautogui.click(x=450+rand, y=450+rand)
  elif(left[0] < right[0]):
    print("*** RIGHT WINS ***")
    pyautogui.click(x=900+rand, y=450+rand)
  else:
    if(r_left > r_right):
      print("*** LEFT WINS ***")
      pyautogui.click(x=450+rand, y=450+rand)
    elif(r_left < r_right):
      print("*** RIGHT WINS ***")
      pyautogui.click(x=900+rand, y=450+rand)
    else:
      print("*** TIE*** !")
  print(datetime.now() - startTime)

def wait():
  im = pyautogui.screenshot(region=(610,190,120,155))

  pos = imagesearcharea("back.png", 610, 190, 730, 345, 0.6, im)

  while pos[0] == -1:
    print("waiting")
    im = pyautogui.screenshot(region=(610,190,120,155))
    pos = imagesearcharea("back.png", 610, 190, 730, 345, 0.6, im)
  return

def main():
  try:
    while True:
      play()
      wait()
      time.sleep(0.55)
  except KeyboardInterrupt:
    pass

if __name__ == "__main__":
  main()
      



