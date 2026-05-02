class HandEvaluator:
    RANK_VALUES = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "J": 11, "Q": 12, "K": 13, "A": 14
    }

    @staticmethod
    def get_best_hand(cards):
        """
        Prend une liste de 7 cartes (ou plus) et retourne un tuple:
        (Nom de la combinaison, Score de comparaison)
        Score de comparaison est un tuple d'entiers pour permettre la comparaison directe.
        """
        cards = sorted(cards, key=lambda c: HandEvaluator.RANK_VALUES[c.rank], reverse=True)
        
        # 1. Quinte Flush
        res = HandEvaluator._check_straight_flush(cards)
        if res: return "Quinte Flush", res

        # 2. Carré
        res = HandEvaluator._check_four_of_a_kind(cards)
        if res: return "Carré", res

        # 3. Full
        res = HandEvaluator._check_full_house(cards)
        if res: return "Full", res

        # 4. Couleur
        res = HandEvaluator._check_flush(cards)
        if res: return "Couleur", res

        # 5. Quinte
        res = HandEvaluator._check_straight(cards)
        if res: return "Quinte", res

        # 6. Brelan
        res = HandEvaluator._check_three_of_a_kind(cards)
        if res: return "Brelan", res

        # 7. Double Paire
        res = HandEvaluator._check_two_pair(cards)
        if res: return "Double Paire", res

        # 8. Paire
        res = HandEvaluator._check_one_pair(cards)
        if res: return "Paire", res

        # 9. Carte Haute
        return "Carte Haute", HandEvaluator._check_high_card(cards)

    @staticmethod
    def _check_straight_flush(cards):
        suits = [c.suit for c in cards]
        for suit in set(suits):
            if suits.count(suit) >= 5:
                flush_cards = [c for c in cards if c.suit == suit]
                res = HandEvaluator._check_straight(flush_cards)
                if res: return (9, res[1]) 
        return None

    @staticmethod
    def _check_four_of_a_kind(cards):
        ranks = [c.rank for c in cards]
        for rank in set(ranks):
            if ranks.count(rank) == 4:
                val = HandEvaluator.RANK_VALUES[rank]
                kickers = [HandEvaluator.RANK_VALUES[c.rank] for c in cards if c.rank != rank]
                return (8, val, kickers[0])
        return None

    @staticmethod
    def _check_full_house(cards):
        ranks = [c.rank for c in cards]
        threes = []
        pairs = []
        
        for rank in set(ranks):
            count = ranks.count(rank)
            val = HandEvaluator.RANK_VALUES[rank]
            if count >= 3:
                threes.append(val)
            if count >= 2:
                pairs.append(val)
        
        if threes:
            best_three = max(threes)
            remaining_pairs = [p for p in pairs if p != best_three]
            if remaining_pairs:
                return (7, best_three, max(remaining_pairs))
        return None

    @staticmethod
    def _check_flush(cards):
        suits = [c.suit for c in cards]
        for suit in set(suits):
            if suits.count(suit) >= 5:
                vals = sorted([HandEvaluator.RANK_VALUES[c.rank] for c in cards if c.suit == suit], reverse=True)
                return (6, vals[0], vals[1], vals[2], vals[3], vals[4])
        return None

    @staticmethod
    def _check_straight(cards):
        values = sorted(list(set([HandEvaluator.RANK_VALUES[c.rank] for c in cards])), reverse=True)
        if 14 in values:
            values.append(1)
        
        for i in range(len(values) - 4):
            if values[i] - values[i+4] == 4:
                return (5, values[i])
        return None

    @staticmethod
    def _check_three_of_a_kind(cards):
        ranks = [c.rank for c in cards]
        for rank in sorted(set(ranks), key=lambda r: HandEvaluator.RANK_VALUES[r], reverse=True):
            if ranks.count(rank) >= 3:
                val = HandEvaluator.RANK_VALUES[rank]
                kickers = sorted([HandEvaluator.RANK_VALUES[c.rank] for c in cards if c.rank != rank], reverse=True)
                return (4, val, kickers[0], kickers[1])
        return None

    @staticmethod
    def _check_two_pair(cards):
        ranks = [c.rank for c in cards]
        pairs = []
        for rank in set(ranks):
            if ranks.count(rank) >= 2:
                pairs.append(HandEvaluator.RANK_VALUES[rank])
        
        if len(pairs) >= 2:
            pairs = sorted(pairs, reverse=True)
            best_pairs = pairs[:2]
            kickers = sorted([HandEvaluator.RANK_VALUES[c.rank] for c in cards if HandEvaluator.RANK_VALUES[c.rank] not in best_pairs], reverse=True)
            return (3, best_pairs[0], best_pairs[1], kickers[0])
        return None

    @staticmethod
    def _check_one_pair(cards):
        ranks = [c.rank for c in cards]
        for rank in sorted(set(ranks), key=lambda r: HandEvaluator.RANK_VALUES[r], reverse=True):
            if ranks.count(rank) >= 2:
                val = HandEvaluator.RANK_VALUES[rank]
                kickers = sorted([HandEvaluator.RANK_VALUES[c.rank] for c in cards if HandEvaluator.RANK_VALUES[c.rank] != val], reverse=True)
                return (2, val, kickers[0], kickers[1], kickers[2])
        return None

    @staticmethod
    def _check_high_card(cards):
        vals = sorted([HandEvaluator.RANK_VALUES[c.rank] for c in cards], reverse=True)
        return (1, vals[0], vals[1], vals[2], vals[3], vals[4])

    @staticmethod
    def compare_hands(score1, score2):
        """
        Compare deux scores (tuples d'entiers).
        Retourne 1 si score1 gagne, 2 si score2 gagne, 0 si égalité.
        """
        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0

    @staticmethod
    def find_winners(players, community_cards):
        best_players = []
        best_score = None

        for player in players:
            full_hand = player.hand + community_cards
            hand_name, score = HandEvaluator.get_best_hand(full_hand)
            
            if not best_players:
                best_players = [(player, hand_name, score)]
                best_score = score
            else:
                comparison = HandEvaluator.compare_hands(score, best_score)
                if comparison == 1:
                    best_players = [(player, hand_name, score)]
                    best_score = score
                elif comparison == 0:
                    best_players.append((player, hand_name, score))
        
        return best_players
