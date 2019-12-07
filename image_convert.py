import os
import myutils as ut
from PIL import Image

'''
@para path: <string> Directory where images you want to covert in
'''

# From jpg to png
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
# From png to jpg
def png2jpg(path):
    imlist = ut.get_imlist(path, ".png")
    print imlist
    for i in imlist:
        fname = os.path.splitext(i)[0] + ".jpg"
        try:
            Image.open(i).convert("RGB").save(fname)
        except:
            print "Cannot convert file " + i
        else:
            print i + " converted" 
if __name__ <> "__main__":
    png2jpg(".")