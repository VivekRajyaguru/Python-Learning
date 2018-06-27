import random

class Coin():
    def __init__(self, rare = False, clean = True, heades = True, **kwargs): #Constructor
        for key,value in kwargs.items():
            setattr(self, key, value)
        
        self.is_rare = rare
        self.is_clean = clean
        self.heades = heades

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
        
        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color
        
    
    def rust(self):
        self.color = self.rusty_color
    
    def clean_coin(self):
        self.color = self.clean_color

    def flip(self):
        option = [True, False]
        self.heades = random.choice(option)

    def __str__(self):
        return "{} coin".format(self.original_value)
        

    def __del__(self): #Destuctor -- Distory Object
        print('Distroy Coin')


class OneRupee(Coin):
    def __init__(self):
        data = {
            'original_value': 1.00,
            'clean_color': 'silver',
            'rusty_color': 'brown',
            'diameter': 25,
            'edges': 1
        }
        super().__init__(**data)

class TwoRupee(Coin):
    def __init__(self):
        data = {
            'original_value': 2.00,
            'clean_color': 'silver',
            'rusty_color': 'brown',
            'diameter': 25,
            'edges': 1
        }
        super().__init__(**data)


class FiveRupee(Coin):
    def __init__(self):
        data = {
            'original_value': 5.00,
            'clean_color': 'gold',
            'rusty_color': 'green',
            'diameter': 25,
            'edges': 1
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.clean_color

    def clean_coin(self):
        self.color = self.clean_color


coins = [OneRupee(), TwoRupee(), FiveRupee()]

for coin in coins:
    args = [coin, coin.color, coin.value, coin.diameter, coin.edges]

    print('{} - Color: {}, value: {}, diameter: {}, edges: {}'.format(*args))
    