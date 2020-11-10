import cv2
import pytesseract


# function to write the output to the file(
def write_to_file(text):
    f = open('extractedtext.txt', 'a')
    f.write(text)
    f.close()


# providing the path to the pytysseract Executables:
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

frame_rate = 100

print('\n\nPLease enter a choice:\n')
choice = int(input('To Extract text from a video press 1 \nTo extract text from webCam press  2 \nChoice: '))

if (choice == 1):

    # capturing the video using the openCV Video Capture method
    vid = cv2.VideoCapture('Resources/videofile.mp4')

    # initial frame count (starting of counting of the frames)
    frameCount = 0
    success = 1

    # main program loop
    while success:

        success, img = vid.read()  # reading the video image by image
        frameCount += 1  # increasing the count on reading a single frame in the form of image
        if (frameCount % frame_rate == 0 and success):
            cv2.imshow('video', img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            text = pytesseract.image_to_string(img)

            write_to_file(text)
            print(text)

        if cv2.waitKey(1) == ord('q'):
            break






elif (choice == 2):

    # capturing the video using the openCV Video Capture method
    vid = cv2.VideoCapture(0)  # 0 signifies default webcam

    # initial frame count (starting of counting of the frames)
    frameCount = 0
    success = 1

    # main program loop
    while success:

        success, img = vid.read()  # reading the video image by image
        frameCount += 1  # increasing the count on reading a single frame in the form of image

        if (frameCount % frame_rate == 0 and success):

            hImg, wImg, _ = img.shape
            boxes = pytesseract.image_to_boxes(img)

            for b in boxes.splitlines():
                b = b.split()
                x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
                cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 255, 0), 1)

            cv2.imshow('video', img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            text = pytesseract.image_to_string(img)
            write_to_file(text)
            print(text)

        if cv2.waitKey(1)  == ord('q'):
            break