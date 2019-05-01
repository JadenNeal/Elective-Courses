import os


filepath = r"./cats/"
photo_list = os.listdir(filepath)
startNumber = 1000
os.chdir(filepath)

for src in photo_list:
    dst = "cat." + str(startNumber) + ".jpg"
    os.rename(src, dst)
    startNumber += 1
