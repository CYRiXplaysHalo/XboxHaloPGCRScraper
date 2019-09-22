from PIL import Image
import pytesseract
import argparse
import cv2
import os
from datetime import datetime

#construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required=True,
	help="path to input video to be OCR'd")
args = vars(ap.parse_args())

#pass video argument into cv2
vidcap = cv2.VideoCapture(int(args["index"]))

timestamp = datetime.now().strftime('%H-%M-%S')

#get video file info
count = 0
success,image = vidcap.read()
print(success)
cv2.imwrite(timestamp + " - Test Screenshot.png", image)
height, width, channels = image.shape
banner_height = int((80/480)*height)
footer_height = int((400/480)*height)
pgcr_flag = 0

#print("Video Resolution = " + str(height) + "x" + str(width))
print("Reading capture device now. Force quit to stop.")

blue_team_series_score = 0
red_team_series_score = 0

while success:
    timestamp = datetime.now().strftime('%H-%M-%S')
    print(timestamp + " - Reading frames ")
    
    #crop image only to area that would have Post Game Carnage Report Banner
    banner = image[0:banner_height, 0:width] #for 640x480 image, fixed values are image[0:80, 0:640]

    #convert to grayscale for better OCR results
    gray = cv2.cvtColor(banner, cv2.COLOR_BGR2GRAY)

    #run OCR on cropped grayscale image
    text = pytesseract.image_to_string(gray)

    #if the text we are looked for is there, save screenshot with video timestamp
    if "POSTGAME CARNAGE REPORT" in text and pgcr_flag == 0:
        print("PGCR Present at frame " + str(count))
	
	#Perform OCR on footer of screen to get file name
	footer = image[footer_height:height, 0:width-140] #must omit right part incase timer or prompts appear
        gray = cv2.cvtColor(footer, cv2.COLOR_BGR2GRAY)
        footer_text = pytesseract.image_to_string(gray)
        footer_text = footer_text.strip()
        footer_text = ''.join(x for x in footer_text if x.isalpha())
	
	#output screen shot
        cv2.imwrite(timestamp + " - " + footer_text + " - PGCR.png", image)
        gray2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        pgcr_text = pytesseract.image_to_string(cv2.threshold(gray2, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1])
        print(pgcr_text)
        text_arr = pgcr_text.split('\n')
	
	#read in score files incase scores were edited
	file = open("red_team_series_score.txt","r")
        red_team_series_score = int(file.read())

        file = open("blue_team_series_score.txt","r")
        blue_team_series_score = int(file.read())
	
	#whichever team shows up first is the one that one
	#no this doesn't account for weird tie situations
        for row in text_arr:
            if "Blue Team" in row:
                    blue_team_series_score += 1
                    break
            elif "Red Team" in row:
                    red_team_series_score += 1
                    break

	#update score files
        file = open("red_team_series_score.txt","w") 
        file.write(str(red_team_series_score)) 
        file.close()

        file = open("blue_team_series_score.txt","w") 
        file.write(str(blue_team_series_score)) 
        file.close() 
        pgcr_flag = 1             

    #to prevent screenshotting the same PGCR potentially hundreds of times, use this flag prevent that
    elif "POSTGAME CARNAGE REPORT" not in text and pgcr_flag == 1:
        pgcr_flag = 0

    #increment video by one second, then read frame
    success,image = vidcap.read()
    
