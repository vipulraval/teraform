# Intro to Programming Using Python - Assignment #1
# Completed by:

# 1. Print out the following text:
# You've reached [your name].
# I'm not available right now, so leave a message and I'll call you back.
print ("""You've reached Vipul Raval.
I'm not available right now, so leave a message and I'll call you back.""")


# 2. Create five variables for your first name, last name, shoe size, height, and age.
# And then print them out on one line.
firstname="vipul"
lastname="Raval"
shoesize=9
height=5.9
age=37

print(firstname,lastname,shoesize,height,age)

# 3. If subtotal = 10.58 and tip = 0.22 (22%) then calculate the total bill amount
# in a variable named total and print it out.
subtotal=10.58
tip= 0.22
total=(subtotal)*(tip)
print("the total payment is", round ((subtotal + total),2))

# 4. Convert 158.8 into an integer.
# Convert 75 into a float.
# Convert "244.9" into a float and then an integer.
converti=158.58
print("converting to integer", int (converti))
convertf=75
print("converting to float",float (convertf))
convertif=244.9
print("converting to integer",int (convertif), "and converting to float",float (convertif))
# 5. Use \t and \n in a string and then print it out so that it matches (approximately) the following:
# -in the woods
#               which
#                   stutter
#                           and
#
#                               sing
words= "         \twhich  \n \
               \t stutter \n \
                           \tand \n \
                                \tsing"
print(words)
# 6. Put your first name and total from above into an f-string (f"...") so that it reads:
# Mattan, your total is $12.91
# (remember to round the total to the nearest cent)
print (f"vipul,your total is", round ((subtotal+total),2))
# 7. Use input() to ask a user for the city they live in, and then print it back to them.
city=input("which city do you live in?")
print(city)
# 8. Build a future value calculator by using input() to get values from the user.
# (Make sure you convert them into integers or floats before doing any math on them.)
# Print out the result.
# Hint: Future Value = Present Value x (1 + rate of return) ^ number of periods
presentvalue= float (input("please enter the present value?"))
retrun= float (input("please enter rate of retrun expected"))
period= float(input("please enter the number of periods?"))
retrun/=100
futurevalue= presentvalue*(1+ retrun)**period

print (f"your future value of your (presentvalue) is $", (round (futurevalue,2)))
