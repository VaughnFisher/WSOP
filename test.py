from PIL import Image, ImageFilter
from imagesearch import imagesearch_from_folder, screenshotter
from best_hand import separate, rank

'''
test = Image.open("2d.png")
test2 = test.filter(filter=ImageFilter.BoxBlur(2))
test2.show()
test2.save('2dblur.png')

'''

results = imagesearch_from_folder("./dbcards/", 0.95) #0.95
print(results)
hands = separate(results)
print("%-25s %-15s %s" % ("HAND", "CATEGORY", "TIE-BREAKER"))
left = rank(hands[0])
print("%-25r %-15s %r" % (hands[0], left[0], left[1]))
right = rank(hands[1])
print("%-25r %-15s %r" % (hands[0], right[0], right[1]))

if(left[0] > right[0]):
  print("LEFT WINS")
elif(left[0] < right[0]):
  print("RIGHT WINS")
else:
  if(left[1] > right[1]):
    print("LEFT WINS")
  elif(left[1] < right[1]):
    print("RIGHT WINS")
  else:
    print("TIE!")




