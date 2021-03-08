# Store operation program
# Created By Abraham Baffoe CEO of WeGo GH and tutor of bestpointtutorials on youtube and instagram.
#Do not copy this code by you can edit the code. Thank you!

input('Enter your name dear Customer: ')
str(input('Enter your location to find: '))
print('You are welcome to WeGo gh Customer !')

days_of_operation = 'Monday'
user_choice_of_day = input('Enter any of the working day: ')
user_choice_of_time = int(input('Enter the time: '))
time_of_operation_morning = 10
time_of_operation_evening = 12
        #checking the validity of the working days
if days_of_operation != user_choice_of_day and user_choice_of_time != time_of_operation_morning:
	print('Sorry, the info did not match')

if days_of_operation >= user_choice_of_day and user_choice_of_time <= time_of_operation_evening :
    print('Huray, the store is opened customer!')
else:
   print('Oops! The store is closed!')
