class CAccount:
    def __init__(self, accNo, accNm, bal, minAmt=50.00):
        self.__accNo = accNo
        self.__accNm = accNm
        self.__bal = bal
        self.__minAmt = minAmt

    def getAccNo(self):
        return self.__accNo

    def getAccNm(self):
        return self.__accNm

    def getBal(self):
        return self.__bal

    def deposit(self, amount):
        if float(amount) < self.__minAmt:
            print("Minimum Amount: $" + str(self.__minAmt))
            print("Deposit amount is less than minimum amount")
            print("Card transaction failed!")
            print("------------------------")
            return False

        else:
            self.__bal += float(amount)
            self.__bal = round(self.__bal, 2)
            print("Balance: $" + str(self.__bal))
            print("Card transaction completed!")
            print("---------------------------")
            return True

    def withdraw(self, amount):
        if float(amount) > self.__bal:
            print("Balance: $" + str(self.__bal))
            print("Insufficient funds")
            print("Card Transaction failed!")
            print("------------------------")
            return False

        else:
            self.__bal -= float(amount)
            self.__bal = round(self.__bal, 2)
            print("Balance: $" + str(self.__bal))
            print("Card transaction completed!")
            print("---------------------------")
            return True

    def __str__(self):
        return "Account Number: " + str(self.__accNo) + "\nAccount Name: " + self.__accNm + "\nBalance: $" + str(self.__bal) + "\nMinimum Amount: $" + str(self.__minAmt)
