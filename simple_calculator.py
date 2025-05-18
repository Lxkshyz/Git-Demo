class SimpleCalculator:
## INITIALIZE
    def __init__(self):
        self.ui_1 = int(input("Number 1: "))
        self.ui_2 = int(input("Number 2: "))

## MENU
        print("<--- MENU --->\n(1) for ADDITION\n(2) for SUBSTRACTION\n(3) for MULTIPLICATION\n(4) for DIVISION\n(5) to EXIT")
        while True:
            self.usr_choice = int(input("Enter here: "))
            if self.usr_choice == 1:
                self.add()
            if self.usr_choice == 2:
                self.sub()
            if self.usr_choice == 3:
                self.mult()
            if self.usr_choice == 4:
                self.div()
            if self.usr_choice == 5:
                exit()

## LOGIC
    def add(self):
        x = self.ui_1 + self.ui_2
        print(f"Addition Result: {x}")
    def mult(self):
        x = self.ui_1 * self.ui_2
        print(f"Multiplication Result: {x}")
    def div(self):
        x = self.ui_1 / self.ui_2
        print(f"Division Result: {x}")
    def sub(self):
        x = self.ui_1 - self.ui_2
        print(f"Substraction Result: {x}")