#import modules
import subprocess
import getpass
import pathlib

# @TheOriginalTimApple, what's this do? Also pick a better name than "run"
def run(self, cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

# Returns path to Spotify's prefs file
def get_spot_prefs_path():
	return pathlib.Path.home().joinpath("AppData","Roaming","Spotify","prefs","prefs")

# Returns path to LastVersion.dat file.
def get_last_version_file_path():
	return pathlib.Path.cwd().joinpath("LastVersion.dat")

# opens prefs file in read-only
PrefsPath = get_spot_prefs_path())
with open(PrefsPath,"r") as f:
	PrefsFile = f.read
print(f.closed) #Checks to make sure the file's closed and I'm not doing a dumb-dumb. Delete later.

# opens last version file in read+write
LastVersionPath = get_last_version_file_path()
with open(LastVersionPath,"r+") as LastVersionFile:
	#Do the stuff in here
	#Parse, etc.
	print("this is a placeholder so vs code won't yell at me. (-:")
print(LastVersionFile.closed)