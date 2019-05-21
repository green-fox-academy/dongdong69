import random

class CowsAndBolls:
    def __init__(self, number = random.randint(1000, 9999)):
        self.number = number
        self.state = "playing"
        self.counter = 0

    def guess(self, guess_number):
        self.counter += 1
        if guess_number == self.number:
            self.state = "finished"
            return "4 cow, 0 bull"

        guess_number = str(guess_number)
        str_number = str(self.number)
        remaining_number = [char for char in str_number]
        cow, bull = 0, 0

        for i in range(4):
            if guess_number[i] == str_number[i]:
                cow += 1
                remaining_number.remove(guess_number[i])
            elif guess_number[i] in remaining_number:
                bull += 1
                remaining_number.remove(guess_number[i])

        return f"{cow} cow, {bull} bull"
