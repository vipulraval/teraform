# Intro to Programming Using Python - Assignment #3
# Completed by: Uma Radhakrishnan

# Be sure to read the instructions carefully!

# 1. Create three dictionaries, each one will contain information about a particular student: Steve, Alice and Tyler
#   a. Assign each dictionary to a variable – eg. steve, alice and tyler
#   b. Create the following keys: name, homework, quizzes, and tests
#   c. Set the value of the name key to the name of the student – e.g. Steve's name should be "Steve"
#   d. Set the other keys – e.g. homework, quizzes, and tests – to empty lists (we'll fill them in later)
#   e. Print these empty dictionaries

Steve = {'name': 'Steve', 'homework': [ ] , 'quizzes':[ ] , 'tests': [ ]}
Alice = {'name': 'Alice', 'homework':[ ] , 'quizzes':[ ] , 'tests': [ ]}
Tyler = {'name': 'Tyler', 'homework':[ ] , 'quizzes':[ ] , 'tests':[ ] }
g = ["A","B","C","D","F"]
print(g[0])
print(Steve)
print(Alice)
print(Tyler)

# 2. Now fill in the dictionaries above with the following scores and print the dictionaries:
# Steve
#   Homework: 90, 97, 75, 92
#   Quizzes: 88, 40, 94
#   Tests: 75, 90
# Alice
#   Homework: 100, 92, 98, 100
#   Quizzes: 82, 83, 91
#   Tests: 89, 97
# Tyler
#   Homework: 0, 87, 75, 22
#   Quizzes: 0, 75, 78
#   Tests: 100, 100

Steve = {'name': 'Steve', 'homework': [90,97,75,92 ] , 'quizzes':[88,40,94 ] , 'tests': [75,90 ]}
Alice = {'name': 'Alice', 'homework':[100,92,98,100 ] , 'quizzes':[ 82,83,91] , 'tests': [89,97 ]}
Tyler = {'name': 'Tyler', 'homework':[ 0,87,75,22] , 'quizzes':[0,75,78 ] , 'tests':[ 100,100] }

print(Steve)
print(Alice)
print(Tyler)



# 3. Create a list called students that contains your three students and print the list

students = [ Steve, Alice, Tyler]
print(students)

# 4. Loop over your students list and print out the following for each student:
#   - Name: (print out the student's name)
#   - Homework: (print out the student's homework)
#   - Quizzes: (print out the student's quizzes)
#   - Tests: (print out the student's tests )

for student in students:
    print(f" Students name is {student['name']}")
    print(f"{student['name']}'s Homework is {student['homework']}")
    print(f"{student['name']}'s Quizzes is {student['quizzes']}")
    print(f"{student['name']}'s Tests is {student['tests']}")


# 5. Define a function to calculate the average of a list
#   a. Define a function called average() that has one argument, a list of numbers
#   b. Inside the function, use the built-in Python functions sum() and len() to calculate the average
#   c. Return the result 
#   d. Test it out to make sure it works

def average(list):
    return sum(list)/len(list)

list=[10,20,30]
print (average(list))


# 6. Write a function to calculate the weighted average score for a student
#   a. Define a function called get_weighted_average() that takes one argument: student (see the dictionaries we created above)
#   b. Use your average() function to calculate the average of the student's homework, quizzes, and test scores
#   d. Return the weighted average score for each student (homework is 10%, quizzes are 30%, and tests are 60%  of the grade).
#   e. Test out your get_weighted_average() function on each student

def get_weighted_average(student):
    #print(average(student['homework']))
    #print(average(student['quizzes']))
    #print(average(student['tests']))
    return .10*average(student['homework'])+ .30*average(student['quizzes'])+.60*average(student['tests'])

print(get_weighted_average(Tyler))
print(get_weighted_average(Alice))
print(get_weighted_average(Steve))

# 7. Write a function to convert a grade into a letter grade
#   a. Define a function called get_letter_grade() that has one argument called score (a number)
#   b. Inside your function, use if / elif /else to return the following letter grades:
#       - 90 or above: “A"
#       - 80 or above: “B"
#       - 70 or above: “C"
#       - 60 or above: “D"
#       - Below 60: “F"
#   c. Test it out on a few different numbers to make sure it works properly
#   d. Use a for loop to get each student's letter grade

def get_letter_grade(score):
        if score >= 90 and score <=100:
            return g[0]
        elif score < 90 and score >= 80:
            return g[1]
        elif score <80 and score>=70:
            return g[2]
        elif score <70 and score >= 60:
            return g[3]
        elif score>=0 and score<60:
            return g[4]
        else:
            return print("Score is not valid")

#test to see if the loop works
print(get_letter_grade(90))


for student in students:
    print("student")
    print(student)
    score=get_weighted_average(student)
    print(score)
    grade= get_letter_grade(score)
    print(grade)
    print(f"{student['name']}'s letter grade is '{grade}'")

# 8. Write a function to calculate the class average
#   a. Create a function called get_class_average() that has one argument, students (a list of dictionaries)
#   b. Inside the function, create a temporary empty list called results to store each student's grade
#   c. Loop over the list of students, appending each student's grade into your results list
#   d. Finally, return the average of the results
#   e. Test out your function by printing out the class average


#NOT SURE HOW TO DO Q8

def get_class_average(dictio):
    results=[]
    for student in students:
        results.append(grade)

print(get_class_average(students))

# 9. The class has now a new student, Thomas, with the following grades:
#   Homework: 90, 85, 80, 0
#   Quizzes: 80, 100, 87
#   Tests: 85, 90
#   a. Create a dictionary for Thomas (as you did in #1)
#   b. add him to the class, by appending the dictionary to your list of students
#   c. Calculate the new class average and print your results

Thomas = {'name': 'Thomas', 'homework':[ 90,85,80,0] , 'quizzes':[80,100,87 ] , 'tests':[ 85,90] }
students.append(Thomas)
print(students)

#calculating avergae of weighted averages
new_class_total= get_weighted_average(Alice) + get_weighted_average(Tyler)+ get_weighted_average(Thomas) + get_weighted_average(Steve)
print(new_class_total)
new_class_avg=new_class_total/len(students)
print(new_class_avg)


# BONUS: Move all of the functions out of this file and into another Python file
# called grading_functions.py. Then import them into this file so that it runs.
