from PIL import Image, ImageDraw, ImageFont
import myutils as ut
import os
'''
add_watermarks adds the image-type logo to origin images in specified directory
@para path: <string> select a directory to process all jpg
@para logopath: <string> select a image's path which used as water mark
@para logo_size: <list> a list of length 2 to describe the logo size (width, height)
@para position: <list> a list with length 2
'''
def add_watermarks(path, logopath, logo_size = (200, 100), position = (0, 0)):
    imlist = ut.get_imlist(path, ".jpg")
    for i in imlist:
        fname = os.path.splitext(i)[0] + '_w.jpg'
        im = Image.open(i).convert('RGBA')
        logo = Image.open(logopath).convert('RGBA')
        try:
            out = add_watermark_single(im, logo, logo_size, position)
            out.convert('RGB').save(fname)
        except Exception as e:
            print("Cannot convert file.Error info: {0}".format(i), e)
        else:
            print("{0} coverted".format(i))
'''
logo_resize resize the logo image to fit the image size

@para logo: <class 'PIL.PngImagePlugin.PngImageFile'> image used as water mark
@para logo_size: <list> a list of length 2 to describe the logo size (width, height)
'''
def logo_resize(logo, logo_size):
    return logo.resize(logo_size)
'''
add_watermark_single add water mark to one image
@para im: <class 'PIL.PngImagePlugin.PngImageFile'> origin image
@para logo: <class 'PIL.PngImagePlugin.PngImageFile'> image used as water mark
@para position: <list> a list with length 2
'''
def add_watermark_single(im, logo, logo_size, position):
    panel = Image.new("RGBA", im.size, (0, 0, 0, 0))
    logo = logo_resize(logo, logo_size)
    panel.paste(logo, position)
    output = Image.alpha_composite(im, panel)
    return output
# Example
if __name__ == "__main__":
    add_watermarks("images", "images/python-logo.png")
