fh = open("story.txt","r")
line = fh.readlines()
for each in line:
    if each.find("the") != -1:
     print(each)    
          