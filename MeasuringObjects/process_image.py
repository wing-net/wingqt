# import the necessary packages
import cv2
import numpy as np


# Splits the image into 4 equal parts
def split(img):
    m = img.shape[0] // 2
    n = img.shape[1] // 2

    tiles = [img[x:x + m, y:y + n] for x in range(0, img.shape[0], m)
             for y in range(0, img.shape[1], n)]

    # sTR = cv2.imshow('Tright half', tiles[ 0 ])
    # sTL = cv2.imshow('TLeft half', tiles[ 1 ])
    # sBR = cv2.imshow('Bright half', tiles[ 2 ])
    # sBL = cv2.imshow('BLeft half', tiles[ 3 ])
    return tiles

def thresh_img_2(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    # perform edge detection, then perform a dilation + erosion to
    # close gaps in between object edges

    edged = cv2.Canny(gray, 40, 20)
    edged = cv2.dilate(edged, None, iterations=4)

    #edged = cv2.Canny(gray, 20, 20)
    #edged = cv2.dilate(edged, None, iterations=3)

    edged = cv2.erode(edged, None, iterations=1)
    return edged

def thresh_img(img):
    # Blurs the image
    image_blur = cv2.GaussianBlur(img, (7, 7), 0)
    image_blur = cv2.cv2.bilateralFilter(image_blur, d=7, sigmaSpace=75, sigmaColor=75)

    # Convert to gray scale
    img_gray = cv2.cvtColor(image_blur, cv2.COLOR_RGB2GRAY)

    # Apply thresholding
    a = img_gray.max()  # The largest pixel value
    # cv2.threshold(image file, value to classify the pixel values, maximum value which is assigned to pixel values exceeding the threshold)
    _, edged = cv2.threshold(img_gray, a / 1.94, a, cv2.THRESH_BINARY_INV)

    # Display
    #cv2.imshow('thresh', edged)
    #cv2.waitKey(0)
    return edged

# Converts our filled image into a black and white image
def conv_blkwht(flooded):
    a = flooded.max()
    _, edged_flooded = cv2.threshold(flooded, a/2, a, cv2.THRESH_BINARY_INV)
    return edged_flooded

# I don't think I need this.
def fill_img(edged):
    im_floodfill = edged.copy()
    h, w = im_floodfill.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    # flood fill
    cv2.floodFill(im_floodfill, mask, (0, 0), 255)

    im_floodfill_inv = cv2.bitwise_not(im_floodfill)

    im_out = edged | im_floodfill_inv

    # cv2.imshow("THRESH", result)
    # cv2.imshow("Floodfilled", im_floodfill)
    # cv2.imshow("Inverted Floodfilled", im_floodfill_inv)
    # cv2.imshow('foreground', im_out)

    cv2.imwrite('./temp2.png', im_out)
    im_out = cv2.imread('./temp2.png')
    a = im_out.max()
    _, edged_flooded = cv2.threshold(im_out, a / 2, a * 2, cv2.THRESH_BINARY_INV)
    edged = cv2.cvtColor(im_out, cv2.COLOR_RGB2GRAY)

    return edged


def resize(img):
    scale_percent = 60  # percent of original size
    width = int(img.shape[ 1 ] * scale_percent / 100)
    height = int(img.shape[ 0 ] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
   # print('Resized Dimensions : ', resized.shape)

    cv2.imshow("Resized image", resized)

