# XboxHaloPGCRScraper
Simple python script that can be used to automatically save screenshots of post game carnage reports in the xbox game Halo 1.

# How it works

Video of it in action: https://www.twitch.tv/videos/367828464

- We take the top 16% of the frame, convert it to grayscale, run OCR on it and see if it says "POSTGAME CARNAGE REPORT"

![Nope](https://raw.githubusercontent.com/CYRiXplaysHalo/XboxHaloPGCRScraper/master/13844.png)

![Nope](https://raw.githubusercontent.com/CYRiXplaysHalo/XboxHaloPGCRScraper/master/11312.png)

There we go:

![Yup!](https://raw.githubusercontent.com/CYRiXplaysHalo/XboxHaloPGCRScraper/master/10096.png)

And then we save the whole screen:

![Perfect!](https://raw.githubusercontent.com/CYRiXplaysHalo/XboxHaloPGCRScraper/master/4_21.png)

# Instructions

- Get Python (I used 3.7) and install the following libraries
  - PIL
  - cv2
  - tesseract
  - tesseract-ocr
  - pytesseract
- Run the script via command line like so:
  - For a video file use "Scrape_PGCR_From_Video.py -video out.mp4" without the quotations. 
    - Replace out.mp4 with the video file of your choice.
    - The script will tell you when it's complete.
  - For a capture device use "Scrape_PGCR_From_Device.py -index 0" without the quotations. 
    - The index number represents which connected capture device to pull from. If you only have one capture device that index is 0. Unfortunately there is no current way to list the indices of all capture devices so you will probably just have to increment the index until it works for you.
    - To stop the script from running, just exit out of the command line window.
  - The script should update it's status in the command line window.
    - When the script first starts it will save a test screen shot to the local folder named "HH-MM-SS - Test Screenshot.png"
      - Use this to verify the capture device index you provided is the right one.
  - If the script finds a PGCR frame, it will save it in the folder the script is located in.
    - The image has the naming scheme of "HH-MM-M-SS - PGR.png" 
      - HH = hours, M = minutes and SS = seconds (into the video file)
  - The script will also keep series score.
    - It does this by writing the score for each team into the following files:
      - Blue team = blue_team_series_score.txt
      - Red team = red_team_series_score.txt
    - To reset the series score, simply edit the text files.
  - To see the capture device script in action, watch this video: https://www.twitch.tv/videos/370337250
  - It is recommended you use the OBS-VirtualCam plug-in as the input capture device for this script.
    - You can run two instances of OBS-Studio at once
    - You can find the OBS-VirtualCam plug-in here: https://obsproject.com/forum/resources/obs-virtualcam.539/

Getting tesseract OCR to work in Python isn't super easy. Please follow the instructions on their website to make sure it's working: https://pypi.org/project/pytesseract/

I also recommend running this script in the base Python folder, to prevent an error that looks like this: https://stackoverflow.com/questions/24672531/annoying-python-tesseract-error-error-opening-data-file-tessdata-eng-trainedda
