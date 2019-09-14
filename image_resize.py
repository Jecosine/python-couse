import myutils as ut
from PIL import Image
import os

'''
@para path: <string> select a directory to process all jpg
@para size: <list> a list of length 2 to describe the image size (width, height)
'''
def resize(path, size=(640, 480)):
    # Default size of thumbnail is 128, 128
    imlist = ut.get_imlist(path, ".jpg")
    for i in imlist:
        fname = os.path.splitext(i)[0] + "_{0}.jpg".format(size[0])
        try:
            im = Image.open(i)
            im = im.resize(size, Image.ANTIALIAS)
            im.save(fname)
        except Exception as e:
            print("Cannot resize {0} due to error(s): {1}".format(i, e))
        else:
            print("{0} is resized to {1[0]}, {1[1]}".format(i, size))

# Example
if __name__ == "__main__":
    resize("images")
