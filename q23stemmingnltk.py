# importing the required modules  
from nltk.stem import PorterStemmer  
from nltk.tokenize import word_tokenize  
  
# creating an object of the PorterStemmer class  
pStemmer = PorterStemmer()  
  
# selecting some words to be stemmed  
list_of_words = ["consult", "consultant", "consulting", "consultantative", "consultants", "consulting"]  
  
for words in list_of_words:  
    print(words + ": " + pStemmer.stem(words))  