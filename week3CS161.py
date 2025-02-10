# Part 1
#Asking for user input
name = input('What is your name?')
#Saying hello to user
print('Hello ' + name)
#Part 2
# x = input('Whats your age?')
# print(x + 5)
#This gives the error :TypeError: can only concatenate str (not "int") to str"
#This is because its defaulted as a string, so it needs to be converted into an integer.
x = input('Whats your age?')
#turning it into an integer
x = int(x)
#adding 5 years onto users age
print(x+5)
# Part 3
age = int(input('How old are you?'))
years_added = int(input('How many years would you like to add?'))
future_age = age + years_added
print('In ' + str(years_added) + ' you will be ' + str(future_age) + ' years old.')
# Part 4
#asking for user input
hours_worked = int(input('Enter the number of hours worked:'))
#asking for user input
hourly_wage = int(input('Enter your hourly wage, without the $:'))
#multi hours and wage
gross_pay_week = hourly_wage * hours_worked
print('Your gross pay this week is $' + str(gross_pay_week))
#finding daily by dividing gross pay by 7.
daily_gross = hours_worked * hourly_wage / 7
#finding annual by multi daily by 365
annual_gross = daily_gross * 365
#rounding the annual pay so output looks cleaner
rounded_annual = round(annual_gross, 2)
print('Your estimated annual gross pay will be $' + str(rounded_annual))
