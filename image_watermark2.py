from PIL import Image, ImageDraw, ImageFont
import myutils as ut
import os
def add_watermarks(path):
    imlist = ut.get_imlist(path, ".jpg")
    for i in imlist:
        fname = os.path.splitext(i)[0] + '_w.jpg'
        im = Image.open(i).convert('RGBA')
        out = add_watermark_single(im, "Python", [0, 0], [255,255,255,100], "LucidaTypewriterRegular.ttf")
        out.convert("RGB").save(fname)


'''
@para im: <class 'PIL.PngImagePlugin.PngImageFile'> origin image
@para content: <string> content of watermark
@para position: <list> a list with length 2
@para color: <list> a list with length 4
@para fpath: <string> the path of font
'''
def add_watermark_single(im, content, position, color, fpath):
    panel = Image.new("RGBA", im.size, (0,0,0,0))
    font = ImageFont.truetype(fpath)
    mask = ImageDraw.Draw(panel)
    mask.text(position[0], position[1], content, font, color)
    output = Image.alpha_composite(im, mask)
    return output
