class Sharpie:

    def __init__(self, color, width = 100, ink_amount = 100):
        self.color = color
        self.width = float(width)
        self.ink_amount = float(ink_amount)

    def use(self):
        self.ink_amount -= 1
