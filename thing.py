#import modules
import subprocess
import getpass

# obtains current spotify version info
def get_spot_prefs_path(username):
	return "C:\\Users\\"+username+"\\AppData\\Roaming\\Spotify\\prefs"

# obtains previous version info
def get_last_version_file_path(username):
	return "C:\\Users\\"+username+"\\AppData\\Roaming\\AutoSpotBlock\\LastVersion.dat"


# executes the install .bat file (thing2)
def reinstall():
	subprocess.call([r'C:\Users\"+username+"\Documents\GitHub\fuckin-idk-uh\thing2.bat'])

# gets windows username
username = getpass.getuser()

# opens prefs file in read-only
PrefsPath = get_spot_prefs_path(username)
with open(PrefsPath,"r") as f:
	PrefsFile = f.read
print(f.closed) # Checks to make sure the file's closed and I'm not doing a dumb-dumb. Delete later.

# opens last version file in read+write
LastVersionPath = get_last_version_file_path(username)
with open(LastVersionPath,"r+") as LastVersionFile:
	#Do the stuff in here
	#Parse, etc.
	print("this is a placeholder so vs code won't yell at me. (-:")
print(LastVersionFile.closed)