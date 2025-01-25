from exchange import *
import random

class Round:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.winner = None
        self.fighter1_starting_health = fighter1.health
        self.fighter2_starting_health = fighter2.health
        self.execute_exchanges()
    
    def execute_exchanges(self):
        for i in range(random.randint(4, 7)):
            exch = Exchange(self.fighter1, self.fighter2)
            if exch.fighter1.health <= 0:
                if exch.fighter1.toughness >= random.randint(1, 10):
                    exch.fighter1.health = 15
                    exch.fighter2.health += 15
                else:
                    exch.fighter1.knockout_status = True
                    self.winner = self.fighter1
                    self.fighter1 = exch.fighter1
                    self.fighter2 = exch.fighter1
                    break
            if exch.fighter2.health <= 0:
                if exch.fighter2.toughness >= random.randint(1, 10):
                    exch.fighter2.health = 15
                    exch.fighter1.health += 15
                else:
                    exch.fighter2.knockout_status = True
                    self.winner = self.fighter2
                    self.fighter1 = exch.fighter1
                    self.fighter2 = exch.fighter1
                    break
            self.fighter1 = exch.fighter1
            self.fighter2 = exch.fighter2
        fighter1_health_change = self.fighter1_starting_health - self.fighter1.health
        fighter2_health_change = self.fighter2_starting_health - self.fighter2.health
        if fighter1_health_change > fighter2_health_change:
            self.winner = self.fighter2
        elif fighter1_health_change < fighter2_health_change:
            self.winner = self.fighter1
        else:
            if random.randint(1, 2) == 1:
                self.winner = self.fighter1
            else:
                self.winner = self.fighter2

            
         
        
