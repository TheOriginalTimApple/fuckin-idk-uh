#import modules
from os import write
import subprocess
import getpass
import pathlib

def run(self, cmd):
	# @TheOriginalTimApple, what's this do? Also pick a better name than "run"
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed
def get_spot_prefs_path():
	# Returns path to Spotify's prefs file
	return pathlib.Path.home().joinpath("AppData","Roaming","Spotify","prefs")
def get_last_version_file_path():
	# Returns path to LastVersion.dat file.
	return pathlib.Path.cwd().joinpath("LastVersion.dat")
def reinstall():
	# executes the install .bat file (thing2)
	subprocess.call(str(pathlib.Path.cwd().joinpath("thing2.bat")))
def update_current_version():
	f = open('LastVersion.dat'['w'['-1']])
	#f.write(SpotifyVersion)
	f.close()
def get_second_quote_index(stringToScan):
	# Returns location of second quote
	return int(stringToScan.find("\n"))-1 
def get_first_quote_index(stringToScan):
	# Returns location of first quote
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
