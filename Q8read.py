line = open("poem.txt",encoding="utf8")
no = line.readlines()
count=0
for lines in no:
 
 count = count+1
 print(lines)
print(count) 