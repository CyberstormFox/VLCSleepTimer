Ever wish VLC had a sleep timer feature?
I've written this Python script to quickly and easily have VLC fade out and close after a user defined time.
Only uses  default module,s and just requires you to open a remote control socket in VLC, usually by using the command line
vlc.exe --extraintf rc --rc-quiet --rc-host 0.0.0.0:8080
This can be put into a shortcut for ease of use in Windows.
