import os
folder = r'C:\Users\bdebe_000\Documents\DeBear_Necessities\dabear57.github.io\assets\flowers'
files = os.listdir(folder)
for i in range(len(files)):
    #print(files[i])
    os.system("rename "+folder+"\\"+files[i]+" img"+str(i+1)+".jpg")
os.system("git add -A")
os.system("git commit -m newpics")
os.system("git push")
