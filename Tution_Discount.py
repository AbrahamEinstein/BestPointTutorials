# School Tution fee Discount
# Problem: Use the chaining multiple condition to write a program that will calculate the average score and define tutition fee discounts
# Created by Abraham Baffoe
import math
print('Welcome to the Univeristy of Experts, London')
average_score = 100
student_name = str(input('Enter your name as a student: '))
student_ID = int(input('Enter studnt ID No`: '))
student_score = int(input('Enter your score Student: '))

if(average_score >= 70 and student_score >= 50 and average_score == 100):
    print('You qualify for discount student!')
else:
    print('Sorry, you do not qualify for the discount student!')

# if(average_score is not 100):
#     print('you have exceed your limit')
# I was trying to write the program that will terminate the code when it exceeds 100 as the average score
