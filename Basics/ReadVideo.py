import cv2
capture = cv2.VideoCapture("videos/CC.mp4") #It takes either integer arguments when you have a webcam (0) or path of the video
#We will make a loop to loop on each frame of the video and read it
while True:
    isTrue, frame = capture.read() #The capture will read frame by frame and store it in frame variable and isTrue to check if its read successfully or not.
    cv2.imshow("Coffee", frame) #This will show frame by frame.
    if cv2.waitKey(0) & 0xFF==ord('d'): #This to break out of the loop when the d is pressed & break out of loop (Stop Video)
        break
    capture.release() #Release all the capture device
    cv2.destroyAllWindows() #Destory All Windows
#-215 Assertion Failed means that opencv cannot find media files in this location and Also for videos this means no frames are found after the last frame so it broke out automatically