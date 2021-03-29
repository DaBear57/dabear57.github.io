import os
files = os.listdir(".\\assets\\flowers")
for i in range(len(files)):
    os.system("rename .\\assets\\flowers\\"+flowers[i]+" img"+str(i+1)+".jpg")
os.system("git add -A")
os.system("git commit -m 'uploaded gallery pictures")
os.system("git push")