import os
from PIL import Image
import myutils as ut
def thumbnail(path):
    imlist = ut.get_imlist(path, ".jpg")
    for i in imlist:
        fname = os.path.splitext(i)[0] + "_s.jpg"
        print fname
        try:
            Image.open(i).thumbnail(128,128).save(fname)
        except:
            print "Cannot create thumbnail of file " + i
        else:
            print "Thumbnail of {0} created".format(i)
         
thumbnail(".")
