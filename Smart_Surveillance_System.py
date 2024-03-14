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
