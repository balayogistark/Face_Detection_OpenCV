import cv2

#get user supplied values
cascPath = "haarcascade_frontalface_default.xml"

#Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

#read image
image = cv2.imread('humans.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#detect faces in the image
faces  = faceCascade.detectMultiScale(
    gray,
    scaleFactor = 1.1,
    minNeighbors = 5,
    minSize = (30,30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print("found {0} faces!".format(len(faces)))

#draw a rectangle around the faces
for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("Faces found",image)
cv2.waitKey(0)
