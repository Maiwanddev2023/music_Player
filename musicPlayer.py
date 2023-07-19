"""
Program: musicPlayer.py
Author hamza 7/5/2023

Simple command-line based music player app that can play a standard .mp3 audio file.
***  MUST INSTALL the pygame package before running this APP!!!!!!!
At command prompt run: pip install pygame --pre
"""
# Import statement for the pygame mixer module
from pygame import mixer

# Initialize the mixer module
mixer.init()

# Display a menu for the user interface
print("\nWelcome to the Python Music Player!")
print("Press 1 to select a song file.")
print("press 2 to play the chosen song.")
print("press 3 to pause an active song.")
print("press 4 to unpause the song.")
print("Press any other key to exit the program.")

while True:
	menuChoice = input("Enter a menu option >> ")

	# Decision making that triggers each feature.
	if menuChoice == "1":
		songFile = input("Please enter the song's filename >> ")
		mixer.music.load(songFile)
	elif menuChoice == "2":
		mixer.music.play()
	elif menuChoice == "3":
		mixer.music.pause()
	elif menuChoice == "4":
		mixer.music.unpause()
	else:
		input("Thank you for using music player. Press ENTER to close.")
		break

