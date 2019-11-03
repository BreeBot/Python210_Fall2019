#-------------------------------------------------#
# Title: List Lab
# Dev:   Breana K. Merriweather
# Date:  October 27, 2019
# ChangeLog: (Who, When, What)
#   BKM, 10/27/2019, Created Script

#-------------------------------------------------#

#-- Objective --#
#Learn the basic ins and outs of Python lists.

# Series 1
#Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches” and print it.
fruitList = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruitList)

#Ask the user for another fruit and add it to the end of the list and print it.
newFruit = input('Enter a Fruit: ')
fruitList.append(newFruit)
print(fruitList)

#Ask the user for a number and display the number
#back to the user and the fruit corresponding to that number (on a 1-is-first basis).
#Remember that Python uses zero-based indexing, so you will need to correct.

numFruit = int(input('Enter a Number: '))
print(numFruit)
print(fruitList[numFruit -1])

#Add another fruit to the beginning of the list using “+” and display the list.

newFruit2 = input('Enter a new Fruit: ')
print(newFruit2)
print(fruitList)
fruitList2 = [newFruit2] + fruitList
print(fruitList2)

#Add another fruit to the beginning of the list using insert() and display the list.
newFruit3 = input('Enter a new Fruit: ')
fruitList.insert(0, newFruit3)
print(fruitList)

fruitList2 = fruitList
#Display all the fruits that begin with “P”, using a for loop.
newList = []
for i in fruitList:
    if i.startswith('P'):
        newList.append(i)

#Series 2

#Using the list created in series 1 above:

    #Display the list.
print(fruitList2)
    #Remove the last fruit from the list.
del fruitList2[-1]
    #Display the list.
print(fruitList2)
    #Ask the user for a fruit to delete, find it and delete it.
newFruit4 = input('Enter fruit from list above to delete: ')
fruitList2.remove(newFruit4)       
print(fruitList2)



#Series 3

#Again, using the list from series 1:

    #for each fruit in the list (making the fruit all lowercase).
ogList = ["Apples", "Pears", "Oranges", "Peaches"]
print(ogList)
ogList = [item.lower() for item in ogList]
print(ogList)

# Ask the user for input displaying a line like “Do you like apples?”
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”,prompt the user to
# answer with one of those two values (a while loop is good here)

keeper = []
tosser = []
number=len(ogList[:])
for i in range(number):
    fruitA = str(input(('Do you like  ' + ogList[i] + '? '))).upper().strip()
    print(fruitA)
    if fruitA != 'Y' and fruitA !='N':
        while fruitA != 'Y' and fruitA != 'N':
            fruitA = str(input("DO YOU LIKE THE FRUIT Y OR N!")).upper().strip()
            if fruitA == 'Y':
                print('excellent')
            if fruitA == 'N':
                print('AWWWW')
    if fruitA == 'Y':
        print('excellent')
        keeper.append(ogList[i])
    else:
        tosser.append(ogList[i])
    print(keeper[:])
    print(tosser[:])
ogList=keeper


 
#Series 4

#Once more, using the list from series 1:
ogList2 = ["Apples", "Pears", "Oranges", "Peaches"]

    #Make a new list with the contents of the original, but with all the
        #letters in each item reversed.

reverse_ogList2 = [x[::-1] for x in ogList2][::-1]
print(reverse_ogList2)

    #Delete the last item of the original list. Display the original list and the copy.
print(ogList2)
ogList2.pop()
print(ogList2)


















































































