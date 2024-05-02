import cv2
face_detect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('img.jpeg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_detect.detectMultiScale(gray,1.2,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),5)
cv2.imshow('img',img)
cv2.waitKey()
