from PIL import Image, ImageDraw, ImageFont
import myutils as ut
import os
def add_watermarks(path, logopath, logo_size = [200, 100], position = [0, 0]):
    imlist = ut.get_imlist(path, ".jpg")
    for i in imlist:
        fname = os.path.splitext(i)[0] + '_w.jpg'
        im = Image.open(i).convert('RGBA')
        logo = Image.open(logopath).convert('RGBA')
        try: 
            out = add_watermark_single(im, logo, logo_size, position)
            out.convert('RGB').save(fname)
        except Exception as e:
            print "Cannot convert file {0}".format(i), e
        else:
            print "{0} coverted".format(i)

'''
@para im: <class 'PIL.PngImagePlugin.PngImageFile'> origin image
@para content: <string> content of watermark
@para position: <list> a list with length 2
@para color: <list> a list with length 4
@para fpath: <string> the path of font
'''
def logo_resize(logo, logo_size):
    return logo.resize(logo_size)

def add_watermark_single(im, logo, logo_size, position):
    panel = Image.new("RGBA", im.size, (0,0,0,0))
    logo = logo_resize(logo, logo_size)
    panel.paste(logo, position)
    output = Image.alpha_composite(im, panel)
    return output
if __name__ == "__main__":
    add_watermarks(".", "python-logo.png", [200, 100], [0, 0])