''' 
    #! grading Example:
    
    #* Write an if/elif/else statement for a college with a grading system as shown below:

    # ~If grade is 90 or higher, print "A"
    #~ Else if grade is 80 or higher, print "B"
    #~ Else if grade is 70 or higher, print "C"
    #~ Else if grade is 60 or higher, print "D"
    # ~Else, print "F"
    # 

'''
print("\n  -----_____ SCHOOL GRADING SYSTEM_____------\n")
score = input("Enter mark score: ")
# grade = ''

if int(score) >= 90:
    grade = 'A'
elif int(score) >= 80:
    grade = 'B'
elif int(score) >= 70:
    grade = 'C'
elif int(score) >= 60:
    grade = 'D'
else:
    grade = 'F'

print("\t Mark score is: ", score)
print("\t Your grade is: ", grade)

