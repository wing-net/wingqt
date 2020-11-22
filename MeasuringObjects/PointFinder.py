# import the necessary packages
import math
import matplotlib.pyplot as plt
import pprint
import cv2
import imutils
from MeasuringObjects.OrientationFinder import orientation
from MeasuringObjects.OrientationFinder import dist


#def findContour(image, edged, threshed):
def findContour(image, edged):
    startpoint = (0,0)
    endpoint = (0,0)
    ornt = 'left'
    mask = []
    # find contours in the edge map
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)
    orig = image.copy()
    # loop over the contours individually
    counter = 0
    for c in cnts:

        # if the contour is not sufficiently large, ignore it
        if cv2.contourArea(c) < 70000:
            continue
        counter+=1
        # polygon Bounds
        # Hull is the polygon contour
        hull = cv2.convexHull(c)
        mask.append(hull)

        # Draw a Polygon??
        cv2.drawContours(orig, contours=[hull], contourIdx=0, color=(255, 0, 0), thickness=2)
        cv2.drawContours(orig, contours=[ c ], contourIdx=0, color=(255, 0, 0), thickness=2)
        cMax = hull
        extLeft = tuple(cMax[ cMax[ :, :, 0 ].argmin() ][ 0 ])
        extRight = tuple(cMax[ cMax[ :, :, 0 ].argmax() ][ 0 ])
        extTop = tuple(cMax[ cMax[ :, :, 1 ].argmin() ][ 0 ])
        extBot = tuple(cMax[ cMax[ :, :, 1 ].argmax() ][ 0 ])

        # cv2.line(orig, (extLeft), (extRight), (0, 255, 255), thickness=3, lineType=8)
        # cv2.line(orig, (extTop), (extBot), (0, 255, 0), thickness=3, lineType=8)

        # Measures the distance from the extreme left point, and extreme right points
        h_len = math.hypot(extLeft[0] - extRight[0], extLeft[1] - extRight[1])
        # Measures the distance from the extreme top point to extreme right points
        v_len = math.hypot(extTop[0] - extBot[0], extTop[1] - extBot[1])

        cv2.drawContours(image, [ cMax ], -1, (0, 255, 255), 2)
        # cv2.circle(orig, extLeft, 8, (0, 255, 0), -1)
        # cv2.circle(orig, extRight, 8, (0, 255, 0), -1)
        # cv2.circle(orig, extTop, 8, (0, 255, 0), -1)
        # cv2.circle(orig, extBot, 8, (0, 255, 0), -1)

        ornt = orientation(h_len, v_len, hull, orig)

        if(ornt == 'left'):
            startpoint = extRight
            tip = extLeft
        elif(ornt == 'right'):
            startpoint = extLeft
            tip = extRight
        elif(ornt == 'top'):
            startpoint = extBot
            tip = extTop
        else:
            startpoint = extTop
            tip = extBot

        startpoint, endpoint, orig = findSmallContours(orig, edged, mask, startpoint, ornt, tip)

        print("Start: " + str(startpoint))
        print("end: " + str(endpoint))
    print(counter)

    return startpoint, endpoint, orig


def findRightMostContour(cnts, orig, tip):
    print(orig.shape)
    # shape will give you [height, width, channel]
    h, w = orig.shape[ 0:2 ]
    # get the bottom right pixel
    minPoint = (0, h/2)

    #print("minPoint = " + str(minPoint))
    min = dist(tip, minPoint)

    for c in cnts:
        for points in c:
            for point in points:

                d = dist(tip, point)
                if (min > d):
                    minPoint = point
                    min = d
    return minPoint[ 0 ], minPoint[ 1 ]


def findLeftMostContour(cnts, orig, tip):
    print(orig.shape)
    # shape will give you [height, width, channel]
    h, w = orig.shape[ 0:2 ]
    # get the bottom right pixel
    minPoint = (h, w)

   # print("minPoint = " + str(minPoint))
    min = dist(tip, minPoint)

    for c in cnts:
        for points in c:
            for point in points:
                d = dist(tip, point)
                if(min > d):
                    minPoint = point
                    min = d
    return minPoint[0], minPoint[1]


def findSmallContours(image, edged, mask, startpoint, ornt, tip):

    inverted = cv2.bitwise_not(edged)

    cnts = cv2.findContours(inverted.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    if len(cnts) == 0:
        return None, None, None
    bounded = []

# Filters contours out so that only nicely sized contours within the outer contour are counted.
    for c in cnts:
        if cv2.contourArea(c) < 400:

            #cv2.imshow('small', image)
            continue
        if cv2.contourArea(c) > 70000:
            continue
        cv2.drawContours(image, [ c ], -1, (0, 255, 255), 2)
        for points in c:
            for x,y in points:
                for m in mask:
                    if cv2.pointPolygonTest(m, (x, y), False) == 1:
                        bounded.append(c)

    print("Total bounded: " + str(len(bounded)))

    cnts = bounded

    orig = image.copy()

    # If the program is unable to find contours within the bounding contour,
    # set end point to a fixed position
    if len(bounded) == 0:
        return startpoint, (0, 0), orig

    if ornt == 'left':
        c = cnts[0]
        return startpoint, findLeftMostContour(cnts, orig, tip), orig
    elif ornt == 'right':
        c = cnts[len(cnts) - 1]
        return startpoint, findRightMostContour(cnts, orig, tip), orig
    elif ornt == 'top':
        c = cnts[0]
        return startpoint, findLeftMostContour(cnts,orig,tip), orig
    else:
        c = cnts[len(cnts) - 1]
        return startpoint, findRightMostContour(cnts, orig, tip), orig

    # #----------- Unsure if I need this yet
    # #for c in cnts:
    #
    # #c = cnts[0]
    # cMax = c
    #
    # # polygon Bounds
    # c_0 = c
    # hull = cv2.convexHull(c_0)
    #
    # # Draw a Polygon??
    # cv2.drawContours(orig, contours=[hull], contourIdx=0, color=(0, 0, 255), thickness=2)
    # cMax = hull
    # extLeft = tuple(cMax[ cMax[ :, :, 0 ].argmin() ][ 0 ])
    # extRight = tuple(cMax[ cMax[ :, :, 0 ].argmax() ][ 0 ])
    # extTop = tuple(cMax[ cMax[ :, :, 1 ].argmin() ][ 0 ])
    # extBot = tuple(cMax[ cMax[ :, :, 1 ].argmax() ][ 0 ])
    #
    # cv2.drawContours(image, [ cMax ], -1, (0, 255, 255), 2)
    # cv2.circle(orig, extLeft, 4, (0, 255, 0), -1)
    # cv2.circle(orig, extRight, 4, (0, 255, 0), -1)
    # cv2.circle(orig, extTop, 4, (0, 255, 0), -1)
    # cv2.circle(orig, extBot, 4, (0, 255, 0), -1)
    #
    # if ornt == 'left':
    #     return startpoint, extLeft, orig
    # elif ornt == 'right':
    #     return startpoint, extRight, orig
    #
    # # for point in hull:
    # #     for i in range(len(point)):
    # #         print('making circles....')
    # #         cv2.circle(orig, (point[ i ][ 0 ], point[ i ][ 1 ]), 8, (0, 0, 255), -1)
    # #return orig
    # #process_image.resize(orig)
    # # print(count)
    # #cv2.imshow("Image", orig)
    # #cv2.waitKey(0)


