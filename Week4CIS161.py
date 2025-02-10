"Part1"
def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3
'''add num1, num2, and num3 together then divide the total by 3'''
print(average(7, 5, 9))
print(average(6, 6, 7))
"part2"
#print(average(7,5,3))
#print(average(6,6,7))
#def average(num1, num2, num3):
#   return (num1 + num2 + num3)/3
'''add num1, num2, and num3 together then divide the total by 3'''
#This script does not run and this is because code is read up to down and the function "average" is being called before the function is defined.
"part3"
#def average(num1, num2, num3):
    #return (num1 + num2 + num3) / 3
'''add num1, num2, and num3 together then divide the total by 3'''
#print(average(7, 5, 9))
#print(average(6, 6, 7))
#print(num1)
#this script does not run because num1 hasn't been defined so it cant print it.
"Part4"
def dog_human_age(dogs_age):
    return 24 + (dogs_age - 2)*4
"""Get the dogs age and subract it by 2 then multiply it by 4, finish by adding 24"""
print('5 dogs years is equivalent to', dog_human_age(5), 'human years.')
print('11 dogs years is equivalent to', dog_human_age(11), 'human years.')
"Part5"
def value_of_car(car, purchase_price, years):
#If statement was what I thought was the easiest to approach this but please let me know if there was an easier option
    if car == "German":
        rate = 0.05
        value = purchase_price * (1-rate) ** years
        return print("The value of a German car will be $" + str(round(value,2)) +" after " + str(years) + " years.")
    elif car == "Japanese":
        rate = 0.07
        value = purchase_price * (1-rate) ** years
        return print("The value of a Japanese car will be $" + str(round(value,2)) +" after " + str(years) + " years.")
    elif car == "Italian":
        rate = 0.05
        value = purchase_price * (1+rate) ** years
        return print("The value of a Italian car will be $" + str(round(value,2)) +" after " + str(years) + " years.")
#I did all the purchase prices and years the same so that you could see the difference
value_of_car("German", 100000, 5)
value_of_car("Japanese", 100000, 5)
value_of_car("Italian", 100000, 5)
"Part6"
def human_years(name, age_now):
    new_age = 24 + (age_now - 2) * 4
    print(f"Your " + str(name) + " is " + str(new_age) + " years old.")
"""Get the dogs age and subract it by 2 then multiply it by 4, finish by adding 24"""
print("Dog’s Age calculator:")
#user input on dogs name
name = input("What is your dogs name? ")
#user input on dogs age
age_now = float(input(f"How old is {name}?"))
#calling the function
human_years(name, age_now)
"Part7"
def price_of_cone(amount_of_scoops):
    total = amount_of_scoops * 1.15 + 2.25
    return print("A " + str(amount_of_scoops) + "-scoop cone will cost $" + str(total) + ".")
print("Ice cream cone price calculator:")
#asking user how many scoops they would like
amount_of_scoops = float(input("How many scoops would you like? "))
#calling the function so it returns the prices of however many scoops
price_of_cone(amount_of_scoops)