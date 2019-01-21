from PIL import Image
import pytesseract
import argparse
import cv2
import os

#construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required=True,
	help="path to input video to be OCR'd")
args = vars(ap.parse_args())

#pass video argument into cv2
vidcap = cv2.VideoCapture(args["index"])

#get video file info
fps = vidcap.get(cv2.CAP_PROP_FPS)
count = 0
vidcap.set(1,count-1)
success,image = vidcap.read()
height, width, channels = image.shape
banner_height = int((80/480)*height)
pgcr_flag = 0

print("Video Framerate = " + str(fps))
print("Video Resolution = " + str(height) + "x" + str(width))
print("Reading video")

while success:
    print("Reading frame " + str(count))
    
    #crop image only to area that would have Post Game Carnage Report Banner
    banner = image[0:banner_height, 0:width] #for 640x480 image, fixed values are image[0:80, 0:640]

    #convert to grayscale for better OCR results
    gray = cv2.cvtColor(banner, cv2.COLOR_BGR2GRAY)

    #run OCR on cropped grayscale image
    text = pytesseract.image_to_string(gray)

    #if the text we are looked for is there, save screenshot with video timestamp
    if "POSTGAME CARNAGE REPORT" in text and pgcr_flag == 0:
        minutes = int(count/60)
        seconds = count % 60
        print("pgcr present = " + str(count))
        cv2.imwrite(str(minutes) + "_" + str(seconds) + ".png", image)
        pgcr_flag = 1
    #to prevent screenshotting the same PGCR potentially hundreds of times, use this flag prevent that
    elif "POSTGAME CARNAGE REPORT" not in text and pgcr_flag == 1:
        pgcr_flag = 0

    #increment video by one second, then read frame
    count += int(fps)
    vidcap.set(1,count-1)
    success,image = vidcap.read()
    
print("Script complete")
