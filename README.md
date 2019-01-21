# XboxHaloPGCRScraper
Simple python script that can be used to automatically save screenshots of post game carnage reports in the xbox game Halo 1.

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
  - If the script finds a PGCR frame, it will save it in the folder the script is located in.
    - The image has the naming scheme of M_SS.png where M = minutes and SS = seconds (into the video file)

Getting tesseract OCR to work in Python isn't super easy. Please follow the instructions on their website to make sure it's working: https://pypi.org/project/pytesseract/

I also recommend running this script in the base Python folder, to prevent an error that looks like this: https://stackoverflow.com/questions/24672531/annoying-python-tesseract-error-error-opening-data-file-tessdata-eng-trainedda

