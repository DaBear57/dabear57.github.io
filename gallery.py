import os
files = os.listdir(".\\assets\\flowers")
for i in range(len(files)):
    #print(files[i])
    os.system("rename .\\assets\\flowers\\"+files[i]+" img"+str(i+1)+".jpg")
os.system("git add -A")
os.system("git commit -m newpics")
os.system("git push")
