from PIL import Image
from numpy import *
from scipy import ndimage
import time
'''
First implement: use numpy to convert image to an array, then rebuild an image copy from this array
@para im: <class 'PIL.PngImagePlugin.PngImageFile'> image object that you want to copy 
'''
# def copy(im):
#     imdata = array(im)
#     clone = Image.fromarray(imdata)
#     clone.show()
#     return clone


'''
Second implement: use nested-loop to iterate each pixel
@para im: <class 'PIL.PngImagePlugin.PngImageFile'> image object that you want to copy 
'''
def copy(im):
    width, height = im.size
    clone = Image.new(im.mode, im.size)
    for i in range(width):
        for j in range(height):
            pixel = im.getpixel((i,j))
            clone.putpixel((i,j), pixel)
    clone.show()
    return clone

'''
First implement: use numpy to convert image to an array, then rebuild an image copy from this array
@para im: <class 'PIL.PngImagePlugin.PngImageFile'> image object that you want to copy 
@para crop_box: <tuple> a 4d tuple include two point (x1, y1,   x2, y2)
'''
def crop(im, crop_box):
    x1, y1, x2, y2 = crop_box
    x1, x2 = x1 > x2 and (x2, x1) or (x1, x2)
    y1, y2 = y1 > y2 and (y2, y1) or (y1, y2)
    # Judge whether input is valid
    if x2 > im.size[0] or y2 > im.size[1] or x1 < 0 or y1 < 0:
        print("position overlap")
        return None
    imdata = array(im)
    print(x1,y1,x2,y2)
    croped_data = imdata[y1: y2, x1: x2]
    croped = Image.fromarray(croped_data)
    croped.show()
    return croped

'''
Second implement: use nested-loop to iterate each pixel
@para im: <class 'PIL.PngImagePlugin.PngImageFile'> image object that you want to crop 
@para crop_box: <tuple> a 4d tuple include two point (x1, y1,   x2, y2)
'''
# def crop(im, crop_box):
#     w, h = im.size
#     x1, y1, x2, y2 = crop_box
#     x1, x2 = x1 > x2 and (x2, x1) or (x1, x2)
#     y1, y2 = y1 > y2 and (y2, y1) or (y1, y2)
#     # Judge whether input is valid
#     if x2 > w or y2 > h or x1 < 0 or y1 < 0:
#         print("position overlap")
#         return None
#
#     croped = Image.new(im.mode, (x2 - x1, y2 - y1))
#     for i in range(x1, x2):
#         for j in range(y1, y2):
#             pixel = im.getpixel((i,j))
#             croped.putpixel((i - x1, j - y1), pixel)
#     croped.show()
#     return croped


'''
First implement: use numpy to convert image to an array, then rebuild an image copy from this array
@para im: <class 'PIL.PngImagePlugin.PngImageFile'> image object that you want to copy 
@para mode: <bool> default value is True, imply to Horizontal flip, while False imply to Vertical
'''
def flip(im, mode = True):
    imdata = array(im)
    flipedata = imdata[::, ::-1] if mode else imdata[::-1, ::]
    fliped = Image.fromarray(flipedata)
    fliped.show()
    return fliped
'''
Second implement: use nested-loop to iterate each pixel
@para im: <class 'PIL.PngImagePlugin.PngImageFile'> image object that you want to flip
@para mode: <bool> default value is True, imply to Horizontal flip, while False imply to Vertical
'''
# def flip(im, mode = True):
#     w, h = im.size
#     if mode:
#         _w = w // 2
#         for i in range(_w):
#             for j in range(h):
#                 pixel = im.getpixel((i,j))
#                 im.putpixel((i, j), im.getpixel((w - i - 1, j)))
#                 im.putpixel((w - i - 1, j), pixel)
#
#     else:
#         _h = h // 2
#         for i in range(w):
#             for j in range(_h):
#                 pixel = im.getpixel((i, j))
#                 im.putpixel((i, j), im.getpixel((i, h - j - 1)))
#                 im.putpixel((i, h - j - 1), pixel)
#     im.show()
#     return im


'''
First implement: use numpy to convert image to an array, then rebuild an image copy from this array
@para im: <class 'PIL.PngImagePlugin.PngImageFile'> image object that you want to rotate 
@para mode: <bool> default value is True, imply to rotate 90 degree in clockwise , while False imply to in anticlockwise
'''
def rotate(im, mode = True):
    imdata = array(im)
    rotatedata = imdata[::-1].transpose((1, 0, 2)) if mode else imdata.transpose(1, 0, 2)[::-1]
    rotated = Image.fromarray(rotatedata)
    rotated.show()
    return rotated
'''
Second implement: use nested-loop to iterate each pixel
@para im: <class 'PIL.PngImagePlugin.PngImageFile'> image object that you want to rotate
@para mode: <bool> default value is True, imply to rotate 90 degree in clockwise , while False imply to in anticlockwise
'''
def rotate(im, mode = True):
    w, h = im.size
    rotated = Image.new(im.mode, im.size[::-1])
    w, h = im.size
    for i in range(w):
        for j in range(h):
            pixel = im.getpixel((i, j))
            if mode:
                rotated.putpixel((h - j - 1, i), pixel)
            else:
                rotated.putpixel((j, w - i - 1), pixel)

    rotated.show()
    return rotated
'''


@para im: <class 'PIL.PngImagePlugin.PngImageFile'> image object that you want to smooth 
'''
def smooth2(im):
    smoothed = Image.new(im.mode, im.size)
    w, h = im.size
    # print(im.getpixel((0, 0)))
    #kernel = array([[[1/9, 1/9, 1/9],[1/9, 1/9, 1/9],[1/9, 1/9, 1/9]],[[1/9, 1/9, 1/9],[1/9, 1/9, 1/9],[1/9, 1/9, 1/9]],[[1/9, 1/9, 1/9],[1/9, 1/9, 1/9],[1/9, 1/9, 1/9]]])
    kernel = ones((3, 3, 3)) / 27
    imdata = array(im)
    temp = ndimage.convolve(imdata, kernel)
    smoothed = Image.fromarray(temp)
    smoothed.show()
    return smoothed

def smooth1(im):
    smoothed = Image.new(im.mode, im.size)
    w, h = im.size
    # print(im.getpixel((0, 0)))
    for i in range(w):
        for j in range(h):
            smoothed.putpixel((i, j), get_average(im, i, j))
    #smoothed.show()
    return smoothed

def get_average(im, i, j):
    w, h = im.size
    r, g, b = 0, 0, 0
    count = 0
    for i in range(max(i - 1, 0), min(w, i + 1)):
        for j in range(max(j - 1, 0), min(j + 1, h)):
            pixel = im.getpixel((i, j))
            r += pixel[0]
            g += pixel[1]
            b += pixel[2]
            count += 1
    return (r // count, g // count, b // count)
# Example
if __name__ == "__main__":
    im = Image.open("images/02.jpg")
    # t1 = time.time()
    # smooth1(im)
    # t2 = time.time()
    # smooth2(im)
    # t3 = time.time()
    # print("Method 1 use: {0} s\nMethod 2 use: {1} s".format(t2 - t1, t3 - t2))
    smooth2(im)