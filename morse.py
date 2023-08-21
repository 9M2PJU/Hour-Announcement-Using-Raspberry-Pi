import time
import datetime
import subprocess

def play_intro_sound():
    subprocess.call(["play", "intro.wav"])

def play_morse_digit(digit):
    subprocess.call(["play", f"morse/{digit}.wav"])
    time.sleep(0.2)  # Pause between digits

def speak_hour(hour):
    for digit in hour:
        play_morse_digit(digit)

def main():
    while True:
        current_minute = datetime.datetime.now().strftime("%M")
        
        if current_minute == "00":
            # First sequence
            play_intro_sound()
            current_hour = datetime.datetime.now().strftime("%I")
            speak_hour(current_hour)
            
            # Delay between sequences
            time.sleep(2)
            
            # Second sequence
            play_intro_sound()
            speak_hour(current_hour)
            
            # Sleep until the next hour
            sleep_duration = 3600 - datetime.datetime.now().second
        else:
            sleep_duration = 60  # Sleep for 60 seconds
        
        time.sleep(sleep_duration)

if __name__ == "__main__":
    main()
