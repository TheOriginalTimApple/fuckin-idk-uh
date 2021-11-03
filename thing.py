from os import write
import subprocess
import getpass
import pathlib

def get_spot_prefs_path():
	# Returns path to Spotify's prefs file
	return pathlib.Path.home().joinpath("AppData","Roaming","Spotify","prefs")

def get_stored_version_file_path():
	# Returns path to StoredVersion.dat file.
	return pathlib.Path.cwd().joinpath("StoredVersion.dat")

def get_spot_version():
	# obtains current spotify version
	f = open( get_spot_prefs_path() , 'r')	
	SpotifyVersion = f.readline() 
	f.close()	
	return SpotifyVersion

#def update_current_version():
	f = open('LastVersion.dat'['w'['-1']])
	f.write(get_spotify_version())
	f.close()
	# this is tagged because it will probably be replaced with a var

def store_spot_version():
	f = open('StoredVersion.dat', 'w')
	f.write(get_spot_version())
	f.close

def return_old_spot_version():
	f = open('StoredVersion.dat', 'r')
	OldSpotVersion = f.readline()
	f.close
	return OldSpotVersion

def reinstall():
	# executes the install .bat file (thing2)
	subprocess.call(str(pathlib.Path.cwd().joinpath("thing2.bat")))

def spot_version_compare():
	if get_spot_version() != return_old_spot_version():
		reinstall()
		print('Spotify Update Detected')
	else:
		print('Spotify Has Not Updated')

# gets windows username
username = getpass.getuser()

# opens prefs file in read-only
PrefsPath = get_spot_prefs_path()
with open(PrefsPath,"r") as f:
	PrefsFile = f.read

# opens stored version file in read+write
StoredVersionPath = get_stored_version_file_path()
with open(StoredVersionPath,"r+") as StoredVersionFile:

	#Do the stuff in here

	#Parse, etc.
	
	print(get_spot_version())

# get_spot_prefs_path()
# update_current_version()


spot_version_compare()

store_spot_version()
