import time, socket, math
TCP_IP = '127.0.0.1'
TCP_PORT = 8080
volDown = "voldown 1 \n" #Lower volume command
vlcStop = "stop \n" # Stop playback command
vlcExit = "quit \n" # Exit VLC command

print("\n         ---- VLC Sleep Timer ----\n")
print("Fades out and closses VLC after a defined time.\n")
print("                   by Cyberstorm Systems 9/3/17\n\n")

#Setup the timer
sleepTime = 0
while (sleepTime > 720 or sleepTime <= 0):
	sleepTime = int(input("Enter number of minutes [1 to 720]: "))
	if (sleepTime > 720 or sleepTime <= 0):
		print("I'm sorry, that's outside the acceptable range.")

print("\n")

# Run the timer
sleepTime *= 60
while sleepTime > 0:
	minutes = math.floor(sleepTime/60)
	seconds = sleepTime%60
	print("        --- Waiting for ({0}:{1:02d}) --- ".format(minutes,seconds), end="\r")
	time.sleep(1)
	sleepTime -=1

# Time is up!
print("Goodnight! Fading out.")

#Connect to VLC socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

#How many times to turn down
turnDown = 7
while turnDown > 0:
	s.send(volDown.encode())
	time.sleep(3)
	turnDown-=1
	
#Done turning down. Stop playback.
print("Faded out, stopping playback in a 3 seconds")
time.sleep(3)
s.send(vlcStop.encode())

#Quit VLC
print("Done, now exiting VLC")
time.sleep(1)
s.send(vlcExit.encode())
time.sleep(1)
s.close()
