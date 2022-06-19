class SAccount:
    def __init__(self, accNo, accNm, bal, maxAmt=500.00):
        self.__accNo = accNo
        self.__accNm = accNm
        self.__bal = bal
        self.__maxAmt = maxAmt

    def getAccNo(self):
        return self.__accNo

    def getAccNm(self):
        return self.__accNm

    def getBal(self):
        return self.__bal

    def deposit(self, amount):
        if float(amount) > self.maxAmt:
            print("Maximum Amount: $" + str(self.__maxAmt))
            print("Reload amount is less than the minimum amount")
            print("Card transaction failed!!!!")
            print("---------------------------------")
            return False

        else:
            self.__bal += float(amount)
            self.__bal = round(self.__bal, 2)
            print("Balance: $" + str(self.__bal))
            print("Card transaction completed!")
            print("---------------------------")

    def withdraw(self, amount):
        if float(amount) > self.__bal:
            print("Balance: $" + str(self.__bal))
            print("Insufficient funds")
            print("Card transaction completed!")
            print("---------------------------")

        else:
            self.__bal -= float(amount)
            self.__bal = round(self.__bal, 2)
            print("Balance: $" + str(self.__bal))
            print("Card transaction successful!")
            print("----------------------------")

    def __str__(self):
        return "Account Number: " + str(self.__accNo) + "\nAccount Name: " + self.__accNm + "\nBalance: $" + str(self.__bal) + "\nMaximum Amount: $" + str(self.__maxAmt)
