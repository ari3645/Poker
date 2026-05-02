class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []
        self.is_folded = False
        self.is_all_in = False
        self.current_bet = 0  # To track how much the player has bet in the current round

    def receive_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []
        self.is_folded = False
        self.is_all_in = False
        self.current_bet = 0

    def bet(self, amount):
        if amount > self.chips:
            # Handle all-in automatically if they try to bet more than they have?
            # Or just raise an error and let the game logic handle it.
            # Let's be strict for now.
            amount = self.chips
        
        self.chips -= amount
        self.current_bet += amount
        
        if self.chips == 0:
            self.is_all_in = True
            
        return amount

    def __str__(self):
        return f"Player {self.name} ({self.chips} chips) - Hand: {self.hand}"

    def __repr__(self):
        return self.__str__()
