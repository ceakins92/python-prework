#Question 1: hello_name____________________________________

def hello_name(username):
    """Display username greeting."""
    print("Hello " + username.title() + "!")
username = input("Please enter your Username: ")
hello_name(username)

#Question 2: first_odds____________________________________

def first_odds():
    """Prints odd number to 100, but returns nothing"""
    current_number = 0
    while current_number < 100:
        current_number += 1
        if current_number % 2 == 0:
            continue


#Question 3: max_num_in_list_______________________________

def max_num_in_list(a_list):
    """Returns the max number in a given list"""
    a_list.sort()
    print("The largest number in the list is: ", a_list[-1])

list = [256, 12, 88, 1243, 356, 7]
max_num_in_list(list)


#Question 4: is_leap_year__________________________________

def is_leap_year(a_year):  
    """Checks if the given year is leap year"""  
    if((year % 400 == 0) or  
        (year % 100 != 0) and  
        (year % 4 == 0)):   
        print("The year " + str(year) + " is a leap Year!");  

    else:  
        print ("Sorry! The year " + str(year) + " is not a leap Year.")  
 

print("Is it a Leap-Year? Find out!")
year = int(input("Enter a Year: "))  

is_leap_year(year)  

#Question 5: is_consecutive________________________________

#def is_consecutive(a_year):
#    """Doesn't work"""
#    list1 = [2, 3, 1, 4, 5]
#    sorted_list1 = sorted(list1)
#    range_list1 = list1(range(min(list1), max(list1)+1))
#
#    if sorted_list1 == range_list1:
#        print("The list has consecutive numbers!")
#    else:
#        print("The list has no consecutive numbers.")
#
#
#is_consecutive(list1)