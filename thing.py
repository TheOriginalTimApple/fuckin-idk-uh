from os import write
import subprocess
import getpass
import pathlib



# @TheOriginalTimApple, what's this do? Also pick a better name than "run"
#def run(self, cmd):
    #completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    #eturn completed

# Returns path to Spotify's prefs file

def get_spot_prefs_path():
	# Returns path to Spotify's prefs file
	return pathlib.Path.home().joinpath("AppData","Roaming","Spotify","prefs")
def get_last_version_file_path():
	# Returns path to LastVersion.dat file.
	return pathlib.Path.cwd().joinpath("LastVersion.dat")

def get_spotify_version():
	f = open('prefs', 'r')	
	SpotifyVersionCurrent = f.readline()

# writes current spotify version to LastVersion.dat
def update_current_version():
	f = open('LastVersion.dat','w','-1')
	f.write(str(SpotifyVersionCurrent))
	f.close()
def get_second_quote_index(stringToScan):
	# Returns location of second quote
	return int(stringToScan.find("\n"))-1 
def get_first_quote_index(stringToScan):
	# Returns location of first quote
	return int(stringToScan.find('"'))

# executes the install .bat file (thing2)
def reinstall():
	subprocess.call(str(pathlib.Path.cwd().joinpath("thing2.bat")))

# gets windows username
username = getpass.getuser()

# opens prefs file in read-only
PrefsPath = get_spot_prefs_path()
with open(PrefsPath,"r") as f:
	PrefsFile = f.read

# opens last version file in read+write
LastVersionPath = get_last_version_file_path()
with open(LastVersionPath,"r+") as LastVersionFile:
	#Do the stuff in here

	#Parse, etc.



#reinstall();

	print("this is a placeholder so vs code won't yell at me. (-:")


update_current_version()
print(SpotifyVersionCurrent)
	print("this is a placeholder so vs code won't yell at me. (-:")
