import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

username = 'USERNAME' #you don't need the "@gmail.com" bit.
password = 'PASSWORD'

From =  "EMAIL"

To =  "PHONE@vtext.com"
# To =  "7325339002@txt.att.net"

#######################################
# Email Parameters when sensor is Wet #
#######################################

Subject_wet = "IP address"
Body_wet = "msg body"


Subject_dry = "RPi Water Sensor is DRY"
Body_dry = " Your water sensor is dry again!"

import smtplib
from email.mime.text import MIMEText
# import RPi.GPIO as GPIO
import string
import time
from time import gmtime, strftime, ctime
import os
# Function Definitions

#takes either "wet" or "dry" as the condition.
# def email(condition):
def email(message):
    # Current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    Current_time = ctime()
    print ("Attempting to send email at %s" % Current_time)
    str=" "
    # Body = string.join((
    Body = "From: %s\nTo: %s\nSubject: %s\n %s %s \r\n" % (From, To, Subject_wet, message, Current_time)
    # The actual mail send
    server = smtplib.SMTP('smtp.mail.yahoo.com',587)
    server.starttls()
    print ("Logging in...")
    server.login(username,password)
    print ("Logged in as "+username+".")
    server.sendmail(From, [To], Body)
    server.quit()
    print ("Email sent.")

myIP=get_ip()
email(myIP)
print(get_ip())
