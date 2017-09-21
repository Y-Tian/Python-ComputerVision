import cv2
import sys

#cascPath = sys.argv[1]
cascPath = "C:\Users\Tony\Downloads\opencv\sources\data\haarcascades_cuda\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video = cv2.VideoCapture(0)

scale_f = float(sys.argv[1])

while True:
    ret, frame = video.read()

    #not working
    #fps = video.get(cv2.CAP_PROP_FPS)
    #print fps

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #scaleFactor = 1.1
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = scale_f,
        minNeighbors = 5,
        minSize = (30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print repr(x) + ',' + repr(y)

        #motor functions here, to center the camera for point x,y
        #the rectangle vertex is top left of the rectangle
        #if: c-x < 0, Mh is right; c-x >= 0, Mh is left; c-y < 0, Mv is down; c - y >= 0, Mv is up
        #c = 320, 240; it represents the center of the camera's vision

        if 320 - x < 0:
            #Motor turns right
        elif 320 - x > 0:
            #Motor turns left
        
        if 240 - y < 0:
            #Motor turns down
        elif 240 - y > 0:
            #Motor turns up
    
        #only want to detect one face at a time for the camera to track
        break
            

    cv2.imshow('Video', frame)


    #sometimes works
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

print repr(video.get(3)) + ',' + repr(video.get(4))


video.release()
cv2.destroyAllWindows()
