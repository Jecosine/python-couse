import os
from PIL import Image
import myutils as ut


def thumbnail(path, size=(128, 128)):
    # Default size of thumbnail is 128, 128
    imlist = ut.get_imlist(path, ".jpg")
    for i in imlist:
        fname = os.path.splitext(i)[0] + "_s.jpg"
        try:
            im = Image.open(i)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(fname)
        except Exception as e:
            print("Cannot create thumbnail of file {0} due to error(s): {1}".format(i, e))
        else:
            print("Thumbnail of {0} created".format(i))


if __name__ == "__main__":
    thumbnail("images")
