file = open("story.txt",encoding="utf8")
mlines = file.readlines()
count =0
for oline in mlines:
    if oline.startswith("t"):
        continue
    else:
        count =count+1
print(count)        