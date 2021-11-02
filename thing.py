#import modules
import subprocess
import getpass

# @TheOriginalTimApple, what's this do? Also pick a better name than "run"
def run(self, cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

def get_spot_prefs_path(username):
	return "C:\\Users\\"+username+"\\AppData\\Roaming\\Spotify\\prefs\\prefs"

def get_last_version_file_path(username):
	return "C:\\Users\\"+username+"\\AppData\\Roaming\\AutoSpotBlock\\LastVersion.dat"
	# might have to create that directory before making the file or something
    # >the directory may need to contain the drive name, not just "C:"
	# >>No

# gets windows username
username = getpass.getuser()

# opens prefs file in read-only
PrefsPath = get_spot_prefs_path(username)
with open(PrefsPath,"r") as f:
	PrefsFile = f.read
print(f.closed) #Checks to make sure the file's closed and I'm not doing a dumb-dumb. Delete later.

# opens last version file in read+write
LastVersionPath = get_last_version_file_path(username)
with open(LastVersionPath,"r+") as LastVersionFile:
	#Do the stuff in here
	#Parse, etc.
	print("this is a placeholder so vs code won't yell at me. (-:")
print(LastVersionFile.closed)