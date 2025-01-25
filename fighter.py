class Fighter:
    def __init__(self, name):
        self.name = name
        file = open(f"./fighters/{name}.txt", "r")
        for line in file:
            attrib = line.split("=")
            setattr(self, attrib[0], int(attrib[1]))
        file.close
        self.strategy = "punch"
        self.knockout_status = False
    
    def set_strategy(self, choice):
        if choice == "1":
            self.strategy = "punch"
        elif choice == "2":
            self.strategy = "kick"
        elif choice == "3":
            self.strategy = "clinch"