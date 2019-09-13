import os
import myutils as ut
from PIL import Image
def jpg2png(path):
    imlist = ut.get_imlist(path, ".jpg")
    print imlist
    for i in imlist:
        fname = os.path.splitext(i)[0] + ".png"
        try:
            Image.open(i).save(fname)
        except:
            print "Cannot convert file " + i
        else:
            print i + " converted" 
def png2jpg(path):
    imlist = ut.get_imlist(path, ".png")
    print imlist
    for i in imlist:
        fname = os.path.splitext(i)[0] + ".jpg"
        try:
            Image.open(i).save(fname)
        except:
            print "Cannot convert file " + i
        else:
            print i + " converted" 
png2jpg(".")