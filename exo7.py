year=int(input('please enter write in a year :'))

if (year%4==0) :
    print(f'the year{year} is leap')
elif (year%100==0) and (year%400==0) :
    print(f'the year {year} is leap')
else:
    print('this year is not a leap year')