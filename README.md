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



### Instructions
Put all the images in 'student_db' directory & run the 'db_maker.py' file 
```bash
python3 db_maker.py
```
then excel file named 'people_db.xlsx' is made inside the 'student_db' directory
- name of the person is extracted from the image name
- second column has the file name (files are renamed by replacing spaces by underscores)
- roll no. is given from 1 to N you can edit according to your needs

To run the facial recognition system run 'main.py'
```bash
python3 main.py
```
###### Press q to Quit

After running the program attendance record is generated with current timestamp (Ex. 'attendance_record Sun 06 Sep 2020 18:40:11 IST.xlsx' ) providing the details of the students recognised by the camera
