#!/usr/bin/env python
"""
Copyright (c) 2013, Zeke Huang
All rights reserved.
https://github.com/zxhuang/raspberry-pi-motion-alert
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def smtp_email(server, username, password, from_email, to_emails, subject, message, image=None):
    """ Send email with image attachment through smtp.
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ','.join(to_emails) if type(to_emails) is list else to_emails
    msg.attach(MIMEText(message))
    if image is not None:
        with open(image, 'rb') as fp:
            img = MIMEImage(fp.read())
            msg.attach(img)

    s = smtplib.SMTP(server)
    s.starttls()
    s.login(username, password)
    s.sendmail(from_email, to_emails, msg.as_string())
    s.quit()




##########################
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Send email with image attachment through smtp.')
    parser.add_argument('--server', required=True, help='SMTP server:port')
    parser.add_argument('--username', required=True, help='SMTP server username')
    parser.add_argument('--password', required=True, help='SMTP server password')
    parser.add_argument('--from_email', required=True, help='from email address')
    parser.add_argument('--to_emails', required=True, help='to email addresses separated by comma')
    parser.add_argument('--subject', required=True, help='email subject')
    parser.add_argument('--message', required=True, help='email message')
    parser.add_argument('--image', required=False, help='image file path')
    args = parser.parse_args()

    smtp_email(**vars(args))


