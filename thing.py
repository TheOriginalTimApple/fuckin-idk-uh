from os import write
import subprocess
import getpass
import pathlib

def get_spot_prefs_path():
	# Returns path to Spotify's prefs file
	return pathlib.Path.home().joinpath("AppData","Roaming","Spotify","prefs")
def get_last_version_file_path():
	# Returns path to LastVersion.dat file.
	return pathlib.Path.cwd().joinpath("LastVersion.dat")
def get_spotify_version():
	f = open('prefs', 'r')	
	SpotifyVersionCurrent = f.readline()
def update_current_version():
	# writes current spotify version to LastVersion.dat
	f = open('LastVersion.dat','w','-1')
	f.write(str(SpotifyVersionCurrent))
	f.close()
def get_second_quote_index(stringToScan):
	# Returns location of second quote
	return int(stringToScan.find("\n"))-1 
def get_first_quote_index(stringToScan):
	# Returns location of first quote
	return int(stringToScan.find('"'))
def reinstall():
	# executes the install .bat file (thing2)
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
	print("this is a placeholder so vs code won't yell at me. (-:")


update_current_version()
print(SpotifyVersionCurrent)
