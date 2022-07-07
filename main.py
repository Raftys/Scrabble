import sys
import os.path

from classes import *

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
