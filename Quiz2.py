name = raw_input("What is your name?")
last = raw_input("What is your last name?")
year = input("What is your birth year?")
grade1 = input("What is your first semester grade?")
grade2 = input("What is your second semester grade?")

age = 2015 - year
avg = (grade1+grade2)*.5

print "You are" , age , "years old."
print "Your final grade is", avg, "."
