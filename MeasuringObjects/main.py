import os

import process_image
from pointFinder import findContour, findSmallContours
from process_image import conv_blkwht, resize, thresh_img, fill_img, split
import cv2


def main():
    path = 'C:\\Users\\monic\\PycharmProjects\\MeasuringObjectsRevised\\images'
    image_dir = os.listdir(path)
    for img in image_dir:
        original = cv2.imread(f'{path}/{img}')
        print('----------')
        print(img)
       # print("Original: " + str(original.dtype))
        edged = thresh_img(original)
       #print("edged: " + str(edged.dtype))
        flooded = fill_img(edged)
        #print("Flooded " + str(flooded.dtype))
        cv2.imwrite('temp2.JPG', conv_blkwht(flooded))
        bin_img = cv2.imread('./temp2.JPG')
        bin_img = thresh_img(bin_img)
        #print("bin_img: " + str(bin_img.dtype))
        start,end,original = findContour(original, bin_img, edged)
        print(start)
        print(type(start))
        print(end)
        print(type(end))
        #findContour(original, bin_img, edged)
        cv2.circle(original, start, 8, (0, 255, 0), -1)
        cv2.circle(original, end, 8, (0, 255, 0), -1)
        process_image.resize(original)
        # cv2.imshow("Image", orig)
        cv2.waitKey(0)



if __name__ == "__main__":
    main()