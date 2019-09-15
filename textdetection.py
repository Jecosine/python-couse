from PIL import Image
import cv2
import numpy as np
import pytesseract as pyt
import image_process as ip
def mainprocess(path):
    pyt.pytesseract.tesseract_cmd = r'D:/Program Files/Tesseract-OCR/tesseract.exe'
    #tessdata_dir_config = r' - tessdata-dir "D:\\Program Files\\Tesseract-OCR\\tessdata"'
    im = cv2.imread(path)
    h, w, _ = im.shape
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    morph = preprocess(gray)
    textarea = get_area(morph)
    for box in textarea:
        #cv2.drawContours(im, [box], 0, (0, 255, 0), 2)
        t = np.array(box).transpose()
        x1, y1, x2, y2 = (min(t[0]), min(t[1]), max(t[0]), max(t[1]))
        print(pyt.image_to_string(im[y1:min(y2 + 5, h), x1:min(x2 + 5, w)], lang="chi_sim"))




def preprocess(gray):
    # Use sobel
    sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize = 3)
    # Binarization
    ret, binary = cv2.threshold(sobel, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
    # dilations and erosions
    erosions_core = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 9))
    dilation_core = cv2.getStructuringElement(cv2.MORPH_RECT, (24, 6))

    #dilations once
    dilation = cv2.dilate(binary, dilation_core, iterations=1)
    #erosion once
    erosion = cv2.erode(dilation, erosions_core, iterations=1)
    #dilation twice
    dilation2 = cv2.dilate(erosion, dilation_core, iterations=3)


    cv2.imwrite("binary.png", binary)
    cv2.imwrite("dilation.png", dilation)
    cv2.imwrite("erosion.png", erosion)
    cv2.imwrite("dilation2.png", dilation2)
    return dilation2

def get_area(im):
    region = []
    contours, hierarchy = cv2.findContours(im, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        cnt = contours[i]
        # calculate area
        area = cv2.contourArea(cnt)
        # ignore too small contour
        if (area < 2000):
            continue
        epsilon = 0.001 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        # get width and height
        height = abs(box[0][1] - box[2][1])
        width = abs(box[0][0] - box[2][0])

        # 筛选那些太细的矩形，留下扁的
        if (height > width * 1.2):
            continue
        region.append(box)
    return region


if __name__ == "__main__":
    mainprocess("images/t.jpg")