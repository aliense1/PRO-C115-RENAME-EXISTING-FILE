import os

source = "C:/home/ryanking/Desktop/Animation For Beginners/Frames/New Folder/Main.txt"

dest = "C:/home/ryanking/Desktop/Animation For Beginners/Frames/New Folder/newfile.txt"

os.rename(source,dest)

if source != dest :
    print("Renamed Succesfully")