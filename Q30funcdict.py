#1function
dict1={1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
print("dictionary is : ",dict1)
dict1.clear()
print("after clearing dictioinary will be : ",dict1)

#2functuion
dict2={1:'I', 2:'II', 3:'III', 4:'IV', 5:'V'}
popped=dict2.pop(5)
print("the poped element is:- ",popped)
print("the updated dictionary is:- ",dict2)

#3function
keys = {'Mumbai','Bangalore','Chicago','New York'}
value = 'city'
dictionary = dict.fromkeys(keys, value)
print(dictionary)

#4function
romanNums = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5 }
newRomanNums = romanNums.copy()
print("Original dictionary: ",romanNums)
print("Copied dictionary: ",newRomanNums)

#5funtion
romanNums = {'I':1,'III':3,'V':5}
print("Dictionary: ",romanNums)

evenRomanNums = {'II':2,'IV':4}
romanNums.update(evenRomanNums)
print("Updated Dictionary: ",romanNums)