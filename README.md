# FaceRecProj

### src:
* makeFaceEnc:
	* Creates encodings of the pictures from data.
	* Saves the encodings to face_enc.dat
* fr_text:
	* Loads face_enc.dat.
	* Opens webcam.
		* Press 'c' to capture current frame and compare to face encodings.
			* If a match is found, the original picture will be shown.
		* Press 'q' to quit program.

### data:
* Contains pictures of each person from class

### Dependencies:
* Python3
* OpenCV (opencv-contrib-python)
* face_recognition (https://github.com/ageitgey/face_recognition)
	* dlib
	
### Steps:
1. Install Python3 & pip
	```
	sudo apt install python3-pip
	```
2. Install opencv-contrib-python (pip3)  
	```
	pip3 install opencv-contrib-python
	```
3. Install dlib (https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)
	* Install packages:  
	```
	sudo apt install build-essential cmake gfortran git wget curl graphicsmagick libgraphicsmagick1-dev libatlas-dev libavcodec-dev ibavformat-dev libgtk2.0-dev libjpeg-dev liblapack-dev libswscale-dev pkg-config python3-dev python3-numpy software-properties-common zip
	```
	* Clone the dlib repository:  
	```
	git clone https://github.com/davisking/dlib.git
	```
	* Build the dlib repository:  
	```
	cd dlib
	mkdir build; cd build; cmake ..; cmake --build .
	```
	* Install dlib
	```
	cd ..
	python3 setup.py install
	```
	* Install face_recognition library (https://github.com/ageitgey/face_recognition)
	```
	pip3 install face_recognition
	```
	
