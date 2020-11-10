# import the necessary packages
import math
import matplotlib.pyplot as plt

import cv2
import imutils

import process_image

# Finds the point between two points.
def midpoint(pta, ptb):
    return (pta[0] + ptb[0]) * 0.5, (pta[1] + ptb[1]) * 0.5


def findContour(image, bin_image, edged):
    mask = []
    # find contours in the edge map
    cnts = cv2.findContours(bin_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)
    orig = image.copy()
    # cv2.putText(image, "{:.1f}px".format(dLR), (int(TBX - 30), int(TBY + 30)), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 0), 2)

    # loop over the contours individually
    for c in cnts:

        # if the contour is not sufficiently large, ignore it
        if cv2.contourArea(c) < 70000:
            continue

        # polygon Bounds
        c_0 = c
        hull = cv2.convexHull(c_0)
        mask.append(c)
        # # box bounds
        # box = cv2.minAreaRect(c)
        # box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
        # box = np.array(box, dtype="int")
        #
        # # order the points in the contour such that they appear
        # # in top-left, top-right, bottom-right, and bottom-left
        # # order, then draw the outline of the rotated bounding
        # # box
        # box = perspective.order_points(box)

        # Draw a Polygon??
        cv2.drawContours(orig, contours=[ hull ], contourIdx=0, color=(255, 0, 0), thickness=2)
        cMax = hull
        extLeft = tuple(cMax[ cMax[ :, :, 0 ].argmin() ][ 0 ])
        extRight = tuple(cMax[ cMax[ :, :, 0 ].argmax() ][ 0 ])
        extTop = tuple(cMax[ cMax[ :, :, 1 ].argmin() ][ 0 ])
        extBot = tuple(cMax[ cMax[ :, :, 1 ].argmax() ][ 0 ])

        cv2.line(orig, (extLeft), (extRight), (0, 255, 255), thickness=3, lineType=8)
        w_len = math.hypot(extLeft[0] - extRight[0], extLeft[1] - extRight[1])
        cv2.line(orig, (extTop), (extBot), (0, 255, 0), thickness=3, lineType=8)
        h_len = math.hypot(extTop[0] - extBot[0], extTop[1] - extBot[1])
        # cv2.drawContours(image, [ cMax ], -1, (0, 255, 255), 2)
        cv2.circle(orig, extLeft, 8, (0, 255, 0), -1)
        cv2.circle(orig, extRight, 8, (0, 255, 0), -1)
        cv2.circle(orig, extTop, 8, (0, 255, 0), -1)
        cv2.circle(orig, extBot, 8, (0, 255, 0), -1)

        # Trying to figure out orientation
        # Thoughts:
        if w_len > h_len:
            print("The wing tip is left or right")
            # im = orig
            # implot = plt.imshow(im)
            # # put a blue dot at (10, 20)
            # plt.scatter([ extLeft[0] ], [ extLeft[1] ])
            # plt.scatter([ extRight[0] ] , [ extRight[1] ])
            # # put a red dot, size 40, at 2 locations:
            # x_list = []
            # for points in c:
            #     for x,y in points:
            #         x_list.append((x,y))
            # #x_list.sort()
            # print(x_list)
            # x_mid = c[int(len(x_list)/2)][0][0]
            # y_mid = c[int(len(x_list)/2)][0][1]
            # plt.scatter(x=[ 750 ], y=[ 512 ], c='r', s=100)
            # #cv2.line(orig, (x_mid,extTop[1]), (x_mid,extBot[1]), (0, 255, 0), thickness=3, lineType=8)
            # plt.show()
            # #print(c)
        else:
            print("The wing tip is top or bottom")
            #print(c)

        # # Draw a rectangle?
        # # cv2.drawContours(orig, [ box.astype("int") ], -1, (0, 255, 0), 2)
        #
        # # loop over the original points and draw them
        # for (x, y) in box:
        #     cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)
        #
        # # unpack the ordered bounding box, then compute the midpoint
        # # between the top-left and top-right coordinates, followed by
        # # the midpoint between bottom-left and bottom-right coordinates
        # (tl, tr, br, bl) = box
        #
        # (tltrX, tltrY) = midpoint(tl, tr)
        # (blbrX, blbrY) = midpoint(bl, br)
        # # compute the midpoint between the top-left and top-right points,
        # # followed by the midpoint between the top-righ and bottom-right
        # (tlblX, tlblY) = midpoint(tl, bl)
        # (trbrX, trbrY) = midpoint(tr, br)
        # # draw the midpoints on the image
        # cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
        # cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
        # cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
        # cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
        # draw lines between the midpoints
        # vertical line
        # cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)), (255, 0, 255), 2)
        # # horizontal Line
        # cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)), (255, 0, 255), 2)
        # # compute the Euclidean distance between the midpoints
        # dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
        # dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
        # # if the pixels per metric has not been initialized, then
        # # compute it as the ratio of pixels to supplied metric
        # # (in this case, inches)
        # # if pixelsPerMetric is None:
        # # pixelsPerMetric = dB / args[ "width" ]
        # # compute the size of the object
        # dimA = dA  # / pixelsPerMetric
        # dimB = dB  # / pixelsPerMetric
        # # draw the object sizes on the image
        # cv2.putText(orig, "{:.1f}px".format(dimA), (int(tltrX - 30), int(tltrY + 30)), cv2.FONT_HERSHEY_SIMPLEX,
        #             0.65, (0, 0, 255), 2)
        # cv2.putText(orig, "{:.1f}px".format(dimB), (int(trbrX - 100), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX, 0.65,
        #             (0, 0, 255), 2)
        # show the output image


    findSmallContours(orig, edged, mask)


def findSmallContours(image, edged, mask):

    inverted = cv2.bitwise_not(edged)

    cnts = cv2.findContours(inverted.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    bounded = []

# Filters contours out so that only nicely sized contours within the outer contour are counted.
    for c in cnts:
        if cv2.contourArea(c) < 400:
            continue
        if cv2.contourArea(c) > 70000:
            continue
        for points in c:
            for x,y in points:
                for m in mask:
                    if cv2.pointPolygonTest(m, (x, y), False) == 1:
                        bounded.append(c)

    print("Total bounded: " + str(len(bounded)))

    cnts = bounded
    orig = image.copy()
    count = 0
    for c in cnts:
        count += 1
        cMax = c

        # polygon Bounds
        c_0 = c
        hull = cv2.convexHull(c_0)

        # Draw a Polygon??
        cv2.drawContours(orig, contours=[hull], contourIdx=0, color=(0, 0, 255), thickness=2)
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

    process_image.resize(orig)
    print(count)
    #cv2.imshow("Image", orig)
    cv2.waitKey(0)


