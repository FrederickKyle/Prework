# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_USERNAME!")

hello_name('username'.upper())


# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for odd_numbers in range(0, 101):
        if odd_numbers % 2 != 0:
            print(odd_numbers)

print(first_odds())


# Question 3:
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    print(a_list)

my_list = [12, 22, 35, 68]
print("My max number in my list is: ")
max_num_in_list(73)
    

# Question 4:
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100,
# unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    
    print(True or False)
y = 'years_divisible'
for y in range(0):
    if y % 4 == 0:
        print(True)
    if y % 100 != 0:
        print(False)
    elif y % 400 == 0:
        print(True)

print(y)
is_leap_year(True)

# Question 5:
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.

def is_consecutive(a_list):
    unconsecutive_list = [5, 6, 7, 8, 9]

if 'unconsecutive_list' == is_consecutive:
    print(True)
elif 'unconsecutive_list' != is_consecutive:
    print(False)


is_consecutive(True)