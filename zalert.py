#!/usr/bin/env python
"""
Copyright (c) 2013, Zeke Huang
All rights reserved.
https://github.com/zxhuang/raspberry-pi-motion-alert
"""

import datetime
from zemail import smtp_email
from zupload import gd_avi_upload

SMTP_SERVER = 'smtp.gmail.com:587' # or your SMTP server:port
USERNAME = 'YOUR_USERNAME_HERE'
PASSWORD = 'YOUR_PASSWORD_HERE'
TO_FOLDER = 'motion'
FROM_EMAIL = 'YOUR_EMAIL_ADDRESS_HERE'
TO_EMAILS = 'YOUR_EMAIL_ADDRESS_HERE'
SUBJECT = 'Motion Detected @ ' + datetime.datetime.now().isoformat()
MESSAGE = SUBJECT


def send_alert_email(avideo=None):
    email_args = {
        'server': SMTP_SERVER,
        'username': USERNAME,
        'password': PASSWORD,
        'from_email': FROM_EMAIL,
        'to_emails': TO_EMAILS,
        'subject': SUBJECT,
        'message': MESSAGE,
    }
    if avideo is not None:
        upload_args = {
            'username': USERNAME,
            'password': PASSWORD,
            'to_folder': TO_FOLDER,
            'avideo': avideo
        }
        link = gd_avi_upload(**upload_args)
        email_args['image'] = avideo.split('.')[0] + '.jpg'
        email_args['message'] = MESSAGE + '\n' + link

    smtp_email(**email_args)


##########################
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Send alert email optionally with image attachment and video link through smtp.')
    parser.add_argument('--avideo', required=False, help='AVI video file path')
    args = parser.parse_args()

    send_alert_email(**vars(args))


