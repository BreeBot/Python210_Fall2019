#-------------------------------------------------#
# Title: Slicing Lab
# Dev:   Breana K. Merriweather
# Date:  October 27, 2019
# ChangeLog: (Who, When, What)
#   BKM, 10/27/2019, Created Script

#-------------------------------------------------#

#-- Objective --#
#Write some functions that take a sequence as an argument, and return a copy of that sequence:
    #with the first and last items exchanged.
    #with every other item removed.
    #with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
    #with the elements reversed (just with slicing).
    #with the last third, then first third, then the middle third in the new order.


# function with the first and last items exchanged.
#def exchange_first_last(seq):
    #return a_new_sequence

a_string = "this is a string"
newString = a_string[-1] + a_string[1:15] + a_string[0]
print(newString)





#function with every other item removed.

#def every_other(seq):
    #return a_new_sequence

a_string2 = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

# optional second clause that we can add that
#allows us to set how the list's index will increment between the indexes that we've set

newString2 = a_string[::2]
print(newString2)


#function
#with the first 4 and the last 4 items removed, and then
#every other item in the remaining sequence.


#def first_last_four(seq):
#return a_new_sequence

newString3 = a_string[4:-4:2]
print(newString3)

#with the elements reversed (just with slicing).

#def first_last_four(seq):
#return a_new_sequence

newString4 = a_string[::-1]
print(newString4)


#with the last third, then first third, then the middle third in the new order.

newString5 = a_string[0:-3]
print(newString5)

a_string6 = "this is a string"
newString6 = a_string6[13:] 
print(newString6)

print(newString6 + newString5)




