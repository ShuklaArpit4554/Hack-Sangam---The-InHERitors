#in this program we are using six libraries of python programing

#import necesseary libraries

import cv2      #open cv library for take input from camera
from datetime import datetime   #for current date and time
import time     #to work with time related  functions
from twilio.rest import Client  #Twilio API for sending SMS
from plyer import notification  #plyer library for desktop notification
import pygame       #pygame library for playing sound

# Twilio credentials (replace with your own values)
account_sid = 'Enter your account sid'
auth_token = 'Enter your auth token'
twilio_phone_number = 'Enter twilio phone number'
your_phone_number = 'Enter your phone number'


#initialize Twilio client
client = Client(account_sid, auth_token)

#Load The  Haar cascade classifier for face detection

#NOTE -> The Haar Cascade classifier is like a smart tool in Python that can quickly find faces in pictures or videos.-
# It has been trained to recognize patterns that make up a face, such as eyes, nose,-
# and mouth. When you use this tool, it scans through images, and when it thinks it has found a face,-
# it lets your program know. It's like giving your computer the ability to see and point out faces!

face_cascade = cv2.CascadeClassifier("D:\Hack-Sangam---The-InHERitors\haarcascade_frontalface_default.xml")

#open a video capture object , here we are using the default camera(camera index 0)
video = cv2.VideoCapture(1)

# Define intervals for different actions
photo_capture_interval = 4       # Capture interval in seconds
notification_interval = 3       # Notification interval in seconds
sms_interval = 25                 # SMS interval in seconds
siren_interval = 3                # Siren interval in seconds

#initialize time variables
start_time = time.time()
notification_start_time = time.time()
sms_start_time = time.time()
siren_start_time = time.time()
exact_time = ""         # Initialize exact_time outside the loop

# Initialize Pygame for sound
pygame.mixer.init()
siren_sound = pygame.mixer.Sound(r"D:\Hack-Sangam---The-InHERitors\siren.wav")


# Main loop for video capture and face detection
while True:
    # Read a frame from the video capture
    check, frame = video.read()

    # Check if the frame is not None (valid frame)
    if frame is not None:
        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame using the Haar Cascade classifier
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

        # Loop over the detected faces
        for x, y, w, h in faces:
            # Draw a rectangle around each detected face
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            current_time = time.time()

            # Photo capture every 4 seconds
            if current_time - start_time >= photo_capture_interval:
                exact_time = datetime.now().strftime('%Y-%b-%d-%H-%M-%S-%f')
                cv2.imwrite("D:\Hack-Sangam---The-InHERitors/DETECTED STRANGERS/face_detected_" + str(exact_time) + ".jpg", img)
                start_time = current_time  # Update the start time for the next capture

            # Send notification every 10 seconds
            if current_time - notification_start_time >= notification_interval:
                notification_title = "Human Detected"
                notification_text = "Photo captured at {}".format(exact_time)
                notification.notify(
                    title=notification_title,
                    message=notification_text,
                    app_name='FaceDetectionApp',
                    timeout=10
                )

                notification_start_time = current_time  # Update the start time for the next notification

            # Send SMS every 30 seconds
            if current_time - sms_start_time >= sms_interval:
                message_body = " -> ! Human Detected Be Alert ! <-  {}".format(exact_time)
                message = client.messages.create(
                    body=message_body,
                    from_=twilio_phone_number,
                    to=your_phone_number
                )
                sms_start_time = current_time  # Update the start time for the next SMS

            # Play siren sound every 5 seconds
            if current_time - siren_start_time >= siren_interval:
                siren_sound.play()
                siren_start_time = current_time  # Update the start time for the next siren sound

        # Display the frame with detected faces
        cv2.imshow("home surv", frame)
        key = cv2.waitKey(1)

        # Break the loop if 'a' key is pressed
        if key == ord('a'):
            break

# Release video capture and close all windows
video.release()