import random

class Exchange:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.counter = None
        self.determine_aggressor()
        self.determine_method()
        self.determine_outcome()
        

    def determine_aggressor(self):
        chance = .5 * random.uniform(.8, 1.2)
        difference = self.fighter1.aggression - self.fighter2.aggression
        modifier = difference / 100
        chance += modifier
        if chance > .5:
            self.aggressor = self.fighter1
            self.defender = self.fighter2
        elif chance < .5:
            self.aggressor = self.fighter2
            self.defender = self.fighter1
        else:
            if random.randint(1, 2) == 1:
                self.aggressor = self.fighter1
            else:
                self.defender = self.fighter2
    
    def determine_method(self):
        base_chance = .5
        balance_modifier = self.aggressor.balance/100
        total_chance = (base_chance + balance_modifier) * 100
        if random.randint(0, 100) < total_chance:
            self.method = self.aggressor.strategy
        else:
            if self.aggressor.strategy == "punch":
                if random.randint(1, 2) == 1:
                    self.method = "kick"
                else:
                    self.method = "clinch"
            elif self.aggressor.strategy == "kick":
                if random.randint(1, 2) == 1:
                    self.method = "punch"
                else:
                    self.method = "clinch"
            elif self.aggressor.strategy == "clinch":
                if random.randint(1, 2) == 1:
                    self.method = "kick"
                else:
                    self.method = "punch"

    def determine_outcome(self):
        counter_chance = self.defender.counter*5 + random.randint(-5, 5)
        if counter_chance > random.randint(1, 100):
            self.counter = self.defender
            self.damage = round((self.defender.balance + random.randint(1, 10)) * (self.defender.stamina/100)) - (self.aggressor.toughness % 2)
            self.aggressor.health -= self.damage
            self.aggressor.stamina -= random.randint(1, 7)
            if self.aggressor.stamina <= 0:
                self.aggressor.stamina = 10
            self.defender.stamina -= random.randint(1, 4)
            if self.defender.stamina <= 0:
                self.defender.stamina = 10
        else:
            if self.method == "punch":
                self.damage = round((self.aggressor.punch_skill + random.randint(1, 10)) * (self.defender.stamina/100)) - (self.defender.toughness % 2)
                self.defender.health -= self.damage
                self.aggressor.stamina -= random.randint(1, 7)
                if self.aggressor.stamina <= 0:
                    self.aggressor.stamina = 10
            elif self.method == "kick":
                self.damage = round((self.aggressor.kick_skill + random.randint(1, 10)) * (self.defender.stamina/100)) - (self.defender.toughness % 2)
                self.defender.health -= self.damage
                self.aggressor.stamina -= random.randint(1, 7)
                if self.aggressor.stamina <= 0:
                    self.aggressor.stamina = 10
            elif self.method == "clinch":
                self.damage = round((self.aggressor.clinch_skill + random.randint(1, 10)) * (self.defender.stamina/100)) - (self.defender.toughness % 2)
                self.defender.health -= self.damage
                self.aggressor.stamina -= random.randint(1, 7)
                if self.aggressor.stamina <= 0:
                    self.aggressor.stamina = 10
    
    def report(self):
        print("RESULT OF EXCHANGE:")
        print(f"{self.aggressor.name} tried to {self.method} {self.defender.name}.")
        if self.counter != None:
            print(f"{self.counter.name} countered the attack and did {self.damage} damage.")
        else:
            print(f"{self.aggressor.name} did {self.damage} with the strike.")