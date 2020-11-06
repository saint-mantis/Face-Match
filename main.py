
import face_recognition
import pyttsx3

def speak(sp):
    engine=pyttsx3.init()
    engine.say(sp)
    print(sp)
    engine.runAndWait()

image1 = face_recognition.load_image_file("first_image.jpg")
face_locations1 = face_recognition.face_locations(image1)
image2 = face_recognition.load_image_file("second_image.jpg")
face_locations2 = face_recognition.face_locations(image2)


if face_locations2 == face_locations1:
	speak("match found")
else:
    speak("sorry,no match found")
