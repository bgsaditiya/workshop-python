import os
import shutil
os.getcwd()      # Return the current working directory

os.chdir('/server/accesslogs')   # Change current working directory
os.system('mkdir today')   # Run the command mkdir in the system shell

dir(os)

help(os)

shutil.copyfile('data.db', 'archive.db')

shutil.move('/build/executables', 'installdir')