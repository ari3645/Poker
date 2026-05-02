import os
from .deck import Deck
from .player import Player

class PokerGame:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.pot = 0
        self.community_cards = []
        self.current_bet_to_follow = 0
        self.small_blind = 10
        self.big_blind = 20

    def setup_players(self, num_players, starting_chips=2000):
        self.players = []
        for i in range(num_players):
            name = f"Joueur {i+1}"
            self.players.append(Player(name, starting_chips))

    def clear_screen(self):
        # Pour Windows: 'cls', pour Mac/Linux: 'clear'
        os.system('cls' if os.name == 'nt' else 'clear')

    def handle_blinds(self):
        if len(self.players) < 2:
            return
        
        sb_player = self.players[0]
        bb_player = self.players[1]
        
        print(f"\n--- BLINDES ---")
        self.pot += sb_player.bet(self.small_blind)
        print(f"{sb_player.name} pose la Petite Blinde ({self.small_blind})")
        
        self.pot += bb_player.bet(self.big_blind)
        print(f"{bb_player.name} pose la Grosse Blinde ({self.big_blind})")
        
        self.current_bet_to_follow = self.big_blind

    def deal_preflop(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.community_cards = []
        self.pot = 0
        for player in self.players:
            player.clear_hand()
            player.receive_card(self.deck.deal())
            player.receive_card(self.deck.deal())
        
        self.handle_blinds()

    def deal_flop(self):
        self.deck.deal() 
        self.community_cards.extend(self.deck.deal(3))

    def deal_turn(self):
        self.deck.deal()
        self.community_cards.append(self.deck.deal())

    def deal_river(self):
        self.deck.deal()
        self.community_cards.append(self.deck.deal())

    def display_community_cards(self, phase_name):
        print(f"\n--- {phase_name.upper()} ---")
        print(f"Table : {self.community_cards}")
        print("--------------------\n")

    def get_active_players(self):
        return [p for p in self.players if not p.is_folded]

    def award_pot(self, winner):
        print(f"\n{winner.name} gagne le pot de {self.pot} jetons !")
        winner.chips += self.pot
        self.pot = 0

    def split_pot(self, winners):
        share = self.pot // len(winners)
        print(f"\nÉgalité ! Le pot de {self.pot} est partagé entre :")
        for winner in winners:
            print(f"- {winner.name} gagne {share} jetons")
            winner.chips += share
        self.pot = 0

    def check_hand_over(self):
        active_players = self.get_active_players()
        if len(active_players) == 1:
            winner = active_players[0]
            print(f"\nTous les autres joueurs se sont couchés.")
            self.award_pot(winner)
            return True
        return False

    def play_action_round(self, phase_name):
        print(f"\n--- ACTION : {phase_name.upper()} ---")
        
        for player in self.players:
            player.current_bet = 0
            
        if phase_name == "Pre-flop":
            self.players[0].current_bet = self.small_blind
            self.players[1].current_bet = self.big_blind
            self.current_bet_to_follow = self.big_blind
            current_index = 2 % len(self.players)
        else:
            self.current_bet_to_follow = 0
            current_index = 0

        has_acted = {p.name: False for p in self.players}

        while True:
            active_players = self.get_active_players()
            if len(active_players) <= 1:
                return self.check_hand_over()

            all_equal = True
            for p in active_players:
                if p.current_bet != self.current_bet_to_follow or not has_acted[p.name]:
                    all_equal = False
                    break
            
            if all_equal:
                break

            player = self.players[current_index]

            if player.is_folded or player.is_all_in:
                current_index = (current_index + 1) % len(self.players)
                continue

            # --- SYSTEME DE CACHE ---
            self.clear_screen()
            print(f"========================================")
            print(f" PHASE : {phase_name.upper()}")
            print(f" TOUR DE : {player.name}")
            print(f"========================================")
            input(f"\n{player.name}, appuyez sur Entrée quand vous êtes prêt à voir votre main...")
            
            print(f"\nVos jetons : {player.chips}")
            print(f"VOTRE MAIN : {player.hand}")
            if self.community_cards:
                print(f"Table : {self.community_cards}")
            print(f"Pot actuel : {self.pot}")
            print(f"Mise à suivre : {self.current_bet_to_follow} (Déjà mis : {player.current_bet})")
            
            action = ""
            options = []
            if self.current_bet_to_follow == 0:
                print("\n1. Checker")
                print("2. Miser (20)")
                options = ["1", "2", "3"]
            else:
                print("\n1. Suivre")
                print("2. Relancer (+40)")
                options = ["1", "2", "3"]
            print("3. Se Coucher")
            
            while action not in options:
                action = input("Votre choix : ")
                
                if action == "3":
                    player.is_folded = True
                    print(f"{player.name} s'est couché.")
                    input("\nAppuyez sur Entrée pour passer au joueur suivant...")
                    if self.check_hand_over():
                        return True
                elif action == "1":
                    if self.current_bet_to_follow == 0:
                        print(f"{player.name} a checké.")
                    else:
                        amount_to_call = self.current_bet_to_follow - player.current_bet
                        if amount_to_call >= player.chips:
                            print(f"{player.name} n'a pas assez de jetons pour suivre totalement. ALL-IN !")
                            actual_bet = player.bet(player.chips)
                        else:
                            actual_bet = player.bet(amount_to_call)
                        
                        self.pot += actual_bet
                        print(f"{player.name} a misé {actual_bet} (Total: {player.current_bet}).")
                    input("\nAppuyez sur Entrée pour passer au joueur suivant...")
                elif action == "2":
                    min_total = self.current_bet_to_follow * 2
                    if min_total == 0: min_total = 20
                    
                    print(f"Quel montant TOTAL voulez-vous miser pour ce tour ? (Minimum {min_total})")
                    
                    valid_raise = False
                    while not valid_raise:
                        try:
                            target_total = int(input(f"Total visé (votre tapis: {player.chips}, déjà mis: {player.current_bet}): "))
                            amount_to_add = target_total - player.current_bet
                            
                            if amount_to_add > player.chips:
                                print(f"Erreur : Vous n'avez que {player.chips} jetons.")
                            elif target_total < min_total and amount_to_add < player.chips:
                                print(f"Erreur : Le total de la relance doit être au moins de {min_total}.")
                            elif target_total <= self.current_bet_to_follow:
                                print(f"Erreur : Pour relancer, votre total doit être supérieur à {self.current_bet_to_follow}.")
                            else:
                                actual_bet = player.bet(amount_to_add)
                                self.current_bet_to_follow = player.current_bet
                                self.pot += actual_bet
                                print(f"{player.name} a relancé. Nouveau total : {player.current_bet}.")
                                
                                for p in self.players:
                                    if p.name != player.name:
                                        has_acted[p.name] = False
                                valid_raise = True
                        except ValueError:
                            print("Veuillez entrer un nombre entier.")
                    
                    input("\nAppuyez sur Entrée pour passer au joueur suivant...")
                else:
                    print("Choix invalide.")
            
            has_acted[player.name] = True
            current_index = (current_index + 1) % len(self.players)
        
        self.clear_screen()
        print(f"\n--- TOUS LES JOUEURS ONT PARLÉ : {phase_name.upper()} ---")
        return False

    def display_players_hands(self):
        print("\n--- Mains des Joueurs ---")
        for player in self.players:
            print(f"{player.name}: {player.hand}")
        print("------------------------\n")
