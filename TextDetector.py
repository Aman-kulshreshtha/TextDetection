import cv2
import pytesseract


path_to_output_file = 'extractedtext'
path_to_pytesseract_executable = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
video_file_name = 'videofile.mp4'
frame_rate = 100







# function to write the output to the file(
def write_to_file(text):
    f = open(path_to_output_file,'a')
    f.write(text)
    f.close()



# providing the path to the pytysseract Executables:
pytesseract.pytesseract.tesseract_cmd = path_to_pytesseract_executable


# capturing the video using the openCV Video Capture method
vid = cv2.VideoCapture('Resources/' + video_file_name)


#initial frame count (starting of counting of the frames)
frameCount = 0
success = 1

#main program loop
while success:

    success, img = vid.read()                       #reading the video image by image
    frameCount += 1                                 #increasing the count on reading a single frame in the form of image



    if (frameCount % frame_rate == 0 and success):



        #cv2.imshow('video', img)

        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        text = pytesseract.image_to_string(img)

        write_to_file(text)
        print(text)

        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

