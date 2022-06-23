

    #I originally wrote this for loop but it is not needed in a dictionary.  This program takes a number
    #inputed - between 0-9 and returns it as the word.  The get method for a dictionary you give two parameters
    #what you are looking to get and then if the number you want is not listed.  It looks for the key and then
    #returns the value.  So, if I put 0 it looks for that key and returns its value which is zero.
def wordswitch(number):
    words = {0:"Zero", 1:"One", 2:"Two", 3:"Three",4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight",
    9:"Nine"}
    
    
    
    return words.get(number, "This number is not in the list!")
    

answer = wordswitch(3)
print(answer)