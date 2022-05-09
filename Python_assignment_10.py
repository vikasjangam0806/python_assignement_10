#Q-1 Python | Ways to remove a key from dictionary
# Python code to demonstrate
# removal of dict. pair 
# using del
  
# Initializing dictionary
test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
  
# Printing dictionary before removal
print ("The dictionary before performing remove is : " + str(test_dict))
  
# Using del to remove a dict
# removes Mani
del test_dict['Mani']
  
# Printing dictionary after removal
print ("The dictionary after remove is : " + str(test_dict))
  
# Using del to remove a dict
# raises exception
del test_dict['Manjeet']

#Q-2 Ways to sort list of dictionaries by values in Python – Using itemgetter

# Python code demonstrate the working of sorted()
# and itemgetter
  
# importing "operator" for implementing itemgetter
from operator import itemgetter
  
# Initializing list of dictionaries
lis = [{ "name" : "Nandini", "age" : 20}, 
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]
  
# using sorted and itemgetter to print list sorted by age 
print ("The list printed sorting by age: ")
print (sorted(lis, key=itemgetter('age')))
  
print ("\r")
  
# using sorted and itemgetter to print list sorted by both age and name
# notice that "Manjeet" now comes before "Nandini"
print  ("The list printed sorting by age and name: ")
print( sorted(lis, key=itemgetter('age', 'name')))
  
print ("\r")
  
# using sorted and itemgetter to print list sorted by age in descending order
print ("The list printed sorting by age in descending order: ")
print(sorted(lis, key=itemgetter('age'),reverse = True))


#Q-3 Ways to sort list of dictionaries by values in Python – Using lambda function
# Python code demonstrate the working of
# sorted() with lambda
 
# Initializing list of dictionaries
lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]
 
# using sorted and lambda to print list sorted
# by age
print ("The list printed sorting by age: ")
print (sorted(lis, key = lambda i: i['age']))
 
print ("\r")
 
# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# now comes before "Nandini"
print ("The list printed sorting by age and name: ")
print (sorted(lis, key = lambda i: (i['age'], i['name'])))
 
print ("\r")
 
# using sorted and lambda to print list sorted
# by age in descending order
print ("The list printed sorting by age in descending order: ")
print (sorted(lis, key = lambda i: i['age'],reverse=True))

#Q-4 Python | Merging two Dictionaries

# Python code to merge dict using update() method
def Merge(dict1, dict2):
    return(dict2.update(dict1))
     
# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
 
# This return None
print(Merge(dict1, dict2))
 
# changes made in dict2
print(dict2)

#Q-5 Python – Convert key-values list to flat dictionary

# Python3 code to demonstrate working of 
# Convert key-values list to flat dictionary
# Using dict() + zip()
from itertools import product
  
# initializing dictionary
test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}
  
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
  
# Convert key-values list to flat dictionary
# Using dict() + zip()
res = dict(zip(test_dict['month'], test_dict['name']))
  
# printing result 
print("Flattened dictionary : " + str(res)) 

#Q-6 Python – Insertion at the beginning in OrderedDict

# Python code to demonstrate
# insertion of items in beginning of ordered dict
from collections import OrderedDict
 
# initialising ordered_dict
iniordered_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])
 
# inserting items in starting of dict
iniordered_dict.update({'manjeet':'3'})
iniordered_dict.move_to_end('manjeet', last = False)
 
# print result
print ("Resultant Dictionary : "+str(iniordered_dict))

#Q-7 Python | Check order of character in string using OrderedDict( )

# Function to check if string follows order of 
# characters defined by a pattern 
from collections import OrderedDict 
  
def checkOrder(input, pattern): 
      
    # create empty OrderedDict 
    # output will be like {'a': None,'b': None, 'c': None} 
    dict = OrderedDict.fromkeys(input) 
  
    # traverse generated OrderedDict parallel with 
    # pattern string to check if order of characters 
    # are same or not 
    ptrlen = 0
    for key,value in dict.items(): 
        if (key == pattern[ptrlen]): 
            ptrlen = ptrlen + 1
          
        # check if we have traverse complete 
        # pattern string 
        if (ptrlen == (len(pattern))): 
            return 'true'
  
    # if we come out from for loop that means 
    # order was mismatched 
    return 'false'
  
# Driver program 
if __name__ == "__main__": 
    input = 'engineers rock'
    pattern = 'egr'
    print (checkOrder(input,pattern)) 

#Q-8 Dictionary and counter in Python to find winner of election

# Function to find winner of an election where votes
# are represented as candidate names
from collections import Counter
 
def winner(input):
 
    # convert list of candidates into dictionary
    # output will be likes candidates = {'A':2, 'B':4}
    votes = Counter(input)
     
    # create another dictionary and it's key will
    # be count of votes values will be name of
    # candidates
    dict = {}
 
    for value in votes.values():
 
        # initialize empty list to each key to
        # insert candidate names having same
        # number of votes
        dict[value] = []
 
    for (key,value) in votes.items():
        dict[value].append(key)
 
    # sort keys in descending order to get maximum
    # value of votes
    maxVote = sorted(dict.keys(),reverse=True)[0]
 
    # check if more than 1 candidates have same
    # number of votes. If yes, then sort the list
    # first and print first element
    if len(dict[maxVote])>1:
        print (sorted(dict[maxVote])[0])
    else:
        print (dict[maxVote][0])
 
# Driver program
if __name__ == "__main__":
    input =['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john']
    winner(input)

#Q-9 Python – Append Dictionary Keys and Values ( In order ) in dictionary
# Python3 code to demonstrate working of 
# Append Dictionary Keys and Values ( In order ) in dictionary
# Using values() + keys() + list()
  
# initializing dictionary
test_dict = {"Gfg" : 1, "is" :  3, "Best" : 2}
  
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
  
# + operator is used to perform adding keys and values
res = list(test_dict.keys()) + list(test_dict.values())
  
# printing result 
print("The ordered keys and values : " + str(res)) 

#Q-10 Python | Sort Python Dictionaries by Key or Value

# Function calling
def dictionairy():
 # Declare hash function     
 key_value ={}   
 
# Initializing value
 key_value[2] = 56      
 key_value[1] = 2
 key_value[5] = 12
 key_value[4] = 24
 key_value[6] = 18     
 key_value[3] = 323
 
 print ("Task 1:-\n")
 print ("Keys are")
  
 # iterkeys() returns an iterator over the
 # dictionary’s keys.
 for i in sorted (key_value.keys()) :
     print(i, end = " ")
 
def main():
    # function calling
    dictionairy()            
     
# Main function calling
if __name__=="__main__":     
    main()