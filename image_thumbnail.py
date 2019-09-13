import os
from PIL import Image
import myutils as ut
def thumbnail(path):
    imlist = ut.get_imlist(path, ".jpg")
    for i in imlist:
        fname = os.path.splitext(i)[0] + "_s.jpg"
        print fname
        try:
            im = Image.open(i)
            im.thumbnail((128,128))
            im.save(fname)
        except:
            print "Cannot create thumbnail of file " + i
        else:
            print "Thumbnail of {0} created".format(i)
         
thumbnail(".")
