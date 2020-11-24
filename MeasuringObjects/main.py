from MeasuringObjects.process_image import conv_blkwht, resize, thresh_img, thresh_img_2, fill_img, split
from MeasuringObjects.PointFinder import findContour
import cv2
import argparse

def main():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to the input image")
    args = vars(ap.parse_args())

    original = cv2.imread(args["image"])
    # print('----------')
    # print(args["image"])

    # Will find the overall shape of the wing
    edged = thresh_img_2(original)
    #edged = thresh_img(original)
    #cv2.imshow("edged", edged)

    threshed = thresh_img(original)
    start, end, original = findContour(original, edged, threshed)
    # print(start)
    # print(type(start))
    # print(end)
    # print(type(end))
    #findContour(original, bin_img, edged)
    cv2.circle(original, start, 8, (0, 255, 0), -1)
    cv2.circle(original, end, 8, (0, 255, 0), -1)
    print(start, end)
    #resize(original)
    #cv2.waitKey(0)

# Gets a better shape around the wing
def analyzeWithCanny(path):
    original = cv2.imread(path)
    # Will find the overall shape of the wing
    edged = thresh_img_2(original)
    # cv2.imshow("edged", edged)

    threshed = thresh_img(original)
    start, end, original = findContour(original, edged, threshed)
    print(start, end)
    return (start, end)

def analyze(path):
    original = cv2.imread(path)
    edged = thresh_img(original)
    start, end, _ = findContour(original, edged)
    print(start, end)
    return (start, end)

if __name__ == "__main__":
    main()
