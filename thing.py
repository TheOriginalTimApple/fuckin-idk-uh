#establishes libraries req'd
import subprocess 
import getpass as gp

#establishes filepath req'd to obtain Spotify version info
path = "C:\\Users\\"+gp.getuser()+"\\AppData\\Roaming\\Spotify\\prefs\\prefs"
print(path)


# @TheOriginalTimApple, what's this do? >TheOriginalTimApple: Not sure, saw it in a webpage about PS integration with python
#def run(self, cmd):
   # completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
   # return completed