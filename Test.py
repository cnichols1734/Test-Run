import time
first_name = input('What is your First name? ')
last_name = input('What is your Last name? ')
print('Hello ' + first_name +' ' + last_name,', hope all is well!');

birth_year = input('What year were you born? ')
age = 2022 - int(birth_year)
print('Got it, crunching the numbers')
time.sleep(.3)
print('.')
time.sleep(.3)
print('..')
time.sleep(.3)
print('...')
time.sleep(.3)
print('.....')
time.sleep(.3)
print('......')
time.sleep(.3)
print('.......')
time.sleep(1.5)
print('¯\_(ツ)_/¯')
time.sleep(1.2)
print('Ok, almost there!')
time.sleep(2)
print ('Your age:', str(age))
if age >=30:
    print ('wow, ur old ;)');