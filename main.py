import sys
import os.path

from classes import *

'''
(περισσότερες πληροφορίες για το τι κάνει η κάθε κλάση και μέθοδος υπάρχει ξεχωριστά πριν από
κάθε κλάση/μέθοδο).

1.Έχουν υλοποιηθεί οι εξής κλάσεις:
  α. Letter
  β. SakClass
  γ. Player
  δ. Human
  ε. Computer
  ζ. Game

2. Οι κλάσεις Human και Computer, κληρονομούν την κλάση Player μόνο.

3. Οι κλάσεις Human και Computer, χρησιμοποιούν τις μεθόδους
  a. Print_stats
  β. Calculate_points
  γ. Result
  δ. Print_new_letters
  ε. Word_exist

4. Δεν έχει γίνει υπερφόρτωση τελεστών ούτε χρήση decorators

5.Οι αποδεκτές λέξεις αποθηκεύονται σε μια λίστα μέσα στην κλάση SakClass

6. Υλοποιήθηκαν οι αλγόριθμοι min, max και smart.
'''


'''
Εμφάνιση μενού επιλογών πριν ξεκινήσει το παιχνίδι. Ο χρήστης μπορεί να αλλάξει
τον τρόπο με τον οποίο θα παίζει ο υπολογιστής.
'''


def menu():
    print("***** SCRABBLE *****")
    print("--------------------")
    print("1: Σκορ")
    print("2: Ρυθμίσεις")
    print("3: Παιχνίδι")
    print("q: Έξοδος")
    print("--------------------")
    return input("Επιλογή: ")


'''
Εμφάνιση του σκορ των παικτών που έχουν παίξει μέχρι τώρα.
'''


def score():
    if os.path.exists("Score.txt"):
        file = open("Score.txt", encoding='utf-8')
        pos = 0
        score_list = []
        files = file.readlines()
        for line in files:
            line = line.strip()
            temp = line.split('/')
            score_list.append(str(pos + 1) + "." + temp[0] + "-" + temp[1])
            pos += 1
        print("----Όνομα-Πόντοι----")
        for i in range(len(score_list)):
            print(score_list[i])
    else:
        print("Δεν Υπάρχει Κατάταξη Παικτών Ακόμα :(")
    input("Enter Για Συνέχεια\n")


if __name__ == '__main__':
    choice = "scrabble"
    game = Game()

    while True:
        choice = menu()
        if choice == "1":
            score()
        elif choice == "2":
            game.settings()
        elif choice == "3":
            game.run()
        elif choice == "q":
            sys.exit()
        else:
            print("Παρακαλώ Επιλέξτε μία από τις Διαθέσιμες Επιλογές (1,2,3,q)")
