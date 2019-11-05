#-------------------------------------------------#
# Title: Mailroom
# Dev:   Breana K. Merriweather
# Date:  November 2, 2019
# ChangeLog: (Who, When, What)
#   BKM, 11/02/2019, Created Script

#-------------------------------------------------#

#Create a list of donors and a history of the amounts donated
#At least five donors, with 1 to 3 donations each
#Script should prompt user to choose from a menu of 3 actions:“Send a Thank You”, “Create a Report” or “quit”.



donors = [("Cruz", [500000.00, 20000.00, 30000.00]), ("Buffet", [600000.00, 30000.00]),("Gates", [500.00]), ("Pippy", [100.00, 200.00, 600.00]), ("Joe Biden", [600.00, 10000.00, 300.00])]


#Send thank you note def function
 #If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
 #If the user types list show them a list of the donor names and re-prompt.
 #If the user types a name not in the list, add that name to the data structure and use it.

 #If the user types a name in the list, use it

#Once a name has been selected, prompt for a donation amount.
 #Convert the amount into a number; it is OK at this point
     #for the program to crash if someone types a bogus amount.
 #Add that amount to the donation history of the selected user.

#Finally, use string formatting to compose an email thanking
 #the donor for their generous donation.
#Print the email to the terminal and return to the original prompt.

def thankU():
    global donors
    Check = 0
    check2 = 0
    print("You chose thank you")
    while Check == 0: 
        name = input(" Enter Full Name of Donor or list to see all donors: ")

        if name == "list":
            for a in donors:
                print(a[0])
                check2 = 1
                
        else:
            for a in donors:
                b = a[0]
                if b.__contains__(name):
                    print("Yippy!")
                    return
        if name != "list":
            addDonar()



   
                   
#create report
 #If the user (you) selected “Create a Report,” print a list of your donors,
 #sorted by total historical donation amount.
 #Include Donor Name, total donated, number of donations, and average donation amount as values in each row.
 #You do not need to print out all of each donor’s donations, just the summary info.
 #Using string formatting, format the output rows as nicely as possible.
 #The end result should be tabular (values in each column should align with those above and below).
 # After printing this report, return to the original prompt.

#At any point, the user should be able to quit their current task and return to the original prompt.
#From the original prompt, the user should be able to quit the script cleanly





def addDonar():
    global donors
    newName = input("Please add new donor to list: ")
    newDonation = int(input("Enter a donation amount: "))
    donors.append(((newName),[newDonation]))
    a = donors[-1]
    tup = a[0]#donor
    lst = a[-1] #money
    print(f'Dear {tup}, Thank you very much for your most generous donation of {lst} . Sincerely, PETA')


def report():
    global donors

    headers = ("{:<10}{:>25}{:>20}{:>20}".format("Donor", "Total Given $ ", "Num of Gifts", "Average Gift $"))
    print(headers)
    for x in donors:
        a=x[0]
        #print(a)
        b=x[1]
        #print(b)
        #monies_avg = 0
        qty_donations = len(b)
        #print(qty_donations)
        monies_total = sum(b)
        #print(monies_total)
        monies_avg = int(monies_total / qty_donations)
        #print(monies_avg)
        
       
        print(f"{a[:]:<10}{monies_total:>20}{qty_donations:>20}{monies_avg:>20}")
        
#report()


def main():
    userAction = input('Please choose one of the following values by entering the number associated: 1. Send Thank You Note,  2. Create a Report,  3. Exit the Program   '  )
    if userAction == "1":
         thankU()
    elif userAction == "2":
         report()
    elif userAction == "3":
        exit
#quit: If user selects anything other than 1 or 2 from above, exit the program

main()
