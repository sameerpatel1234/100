class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceeinquiry(self):
        print("Your balance is : $100")

    def cashwidthdrawal(self, amount):
        new_amount = 100-amount
        print("You withrawed: " + str(amount) + "your resemble balance is: " + str(new_amount))

def main():
    name = input("hello what is your name?")
    print("Hello, " + name)
    cardnumber = input("Insert your card number:  ")
    pin = input("Enter your pin: ")
    new_user = Atm(cardnumber, pin)

    print("Choose your acitivity")
    print("1. Balance Inquiry")
    print("2. Cash Withdrawal")
    acicity = int(input("Enter acivity choices: "))

    if(activity == 1):
        new_user.balanceinquiry()
    elif(activity == 2):
        amount = int(input("Enter the amount: "))
        new_user.cashwidthdrawl(amount)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()