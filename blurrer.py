from PIL import Image, ImageFilter
import os


for f in os.listdir('./dbcards'):
  if f.endswith('.png'):
    i = Image.open('./dbcards/{}'.format(f))
    ib = i.filter(filter=ImageFilter.BoxBlur(2))
    fn, fext = os.path.splitext(f)
    ib.save('blurred_cards/{}.png'.format(fn))
'''

i = Image.open('./dbcards/2c.png')
fn = '2c'
fext = '.png'
i.save('blurred_cards/{}.png'.format(fn))
'''