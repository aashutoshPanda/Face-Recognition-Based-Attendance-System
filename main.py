import face_recognition
import cv2
import numpy as np
import os
import pandas as pd
import time
from utils import append_df_to_excel
# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# # Load a sample picture and learn how to recognize it.
# obama_image = face_recognition.load_image_file("obama.jpg")
# obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# # Load a second sample picture and learn how to recognize it.
# biden_image = face_recognition.load_image_file("biden.jpg")
# biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# # Load a second sample picture and learn how to recognize it.
# ronit_image = face_recognition.load_image_file("ronit.png")
# ronit_face_encoding = face_recognition.face_encodings(ronit_image)[0]
# # Create arrays of known face encodings and their names
# panda_image = face_recognition.load_image_file("panda.png")
# panda_face_encoding = face_recognition.face_encodings(panda_image)[0]
# known_face_encodings = [
#     obama_face_encoding,
#     biden_face_encoding,
#     ronit_face_encoding,
#     panda_face_encoding
# ]
# known_face_roll_no = [
#     "Barack Obama",
#     "Joe Biden",
#     "Ronit Sarkar",
#     "Ashutosh Panda"
# ]

# Initialize some variables
known_face_encodings = []
known_face_roll_no = []
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
attendance_record = set([])
roll_record = {}

# Rows in log file
name_col = []
roll_no_col = []
time_col = []

df = pd.read_excel("student_db" + os.sep + "people_db.xlsx")

for key, row in df.iterrows():
    roll_no = row['roll_no']
    name = row['name']
    image_path = row['image']
    roll_record[roll_no] = name
    student_image = face_recognition.load_image_file(
        "student_db" + os.sep + image_path)
    student_face_encoding = face_recognition.face_encodings(student_image)[0]
    known_face_encodings.append(student_face_encoding)
    known_face_roll_no.append(roll_no)


while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding, tolerance=0.5)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_roll_no[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                roll_no = known_face_roll_no[best_match_index]
                # add this to the log
                name = roll_record[roll_no]
                if roll_no not in attendance_record:
                    attendance_record.add(roll_no)
                    print(name, roll_no)
                    name_col.append(name)
                    roll_no_col.append(roll_no)
                    curr_time = time.localtime()
                    curr_clock = time.strftime("%H:%M:%S", curr_time)
                    time_col.append(curr_clock)

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        # top *= 2
        # right *= 2
        # bottom *= 2
        # left *= 2

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# print(name_col)
# print(roll_no_col)
# print(time_col)

# Printing to log file

data = {'Name': name_col, 'Roll No.': roll_no_col, 'Time': time_col}

curr_time = time.localtime()
curr_clock = time.strftime("%c", curr_time)
log_file_name = "attendance_record " + curr_clock + ".xlsx"

append_df_to_excel(log_file_name, data)


# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
