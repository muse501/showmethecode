import os

from PIL import Image
from collections import namedtuple


def resize_img(img_path):
    with Image.open(img_path) as img:
        width_flag = True if img.width > iphone5.width else False
        height_flag = True if img.height > iphone5.height else False
        if width_flag or height_flag:
            print('- resizing %s' % img_path)
            img = img.resize((min(img.width, iphone5.width), min(img.height, iphone5.height)))
            img.save(img_path)


def find_imgs(root_path):
    for level in os.walk(root_path):
        for fn in level[2]:
            img_path = os.path.join(level[0], fn)
            try:
                resize_img(img_path)
            except OSError:
                pass

if __name__ == '__main__':
    resolution = namedtuple('resolution', ['width', 'height'])
    iphone5 = resolution(1136, 640)
    print('- start working ..')
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'q0005')
    find_imgs(path)
    print('- done ..')
