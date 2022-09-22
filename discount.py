# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

subtotal = float(input("Please enter the subtotal:"))
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
day_of_week = 2

if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    discount = (subtotal * 10) /100
    tax_amount = ((subtotal-discount) * 6) / 100 
    total = subtotal - discount + tax_amount
    print(f"Discount amount: {discount:.2f}")
    print (f"Sales tax amount: {tax_amount:.2f}")
    print (f"Total: {total:.2f}")
else:
    tax_amount = (subtotal * 6) / 100 
    total = subtotal + tax_amount
    print (f"Sales tax amount: {tax_amount:.2f}")
    print (f"Total: {total:.2f}")




