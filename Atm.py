class BankAtm:
    def __init__(self,cardnumber,pwd):
        self.cardnumber = cardnumber
        self.pwd = pwd

    def balance(self):
        print("Your balance is 1000000000")

    def withdrawl(self,amount):
        new_amount = 100000000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))


def main():
    Card_number = input("insert your card num:- ")
    pin_number  = input("enter your pwd:- ")

    new_user = BankAtm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1.Balance  2.withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()