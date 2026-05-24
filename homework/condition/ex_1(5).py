#Store customer balance in a variable. Ask user for amount to withdraw. 
#If desired amount is less than total balance display, 123 withdrawn successfully. 
#New Balance: 456 else display Insufficient balance. You only have 123 in your account
total_balance = 600
amt_withdrawn = int(input("enter for amount: "))
if total_balance > amt_withdrawn:
    print(f"{amt_withdrawn} withdrawn successfully.")
else:
    print(f" Insufficient balance. You have only have {total_balance} in your account")