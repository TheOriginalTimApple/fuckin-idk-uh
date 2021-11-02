import subprocess 
import getpass

# @TheOriginalTimApple, what's this do?
def run(self, cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

path = "C:\\Users\\"+getpass.getuser()+"\\AppData\\Roaming\\Spotify\\prefs\\prefs"
print(path)