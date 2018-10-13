import cv2 

face=cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
eye=cv2.CascadeClassifier("haarcascade-eye.xml")

def detect(frame):
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray_frame,1.4,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),2)
        gray_face=gray_frame[y:y+h,x:x+w]
        face_color=frame[y:y+h,x:x+w]
        eyes=eye.detectMultiScale(gray_face,1.2,2)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(face_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),1)
    return frame

def start(path):
    cap = cv2.VideoCapture(path)
    while(cap.isOpened()):
      ret, frame = cap.read()
      if ret == True:
        cv2.imshow('Frame',detect(frame))
        if cv2.waitKey(50) & 0xFF == ord('f'):
          break
      else: 
        break
    
    cap.release()
    cv2.destroyAllWindows()
    
start("video.mp4")