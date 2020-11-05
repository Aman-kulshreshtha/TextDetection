# Python Program to extract text from a video file

### Libraries and modules used

1. OpenCV
2. Pytesseract


### Working

This program extracts the text shown in a video file and writes in the file named 'extractedtext.txt' .
Video is captured using the Opencv video capture method . and then The text is extracted using the pytesseract library.


### To Run in your local machine :

1. Download the project code 
2. Install the pytesseract OCR .
2. Provide the necesary name of video file , name of output file ,framerate and path to pytysseract executable.


### Limitations:
1. It is necessary that the text should be properly focussed for the OCR to work properly.
2. Watermarks and excess of animations will produce garbage results.
3. If a text is displayed for too long , it will be printed multiple times.




