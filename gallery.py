import os
folder = r'C:\Users\bdebe_000\Documents\DeBear_Necessities\dabear57.github.io\assets\flowers'
os.chdir(folder)
files = os.listdir()
for i in range(len(files)):
    #print(files[i])
    os.system("rename "+files[i]+" img"+str(i+1)+".jpg")
os.system("git add -A")
os.system("git commit -m newpics")
os.system("git push")
