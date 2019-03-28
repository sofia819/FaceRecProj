import pickle
import face_recognition
import os

# load all file names from directory and sort
dir = "../data/"
fileList = os.listdir(dir)
fileList.sort()

# make lists to store people's names and images
all_face_encodings = {}

print("Encodings generating")
# make image encodings
for f in fileList:
    name = f.replace(".jpg", "")
    print(name)
    img = face_recognition.load_image_file(dir + f)
    all_face_encodings[name] = face_recognition.face_encodings(img, num_jitters=100)[0]

print("Encodings generated")

# save face encodings
with open('face_enc.dat', 'wb') as f:
    pickle.dump(all_face_encodings, f)

    print("Encodings saved")
