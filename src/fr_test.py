import os
import face_recognition
import cv2
import pickle
import numpy as np

name = ''

# load face encodings
with open('face_enc.dat', 'rb') as f:
	known_image_enc = pickle.load(f)

nameList = list(known_image_enc.keys())
face_encodings = np.array(list(known_image_enc.values()))

print("Encoding generated")

# make a button to take a frame of the video and output recognition result
# that will be the "unknown" image

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
    
while(cap.isOpened()):

    # display stream
    ret, frame = cap.read()
    cv2.imshow('Webcam', frame)

    # listen for keypress
    c = cv2.waitKey(1) % 256 

    # if 'c' is pressed
    if c == ord('c'):

        print("Frame captured")
        
        # get encoding of current frame
        try:
            unknown_image_enc = face_recognition.face_encodings(frame)[0]

            # compare unknown image to existing encoding
            result = face_recognition.compare_faces(face_encodings, unknown_image_enc, tolerance=0.5)

            # find match and print name
            for idx, val in enumerate(result):
                if val:
                    cv2.destroyWindow(name)
                    name = nameList[idx]
                    print(name) # print name
                    im = cv2.imread("../data/%s.jpg" % (name), cv2.IMREAD_COLOR);

                    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
                    cv2.resizeWindow(name, 300, 300)
                    cv2.imshow(name, im) # show picture from db
                    break
                if( (idx) == len(result) - 1):
                    print("Unknown")
                
        except IndexError:
            print("No face detected")
            
            
        

    # 'q' = exit
    elif c == ord('q'):
        break
    
# release resources
cap.release()
cv2.destroyAllWindows()
