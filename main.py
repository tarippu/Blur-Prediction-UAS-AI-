from imutils import paths
import argparse
import cv2
import sys
 
def variance_of_laplacian(image):
	return cv2.Laplacian(image, cv2.CV_64F).var()
 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
	help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

for imagePath in paths.list_images(args["images"]):
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = variance_of_laplacian(gray)

	if fm > args["threshold"]:
		text = imagePath+" - Not Blurry: "+str(fm)
		print(imagePath+" - Not Blurry: "+str(fm))

	if fm < args["threshold"]:
		text = imagePath+" - Blurry: "+str(fm)
		print(imagePath+" - Blurry: "+str(fm))
