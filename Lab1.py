#progrm 2-1 (output.py)
print ('Kate Austen')
print ('123 full circle drive')
print ('ashville, NC 28899')
#progrm 2-2 (double_quotes.py)
print ("kate Austen")
print ("123 Full Circle Drive")
print ("Ashville, NC 28899")
#progrm 2-3 (apostrophe.py)
print ("Don't fear!")
print ("I'm here!")
#progrm 2-4 (display_quoye.py)
print ('Your assignment is to read "Hamlet" by tomorrow.')
#Program 2-5 (comment1.py)
# This program displays a peron's
# name and address
print ('kate austen')
print ('123 Full Circle Drive')
print ('Ashville, NC 28899')
#Program 2-6 (comment2.py)
print ('kate austen') #Display the name.
print ('123 Full Circle Drive') #Display the address
print ('Ashville, NC 28899') #Display the city, state, and ZIP.
#Program 2-7 (variable_demo.py)
# This program demostrates a variable
room = 503
print ('I am staying in room number')
print (room)
#Program 2-8 (variable_demo2.py)
# Create two variables: top_speed and distance.
top_speed = 160
distance = 300

# Display the values referenced by the variables.
print ('the top speed is')
print (top_speed)
print ('The distance traveled is')
print (distance)
#Program 2-9 (variable_demo3.py)
# This program demonstrates a variable.
room = 503
print ('I am staying in room number', room)
#Program 2-10 (variable_demo4.py)
# this program demonstrates variable reassignment
#Assign a value to the dollars variable
dollars = 2.75
print ('I have', dollars, 'in my account.')

#reassign dollars so it references
# a different values.
dollars = 99.95
print ('But now I have', dollars, 'in my account!')
#program 2-11 (string_variable.py)
#Create variables to refrence two strings
first_name = 'kathryn'
last_name = 'marino'
# Display the values referenced by the variables.
# Program 2-12
print (first_name, last_name)
# Get the user's first name.
first_name = input('Enter your first name:')

# Get the user's last name.
Last_name = input('Enter your Last name:')

# Print a greeting to the user.
print ('Hello' , first_name, Last_name)
# Program 2-13
name = input('what is your name?')
age = int(input('what is your age?'))
income = float(input('what is your income? '))

print ('Here is the data you entered:')
print ('Name:', name)
print ('Age:', age)
print ('Income:', income)
# Program 2-14
salary = 2500.0
bonus = 1200.0
pay = salary + bonus
print ('your pay is', pay)
# Program 2-15
#original_price = float(input("Enter the item's original price: "))
#discount = original_price * 0.2
#sale_price = original_price - discount
#print('The sale price is', sale_price
#Program 2-16
test1 = float(input('Enter the first test score: '))
test2 = float(input('Enter the second test score: '))
test3 = float(input('Enter the third test score: '))
average = (test1 + test2 + test3) / 3.0
print ('The average score is', average)
# Program 2-17
total_seconds = float(input('Enter a number of seconds: '))
hours = total_seconds // 3600
minutes = (total_seconds // 60) % 60
seconds = total_seconds % 60
print ('Here is the time in hours, minutes, and seconds:')
print ('Hours:', hours)
print ('Minutes:', minutes)
print ('Seconds:', seconds)
# Program 2-18
future_value = float(input('Enter the desired future value: '))
rate = float(input('Enter the annual interest rate: '))
years = int(input('Enter the number of years the money will grow: '))
present_value = future_value / (1.0 + rate)**years
print ('You will need to deposit this amount:', present_value)
# program 2-19
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print ('The monthly payment is', monthly_payment)
# program 2-20
amount_due = 5000.0
monthly_payment = amount_due / 12
print ('The monthly payment is' , \
       format(monthly_payment, '.2f'))
# program 2-21
#monthly_pay = 5000.00
#annual_pay = monthly_pay * 12
#print ('your annual pay is $', \
#       format (annual_pay, ',.2f'), \
#       sep='')
# program 2-22
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999
print (format(num1, '7.2f'))
print (format(num2, '7.2f'))
print (format(num3, '7.2f'))
print (format(num4, '7.2f'))
print (format(num5, '7.2f'))
print (format(num6, '7.2f'))



       










