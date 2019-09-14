import os
import myutils as ut
from PIL import Image
'''
@para path: <string> Directory where images you want to covert in
@para outpath: <string> Directory where you want to put the converted file in
'''
# From jpg to png
def jpg2png(path, outpath):
    imlist = ut.get_imlist(path, ".jpg")
    # Check whether outpath exists
    try:
        assert(os.path.exists(outpath))
    except:
        print("{0} path not exists".format(outpath))
    # Format outpath
    for i in imlist:
        fname = os.path.join(outpath, os.path.splitext(os.path.split(i)[-1])[0] + ".png")
        try:
            Image.open(i).save(fname)
        except Exception as e:
            print("Cannot convert file {0} due to error: {1}".format(i, e))
        else:
            print("{0} converted".format(i))

# From png to jpg
def png2jpg(path, outpath):
    imlist = ut.get_imlist(path, ".png")
    # Check whether outpath exists
    try:
        assert(os.path.exists(outpath))
    except:
        print("{0} path not exists".format(outpath))
    for i in imlist:
        fname = os.path.join(outpath, os.path.splitext(os.path.split(i)[-1])[0] + ".jpg")
        try:
            Image.open(i).convert("RGB").save(fname)
        except Exception as e:
            print("Cannot convert file {0} due to {1}".format(i, e))
        else:
            print("{0} converted".format(i))


if __name__ == "__main__":
    png2jpg("images", "converted")

