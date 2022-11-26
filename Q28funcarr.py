import array as arr
a=arr.array('i',[1,2,3,4,5])
a.append(8) #1function
a.insert(2,9) #2funtion
a.remove(4) #3function
a.extend([6,7,10])#4function
#for i in range(0,12):
 #   print(a[i])

a.reverse()
print(a)