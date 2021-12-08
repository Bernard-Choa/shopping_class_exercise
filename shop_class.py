class FancyFood:
    def __init__(self, type, weight):
        self.type = type
        self.weight = weight
        self.__standard_price = 0
        self.__calc_price = 0

    def get_standard_price(self):
        return self.__standard_price

    def set_standard_price(self, amnt):
        self.__standard_price = amnt

    def __price_list(self):
        if self.type.lower() == "dry cured iberian ham":
            self.set_standard_price(177.8)

        elif self.type.lower() == "wagyu steaks":
            self.set_standard_price(450)

        elif self.type.lower() == "matsutake mushrooms":
            self.set_standard_price(272)

        elif self.type.lower() == "kopi luwak coffee":
            self.set_standard_price(306.5)

        elif self.type.lower() == "moose cheese":
            self.set_standard_price(487.2)

        elif self.type.lower() == "white truffles":
            self.set_standard_price(3600)

        elif self.type.lower() == "blue fin tuna":
            self.set_standard_price(3603)

        elif self.type.lower() == "le bonnotte potatoes":
            self.set_standard_price(270.81)

    def food_cost(self):
        self.__price_list()
        self.__calc_price = self.__standard_price * self.weight
        return self.__calc_price
