import cv2
img = cv2.imread('images/Cup.jfif') #Matrix of Image Pixels
cv2.imshow("Cup",img) #Show Image os a new window that takes two parameter, 1. Window Name, 2. Actual Matrix of Pixels.
cv2.waitKey(0) #Keyboard Binding Function. It waits for specific time in miliseconds for a key to be pressed.

