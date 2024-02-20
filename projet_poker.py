from random import*
import sys

class carte(): #Création de la classe carte
    def __init__(self):
        self.valeur = valeur
        self.couleur = couleur
        
    #Méthode pour tirer une carte au hasard    
    def carte_hasard(self, jeu):
        i = randint(0,len(jeu)-1)
        self.valeur = jeu[i][0]
        self.couleur = jeu[i][1]
        jeu.pop(i)
        return self.valeur, self.couleur
    
    #Méthode pour montrer la carte
    def carte_montrer(self):
        return [self.valeur, self.couleur]

class main(): #Création de la classe main
    def __init__(self, carte1, carte2):
        self.carte1 = [carte1.valeur, carte1.couleur]
        self.carte2 = [carte2.valeur, carte2.couleur]
        self.joue = True
        
    #Méthode pour afficher la main d'un joueur
    def afficher_main(self, carte1, carte2):
        return [carte1.valeur +" "+ carte1.couleur,carte2.valeur +" "+ carte2.couleur]

class flop(): #Création de la classe flop
    def __init__(self, carte_1, carte_2, carte_3):
        self.carte_1 = [carte_1.valeur, carte_1.couleur]
        self.carte_2 = [carte_2.valeur, carte_2.couleur]
        self.carte_3 = [carte_3.valeur, carte_3.couleur]

    #Méthode pour montrer le flop 
    def montrer(self, carte_1, carte_2, carte_3):
        return [carte_1.valeur +" "+ carte_1.couleur,carte_2.valeur +" "+ carte_2.couleur,carte_3.valeur +" "+ carte_3.couleur]
        
class turn(): #Création de la classe turn
    def __init__(self, carte_1):
        self.carte_1 = [carte_1.valeur, carte_1.couleur]
        
    #Méthode pour montrer le turn
    def montrer(self, carte_1):
        return [carte_1.valeur +" "+ carte_1.couleur]
    
class river(): #Création de la classe river
    def __init__(self, carte_1):
        self.carte_1 = [carte_1.valeur, carte_1.couleur]
        
    #Méthode pour montrer la river
    def montrer(self, carte_1):
        return [carte_1.valeur +" "+ carte_1.couleur]
    
class joueur(): #Création de la classe joueur
    def __init__(self,carte_1, carte_2,nb):
        self.carte_1 = carte_1
        self.carte_2 = carte_2
        self.argent = 0
        self.main_joueur = main(carte_1,carte_2)
        self.nb = nb
        self.etat = True
        self.action = None
        
    #Méthode pour afficher l'argent d'un joueur    
    def afficher_argent(self):
        return self.argent

    #Méthode pour afficher le numéro d'un joueur   
    def afficher_nb(self):
        return self.nb
        
def def_carte(jeu) : #Définition des cartes
    
    carte1 = carte()
    carte1.carte_hasard(jeu)
    carte2 = carte()
    carte2.carte_hasard(jeu)
    carte3 = carte()
    carte3.carte_hasard(jeu)
    carte4 = carte()
    carte4.carte_hasard(jeu)
    carte5 = carte()
    carte5.carte_hasard(jeu)
    carte6 = carte()
    carte6.carte_hasard(jeu)
    carte7 = carte()
    carte7.carte_hasard(jeu)
    carte8 = carte()
    carte8.carte_hasard(jeu)
    carte9 = carte()
    carte9.carte_hasard(jeu)
    carte10 = carte()
    carte10.carte_hasard(jeu)
    carte11 = carte()
    carte11.carte_hasard(jeu)
    carte12 = carte()
    carte12.carte_hasard(jeu)
    carte13 = carte()
    carte13.carte_hasard(jeu)
    carte14 = carte()
    carte14.carte_hasard(jeu)
    carte15 = carte()
    carte15.carte_hasard(jeu)
    carte16 = carte()
    carte16.carte_hasard(jeu)
    carte17 = carte()
    carte17.carte_hasard(jeu)
    carte18 = carte()
    carte18.carte_hasard(jeu)
    carte19 = carte()
    carte19.carte_hasard(jeu)
    carte20 = carte()
    carte20.carte_hasard(jeu)
    carte21 = carte()
    carte21.carte_hasard(jeu)
    carte22 = carte()
    carte22.carte_hasard(jeu)
    carte23 = carte()
    carte23.carte_hasard(jeu)
    carte24 = carte()
    carte24.carte_hasard(jeu)
    carte25 = carte()
    carte25.carte_hasard(jeu)

    carte_def = [carte1, carte2, carte3, carte4, carte5, carte6, carte7, carte8, carte9, carte10, carte11, carte12, carte13, carte14, carte15, carte16, carte17, carte18, carte19, carte20, carte21, carte22, carte23, carte24, carte25]

    return carte_def

