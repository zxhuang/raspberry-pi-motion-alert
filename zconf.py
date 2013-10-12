#!/usr/bin/env python
import datetime
SMTP_SERVER = 'smtp.gmail.com:587' # or your SMTP server:port
USERNAME = 'YOUR_USERNAME_HERE'
PASSWORD = 'YOUR_PASSWORD_HERE'
TO_FOLDER = 'motion'
FROM_EMAIL = 'YOUR_EMAIL_ADDRESS_HERE'
TO_EMAILS = 'YOUR_EMAIL_ADDRESS_HERE'
SUBJECT = 'Motion Detected @ ' + datetime.datetime.now().isoformat()
MESSAGE = SUBJECT
