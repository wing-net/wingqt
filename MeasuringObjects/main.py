from process_image import conv_blkwht, resize, thresh_img, fill_img, split
from PointFinder import findContour
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

    edged = thresh_img(original)
    flooded = fill_img(edged)
    cv2.imwrite('temp2.JPG', conv_blkwht(flooded))
    bin_img = cv2.imread('./temp2.JPG')
    bin_img = thresh_img(bin_img)
    start, end, original = findContour(original, bin_img, edged)
    # print(start)
    # print(type(start))
    # print(end)
    # print(type(end))
    #findContour(original, bin_img, edged)
    cv2.circle(original, start, 8, (0, 255, 0), -1)
    cv2.circle(original, end, 8, (0, 255, 0), -1)
    print(start, end)
    resize(original)
    cv2.waitKey(0)



if __name__ == "__main__":
    main()