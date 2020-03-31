import os
import argparse
from PIL import Image
import numpy as np
import cv2

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-d", "--directory", required=True, help="Directory with images")
arg_parser.add_argument("-o", "--output", required=True, help="Filepath where result will saved")

arg_parser.add_argument("-r", "--red", type=int, required=True, help="Color red value")
arg_parser.add_argument("-rt", "--red-tolerance", type=int, required=True, help="Color red tolernace value")
arg_parser.add_argument("-g", "--green", type=int, required=True, help="Color green value")
arg_parser.add_argument("-gt", "--green-tolerance", type=int, required=True, help="Color green tolernace value")
arg_parser.add_argument("-b", "--blue", type=int, required=True, help="Color blue value")
arg_parser.add_argument("-bt", "--blue-tolerance", type=int, required=True, help="Color blue tolernace value")

arg_parser.add_argument("-i", "--interactive", type=bool, required=False, help="Color blue value")
args = arg_parser.parse_args()

def get_size(filename):
    image = Image.open(filename)
    return image.size

def is_greyscale(img_path):
    img = Image.open(img_path).convert('RGB')
    w,h = img.size
    for i in range(w):
        for j in range(h):
            r,g,b = img.getpixel((i,j))
            if r != g != b: return False
    return True

def get_color_coverage(filename):
    image = cv2.imread(filename)
    color = [args.red, args.green, args.blue]

    boundaries = [([color[2]-args.blue_tolerance, color[1]-args.green_tolerance, color[0]-args.red_tolerance], 
                   [color[2]+args.blue_tolerance, color[1]+args.green_tolerance, color[0]+args.red_tolerance])]
    color_coverage = 0
    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)

        color_coverage = cv2.countNonZero(mask)/(image.size/3)
        if args.interactive:
            print('color pixel percentage:', np.round(color_coverage*100, 2))
            cv2.imshow("images", np.hstack([image, output]))
            cv2.waitKey(0)
    return np.round(color_coverage*100, 2)

print("Start generating report ...: " + args.output)

if not os.path.exists(os.path.dirname(args.output)):
    os.makedirs(args.output)

with open(args.output,"w+") as result:
    result.write("image_path,width,height,is_grayscale,color_coverage\n")
    for root, _, files in os.walk(args.directory):
        for file in files:
            if file.lower().endswith("jpg"):
                width, height = get_size(os.path.join(root, file))
                greyscale = is_greyscale(os.path.join(root, file))
                color_coverage = get_color_coverage(os.path.join(root, file))
                result.write("%s,%s,%s,%r,%d\n" % (os.path.join(root, file), width, height, greyscale, color_coverage))
print("Report successfully generated!: " + args.output)

