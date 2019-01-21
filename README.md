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
  - "Scrape_PGCR_From_Video.py -v out.mp4" without the quotations
  - The script should update it's status in the command line video
  - If the script finds a PGCR frame, it will save it in the folder the script is located in.
    - The image has the naming scheme of M_SS.png where M = minutes and S = seconds (into the video file)

Getting tesseract OCR to work in Python isn't super easy. Please follow the instructions on their website to make sure it's working: https://pypi.org/project/pytesseract/

I also recommend running this script in the base Python folder, to prevent an error that looks like this: https://stackoverflow.com/questions/24672531/annoying-python-tesseract-error-error-opening-data-file-tessdata-eng-trainedda
