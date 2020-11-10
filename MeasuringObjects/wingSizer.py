# import the necessary packages
import inline as inline
import matplotlib.pyplot as plt
import PIL
from PIL import ImageOps
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import os
from skimage.filters import try_all_threshold

# Finds the point between two points.
def midpoint(pta, ptb):
    return (pta[0] + ptb[0]) * 0.5, (pta[1] + ptb[1]) * 0.5


# Splits the image into 4 equal parts
def split(img):
    m = img.shape[0] // 2
    n = img.shape[1] // 2

    tiles = [img[x:x + m, y:y + n] for x in range(0, img.shape[0], m)
             for y in range(0, img.shape[1], n) ]

    # sTR = cv2.imshow('Tright half', tiles[ 0 ])
    # sTL = cv2.imshow('TLeft half', tiles[ 1 ])
    # sBR = cv2.imshow('Bright half', tiles[ 2 ])
    # sBL = cv2.imshow('BLeft half', tiles[ 3 ])
    return tiles


def thresh_img(img):
    # load the image, convert it to grayscale, and blur it slightly
    image = img
    img_blur = cv2.GaussianBlur(image, (7, 7), 0)
    img_blur = cv2.bilateralFilter(img_blur, d=7, sigmaSpace=75, sigmaColor=75)
    # Convert to grayscale
    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_RGB2GRAY)
    #fig, ax = try_all_threshold(img_gray, verbose=False)
    #plt.show()

    # Apply the thresholding
    a = img_gray.max()
    _, edged = cv2.threshold(img_gray, a / 1.95, a * 1.5, cv2.THRESH_BINARY_INV)
    cv2.imshow('thresh', edged)
    cv2.waitKey(0)
    return edged


def binarize(flooded):
    a = flooded.max()
    _, edged = cv2.threshold(flooded, a / 2, a * 2, cv2.THRESH_BINARY_INV)
    return edged


def fill_img(thresh_img):

    im_floodfill = thresh_img.copy()
    h, w = im_floodfill.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    # flood fill
    cv2.floodFill(im_floodfill, mask, (0, 0), 255)

    im_floodfill_inv = cv2.bitwise_not(im_floodfill)

    im_out = thresh_img | im_floodfill_inv

    # cv2.imshow("THRESH", result)
    # cv2.imshow("Floodfilled", im_floodfill)
    # cv2.imshow("Inverted Floodfilled", im_floodfill_inv)
    # cv2.imshow('foreground', im_out)

    cv2.imwrite('./temp2.png', im_out)
    im_out = cv2.imread('./temp2.png')
    a = im_out.max()
    _, edged = cv2.threshold(im_out, a / 2, a * 2, cv2.THRESH_BINARY_INV)
    edged = cv2.cvtColor(im_out, cv2.COLOR_RGB2GRAY)


    return edged

