import face_recognition
import os
import cv2
#image = face_recognition.load_image_file("alen.jpg")
#face_locations = face_recognition.face_locations(image)
first=input("enter 1st imag file name")
second=input("enter the second")
with open('uk', 'r') as f:
    data = f.read()
loadimg=face_recognition.load_image_file(first)
loadimg1=face_recognition.load_image_file(2)
face_locations = face_recognition.face_locations(loadimg)
face_locations1=face_recognition.face_locations(loadimg1)
if face_locations == face_locations1:
    print("match found")
else:
    print("match not find")