def tout_joueur(carte_def): #Définition des joueurs

    joueur1 = joueur(carte_def[0],carte_def[1],1)
    joueur2 = joueur(carte_def[2],carte_def[3],2)
    joueur3 = joueur(carte_def[4],carte_def[5],3)
    joueur4 = joueur(carte_def[6],carte_def[7],4)
    joueur5 = joueur(carte_def[8],carte_def[9],5)
    joueur6 = joueur(carte_def[10],carte_def[11],6)
    joueur7 = joueur(carte_def[12],carte_def[13],7)
    joueur8 = joueur(carte_def[14],carte_def[15],8)
    joueur9 = joueur(carte_def[16],carte_def[17],9)
    joueur10 = joueur(carte_def[18],carte_def[19],10)
    
    joueur_def = [joueur1,joueur2,joueur3,joueur4,joueur5,joueur6,joueur7,joueur8,joueur9,joueur10]
    
    # Permet d'afficher toutes les mains des joueurs
    # j=0
    # for i in joueur_def :
    #     print(i.main_joueur.afficher_main(carte_def[j],carte_def[j+1]))
    #     j+=2
        
    return joueur_def

def jeu_poker(jeu, carte_def, tout_les_joueurs, flop1, turn1, river1): #Définition du jeu de poker (Initialisation + Lancement du jeu)
    
    # Lancement du jeu et initialisation des variables
    debut = input('Voulez vous commencez ? ')
    somme_argent = 0 
    nombre = 0

    if debut == 'oui' or debut == "Oui" or debut == "OUI":

        #Demande du nombre de joueurs et de la somme d'argent
        while nombre < 2 or nombre > 10 :
            nombre = int(input("Quel est le nombre de joueur (2 à 10 joueurs) ? "))
        while somme_argent < 2000 :
            somme_argent = int(input("Avec quelle somme d'argent jouez vous ? (Minimum 2000₿) : "))
        
        #Création de la liste des joueurs en jeu et initialisation de leur argent
        tout_les_joueurs_jeu = []
        for i in range(nombre):
            tout_les_joueurs[i].argent = somme_argent
            tout_les_joueurs_jeu.append(tout_les_joueurs[i])
            
        #Initialisation des mises et du pot
        p_blinde = (somme_argent // 400)
        g_blinde = (somme_argent // 200)
        pot = p_blinde + g_blinde

        #Début du jeu
        while verif_continuer(tout_les_joueurs_jeu)[0] == True :

            # Définition de l'état et de l'action des joueurs
            for i in tout_les_joueurs_jeu:
                i.etat = True
                i.action = None
            # print (i.etat), print(i.action)
            
            pre_flop(jeu, carte_def, tout_les_joueurs_jeu, pot, flop1, turn1, river1,p_blinde, g_blinde)
                    
    else :
        print("A bientôt !")

def pre_flop(jeu, carte_def, tout_les_joueurs_jeu, pot, flop1, turn1, river1, p_blinde, g_blinde, continuer = True, couche = 0): #Définition de la phase de pré-flop
    
    #Définition des mises
    mise = g_blinde

    #Lancement de la phase de pré-flop
    while continuer == True :   
        nb_tapis = 0
        pot = p_blinde + g_blinde

        #Réinitialisation des actions des joueurs
        for k in tout_les_joueurs_jeu:
            if k.etat == True and k.action == "Suivre" :
                k.action = None

        for i in tout_les_joueurs_jeu:

            #Vérification si tout le monde est tapis
            for j in tout_les_joueurs_jeu:
                if j.etat == "Tapis" :
                    nb_tapis += 1
            if nb_tapis == len(tout_les_joueurs_jeu) +1 :
                continuer = fin_de_partie(carte_def, tout_les_joueurs_jeu, pot)
                break

            # Vérification du nombre restant de joueurs durant une manche
            if fin(tout_les_joueurs_jeu, pot, couche) == True:
                continuer = False
                break

            # Vérification de l'état des joueurs (si couché ou tapis, on passe au suivant)
            if i.etat == False :
                continue
            if i.etat == "Tapis" :
                continue

            # Affichage des informations pour chaque joueur
            print(f"\nJoueur {i.nb} : Vous avez : {i.argent}₿ ")
            print("Le pot est de : ", pot,"₿")
            print("La mise est de : ", mise,"₿")
            print("Vous avez les cartes : ", i.main_joueur.afficher_main(carte_def[(2*i.nb)-2],carte_def[(2*i.nb)-1]),"\n")
            
            # Demande de l'action du joueur
            action = None
            while verif_action(action) != True:
                action = input("Que voulez vous faire ? (Coucher, Suivre, Relancer) : ")

            # print (action)
            # print(verif_coucher(action))
            # print(verif_suivre(action))
            # print(verif_relancer(action))

            #Si le joueur se couche (il ne joue plus durant la manche)
            if verif_coucher(action) == True:
                i.etat = False
                i.action = "Coucher"
                print(f"Joueur {i.nb} vous vous êtes couché ! \n")

                #Si un seul joueur reste, fin de la manche.
                if fin (tout_les_joueurs_jeu, pot, couche) == True  :
                    continuer = False
                    break

            #Si le joueur suit la mise 
            elif verif_suivre(action) == True:

                #Si la valeur de la mise est égale à l'argent du joueur
                if i.argent == mise :
                    i.action = "Suivre"
                    i.etat = "Tapis"
                    print(f"Joueur {i.nb} vous avez suivi tapis !")
                
                else :
                    i.action = "Suivre"
                    print(f"Joueur {i.nb} vous avez suivi !")

                i.argent -= mise
                pot += mise

                #Si tous les joueurs ont suivi, on passe à la phase de flop
                print(tous_suivi(tout_les_joueurs_jeu))
                if tous_suivi(tout_les_joueurs_jeu)[0] == "True" and tous_suivi(tout_les_joueurs_jeu)[1] == "continu" :
                    continuer = jeu_flop(carte_def, tout_les_joueurs_jeu, mise, pot, g_blinde, flop1, river1, turn1, couche)
                elif tous_suivi(tout_les_joueurs_jeu)[0] == "True" and tous_suivi(tout_les_joueurs_jeu)[1] == "fin":
                    continuer = fin_de_partie(carte_def, tout_les_joueurs_jeu, pot)

            #Si le joueur relance la mise
            elif verif_relancer(action) == True:
                relance = -1
                argent_joueur = i.argent
                joueur_sans_relance = tout_les_joueurs_jeu.copy()

                #Vérification de la relance
                # print (verif_relance(relance, mise, argent_joueur))
                while verif_relance(relance, mise, argent_joueur) != True:

                    if mise*2 > i.argent :
                        relance = int(input(f"De combien voulez vous relancer ? (Minimum {i.argent}, Maximum {i.argent}) : "))

                        #Si le joueur fait tapis
                        if relance == i.argent :
                            print(f"Joueur {i.nb} vous avez fait tapis !")
                            i.etat = "Tapis"
                   
                        i.action = "Relancer"
                        print(f"Joueur {i.nb} vous avez relancé de {relance}₿ !")

                        i.argent -= relance
                        pot += relance

                    else :
                        relance = int(input(f"De combien voulez vous relancer ? (Minimum {mise*2}, Maximum {i.argent}) : "))

                        #Si le joueur fait tapis
                        if relance == i.argent :
                            print(f"Joueur {i.nb} vous avez fait tapis !")
                            i.etat = "Tapis"
                   
                        i.action = "Relancer"
                        print(f"Joueur {i.nb} vous avez relancé de {relance}₿ !")

                        i.argent -= relance
                        pot += relance

                joueur_a_enlever = joueur_sans_relance.index(i)
                joueur_enleve = joueur_sans_relance.pop(joueur_a_enlever)
                joueur_sans_relance.insert(0, joueur_enleve)
                for j in range(1, len(joueur_sans_relance)):
                    # print (joueur_sans_relance [j].nb, joueur_sans_relance[j].etat, joueur_sans_relance[j].action)
                    joueur_sans_relance[j].etat = True
                    joueur_sans_relance[j].action = None
                mise = relance
        
        # Redéfinition des cartes après chaque manche
        valeur=["2","3","10","Valet","Dame","Roi","AS","6","7","4","5","8","9"]
        couleur=["♠","♥","♣","♦"]
        jeu=[]
        [jeu.append([i,j]) for i in valeur for j in couleur]

        carte_def = def_carte(jeu)
        for i in range(len(tout_les_joueurs_jeu)):
            tout_les_joueurs_jeu[i].main_joueur = main(carte_def[(2*i)], carte_def[(2*i)+1])
            tout_les_joueurs_jeu[i].carte1 = carte_def[(2*i)]
            tout_les_joueurs_jeu[i].carte2 = carte_def[(2*i)+1]
            print(tout_les_joueurs_jeu[i].main_joueur.afficher_main(carte_def[(2*i)], carte_def[(2*i)+1]))

        #Création du flop, du turn et de la river
        flop1 = flop(carte_def[20], carte_def[21], carte_def[22])
        # print("Le flop est : ", flop.montrer(carte_def[20], carte_def[21], carte_def[22]))
        turn1 = turn(carte_def[23])
        # print("Le turn est : ", turn.montrer(carte_def[23]))
        river1 = river(carte_def[24])
        # print("La river est : ", river.montrer(carte_def[24]))

    return tout_les_joueurs_jeu, pot

def jeu_flop(carte_def, tout_les_joueurs_jeu, mise, pot, g_blinde, flop1, turn1, river1, couche): #Définition de la phase de flop

    mise = g_blinde
    nb_tapis = 0

    #Réinitialisation des actions des joueurs
    for k in tout_les_joueurs_jeu:
        if k.etat == True and k.action == "Suivre" :
            k.action = None

    #Lancement de la phase de flop
    for i in tout_les_joueurs_jeu:

        #Vérification si tout le monde est tapis
        # print(tout_les_joueurs_jeu)
        for j in tout_les_joueurs_jeu:
            if j.etat == "Tapis" :
                nb_tapis += 1
        if nb_tapis == len(tout_les_joueurs_jeu) +1 :
            continuames = fin_de_partie(carte_def, tout_les_joueurs_jeu, pot)
            if continuames == False :
                return False
            return True

        # Vérification du nombre restant de joueurs durant une manche
        if fin(tout_les_joueurs_jeu, pot, couche) == True:
            return False

        #Vérification de l'état des joueurs (si couché ou tapis, on passe au suivant)
        if i.etat == False :
            continue
        if i.action == "Tapis" :
            continue
        
        #Affichage des informations pour chaque joueur
        print(f"\nJoueur {i.nb} : Vous avez : {i.argent}₿ ")
        print("Le pot est de : ", pot,"₿")
        print("La mise est de : ", mise,"₿")
        print("Le flop est : ", flop1.montrer(carte_def[20], carte_def[21], carte_def[22]))
        print("Vous avez les cartes : ", i.main_joueur.afficher_main(carte_def[(2*i.nb)-2],carte_def[(2*i.nb)-1]),"\n")

        #Demande de l'action du joueur
        action = None
        while verif_action(action) != True:
            action = input("Que voulez vous faire ? (Coucher, Suivre, Relancer) : ")
        
        # print(action)
        # print(verif_coucher(action))  
        # print(verif_suivre(action))
        # print(verif_relancer(action))
            
        #Si le joueur se couche (il ne joue plus durant la manche)
        if verif_coucher(action) == True:
            i.etat = False
            i.action = "Coucher"
            print(f"Joueur {i.nb} vous vous êtes couché ! \n")

            #Si un seul joueur reste, fin de la manche.
            if fin (tout_les_joueurs_jeu,pot) == True  :
                return False

        #Si le joueur suit la mise
        elif verif_suivre(action) == True:

            #Si la valeur de la mise est égale à l'argent du joueur
            if i.argent == mise :
                i.action = "Suivre"
                i.etat = "Tapis"
                print(f"Joueur {i.nb} vous avez suivi tapis !")

            else :
                i.action = "Suivre"
                print(f"Joueur {i.nb} vous avez suivi !")

            i.argent -= mise
            pot += mise

            #Si tous les joueurs ont suivi, on passe à la phase de turn
            # print (tous_suivi(tout_les_joueurs_jeu))
            # print (i.etat, i.action)
            if tous_suivi(tout_les_joueurs_jeu)[0] == "True" and tous_suivi(tout_les_joueurs_jeu)[1] == "continu":
                continuons = jeu_turn(carte_def, tout_les_joueurs_jeu, mise, pot, g_blinde, turn1, river1, couche)
                if continuons == False :
                    return False
            elif tous_suivi(tout_les_joueurs_jeu)[0] == "True" and tous_suivi(tout_les_joueurs_jeu)[1] == "fin":
                continuons = fin_de_partie(carte_def, tout_les_joueurs_jeu, pot)
                if continuons == False :
                    return False

        #Si le joueur relance la mise
        elif verif_relancer(action) == True:
            relance = -1
            argent_joueur = i.argent
            joueur_sans_relance = tout_les_joueurs_jeu

            #Vérification de la relance
            while verif_relance(relance, mise, argent_joueur) != True:

                if mise*2 > i.argent :
                    relance = int(input(f"De combien voulez vous relancer ? (Minimum {i.argent}, Maximum {i.argent}) : "))

                    #Si le joueur fait tapis
                    if relance == i.argent :
                        print(f"Joueur {i.nb} vous avez fait tapis !")
                        i.etat = "Tapis"
               
                    i.action = "Relancer"
                    print(f"Joueur {i.nb} vous avez relancé de {relance}₿ !")

                    i.argent -= relance
                    pot += relance

                else :
                    relance = int(input(f"De combien voulez vous relancer ? (Minimum {mise*2}, Maximum {i.argent}) : "))

                    #Si le joueur fait tapis
                    if relance == i.argent :
                        print(f"Joueur {i.nb} vous avez fait tapis !")
                        i.etat = "Tapis"
                   
                    i.action = "Relancer"
                    print(f"Joueur {i.nb} vous avez relancé de {relance}₿ !")

                    i.argent -= relance
                    pot += relance

            joueur_a_enlever = joueur_sans_relance.index(i)
            joueur_enleve = joueur_sans_relance.pop(joueur_a_enlever)
            joueur_sans_relance.insert(0, joueur_enleve)
            for j in range(1, len(joueur_sans_relance)):
                # print (joueur_sans_relance [j].nb, joueur_sans_relance[j].etat, joueur_sans_relance[j].action)
                joueur_sans_relance[j].etat = True
                joueur_sans_relance[j].action = None
            mise = relance

    return True

def jeu_turn(carte_def, tout_les_joueurs_jeu, mise, pot, g_blinde, turn1, river1, couche): #Définition de la phase de turn

    mise = g_blinde
    nb_tapis = 0

    #Réinitialisation des actions des joueurs
    for k in tout_les_joueurs_jeu:
        if k.etat == True and k.action == "Suivre" :
            k.action = None

    #Lancement de la phase de turn
    for i in tout_les_joueurs_jeu:

        #Vérification si tout le monde est tapis
        for j in tout_les_joueurs_jeu:
            if j.etat == "Tapis" :
                nb_tapis += 1
        if nb_tapis == len(tout_les_joueurs_jeu) +1 :
            continuates = fin_de_partie(carte_def, tout_les_joueurs_jeu, pot)
            if continuates == False :  
                return False
            return True

        # Vérification du nombre restant de joueurs durant une manche
        if fin(tout_les_joueurs_jeu, pot, couche) == True:
            return False

        #Vérification de l'état des joueurs (si couché ou tapis, on passe au suivant)
        if i.etat == False :
            continue
        if i.action == "Tapis" :
            continue
    
        #Affichage des informations pour chaque joueur
        print(f"\nJoueur {i.nb} : Vous avez : {i.argent}₿ ")
        print("Le pot est de : ", pot,"₿")
        print("La mise est de : ", mise,"₿")
        print("Le turn est : ", flop1.montrer(carte_def[20], carte_def[21], carte_def[22]), turn1.montrer(carte_def[23]))
        print("Vous avez les cartes : ", i.main_joueur.afficher_main(carte_def[(2*i.nb)-2],carte_def[(2*i.nb)-1]),"\n")
            
        #Demande de l'action du joueur
        action = None
        while verif_action(action) != True:
            action = input("Que voulez vous faire ? (Coucher, Suivre, Relancer) : ")
    
        # Si le joueur se couche (il ne joue plus durant la manche)
        if verif_coucher(action) == True:
            i.etat = False
            i.action = "Coucher"
            print(f"Joueur {i.nb} vous vous êtes couché ! \n")

            # Si un seul joueur reste, fin de la manche.
            if fin (tout_les_joueurs_jeu,pot) == True  :
                return False
    
        # Si le joueur suit la mise
        elif verif_suivre(action) == True:

            #Si la valeur de la mise est égale à l'argent du joueur
            if i.argent == mise :
                i.action = "Suivre"
                i.etat = "Tapis"
                print(f"Joueur {i.nb} vous avez suivi tapis !")

            else :
                i.action = "Suivre"
                print(f"Joueur {i.nb} vous avez suivi !")
    
            i.argent -= g_blinde
            pot += g_blinde

            # Si tous les joueurs ont suivi, on passe à la phase de river
            if tous_suivi(tout_les_joueurs_jeu)[0] == "True" and tous_suivi(tout_les_joueurs_jeu)[1] == "continu":
                # print(tous_suivi(tout_les_joueurs_jeu))
                continuez = jeu_river(carte_def, tout_les_joueurs_jeu, mise, pot, g_blinde, river1, couche)
                if continuez == False :
                    return False
            elif tous_suivi(tout_les_joueurs_jeu)[0] == "True" and tous_suivi(tout_les_joueurs_jeu)[1] == "fin":
                continuez = fin_de_partie(carte_def, tout_les_joueurs_jeu, pot)
                if continuez == False :
                    return False

        # Si le joueur relance la mise
        elif verif_relancer(action) == True:
            relance = -1
            argent_joueur = i.argent
            joueur_sans_relance = tout_les_joueurs_jeu

            #Vérification de la relance
            while verif_relance(relance, mise, argent_joueur) != True:

                if mise*2 > i.argent :
                    relance = int(input(f"De combien voulez vous relancer ? (Minimum {i.argent}, Maximum {i.argent}) : "))

                    #Si le joueur fait tapis
                    if relance == i.argent :
                        print(f"Joueur {i.nb} vous avez fait tapis !")
                        i.etat = "Tapis"
               
                    i.action = "Relancer"
                    print(f"Joueur {i.nb} vous avez relancé de {relance}₿ !")

                    i.argent -= relance
                    pot += relance

                else :
                    relance = int(input(f"De combien voulez vous relancer ? (Minimum {mise*2}, Maximum {i.argent}) : "))

                    #Si le joueur fait tapis
                    if relance == i.argent :
                        print(f"Joueur {i.nb} vous avez fait tapis !")
                        i.etat = "Tapis"
                   
                    i.action = "Relancer"
                    print(f"Joueur {i.nb} vous avez relancé de {relance}₿ !")

                    i.argent -= relance
                    pot += relance

            joueur_a_enlever = joueur_sans_relance.index(i)
            joueur_enleve = joueur_sans_relance.pop(joueur_a_enlever)
            joueur_sans_relance.insert(0, joueur_enleve)
            for j in range(1, len(joueur_sans_relance)):
                # print (joueur_sans_relance [j].nb, joueur_sans_relance[j].etat, joueur_sans_relance[j].action)
                joueur_sans_relance[j].etat = True
                joueur_sans_relance[j].action = None
            mise = relance

    return True

def jeu_river(carte_def, tout_les_joueurs_jeu, mise, pot, g_blinde, river1, couche): #Définition de la phase de river

    mise = g_blinde
    nb_tapis = 0

    #Réinitialisation des actions des joueurs
    for k in tout_les_joueurs_jeu:
        if k.etat == True and k.action == "Suivre" :
            k.action = None

    #Lancement de la phase de river
    for i in tout_les_joueurs_jeu:

        #Vérification si tout le monde est tapis
        for j in tout_les_joueurs_jeu:
            if j.etat == "Tapis" :
                nb_tapis += 1
        if nb_tapis == len(tout_les_joueurs_jeu) +1 :
            continuerent = fin_de_partie(carte_def, tout_les_joueurs_jeu, pot)
            if continuerent == False :
                return False
            return True

        # Vérification du nombre restant de joueurs durant une manche
        if fin(tout_les_joueurs_jeu, pot, couche) == True:
            return False

        #Vérification de l'état des joueurs (si couché ou tapis, on passe au suivant)
        if i.etat == False :
            continue        
        if i.action == "Tapis" :
            continue    

        #Affichage des informations pour chaque joueur
        print(f"\nJoueur {i.nb} : Vous avez : {i.argent}₿ ")
        print("Le pot est de : ", pot,"₿")
        print("La mise est de : ", mise,"₿")
        print("La river est : ", flop1.montrer(carte_def[20], carte_def[21], carte_def[22]), turn1.montrer(carte_def[23]), river1.montrer(carte_def[24]))
        print("Vous avez les cartes : ", i.main_joueur.afficher_main(carte_def[(2*i.nb)-2],carte_def[(2*i.nb)-1]),"\n")

        #Demande de l'action du joueur    
        action = None
        while verif_action(action) != True:
            action = input("Que voulez vous faire ? (Coucher, Suivre, Relancer) : ")
        
        #Si le joueur se couche (il ne joue plus durant la manche)
        if verif_coucher(action) == True:
            i.etat = False
            i.action = "Coucher"
            print(f"Joueur {i.nb} vous vous êtes couché ! \n")
            
            #Si un seul joueur reste, fin de la manche.
            if fin (tout_les_joueurs_jeu, pot) == True  :
                return False
        
        #Si le joueur suit la mise
        elif verif_suivre(action) == True  :

            #Si la valeur de la mise est égale à l'argent du joueur
            if i.argent == mise :
                i.action = "Suivre"
                i.etat = "Tapis"
                print(f"Joueur {i.nb} vous avez suivi tapis !")
            else :
                i.action = "Suivre"
                print(f"Joueur {i.nb} vous avez suivi !")

            i.argent -= g_blinde
            pot += g_blinde

            #Si tous les joueurs ont suivi, on passe à la fin de la manche
            if tous_suivi(tout_les_joueurs_jeu)[0] == "True" and tous_suivi(tout_les_joueurs_jeu)[1] == "continu":
                # print(tous_suivi(tout_les_joueurs_jeu))
                continuent = fin_de_partie(carte_def, tout_les_joueurs_jeu, pot)
                if continuent == False :
                    return False
            elif tous_suivi(tout_les_joueurs_jeu)[0] == "True" and tous_suivi(tout_les_joueurs_jeu)[1] == "fin":
                continuent = fin_de_partie(carte_def, tout_les_joueurs_jeu, pot)
                if continuent == False :
                    return False

        #Si le joueur relance la mise
        elif verif_relancer(action) == True:
            relance = -1
            argent_joueur = i.argent
            joueur_sans_relance = tout_les_joueurs_jeu

            #Vérification de la relance
            while verif_relance(relance, mise, argent_joueur) != True:

                if mise*2 > i.argent :
                    relance = int(input(f"De combien voulez vous relancer ? (Minimum {i.argent}, Maximum {i.argent}) : "))

                    #Si le joueur fait tapis
                    if relance == i.argent :
                        print(f"Joueur {i.nb} vous avez fait tapis !")
                        i.etat = "Tapis"
               
                    i.action = "Relancer"
                    print(f"Joueur {i.nb} vous avez relancé de {relance}₿ !")

                    i.argent -= relance
                    pot += relance

                else :
                    relance = int(input(f"De combien voulez vous relancer ? (Minimum {mise*2}, Maximum {i.argent}) : "))

                    #Si le joueur fait tapis
                    if relance == i.argent :
                        print(f"Joueur {i.nb} vous avez fait tapis !")
                        i.etat = "Tapis"
                   
                    i.action = "Relancer"
                    print(f"Joueur {i.nb} vous avez relancé de {relance}₿ !")

                    i.argent -= relance
                    pot += relance

            joueur_a_enlever = joueur_sans_relance.index(i)
            joueur_enleve = joueur_sans_relance.pop(joueur_a_enlever)
            joueur_sans_relance.insert(0, joueur_enleve)
            for j in range(1, len(joueur_sans_relance)):
                # print (joueur_sans_relance [j].nb, joueur_sans_relance[j].etat, joueur_sans_relance[j].action)
                joueur_sans_relance[j].etat = True
                joueur_sans_relance[j].action = None
            mise = relance

    return True

def fin_de_partie(carte_def,tout_les_joueurs_jeu, pot): #Définition de la fin de la manche
    
    #Définition du gagnant
    print("Les cartes sont : ", flop1.montrer(carte_def[20], carte_def[21], carte_def[22]), turn1.montrer(carte_def[23]), river1.montrer(carte_def[24]))
    for j in tout_les_joueurs_jeu:
        print(f"Joueur {j.nb} a les cartes : ", j.main_joueur.afficher_main(carte_def[(2*j.nb)-2],carte_def[(2*j.nb)-1]))
    gagnant = int(input("Quel est le numéro du gagnant ? "))
    print(f"Joueur {gagnant} vous avez gagné {pot}!")
    tout_les_joueurs_jeu[gagnant-1].argent += pot

    return True

def verif_action(action): #Vérification que l'action que le joeueur veut exécuter est correcte
    if action == "Coucher" or action == "coucher" or action == "COUCHER" or action == "Suivre" or action == "suivre" or action == "SUIVRE" or action == "Relancer" or action == "relancer" or action == "RELANCER" :
        return True

def verif_coucher(action):  #Vérification de l'action "Coucher"
    if action == "Coucher" or action == "coucher" or action == "COUCHER" :
        return True
    else : 
        return False
    
def verif_suivre(action): #Vérification de l'action "Suivre"
    if action == "Suivre" or action == "suivre" or action == "SUIVRE" :
        return True
    else : 
        return False

def verif_relancer(action): #Vérification de l'action "Relancer"
    if action == "Relancer" or action == "relancer" or action == "RELANCER" :
        return True
    else : 
        return False

def verif_relance(relance, mise, argent): #Vérification de la valeur de la relance
    # print (relance, mise, argent)

    if mise*2 > argent :
        if relance == argent :
            return True
        else :
            return False   

    if relance >= mise*2 and relance <= argent :
        return True
    else : 
        return False

def verif_continuer(tout_les_joueurs_jeu): #Vérifie que tous les joueurs aient encore de l'argent

    continuer = True
    joueur_perdant = -1
    #print(tout_les_joueurs_jeu)
    for i in tout_les_joueurs_jeu:
        #print(tout_les_joueurs_jeu[i].argent)
        if i.argent == 0 or i.argent < 0 :
            joueur_perdant = i
            continuer = False
            break
        
    return [continuer,joueur_perdant]

def fin(tout_les_joueurs_jeu, pot, couche = 0): #Vérifie que tous les joueurs aient suivi ou se soient couchés

    for i in tout_les_joueurs_jeu :
        if i.etat == False :
            couche += 1
    if couche == len(tout_les_joueurs_jeu) - 1:
        print("La partie est terminé !")
        for k in tout_les_joueurs_jeu :
            if k.etat == True :
                k.argent += pot
                print(f"Joueur {k.nb} vous avez gagné !")
                print("C'est parti pour la prochaine manche !")
        return True
    else :
        return False

def tous_suivi(tout_les_joueurs_jeu): #Vérifie que tous les joueurs aient suivi la mise

    joueur_jeu_sans_relance = tout_les_joueurs_jeu.copy()
    nb_tapis = 0

    for i in range(len(tout_les_joueurs_jeu)):
        print(tout_les_joueurs_jeu[i].etat, tout_les_joueurs_jeu[i].action)

        # Si un joueur est couché, on passe au suivant
        if tout_les_joueurs_jeu[i].etat == False and tout_les_joueurs_jeu[i].action == "Coucher" :
            continue

        elif tout_les_joueurs_jeu[i].etat == "Tapis" and tout_les_joueurs_jeu[i].action == "Suivre" :
            continue

        elif tout_les_joueurs_jeu[i].etat == True and tout_les_joueurs_jeu[i].action == "Suivre" :
            continue

        elif tout_les_joueurs_jeu[i].action == None :
            return "False"
        
        # Si un joueur a relancé, on le retire de la liste et on regarde les deux autres joueurs
        elif tout_les_joueurs_jeu[i].action == "Relancer" :
            if tout_les_joueurs_jeu[i].etat == "Tapis" :
                nb_tapis += 1
            joueur_jeu_sans_relance.pop(i)
            for i in range(len(joueur_jeu_sans_relance)):
                print(joueur_jeu_sans_relance[i].nb, joueur_jeu_sans_relance[i].etat, joueur_jeu_sans_relance[i].action)
                if joueur_jeu_sans_relance[i].etat == False and joueur_jeu_sans_relance[i].action == "Coucher" :
                    continue
                elif joueur_jeu_sans_relance[i].action != "Suivre" :
                    return ["False", "continu"]
                elif joueur_jeu_sans_relance[i].etat == "Tapis" and joueur_jeu_sans_relance[i].action == "Suivre" :
                    nb_tapis += 1
            if nb_tapis < len(joueur_jeu_sans_relance) -1:
                return ["True", "continu"]
            else : 
                return ["False", "fin"]

    return ["True", "continu"]

#Création du jeu de carte
valeur=["2","3","10","Valet","Dame","Roi","AS","6","7","4","5","8","9"]
couleur=["♠","♥","♣","♦"]
jeu=[]
[jeu.append([i,j]) for i in valeur for j in couleur]
carte_def = def_carte(jeu)
tout_les_joueurs = tout_joueur(carte_def)

#Création du flop, du turn et de la river
flop1 = flop(carte_def[20], carte_def[21], carte_def[22])
# print("Le flop est : ", flop.montrer(carte_def[20], carte_def[21], carte_def[22]))
turn1 = turn(carte_def[23])
# print("Le turn est : ", turn.montrer(carte_def[23]))
river1 = river(carte_def[24])
# print("La river est : ", river.montrer(carte_def[24]))

#Lancement du jeu
jeu_poker(jeu, carte_def, tout_les_joueurs, flop1, turn1, river1)