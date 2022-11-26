fh = open("story.txt",encoding="utf8")
fh2 = open("cstory.txt","w")
line = fh.readlines()
for each in line:
    fh2.write(each)
    