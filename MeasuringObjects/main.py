import os
from pointFinder import findContour, findSmallContours
from process_image import conv_blkwht, resize, thresh_img, fill_img, split
import cv2


def main():
    path = 'C:\\Users\\monic\\PycharmProjects\\MeasuringObjectsRevised\\images'
    image_dir = os.listdir(path)
    for img in image_dir:
        original = cv2.imread(f'{path}/{img}')
        print(img)
        print('----------')
       # print("Original: " + str(original.dtype))
        edged = thresh_img(original)
       #print("edged: " + str(edged.dtype))
        flooded = fill_img(edged)
        #print("Flooded " + str(flooded.dtype))
        cv2.imwrite('temp2.JPG', conv_blkwht(flooded))
        bin_img = cv2.imread('./temp2.JPG')
        bin_img = thresh_img(bin_img)
        #print("bin_img: " + str(bin_img.dtype))
        findContour(original, bin_img, edged)
        print('\n')



if __name__ == "__main__":
    main()