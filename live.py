import cv2

alg="haarcascade_frontalface_default.xml"
haar_cascade=cv2.CascadeClassifier(alg)

cam=cv2.VideoCapture(0)

while True:
    ret,img= cam.read()

    gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=haar_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (155,155,255), 5)

    cv2.imshow("Face Detection",img)

    key=cv2.waitKey(1)
    if key==27:
        break

cam.release()
cv2.destroyAllWindows()
                                        


                                        
