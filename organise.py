import os
import shutil
source = r"C:\Users\25geo02s\Downloads"

listOfFiles = os.listdir(source)
## print(listOfFiles)

for fileName in listOfFiles:
    root, extension = os.path.splitext(fileName) 
    if extension == "":
        continue
    if extension in [".gif", ".png", ".jpg", ".jpeg",".jfif"]:
        path1 = source + "/" + fileName
        path2 = r"C:\Users\25geo02s\OneDrive - Central Coast Grammar School\Pictures" + "/" + "images"
        path3 = r"C:\Users\25geo02s\OneDrive - Central Coast Grammar School\Pictures" + "/" + "images" + "/" + fileName
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
  #  print(root)
   # print(extension)