def findContour(image, bin_image, edged):

    # find contours in the edge map
    cnts = cv2.findContours(bin_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)

    # cv2.putText(image, "{:.1f}px".format(dLR), (int(TBX - 30), int(TBY + 30)), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 0), 2)

    # loop over the contours individually
    for c in cnts:
        # if the contour is not sufficiently large, ignore it
        if cv2.contourArea(c) < 70000:
            continue

        # compute the rotated bounding box of the contour
        orig = image.copy()

        # WORK IN PROGRESS?

        cMax = c

        # polygon Bounds
        c_0 = c
        hull = cv2.convexHull(c_0)

        # box bounds
        box = cv2.minAreaRect(c)
        box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
        box = np.array(box, dtype="int")

        # order the points in the contour such that they appear
        # in top-left, top-right, bottom-right, and bottom-left
        # order, then draw the outline of the rotated bounding
        # box
        box = perspective.order_points(box)

        # Draw a Polygon??
        cv2.drawContours(orig, contours=[ hull ], contourIdx=0, color=(255, 0, 0), thickness=2)
        cMax = hull
        extLeft = tuple(cMax[ cMax[ :, :, 0 ].argmin() ][ 0 ])
        extRight = tuple(cMax[ cMax[ :, :, 0 ].argmax() ][ 0 ])
        cv2.line(orig, (extLeft), (extRight), (0, 255, 255), thickness=3, lineType=8)

        extTop = tuple(cMax[ cMax[ :, :, 1 ].argmin() ][ 0 ])
        extBot = tuple(cMax[ cMax[ :, :, 1 ].argmax() ][ 0 ])
        cv2.line(orig, (extTop), (extBot), (0, 255, 0), thickness=3, lineType=8)

        # cv2.drawContours(image, [ cMax ], -1, (0, 255, 255), 2)
        cv2.circle(orig, extLeft, 8, (0, 255, 0), -1)
        cv2.circle(orig, extRight, 8, (0, 255, 0), -1)
        cv2.circle(orig, extTop, 8, (0, 255, 0), -1)
        cv2.circle(orig, extBot, 8, (0, 255, 0), -1)

        # Draw a rectangle?
        # cv2.drawContours(orig, [ box.astype("int") ], -1, (0, 255, 0), 2)

        # loop over the original points and draw them
        for (x, y) in box:
            cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)

        # unpack the ordered bounding box, then compute the midpoint
        # between the top-left and top-right coordinates, followed by
        # the midpoint between bottom-left and bottom-right coordinates
        (tl, tr, br, bl) = box

        (tltrX, tltrY) = midpoint(tl, tr)
        (blbrX, blbrY) = midpoint(bl, br)
        # compute the midpoint between the top-left and top-right points,
        # followed by the midpoint between the top-righ and bottom-right
        (tlblX, tlblY) = midpoint(tl, bl)
        (trbrX, trbrY) = midpoint(tr, br)
        # draw the midpoints on the image
        cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
        cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
        cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
        cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
        # draw lines between the midpoints
        # vertical line
        cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)), (255, 0, 255), 2)
        # horizontal Line
        cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)), (255, 0, 255), 2)
        # compute the Euclidean distance between the midpoints
        dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
        dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
        # if the pixels per metric has not been initialized, then
        # compute it as the ratio of pixels to supplied metric
        # (in this case, inches)
        # if pixelsPerMetric is None:
        # pixelsPerMetric = dB / args[ "width" ]
        # compute the size of the object
        dimA = dA  # / pixelsPerMetric
        dimB = dB  # / pixelsPerMetric
        # draw the object sizes on the image
        cv2.putText(orig, "{:.1f}px".format(dimA), (int(tltrX - 30), int(tltrY + 30)), cv2.FONT_HERSHEY_SIMPLEX,
                    0.65, (0, 0, 255), 2)
        cv2.putText(orig, "{:.1f}px".format(dimB), (int(trbrX - 100), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX, 0.65,
                    (0, 0, 255), 2)
        # show the output image
        cv2.imshow("Image", orig)
        cv2.waitKey(0)


def findSmallContours(image, edged):

    inverted = cv2.bitwise_not(edged)

    cnts = cv2.findContours(inverted.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    (cnts, _) = contours.sort_contours(cnts)

    # upperBound = int( (len(cnts)/2 * 0.30)) + int(len(cnts)/2)
    # lowerBound = int(len(cnts) / 2) - int((len(cnts)/ 2 * 0.20))
    # print(upperBound)
    # print(lowerBound)
    #
    # avg = 0
    # for i in range(lowerBound, upperBound):
    #     avg += cv2.contourArea(cnts[i])
    # avg = (avg/len(cnts))
    # below_average = avg - int((0.05 * avg))
    # loop over the contours individually
    for c in cnts:
        # if the contour is not sufficiently large, ignore it
        print("max: " + str(cv2.contourArea(cnts[ -1 ])) + " curr: " + str(cv2.contourArea(c)))
        #skip over if it captures background contour
      #  if cv2.contourArea(c) > cv2.contourArea(cnts[-1]):
       #     continue

        if cv2.contourArea(c) < 150:
            continue
        if cv2.contourArea(c) > 70000:
            continue
        # compute the rotated bounding box of the contour
        orig = image.copy()

        # WORK IN PROGRESS?

        cMax = c

        # polygon Bounds
        c_0 = c
        hull = cv2.convexHull(c_0)

        # Draw a Polygon??
        cv2.drawContours(orig, contours=[ hull ], contourIdx=0, color=(255, 0, 0), thickness=2)
        cMax = hull
        extLeft = tuple(cMax[ cMax[ :, :, 0 ].argmin() ][ 0 ])
        extRight = tuple(cMax[ cMax[ :, :, 0 ].argmax() ][ 0 ])
        extTop = tuple(cMax[ cMax[ :, :, 1 ].argmin() ][ 0 ])
        extBot = tuple(cMax[ cMax[ :, :, 1 ].argmax() ][ 0 ])

        # cv2.drawContours(image, [ cMax ], -1, (0, 255, 255), 2)
        cv2.circle(orig, extLeft, 4, (0, 255, 0), -1)
        cv2.circle(orig, extRight, 4, (0, 255, 0), -1)
        cv2.circle(orig, extTop, 4, (0, 255, 0), -1)
        cv2.circle(orig, extBot, 4, (0, 255, 0), -1)

        resize(orig,inverted)

def resize(img,inv):
    scale_percent = 60  # percent of original size
    width = int(img.shape[ 1 ] * scale_percent / 100)
    height = int(img.shape[ 0 ] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    resized2 = cv2.resize(inv, dim, interpolation=cv2.INTER_AREA)
    print('Resized Dimensions : ', resized.shape)

    cv2.imshow("Resized image", resized)
    cv2.imshow("Resized inv image", resized2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    path = 'C:\\Users\\monic\\PycharmProjects\\MeasuringObjectsRevised\\images'
    image_dir = os.listdir(path)
    for img in image_dir:
        original = cv2.imread(f'{path}/{img}')
       # print("Original: " + str(original.dtype))
        edged = thresh_img(original)
       #print("edged: " + str(edged.dtype))
        flooded = fill_img(edged)
        #print("Flooded " + str(flooded.dtype))
        cv2.imwrite('temp2.JPG', binarize(flooded))
        bin_img = cv2.imread('./temp2.JPG')
        bin_img = thresh_img(bin_img)
        #print("bin_img: " + str(bin_img.dtype))
        findContour(original, bin_img, edged)
        findSmallContours(original, edged)


if __name__ == "__main__":
    main()
