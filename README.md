# Face Recognition Based Attendance System
Makes attendance records in realtime using python's [face recognition](https://pypi.org/project/face-recognition/ "face recognition") library.
All we need is one image of the person to be detected by the camera.

_


#### Installing on Linux

First, make sure you have dlib already installed with Python bindings:

  * [How to install dlib from source on macOS or Ubuntu](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)

Cloning the repository
```bash
git clone https://github.com/aashutoshPanda/Face-Recognition-Based-Attendance-System.git
cd Face-Recognition-Based-Attendance-System
```
Making Virtual environment for the project
```bash
python3 -m venv <myvenv>
source <myvenv>/bin/activate
```
Installing the required packages to our virtual environment
```bash
pip install -r requirements.txt
```
Running the script
```bash
python3 main.py
```
###### Press q to Quit


### Instructions
"student_db/people_db.xlsx " file contains student record and their images 
To add new student add the name,roll no. & image file name to the excel sheet

After running the program attendance record is generated with current time stamp telling the details of the students recognised by the camera
