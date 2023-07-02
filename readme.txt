Minute to Midnight is a dead man's switch set for 23:59 and it is comprised of 3 scripts.
client.py is a simple client script that is ran from the command line and is used to send data to listener.py. The port number and IP address of the listener are to be passed in as arguments along with the data(passphrase) to send.
listener.py is a simple server script that is ran from the command line and logs data sent to it from client.py into a local hidden file, .logg.txt. The port number to listen on needs to be passed in as an argument.
dms_v3.py is the switch part. It checks the contents of .logg.txt at a specified time, 23:59, and attempts to authenticate said contents against a passed in command line argument, a passphrase in this case.
If they match .logg.txt is cleared and the script resumes util 23:59, checks the file again, attempts authenticate and so on. If not, a specified file's contents will be cleared, and the script will exit.
dms_v3.py requires the absolute path of the target file to be cleared in case of a failed authentication attempt(unless said file is in the same directory as dms_v3.py) and the passphrase to authenticate against to be passed in as arguments.
All scripts contain a help option i.e., python script.py (-h / --help)
dms_v3.py and listener.py must be in the same directory.
