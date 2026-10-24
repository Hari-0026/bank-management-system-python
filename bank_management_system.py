print("WELCOME TO BANK MANAGEMENT SYSTEM ".center(50,"*"))
accounts={}

def menu1():
    menu=["="*20,"1) Create account","2) Deposit","3) Withdrawal","4) Account details","5) Transaction history","6) Exit","="*20]
    for i in menu:
        print(i,end="\n")
def get_text(message):
    while True:
        text=input(message)
        if text!="":
            return text
        else:
            print("This field cannot be empty !!")

def get_number(message):
    while True:
        try:
            number=int(input(message))
        except ValueError:
            print("Please enter numbers only !!")
            continue
        if number>0:
            return number
        else:
            print("The value must be greater than 0 !!")

def find_account(message):
    if len(accounts)==0:
        print("No accounts found , please create an account first !!".center(60,"*"))
        return None
    for attempt in range(3):
        acc_num=input(message)
        if acc_num in accounts:
            print("Account found !!\n")
            return accounts[acc_num]
        else:
            print("Invalid account number !! Attempts left:",2-attempt)
    print("Too many wrong attempts , returning to menu".center(60,"*"))
    return None

def check_pin(info):
    for attempt in range(3):
        pin=input("Enter your 4 digit PIN:")
        if pin==info["PIN"]:
            print("Your account is verified !!\n")
            return True
        else:
            print("Wrong PIN !! Attempts left:",2-attempt)
    print("Too many wrong attempts , returning to menu".center(60,"*"))
    return False


def create_acc():
    info={}
    info["Name"]=get_text("\n Enter your name :")
    while True:
        age=get_number("Enter your Age:")
        if age>=18:
            break
        else:
            print("You must be 18 or older to open an account !!")
    info["Age"]=age
    info["Address"]=get_text("Enter your Address:")
    while True:
        contact=input("Enter your Active mobile number:")
        if contact.isdigit() and len(contact)==10:
            break
        else:
            print("Mobile number must be exactly 10 digits !!")
    info["Contact"]=contact
    while True:
        dob=input("Enter your date of birth [DDMMYYYY]:")
        if dob.isdigit() and len(dob)==8:
            break
        else:
            print("Invalid date of birth , please use the format DDMMYYYY !!")
    info["Dob"]=dob
    while True:
        pin=input("Create a 4 digit PIN:")
        if pin.isdigit() and len(pin)==4:
            break
        else:
            print("PIN must be exactly 4 digits !!")
    info["PIN"]=pin
    info["Amount"]=0
    info["History"]=[]
    condition=input("Do you accept our terms of conditions [yes / no ]:")
    if condition=="yes" or condition=="Yes":
        acc_num="115"+dob+str(len(accounts)+1)
        info["Account number"]=acc_num
        accounts[acc_num]=info
        print("your account number is",acc_num)
        print("Your account was created successfully !!".center(50,"*"))
    else:
        print("Please accept terms of conditions to create your account".center(70,"*"),end="\n")
        print("Your account was not created".center(70,"*"),end="\n")

def deposit():
    info=find_account("Enter the account number to deposit:")
    if info is None:
        return
    deposit_amount=get_number("Enter amount to deposit:")
    print("Your deposit process is successfully completed !!".center(60,"*"),end="\n")

    total_deposit=info["Amount"]+deposit_amount
    info["Amount"]=total_deposit
    info["History"].append("Deposit  : +"+str(deposit_amount)+" | Balance : "+str(total_deposit))
    print("AMOUNT DEPOSITED:",deposit_amount)
    print("YOUR ACCOUNT BALANCE IS:",total_deposit)

def withdrawal():
    info=find_account("Enter the account number to withdrawal:")
    if info is None:
        return
    if check_pin(info)==False:
        return
    withdrawal_amount=get_number("Enter amount to withdrawal:")
    if withdrawal_amount>info["Amount"]:
        print("Insufficient balance !!!\n")
        print("Your current balance is:",info["Amount"])
    else:
        print("Your withdrawal process is successfully completed !!".center(60,"*"),end="\n")
        info["Amount"]-=withdrawal_amount
        info["History"].append("Withdraw : -"+str(withdrawal_amount)+" | Balance : "+str(info["Amount"]))
        print("Your account balance is:",info["Amount"])

def details():
    info=find_account("Enter your account number:")
    if info is None:
        return
    if check_pin(info)==False:
        return
    print("\nName:",info["Name"])
    print("\nAge:",info["Age"])
    print("\nAddress:",info["Address"])
    print("\nContact:",info["Contact"])
    print("\nDate of birth:",info["Dob"])
    print("\nAccount number:",info["Account number"])
    print("\nAccount balance:", info["Amount"],end="\n")

def transaction_history():
    info=find_account("Enter your account number:")
    if info is None:
        return
    if check_pin(info)==False:
        return
    if len(info["History"])==0:
        print("No transactions yet !!")
    else:
        print("YOUR TRANSACTION HISTORY".center(50,"*"))
        for i in range(0,len(info["History"])):
            print(i+1,")",info["History"][i])
running=True
while running:
    menu1()
    try:
        menu_ope=int(input("Kindly enter your choice:"))
    except ValueError:
        print("invalid option , Please enter a number from 1 to 6")
        continue
    if menu_ope ==1:
        create_acc()
    elif menu_ope==2:
        deposit()
    elif menu_ope==3:
        withdrawal()
    elif menu_ope==4:
        details()
    elif menu_ope==5:
        transaction_history()
    elif menu_ope==6:
        print("Thank you for using our bank !!")
        running=False
    else:
        print("invalid option , Please select a number from 1 to 6")
