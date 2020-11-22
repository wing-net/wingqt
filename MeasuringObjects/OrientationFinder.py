import cv2
import math


# Divides the wing's contour into two pieces: the middle and the ends.
def divideWing(hull):
    tip1 = [ ]
    tip2 = [ ]

    for i in range(len(hull)):
        mid = int(len(hull) / 2)
        lobound = int(mid / 2)
        upbound = int((len(hull) + mid) / 2)
        # This will extract points on one side of the wing
        if (i >= lobound) & (i <= upbound):
            # cv2.circle(orig, (hull[i][0][0],hull[i][0][1]), 8, (0, 255, 255), -1)
            tip1.append((hull[ i ][ 0 ][ 0 ], hull[ i ][ 0 ][ 1 ]))
        else:  # This will extract the points on the opposite end of the wing
            # cv2.circle(orig, (hull[ i ][ 0 ][ 0 ], hull[ i ][ 0 ][ 1 ]), 8, (255, 0, 255), -1)
            tip2.append((hull[ i ][ 0 ][ 0 ], hull[ i ][ 0 ][ 1 ]))
    return tip1, tip2


# Calculates the distance between points on an end of the wing
def distanceToTip(tip):
    distAvg = 0
    for i in range(len(tip)):
        if i + 1 < len(tip):
            distAvg += dist(tip[ i ], tip[ i + 1 ])
    return distAvg


# Calculates the distance between two points
def dist(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def orientation(h_len, v_len, hull, orig):
    if h_len > v_len:
        tip1, tip2 = divideWing(hull)

        # Finds the distance between corner points in the polygon
        # A close average distance would mean the polygon is curving
        # Which is indicitive of a the tip of the wing
        distAvg1 = distanceToTip(tip1) / (len(tip1))
        distAvg2 = distanceToTip(tip2) / (len(tip2))

        if distAvg1 < distAvg2:
            print('Wing tip is on the left side')
            return 'left'
        else:
            print('wing tip is on the right side')
            return 'right'
    else:
        tip1, tip2 = divideWing(hull)

        # Finds the distance between corner points in the polygon
        # A close average distance would mean the polygon is curving
        # Which is indicitive of a the tip of the wing
        distAvg1 = distanceToTip(tip1) / (len(tip1))
        distAvg2 = distanceToTip(tip2) / (len(tip2))
        if distAvg1 < distAvg2:
            print('Wing tip is on the top')
            return'top'
        else:
            print('Wing tip is on the bottom')
            return 'bottom'

