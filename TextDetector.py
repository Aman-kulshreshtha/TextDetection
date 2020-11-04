import cv2
import pytesseract

path_to_pytesseract_executable = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
video_file_name = 'video.mp4'
frame_rate = 200


pytesseract.pytesseract.tesseract_cmd = path_to_pytesseract_executable

vid = cv2.VideoCapture('Resources/' + video_file_name)

frameCount = 0

while True:

    success, img = vid.read()
    frameCount += 1

    if (frameCount % frame_rate == 0):
        cv2.imshow('video', img)

        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        text = pytesseract.image_to_string(img)

        print(text)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

