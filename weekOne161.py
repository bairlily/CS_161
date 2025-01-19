# this is my week 1 project for 161!
print("Welcome to my program!")
# entering personal pet info
pet_type = "dog"
pet_name = "Duke"
pet_pronoun = "his"
# f-string to display my pets info
print(f"I have a {pet_type} and {pet_pronoun} name is {pet_name}. ")

# this is another f-string but with the users input being used
print("Please enter you name")
user_name = input()
print("How old are you?")
age = int(input())
# adding 10 years onto the user age
new_age = age + 10
print("What is your yearly savings?")
yearly_savings = int(input())
# multiplying users yearly savings
estimated_savings = yearly_savings * 5
# dividing the users yearly savings
monthly_savings = yearly_savings / 12
print(f"Hello {user_name}! You are currently {age} years old.")
print(f"In 10 years, you will be {new_age} years old.")
print(f"If you save ${yearly_savings} each year, in five years you will have saved ${estimated_savings}.")
print(f"Your average monthly savings is ${monthly_savings}.")

# this is an f-string to display how many second are in a month
month = "January"
days = 31
hours = 24
mins = 60
secs = 60
# multiplying all the varables
seconds_total = days * hours * mins * secs
print(f"The number of seconds in {month} is {seconds_total}.")

#this is another f-string but this time with eggs
print("Enter the number of eggs")
# users input
eggs = int(input())
dozen_eggs = 12
#dividing users input by amount of eggs that can fit in a carton
egg_carton = eggs // dozen_eggs
# finding what cant fit in the carton
leftover_eggs = eggs % egg_carton
#telling the user how many cartons and what is left over
print(f"This makes {egg_carton} dozen eggs with {leftover_eggs} leftover. ")