from datetime import date
from datetime import datetime
f_date = date(2021, 4, 10)
l_date = date(2021, 7, 18)
A_date = date(2021, 7, 11)
B_date = date(2021, 7, 10)
one = A_date - B_date
today = date.today()
#print("Today's date:", today)
Total = l_date - f_date
#print(Total.days)
Current = l_date - today
#print(Current.days)
percentage = 100 - (( Current / Total ) * 100 )
weeks = (Current / one) / 7
print (weeks)

