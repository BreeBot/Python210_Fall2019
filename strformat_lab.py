#-------------------------------------------------#
# Title: String Formatting Lab
# Dev:   Breana K. Merriweather
# Date:  October 27, 2019
# ChangeLog: (Who, When, What)
#   BKM, 10/27/2019, Created Script

#-------------------------------------------------#


#Task One
#Write a format string that will take the following four element tuple:


#1. The first element is used to generate a filename that can help with file
#sorting. The idea behind the “file_002” is that if you have a bunch of files
#that you want to name with numbers that can be sorted,
#you need to “pad” the numbers with zeros to get the right sort order


#2. The second element is a floating point number. You should display it
#with 2 decimal places shown.

#3. The third value is an integer, but could be any number.
#You should display it in scientific notation, with 2 decimal places shown.


#4. The fourth value is a float with a lot of digits – display it in
#scientific notation with 3 significant figures.


#'file_002 :   123.46, 1.00e+04, 1.23e+04'

tuple1 = ( 2, 123.4567, 10000, 12345.67)

print('file_{:0>3d}, {:.2f}, {:.2e} , {:.2e} '.format(*tuple1))


#Task Two
#Using your results from Task One, repeat the exercise,
#but this time using an alternate type of format string
#(hint: think about alternative ways to use .format() (keywords anyone?),
#and also consider f-strings if you’ve
#not used them already).

tuple2 = tuple1[0]
tuple3 = tuple1[1]
tuple4 = tuple1[2]
tuple5 = tuple1[3]

print(f"file_{tuple2:0>3d}, {tuple3:.2f}, {tuple4:.2e}, {tuple5:.2e}")


#Task Three

#Dynamically Building up format strings

#Rewrite:

#"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
#to take an arbitrary number of values.


t = (1,2,3)

def numbers(t):
    a = ""
    b = len(t[:])
    
    for _ in t:
        a += '{:d}, '
 

    return  "the " + str(len(t[:])) + 'numbers are' + a.format(*t)
  
print(numbers(t))

#Task Four

#Given a 5 element tuple:

#( 4, 30, 2017, 2, 27)

#use string formating to print:


tuple = ( 4, 30, 2017, 2, 27)

print('{3:0>2d} {4} {2} {0:0>2d} {1} '.format(*tuple))


#Task Five

#Here’s a task for you: Given the following four element list:

    #['oranges', 1.3, 'lemons', 1.1]

#Write an f-string that will display:

    #The weight of an orange is 1.3 and the weight of a lemon is 1.1

listElem = ['oranges', 1.3, 'lemons', 1.1]

print(f'The weight of an {listElem[0]} is {listElem[1]}and the weight of a {listElem[2]} is {listElem[3]}')

 
#Task Six

wines = ('Iron Horse', 'Opus One', 'Quilceda', 'Medoc', 'Napa', 'Paso Robles')
age = (5, 15, 10, 50, 3, 4)
price = (500.00, 1500.00, 200.00, 550.00, 300.00, 400.00)
print(f"{wines[0]:<15}{age[0]:>10}{price[0]:>10.2f}")
print(f"{wines[1]:<15}{age[1]:>10}{price[1]:>10.2f}")
print(f"{wines[2]:<15}{age[2]:>10}{price[2]:>10.2f}")
print(f"{wines[3]:<15}{age[3]:>10}{price[3]:>10.2f}")
print(f"{wines[4]:<15}{age[4]:>10}{price[4]:>10.2f}")
print(f"{wines[5]:<15}{age[5]:>10}{price[5]:>10.2f}")
