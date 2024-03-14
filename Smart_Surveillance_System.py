#in this program we are using six libraries of python programing

#import necesseary libraries

import cv2      #open cv library for take input from camera
from datetime import datetime   #for current date and time
import time     #to work with time related  functions
from twilio.rest import Client  #Twilio API for sending SMS
from plyer import notification  #plyer library for desktop notification
import pygame       #pygame library for playing sound

#Twilio credentials(replace with your own values) 
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
notification_interval = 10       # Notification interval in seconds
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



