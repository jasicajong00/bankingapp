from CAccountOOP import CAccount
from SAccountOOP import SAccount
import re


class Bank:

    def __init__(self):
        self.__CAccount = []
        self.__SAccount = []
        self.__accIdx = -1
        self.__accObj = None

    def loadCAccount(self):
        fr = open(
            "/Users/jasicajong/Documents/Uni/Object-Oriented Programming/Assessment 2/CAccounts.txt", "r")

        for f in fr:
            f = f.rstrip("\n")
            temp = f.split(";")

            if len(temp) == 3:
                c = CAccount(int(temp[0], temp[1], float(temp[2])))
                self.__CAccount.append(c)
            else:
                CAccount(int(temp[0], temp[1], float(temp[2]), float(temp[3])))
                self.__CAccount.append(c)

        fr.close()

    def loadSAccount(self):
        fr = open(
            "/Users/jasicajong/Documents/Uni/Object-Oriented Programming/Assessment 2/SAccounts.txt", "r")

        for f in fr:
            f = f.rstrip("\n")
            temp = f.split(";")

            if len(temp) == 3:
                s = SAccount(int(temp[0]), temp[1], float(temp[2]))
                self.__SAccount.append(s)
            else:
                s = SAccount(int(temp[0]), temp[1],
                             float(temp[2], float(temp[3])))
                self.__SAccount.append(s)

        fr.close()

    def menu(self):
        while True:
            print("------------------ Bank App: ------------------")
            print("1. Checking Accounts")
            print("2. Savings")
            print("3. View Checking Balance")
            print("4. View Savings Balance")
            print("5. Exit")
            print("---------------------------------------------------------")
            opt = input("Select Option: ")

            if opt == "1":
                accNo = input("Enter Checkings Account Number: ")

                if not accNo.isdigit():
                    print("Invalid checking account number. Please try again.")
                    self.menu()

                self.__accIdx = self.getCAccount(accNo)

                if self.__accIdx != -1:
                    self.cMenu()
                else:
                    print("Checking account does not exist. Please try again.")
            elif opt == "2":
                cardNo = input("Enter Savings Account Number: ")

                if not accNo.isdigit():
                    print("Invalid savings account number. Please try again.")
                    self.menu()

                self.__accIdx = self.getSAccount(accNo)

                if self.__accIdx != -1:
                    self.sMenu()
                else:
                    print("Savings accounts does not exist. Please try again.")
            elif opt == "3":
                print("---- Checkings Account Balance: ----")
                for c in self.__CAccount:
                    print(c)
                    print("------------")
            elif opt == "4":
                print("---- Saving Accounts: ----")
                for s in self.__SAccount:
                    print(s)
                    print("------------")
            elif opt == "5":
                print("Exiting Application. Goodbye!!!!")
                exit()
            else:
                print("Invalid option selected. Please try again.")

    def cMenu(self):
        self.__accObj = self.__CAccount[self.__accIdx]

        while True:
            print("---- Checking Account: " +
                  str(self.__accObj.getAccNo())) + "----"
            print("1. Deposit")
            print("2. Withdraw")
            print("3. View Balance")
            print("4. View Account Details")
            print("5. Return to Main Menu")
            print("----------------------")
            opt = input("Select Option: ")

            if opt == "1":
                amt = input("Enter Deposit Amount: $")

                if re.search("^[0-9]+\.*[0-9]*$", amt):
                    self.__accObj.deposit(amt)
                    self.__CAccount[self.__accIdx] = self.__accObj
                    fw = open(
                        "/Users/jasicajong/Documents/Uni/Object-Oriented Programming/Assessment 2/BankingReceipt.txt", "w")
                    fw.write("---- Bank App ----")
                    fw.write("\nAccount Number: " +
                             str(self.__accObj.getAccNo()))
                    fw.write("\nReload Amount: $" + amt)
                    fw.write("\nCurrent Balance: $" +
                             str(self.__accObj.getAccBal()))
                    fw.close()
                else:
                    print("Invalid input entered for deposit amount.")
                    print("Card transaction failed!")

            elif opt == "2":
                amtWithdraw = input("Enter Withdrawal Amount: $")

                if re.search("^[1-9]+$", amtWithdraw):
                    status = self.__accObj.play(amt)
                    if status == True:
                        self.__CAccount[self.__accIdx] = self.__accObj
                        fw = open(
                            "/Users/jasicajong/Documents/Uni/Object-Oriented Programming/Assessment 2/BankingReceipt.txt", "w")
                        fw.write("---- Bank App ----")
                        fw.write("\nAmount Withdrawn: " + amtWithdraw)
                        fw.write("\nAccount Number: " +
                                 str(self.__accObj.getAccNo()))
                    fw.write("\nCurrent Balance: $" +
                             str(self.__accObj.getAccBal()))
                    fw.close()

                else:
                    print("Invalid input entered for number of games to play.")
                    print("Card Transaction failed!!!!")

            elif opt == "3":
                print("Current Balance: $", self.__accObj.getAccBal())
                fw = open(
                    "/Users/jasicajong/Documents/Uni/Object-Oriented Programming/Assessment 2/BankingReceipt.txt", "w")
                fw.write("----------------- Banking Receipt -----------------")
                fw.write("\nAccount Number: " + str(self.__accObj.getAccNo()))
                fw.write("\nCurrent Balance: $" +
                         str(self.__accObj.getAccBal()))
                fw.close()

            elif opt == "4":
                print("----Account Details: ----")
                print(self.__CAccount[self.__accIdx])
            elif opt == "5":
                self.cMenu()
            else:
                print("Invalid option selected. Please try again.")

    def sMenu(self):
        self.__accObj = self.__SAccount[self.__accIdx]

        while True:
            print("---- Savings Account: " +
                  str(self.__accObj.getAccNo()) + "----")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. View Balance")
            print("4. View Account Details")
            print("----------------------")
            opt = input("Select Option: ")

            if opt == "1":
                amt = input("Enter deposit amount: $ ")

                if re.search("^[0-9]+\.*[0-9]*$", amt):
                    self.__accObj.reload(amt)
                    self.__SAccount[self.__accIdx] = self.__accObj
                    fw = open(
                        "/Users/jasicajong/Documents/Uni/Object-Oriented Programming/Assessment 2/BankingReceipt.txt", "w")
                    fw.write("---- Banking Receipt ----")
                    fw.write("\nCard Number: " +
                             str(self.__cardObj.getCardNo()))
                    fw.write("\nReload Amount: $" + amt)
                    fw.write("\nCurrent Balance: $" +
                             str(self.__cardObj.getCardBal()))
                    fw.close()
                else:
                    print("Invalid input entered for deposit amount.")
                    print("Card transaction failed. Please try again")

            elif opt == "2":
                amtWithdraw = input("Enter Withdrawal Amount: $")

                if re.search("^[1-9]+$", amtWithdraw):
                    status = self.__accObj.play(amt)
                    if status == True:
                        self.__SAccount[self.__accIdx] = self.__accObj
                        fw = open(
                            "/Users/jasicajong/Documents/Uni/Object-Oriented Programming/Assessment 2/BankingReceipt.txt", "w")
                        fw.write("---- Bank App ----")
                        fw.write("\nAmount Withdrawn: " + amtWithdraw)
                        fw.write("\nAccount Number: " +
                                 str(self.__accObj.getAccNo()))
                    fw.write("\nCurrent Balance: $" +
                             str(self.__accObj.getAccBal()))
                    fw.close()

                else:
                    print("Invalid input entered for number of games to play.")
                    print("Card Transaction failed!!!!")

            elif opt == "3":
                print("Current Balance: $", self.__accObj.getAccBal())
                fw = open(
                    "/Users/jasicajong/Documents/Uni/Object-Oriented Programming/Assessment 2/BankingReceipt.txt", "w")
                fw.write("\nCard Number: " + str(self.__cardObj.getCardNo()))
                fw.write("\nReload Amount: $" + amt)
                fw.write("\nCurrent Balance: $" +
                         str(self.__cardObj.getCardBal()))
                fw.close()
            elif opt == "4":
                print("----Account Details ----")
                print(self.__SAccount[self.__accIdx])
            elif opt == "5":
                self.menu()
            else:
                print("Invalid option selected. Please try again.")

    def getCAccount(self, accNo):

        for c in self.__CAccount:
            if int(accNo) == c.getAccNo():
                return self.__CAccount.index(c)

        return -1

    def getSAccount(self, accNo):

        for s in self.__SAccount:
            if int(accNo) == s.getAccNo():
                return self.__SAccount.index(s)

        return -1

    def main(self):
        self.loadCAccount()
        self.loadSAccount()
        self.menu()


bank = Bank()
bank.main()
