import time


current = time.strftime ('%H:%M:%S')

if current < ('06:00:00') and current > ('01:00:00'):
    print("Good Morning")
elif current < ('12:00:00') and current > ('06:00:00'):
    print("Good afternoon")
elif current < ('13:00:00') and current > ('23:00:00'):
    print("Good night")
