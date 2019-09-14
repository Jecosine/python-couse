from PIL import Image, ImageDraw, ImageFont
import myutils as ut
import os

'''
@para path: <string> select a directory to process all jpg
@para content: <string> content of watermark
@para size: <int> font size
@para position: <list> a list with length 2
@para color: <list> a list with length 4
@para fpath: <string> the path of font
'''
def add_watermarks(path, content = 'Python', size = 20, position = (0, 0), color = (255,255,255,100), fpath = "fonts/LucidaTypewriterRegular.ttf"):
    # Get image list of specified directory
    imlist = ut.get_imlist(path, ".jpg")
    for i in imlist:
        fname = os.path.splitext(i)[0] + '_w.jpg'
        im = Image.open(i).convert('RGBA')
        try: 
            out = add_watermark_single(im, content, size, position, color, fpath)
            #out is RGBA after alpha composite with watermark
            out.convert("RGB").save(fname)
        except Exception as e:
            print("Cannot add water mark to {0}, due to error(s): {1}".format(i, e))
        else:
            print("Water mark added to {0}".format(i))
'''
@para im: <class 'PIL.PngImagePlugin.PngImageFile'> origin image
'''
def add_watermark_single(im, content, size, position, color, fpath):
    panel = Image.new("RGBA", im.size, (0,0,0,0))
    font = ImageFont.truetype(fpath, size)
    mask = ImageDraw.Draw(panel)
    mask.text(position, content, fill = color, font = font)
    output = Image.alpha_composite(im, panel)
    return output

#Example
if __name__ == "__main__":
    add_watermarks(path = "images")
