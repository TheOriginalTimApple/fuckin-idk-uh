#establishes libraries req'd
import subprocess as sp
import getpass as gp

# @TheOriginalTimApple, what's this do? Also pick a better name than "run"
def run(self, cmd):
    completed = sp.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

def get_spot_prefs_path(username):
	return "C:\\Users\\"+username+"\\AppData\\Roaming\\Spotify\\prefs\\prefs"

def get_last_version_file_path(username):
	return "C:\\Users\\"+username+"\\AppData\\Roaming\\AutoSpotBlock\\LastVersion.dat"
	# might have to create that directory before making the file or something
    # >the directory may need to contain the drive name, not just "C:"

# gets windows username
username = gp.getuser()

# opens prefs file in read-only
PrefsPath = get_spot_prefs_path(username)
PrefsFile = open(PrefsPath,"r")

# opens last version file in read+write
LastVersionPath = get_last_version_file_path(username)
LastVersionFile = open(LastVersionPath,"r+")

