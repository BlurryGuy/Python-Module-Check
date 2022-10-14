import os
try:
   import keyboard
   print("keyboard module is installed")
   input()
except:
   print("keyboard module is not installed")
   input("Press enter to download keyboard module")
   os.system("pip install keyboard")
