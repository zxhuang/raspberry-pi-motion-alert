raspberry-pi-motion-alert
=========================

Thanks to Motion which has GPL license:
http://www.lavrsen.dk/foswiki/bin/view/Motion/WebHome

This repo only has example config file for motion and 
a script that sends email alerts and upload recorded 
video to Google docs.

Install
=======
1. Download and install Rasbian Wheezy on your Raspberry Pi.
2. Download and install motion.
3. Download Google Drive app on your mobile device
4. Create folder named 'motion in your Google Drive
5. Change USERNAME, PASSWORD, FROM_EMAIL and TO_EMAILS in zalert.py
6. sudo cp motion.conf /etc/motion/
7. sudo cp zalert.py zemail.py zupload.py /etc/motion/
8. sudo /etc/init.d/motion restart

Testing
=======
./zalert.py --avideo ./test.avi
