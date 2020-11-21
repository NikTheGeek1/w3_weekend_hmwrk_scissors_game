class Tournament:
    def __init__(self):
        self.history = {'hh': [], 'hc': [], 'cc': []}

    def add_to_history(self, result, type_):
        self.history[type_].append(result)


    def game(self, p1, p2, type_):
        if p1.choice == p2.choice:
            self.add_to_history(f'{p1.name} vs {p2.name}: draw', type_)
            return None

        if p1.choice == 'rock' and p2.choice == 'scissors':
            self.add_to_history(f'{p1.name} vs {p2.name}: {p1.name} won!', type_)
            return p1
        elif p1.choice == 'rock' and p2.choice == 'paper': 
            self.add_to_history(f'{p1.name} vs {p2.name}: {p2.name} won!', type_)
            return p2

        if p2.choice == 'rock' and p1.choice == 'scissors':
            self.add_to_history(f'{p1.name} vs {p2.name}: {p2.name} won!', type_)
            return p2
        elif p2.choice == 'rock' and p1.choice == 'paper': 
            self.add_to_history(f'{p1.name} vs {p2.name}: {p1.name} won!', type_)
            return p1
        
        if p1.choice == 'scissors' and p2.choice == 'paper':
            self.add_to_history(f'{p1.name} vs {p2.name}: {p1.name} won!', type_)
            return p1
        elif p2.choice == 'scissors' and p1.choice == 'paper':
            self.add_to_history(f'{p1.name} vs {p2.name}: {p2.name} won!', type_)
            return p2