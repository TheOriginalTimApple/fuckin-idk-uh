#import modules
from os import write
import subprocess
import getpass
import pathlib

# @TheOriginalTimApple, what's this do? Also pick a better name than "run"
def run(self, cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

# Returns path to Spotify's prefs file
def get_spot_prefs_path():
	return pathlib.Path.home().joinpath("AppData","Roaming","Spotify","prefs")
	
# Returns path to LastVersion.dat file.
def get_last_version_file_path():
	return pathlib.Path.cwd().joinpath("LastVersion.dat")

# executes the install .bat file (thing2)
def reinstall():
	subprocess.call(str(pathlib.Path.cwd().joinpath("thing2.bat")))

def update_current_version():
	f = open('LastVersion.dat'['w'['-1']])
	#f.write(SpotifyVersion)
	f.close()

# Returns location of second quote
def get_second_quote_index(stringToScan):
	return int(stringToScan.find("\n"))-1 

# Returns location of first quote
def get_first_quote_index(stringToScan):
	return int(stringToScan.find('"'))

# gets windows username
username = getpass.getuser()

# opens prefs file in read-only
PrefsPath = get_spot_prefs_path()
with open(PrefsPath,"r") as f:
	PrefsFile = f.read

# opens last version file in read+write
LastVersionPath = get_last_version_file_path()
with open(LastVersionPath,"r+") as LastVersionFile:
	print("this is a placeholder so vs code won't yell at me. (-:")
