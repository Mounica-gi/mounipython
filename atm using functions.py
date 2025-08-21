print("welcome to atm bank..")
name=input("enter your name:")
pin=int(input("enter your pin:"))

def displaymenu():
    print("atm menu")
    print("1.balance")
    print("2.depoist")
    print("3.withdraw")
    print("4.exti")


def balance(balance):
    print(f"your current balance is:,{balance}")




def deposit(balance):
    amount=float("enter your deposit amount:")
    if amount>0:
        return balance+amount
    else:
        print("please enter invaild amount:")



def withdraw(balance):
    amount=int("enter your amount to withdraw:")
    if 0<amount<balance:
        return balance-amount
    else:
        print("invaild amount")
    


def atm():
    balance=1000
    while True:
     displaymenu()
     options=input("etner your options from 1 to 4")
     if options=='1':
        balance(balance)
     elif options=="2":
        balance=deposit(balance)
        print(f"after depositng your balance is {balance}")
     elif options=="3": 
        balance=withdraw(balance)
        print(f"after withdraw your amount is {balance}")
     elif options=="4":
         print("thank you for visting:")
         break

if name=="mouni" and pin==468:
    atm()
else:
     print("check your details:")
    print("enter your current detials")
    



    

        
