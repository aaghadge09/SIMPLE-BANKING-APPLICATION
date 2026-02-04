
balance = 0.0
kyc_documents = {}




def check_balance():
    print(f"Your balance is {balance}")



def deposit(amount):
    global balance
    if amount >= 0:
        balance += amount
    else:
        print("You cannot deposit a negative number")


def withdraw(amount):
    global balance
    if amount <= 0:
        print("You cannot withdraw a negative number")
    elif amount > balance:
        print("INSUFFICIENT BALANCE")
    else:
         balance -= amount


def update_kyc_documents(documents):
    global kyc_documents
    kyc_documents = kyc_documents.update(documents)



def check_kyc():
    if len(kyc_documents) == 0:
        print("You have no kyc documents")
    else:
        for document in kyc_documents:
            print(f"{document} : {kyc_documents}")





if __name__ == "__main__":
    print("=================================")
    print("Welcome to Aryan Banking Application")
    print("================================")
    print()


    while True:
        print("1.CHECK YOUR BALANCE")
        print("2.DEPOSIT YOUR AMOUNT")
        print("3.WITHDRAW YOUR AMOUNT")
        print("4.CHECK YOUR KYC DOCUMENTS")
        print("5.UPADTE YOUR KYC DOCUMENTS")
        print("6.EXIT")
        choice = int(input("Enter your choice(1-6): "))

        if choice == 1:
            check_balance()
        elif choice == 2:
            amount = int(input("Enter your amount: "))
            deposit(amount)
            print(f"YOUR AMOUNT {amount} IS DEPOSITED")
        elif choice == 3:
            amount = int(input("Enter your amount: "))
            withdraw(amount)
            print(f"YOUR AMOUNT {amount} WITHDRAWN SUCCESSFUL")
        elif choice == 4:
            check_kyc()
        elif choice == 5:
            documents = int(input("Enter your number of documents: "))
            new_kyc_documents ={}
            for i in range (documents):
                key=input("Enter the document type: ")
                value=input("Enter your document number : ")
                kyc_documents[key]=value
            update_kyc_documents()
            print(f"YOUR KYC DOCUMENTS ARE UPDATED")
        elif choice == 6:
            print("QUITTING HAVE A NICE DAY ")
            break
        else:
            print("invalid choice")


    print()
    print("THANKS!!!FOR BANKING WITH US ")


