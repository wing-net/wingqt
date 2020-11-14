# import the necessary packages
import math
import matplotlib.pyplot as plt
import pprint
import cv2
import imutils

import process_image

# Finds the point between two points.
def midpoint(pta, ptb):
    return (pta[0] + ptb[0]) * 0.5, (pta[1] + ptb[1]) * 0.5


def findContour(image, bin_image, edged):
    startpoint = (0,0)
    endpoint = (0,0)
    ornt = 'left'
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
        mask.append(hull)
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

        #cv2.line(orig, (extLeft), (extRight), (0, 255, 255), thickness=3, lineType=8)
        w_len = math.hypot(extLeft[0] - extRight[0], extLeft[1] - extRight[1])
       # cv2.line(orig, (extTop), (extBot), (0, 255, 0), thickness=3, lineType=8)
        h_len = math.hypot(extTop[0] - extBot[0], extTop[1] - extBot[1])
        cv2.drawContours(image, [ cMax ], -1, (0, 255, 255), 2)
        #cv2.circle(orig, extLeft, 8, (0, 255, 0), -1)
      #  cv2.circle(orig, extRight, 8, (0, 255, 0), -1)
       # cv2.circle(orig, extTop, 8, (0, 255, 0), -1)
       # cv2.circle(orig, extBot, 8, (0, 255, 0), -1)
        ornt = orientation(w_len,h_len,hull,orig)

        if(ornt == 'left'):
            startpoint = extRight
            tip = extLeft
        elif(ornt == 'right'):
            startpoint = extLeft
            tip = extRight
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
    start, end, orig = findSmallContours(orig, edged, mask, startpoint, ornt, tip)
        #findSmallContours(orig, edged, mask, startpoint, ornt)
       # print("Start: " + str(start))
       # print("end: " + str(end))
    return start,end, orig



def dist(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def orientation(w_len,h_len,hull,orig):
    # Trying to figure out orientation
    # Thoughts:
    tip1 = []
    tip2 = []
    #Is the wing facing horizontally or vertically
    if w_len > h_len:
        for i in range(len(hull)):
            mid = int(len(hull) / 2)
            lobound = int(mid / 2)
            upbound = int((len(hull) + mid) / 2)
            # This will extract points on one side of the wing
            if (i >= lobound) & (i <= upbound):
                #cv2.circle(orig, (hull[i][0][0],hull[i][0][1]), 8, (0, 255, 255), -1)
                tip1.append((hull[i][0][0],hull[i][0][1]))
            else: # This will extract the points on the opposite end of the wing
               # cv2.circle(orig, (hull[ i ][ 0 ][ 0 ], hull[ i ][ 0 ][ 1 ]), 8, (255, 0, 255), -1)
                tip2.append((hull[ i ][ 0 ][ 0 ], hull[ i ][ 0 ][ 1 ]))

        distAvg1,distAvg2 = (0,0)
        # Calculates the distance between points on one end of the wing
        for i in range(len(tip1)):
            if i+1 < len(tip1):
                distAvg1 += dist(tip1[i],tip1[i + 1])

        # Calculates the distance between points on the opposite end of the wing
        for i in range(len(tip2)):
            if i+1 < len(tip2):
                distAvg2 += dist(tip2[i],tip2[i + 1])

        # Calculate Average distance between points
        dist1,dist2 = (distAvg1/(len(tip1)),distAvg2/len(tip2))

        # cv2.circle(orig, (hull[ 0 ][ 0 ][ 0 ], hull[ 0 ][ 0 ][ 1 ]), 8, (0, 0, 255), -1)
        # cv2.circle(orig, (hull[ upbound ][ 0 ][ 0 ], hull[ upbound ][ 0 ][ 1 ]), 8, (255, 255, 0), -1)
        # cv2.circle(orig, (hull[ lobound ][ 0 ][ 0 ], hull[ lobound ][ 0 ][ 1 ]), 8, (255, 0, 0), -1)
        #
        # cv2.putText(orig, "low", (hull[ lobound ][ 0 ][ 0 ], hull[ lobound ][ 0 ][ 1 ]), cv2.FONT_HERSHEY_SIMPLEX, 0.65,
        #             (0, 0, 255), 2)
        # cv2.putText(orig, "up", (hull[ upbound ][ 0 ][ 0 ], hull[ upbound ][ 0 ][ 1 ]), cv2.FONT_HERSHEY_SIMPLEX, 0.65,
        #             (0, 0, 255), 2)
        # cv2.putText(orig, "mid", (hull[ mid ][ 0 ][ 0 ], hull[ mid ][ 0 ][ 1 ]), cv2.FONT_HERSHEY_SIMPLEX, 0.65,
        #             (0, 0, 255), 2)
        # cv2.putText(orig, "start", (hull[ 0 ][ 0 ][ 0 ], hull[ 0 ][ 0 ][ 1 ]), cv2.FONT_HERSHEY_SIMPLEX, 0.65,
        #             (0, 0, 255), 2)

        if dist1 < dist2:
            return 'left'
            # print("Tip 1: " + str(tip1) + " Tip 2:" + str(tip2))
            print("WingTip is on the left side")
        else:
            return 'right'
            print("Wing tip is on the right side")
        # print(widthTip)
        # print(wingEnd)
    else:
        return 'top'
        #print("The wing tip is top or bottom")
        # print(c)
def findRightMostContour(cnts, orig, tip):
    print(orig.shape)
    # shape will give you [height, width, channel]
    h, w = orig.shape[ 0:2 ]
    # get the bottom right pixel
    minPoint = (h, w)

    print("minPoint = " + str(minPoint))
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
    minPoint = (h,w)

    print("minPoint = " + str(minPoint))
    min = dist(tip,minPoint)

    for c in cnts:
        for points in c:
            print(len(c))
            for point in points:
                d = dist(tip, point)
                if(min > d):
                    minPoint = point
                    min = d
    return minPoint[0],minPoint[1]


def findSmallContours(image, edged, mask, startpoint, ornt, tip):

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
    if len(bounded) == 0:
        return startpoint,(0,0), orig


    if ornt == 'left':
        c = cnts[0]
        return startpoint,findLeftMostContour(cnts,orig, tip),orig
    elif ornt == 'right':
        c = cnts[len(cnts) - 1]

    #for c in cnts:

    #c = cnts[0]
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

    cv2.drawContours(image, [ cMax ], -1, (0, 255, 255), 2)
    cv2.circle(orig, extLeft, 4, (0, 255, 0), -1)
    cv2.circle(orig, extRight, 4, (0, 255, 0), -1)
    cv2.circle(orig, extTop, 4, (0, 255, 0), -1)
    cv2.circle(orig, extBot, 4, (0, 255, 0), -1)

    if ornt == 'left':
        return startpoint, extLeft, orig
    elif ornt == 'right':
        return startpoint, extRight, orig

    # for point in hull:
    #     for i in range(len(point)):
    #         print('making circles....')
    #         cv2.circle(orig, (point[ i ][ 0 ], point[ i ][ 1 ]), 8, (0, 0, 255), -1)
    #return orig
    #process_image.resize(orig)
    # print(count)
    #cv2.imshow("Image", orig)
    #cv2.waitKey(0)


