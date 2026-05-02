import sys
from poker.game import PokerGame
from poker.hand_evaluator import HandEvaluator

def clear_screen():
    # Simple print to clear some space, or use OS specific commands
    print("\n" * 50)

def welcome_screen():
    print("=" * 40)
    print("      BIENVENUE SUR POKERSTAR !     ")
    print("=" * 40)
    print("1. Commencer une partie")
    print("2. Quitter")
    print("=" * 40)

def main():
    game = PokerGame()
    
    while True:
        welcome_screen()
        choice = input("Votre choix : ")

        if choice == "1":
            # Demander le nombre de joueurs
            num_players = 0
            while num_players < 2 or num_players > 10:
                try:
                    num_players = int(input("Entrez le nombre de joueurs (2-10) : "))
                    if num_players < 2 or num_players > 10:
                        print("Erreur : Le nombre doit être entre 2 et 10.")
                except ValueError:
                    print("Erreur : Veuillez entrer un nombre valide.")

            # Initialisation du jeu
            game.setup_players(num_players)
            
            # Boucle d'une main
            goto_next_hand = False
            
            # --- PHASE PRE-FLOP ---
            game.deal_preflop()
            if game.play_action_round("Pre-flop"):
                goto_next_hand = True
            
            # --- PHASE FLOP ---
            if not goto_next_hand:
                game.deal_flop()
                game.display_community_cards("Flop")
                if game.play_action_round("Flop"):
                    goto_next_hand = True
            
            # --- PHASE TURN ---
            if not goto_next_hand:
                game.deal_turn()
                game.display_community_cards("Turn")
                if game.play_action_round("Turn"):
                    goto_next_hand = True
            
            # --- PHASE RIVER ---
            if not goto_next_hand:
                game.deal_river()
                game.display_community_cards("River")
                if game.play_action_round("River"):
                    goto_next_hand = True
                else:
                    print("\n" + "="*40)
                    print("   --- SHOWDOWN (FIN DE LA MAIN) ---")
                    print("="*40)
                    print(f"CARTES SUR LA TABLE : {game.community_cards}")
                    print("-" * 40)
                    
                    active_players = game.get_active_players()
                    
                    # Détermination automatique du gagnant
                    winners_info = HandEvaluator.find_winners(active_players, game.community_cards)
                    
                    # Affichage des mains de tout le monde au showdown
                    for player in active_players:
                        h_name, _ = HandEvaluator.get_best_hand(player.hand + game.community_cards)
                        print(f"{player.name} : {player.hand} -> {h_name}")

                    if len(winners_info) == 1:
                        winner, h_name, _ = winners_info[0]
                        print(f"\nGAGNANT : {winner.name} avec {h_name} !")
                        game.award_pot(winner)
                    else:
                        print(f"\nEGALITE entre :")
                        winners_only = []
                        for winner, h_name, _ in winners_info:
                            print(f"- {winner.name} ({h_name})")
                            winners_only.append(winner)
                        game.split_pot(winners_only)
            
            input("\nAppuyez sur Entrée pour continuer...")
            game.clear_screen()

        elif choice == "2":
            print("Merci d'avoir joué ! À bientôt.")
            sys.exit()
        else:
            print("Choix invalide, réessayez.")

if __name__ == "__main__":
    main()
