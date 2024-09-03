import cv2


cap = cv2.VideoCapture(0)

#write the video 
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

#save the video 
out = cv2.VideoWriter("out.mp4",fourcc,15,(469,239))

while True:
    #ret is boolean helps to
    ret, frame = cap.read()

  #color to black and white capture 
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    face = face_cascade.detectMultiScale(gray, scaleFactor =1.1,minNeighbors=5,minSize=(30,30))
  



    for (x,y,w,h) in face:
        cv2.rectangle(gray,(x,y),(x+w, y+h),(0,255,0), 3)

    
    cv2.imshow('Camera Feed', gray)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
