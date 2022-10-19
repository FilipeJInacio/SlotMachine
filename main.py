import random
import os


class caracter:
    Pchar1 = 50
    Pchar2 = 40 + Pchar1
    Pchar3 = 30 + Pchar2
    Pchar4 = 20 + Pchar3
    Pchar5 = 10 + Pchar4
    Pchar6 = 5 + Pchar5
    Pchar7 = 1 + Pchar6
    Tchance = 156
    char = 0

    def roll(self):
        rand = random.randint(1, self.Tchance)
        if rand <= self.Pchar1:
            self.char = 1
        elif rand > self.Pchar1 and rand <= self.Pchar2:
            self.char = 2
        elif rand > self.Pchar2 and rand <= self.Pchar3:
            self.char = 3
        elif rand > self.Pchar3 and rand <= self.Pchar4:
            self.char = 4
        elif rand > self.Pchar4 and rand <= self.Pchar5:
            self.char = 5
        elif rand > self.Pchar5 and rand <= self.Pchar6:
            self.char = 6
        elif rand > self.Pchar6:
            self.char = 7
        return self.char


SlotMachine = caracter()

# 1
print("Welcome")
while True:
    try:
        print("How many credits do you want to deposit?")
        Credits = int(input("Enter your value: "))
        os.system('cls' if os.name == 'nt' else 'clear')

        if Credits <= 0:
            print("Invalid input.")
            continue

        break
    except ValueError:
        print("Please input integer only...")
        continue


lbool = True

while lbool:

    # 3
    while True:
        try:
            print("How many credits do you want to use this round")
            print("Currently you have -> " + str(Credits))
            CreditsToPlay = int(input("Enter your value: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            if CreditsToPlay > Credits:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You don't have that many...")
                continue
            elif CreditsToPlay <= 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid input.")
                continue
            elif CreditsToPlay == Credits:
                print("All in!!!!! Are you crazy?")

            break

        except ValueError:
            print("Please input integer only...")
            continue

    Credits = Credits-CreditsToPlay

    os.system('cls' if os.name == 'nt' else 'clear')

    Slot1 = SlotMachine.roll()
    Slot2 = SlotMachine.roll()
    Slot3 = SlotMachine.roll()

    print()
    print()
    print(" _____________")
    print("| |" + str(Slot1) + "|-|" + str(Slot2) + "|-|" + str(Slot3) + "| |")
    print("|_____________|")
    print()
    print()

    if Slot1 == Slot2 and Slot2 == Slot3:
        if Slot1 == 1:
            Credits = Credits + 5*CreditsToPlay
        elif Slot1 == 2:
            Credits = Credits + 10*CreditsToPlay
        elif Slot1 == 3:
            Credits = Credits + 20*CreditsToPlay
        elif Slot1 == 4:
            Credits = Credits + 70*CreditsToPlay
        elif Slot1 == 5:
            Credits = Credits + 200*CreditsToPlay
        elif Slot1 == 6:
            Credits = Credits + 1000*CreditsToPlay
        elif Slot1 == 7:
            Credits = Credits + 100000*CreditsToPlay

    print()
    print("You have " + str(Credits) + " Credits left.")
    print()

    if Credits == 0:
        break

    # 2
    while True:
        print("Do you want to continue playing?")
        Answer = input("Y/N: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if Answer == "N" or Answer == "n" or Answer == "no" or Answer == "No":
            lbool = False
            break
        elif Answer == "Y" or Answer == "y" or Answer == "yes" or Answer == "Yes":
            break
        else:
            print("Yes or No pls...")
            continue
