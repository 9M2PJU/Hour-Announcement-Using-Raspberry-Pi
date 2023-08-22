


https://github.com/9M2PJU/Morse-code-Hour-Announcement-Using-Python3/assets/991353/4ed60f98-4159-4d10-a928-50d0a4240c60

Python3 code for announcing the time every hour, featuring an introduction and the two-digit hour represented in Morse code:

Place the following files in the same directory: morse.py, intro.wav, and move files 0.wav to 9.wav into a "morse" subfolder.

Make sure to give execution permissions by running: chmod a+x morse.py
Run the script using: python3 morse.py
For automatic execution on boot, add the line @reboot python3 /path/to/morse.py to your crontab.

This Python script utilizes the 'play' command from SoX (install it with apt install sox) to play .wav files.

Folder structure:

morse.py
intro.wav
morse folder (contains 0.wav to 9.wav)
The Morse code will be played at a speed of 20 Words Per Minute (WPM) and a pitch of 600 Hz.

morse.py is 12 hour format.

morse24.py is 24 hour format.

73,

9M2PJU
