print("WELCOME TO BANK MANAGEMENT SYSTEM ".center(50,"*"))
info={}
def menu1():
    menu=["====================","1) Creat account","2) Deposit ","3) Withdrawal","4) Account details","5) Exit","==============="]
    for i in menu:
        print(i,end="\n")


def create_acc():
    
    info["Name"]=input("\n Enter your name :")
    info["Age"]=int(input("Enter your Age:"))
    info["Adress"]=input("Enter your Adresss:")
    info["Contact"]=int(input("Enter your Active mobile number:"))
    info["Dob"]=input("Enter your date of birth [DDMMYYYY]:")
    info["Account number"]="115"+info["Dob"]
    info["Amount"]=0
    condition=input("Do you accept our terms of conditions [yes / no ]:")
    if condition=="yes"or condition=="Yes":
        print("your account number is 115"+info["Dob"])
        print("Your account was created successfully !!".center(50,"*"))
    else:
        print("Please accept terms of conditions to creat your account".center (70,"*"),end="\n")
        print("Please enter your deatils".center(30,"*"),end="\n")
        create_acc()

def deposit():
    acc_num=input("Enter the account number to deposite:")
    if acc_num==info["Account number"]:
        print("Your account is verified !!\n")
        deposit_amount=int(input("Enter amount to deposit:"))
        print("Your deposit process is successfully completed !!".center(60,"*"),end="\n")
        
        total_deposit=info["Amount"]+deposit_amount
        info["Amount"]=total_deposit
        print("AMOUNT IS ADDED TO YOUR ACCOUNT:",total_deposit)
    else:
        print("Enter your account number correctly !!\n".center(30,"*"))
        deposit()

def withdrawal():
    acc_num=input("Enter the account number to withdrawal:")
    if acc_num==info["Account number"]:
        print("Your account is verified !!\n")
        withdrawal_amount=int(input("Enter amount to withdrawal:"))
        if withdrawal_amount>info["Amount"]:
            print("Insufficient balance !!!\n")
            print("Please check your balance !!")
        else:
            print("Your withdrawal process is successfully completed !!".center(60,"*"),end="\n")
            print("Your account balance is:",info["Amount"]-withdrawal_amount)
            info["Amount"]-=withdrawal_amount
    else:
        print("invalid Account number !")
   
def details():
    print("\nName:",info["Name"])
    print("\nAge:",info["Age"])
    print("\nAdress:",info["Adress"])
    print("\nContact:",info["Contact"])
    print("\nDate of birth:",info["Dob"])
    print("\nAccount number:",info["Account number"])
    print("\nAccount balance", info["Amount"],end="\n")
    

running=True
while running:
    menu1()
    menu_ope=int(input("Kindly enter your choice:"))
    if menu_ope ==1:
        create_acc()
    elif menu_ope==2:
        deposit()
    elif menu_ope==3:
        withdrawal()
    elif menu_ope==4:
        details()
    elif menu_ope==5:
        running=False



