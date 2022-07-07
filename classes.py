import random
import unicodedata
import codecs

size = 24

'''
Η κλάση Letter, κρατάει τα δεδομένα για κάθε γράμμα
'''
class Letter:
    def __init__(self):
        self.letter = None
        self.count = 0
        self.points = 0


'''
Η κλάση SakClass, υλοποιεί το σακουλάκι με τα γράμματα καθώς και τις μεθόδους
που πρόκειται να χρειαστούμε για αυτό.
'''
class SakClass:
    def __init__(self):
        self.count_letters = 104
        self.letters = []

    '''
    Διαβάζω όλα τα στοιχεία για όλα τα γράμματα του ελληνικού αλφαβήτου, 
    μέσα από ένα αρχείο κειμένου. Δηλάδη, το γράμμα, τις φορές που θα 
    υπάρχει μέσα στο σακουλάκι και τους πόντους που δίνει. 
    '''
    def set_letters(self):
        file = open("Letters.txt", encoding='utf-8')
        for line in file:
            letter = Letter()
            temp = line.split(", ")
            letter.letter = temp[0]
            letter.count = int(temp[1])
            letter.points = int(temp[2])
            self.letters.append(letter)
        file.close()

    '''
    Με την χρήση της μεθόδου αυτής, επιστρέφονται τα γράμματα του παίκτη στο σακουλάκι.     
    '''
    def return_letters(self, return_list):
        for i in range(len(return_list)):
            for j in range(size):
                if return_list[0] == self.letters[j].letter:
                    self.letters[j].count += 1
                    self.count_letters += 1
                    break

    '''
    Αυτή η μέθοδος, δίνει Ν γράμματα στον παίκτη.
    '''
    def get_letters(self, n):
        temp_list = []
        for i in range(n):
            letter = self.random_letter()
            if letter != 0:
                temp_list.append(letter)
        return temp_list

    '''
    Επιστρέφει ένα τυχαίο γράμμα από το σακουλάκι. Αφού πρώτα ελέγξει αν
    υπάρχει. Ενώ ταυτόχρονα το αφαιρεί από το σακουλάκι 
    '''
    def random_letter(self):
        string = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
        while self.count_letters > 0:
            random_letter = random.choice(string)
            pos: int = self.get_pos(random_letter)
            if self.letters[pos].count > 0:
                self.letters[pos].count -= 1
                self.count_letters -= 1
                return self.letters[pos].letter
        return 0

    def get_pos(self, letter):
        for i in range(size):
            if letter == self.letters[i].letter:
                return i


'''
Η κλάση Player, υλοποιεί κάποιες βασικές μεθόδους που πρόκειται να χρειαστούν οι
παίκτες. Καθώς κρατάει και στοιχεία για αυτούς. Όπως το όνομα, τα γράμματα που διαθέτει
και το score του.
'''
class Player:

    def __init__(self):
        self.name = ""
        self.list = []
        self.points = 0
        self.word = ""

    '''
    Εκτυπώνονται τα γράμματα και οι πόντοι για το κάθε γράμμα, που διαθέτει ο παίκτης 
    (άνθρωπος ή υπολογιστής).
    '''
    def print_letters(self, sak):
        for i in range(len(self.list)):
            pos = sak.get_pos(self.list[i])
            if i == len(self.list) - 1:
                print(self.list[i], "-", sak.letters[pos].points, end=' ')
            else:
                print(self.list[i], "-", sak.letters[pos].points, ",", end=' ')

    '''
    Εκτυπώνεται το όνομα του παίκτη ο οποίος παίζει, ενώ ταυτόχρονα και το score του αλλά
    και τα γράμματα που διαθέτει.
    '''
    def print_stats(self, sak):
        print("*******************************************************")
        print("     *** Παίκτης:", self.name, "*** Σκορ:", self.points)
        print("     >>> Γράμματα:", end=' ')
        self.print_letters(sak)

    '''
    Υπολογισμός των πόντων της λέξης της οποίας έχει σχηματίσει ο παίκτης.
    '''
    def calculate_points(self, sak):
        p = 0
        for i in range(len(self.word)):
            for j in range(len(sak.letters)):
                if self.word[i] == sak.letters[j].letter:
                    p += sak.letters[j].points
        return p

    '''
    Εμφάνιση αποτελεσμάτων, πόντων της λέξης και συνολικοί πόντοι.
    '''
    def result(self, sak):
        p = self.calculate_points(sak)
        self.points += p
        print("Αποδεκτή Λέξη:", self.word, "- Βαθμοί:", p, "- Σκορ:", self.points)
        self.remove_letters_from_list()

    '''
    Εκτύπωση νέων γραμμάτων.
    '''
    def print_new_letters(self, sak):
        print("Καινούργια γράμματα για", self.name, ":", end=' ')
        self.print_letters(sak)
        print("\n*******************************************************")
        input("Enter για Συνέχεια")

    '''
    αφαίρεση γραμμάτων που έχει χρησιμοποιήσει ο παίκτης από την λίστα με τα 
    διαθέσιμα γράμματα.
    '''
    def remove_letters_from_list(self):
        for i in range(len(self.word)):
            for j in range(len(self.list)):
                if self.word[i] == self.list[j]:
                    self.list.remove(self.list[j])
                    break

    '''
    Προσθήκη καινούργιων γραμμάτων στην λίστα με τα διαθέσιμα γράμματα, αφού 
    παίξει ο παίκτης.
    '''
    def new_letters(self, sak):
        if self.word == "Π":
            if sak.count_letters > 7:
                sak.return_letters(self.list)
                letters = 7
                self.list = []
            else:
                temp_list = sak.get_letters(sak.count_letters)
                sak.return_letters(self.list)
                self.list = temp_list
                letters = 7 - len(self.list)
        else:
            letters = len(self.word)
        temp_list = sak.get_letters(letters)
        self.list += temp_list

    '''
    έλεγχος αν η λέξη είναι αποδεκτή
    '''
    def word_exist(self):
        self.word = self.word
        return True


'''
Η κλάση Human, αποτελεί προέκταση της Player. Υλοποιεί κάποιες βασικές μεθόδους που 
πρόκειται να χρειαστεί ο άνθρπωπος-παίκτης.
'''
class Human(Player):

    def __init__(self):
        super().__init__()

    '''
    ελέγχει αν η λέξη που έδωσε ο άνθρωπος αποτελείται μόνο από γράμματα που
    διαθέτει στα χέρια του.
    '''
    def check(self):
        temp = []
        for i in range(len(self.list)):
            temp.append(self.list[i])
        for j in range(len(self.word)):
            boolean = False
            for i in range(len(temp)):
                if self.word[j] == temp[i]:
                    temp.remove(temp[i])
                    boolean = True
                    break
            if not boolean:
                return False
        return True

    '''
    Ο τρόπος με τον οποίο παίζει ο ανθρωπος. Αρχικά εκτυπώνεται το όνομα και το σκόρ του.
    Στην συνέχεια εκτυπώνονται τα διαθέσιμα γράμματα και ο παίκτης δίνει την λέξη με την 
    οποία θέλει να παίξει. Μπορεί να πληκτρολογίση "Π" για να πάει πάσο.
    '''
    def play(self, sak):
        while True:
            self.print_stats(sak)
            self.word = input("\n\n     ΛΕΞΗ: ")
            self.word = unicodedata.normalize('NFD', self.word).upper().translate(
                {ord('\N{COMBINING ACUTE ACCENT}'): None})
            if self.word == "Π" or self.word == " ":
                self.word = "Π"
                print("Pass")
                break
            elif self.check():
                break
            else:
                print("Χρησιμοποίησε μόνο τα γράμματα που διαθέτεις!")
        if self.word != "Π":
            self.result(sak)
        self.new_letters(sak)
        self.print_new_letters(sak)


'''
Η κλάση Computer, αποτελεί προέκταση της Player. Υλοποιεί κάποιες βασικές μεθόδους που 
πρόκειται να χρειαστεί ο υπολογιστής-παίκτης. 
'''
class Computer(Player):

    def __init__(self):
        super().__init__()
        self.algorithm = "min"

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    '''
    Ελέγχει αν το πρώτο γράμμα έχει ξανά υπάρξει πρώτο, στον σχηματισμό λέξεων.
    '''
    def has_never_been_first(self, pos):
        for i in range(pos):
            if self.list[i] == self.list[pos]:
                return False
        return True

    '''
    δημιουργεί όλους τους πιθανούς συνδιασμούς λέξεων με N γράμματα.
    '''
    def generate_words(self, n, sak):
        temp = []
        for i in range(len(self.list)):
            self.word = self.list[i]
            count_letters = 1
            if self.has_never_been_first(i):
                for j in range(len(self.list)):
                    if i != j:
                        self.word += self.list[j]
                        count_letters += 1
                    if count_letters == n:
                        if self.word_exist() and self.algorithm == "smart":
                            temp.append([self.word, self.calculate_points(sak)])
                        elif self.word_exist():
                            return True
                        else:
                            self.word = self.word[:-1]
                            count_letters -= 1
        if self.algorithm == "smart":
            return temp
        del temp
        return False

    '''
    ΜΙΝ Letters: Το πρόγραμμα δημιουργεί όλες τις δυνατές μεταθέσεις
    (permutations) των γραμμάτων που διαθέτει ο Η/Υ ξεκινώντας από 2 και
    ανεβαίνοντας μέχρι τα 7 γράμματα. Για κάθε μετάθεση ελέγχει αν είναι
    αποδεκτή λέξη και παίζει την πρώτη αποδεκτή λέξη που θα εντοπίσει. 
    '''
    def min(self, sak):
        n = 2
        while n <= 7:
            if self.generate_words(n, sak):
                return
            else:
                n += 1
        self.word = "Π"

    '''
    ΜΑΧ Letters: Όπως και στο A αλλά το πρόγραμμα ξεκινά από τις
    μεταθέσεις των γραμμάτων ανά 7 και κατεβαίνει προς το 2. Παίζει πάλι την
    πρώτη αποδεκτή λέξη αλλά τώρα αυτή με τα περισσότερα γράμματα.
    '''
    def max(self, sak):
        n = 7
        while n >= 2:
            if self.generate_words(n, sak):
                return
            else:
                n -= 1
        self.word = "Π"

    '''
    SMART: Όπως και στο Α αλλά εξαντλεί όλες τις μεταθέσεις 2 ως και 7
    γραμμάτων χωρίς να σταματά. Βρίσκει τις αποδεκτές λέξεις και στο τέλος
    παίζει τη λέξη που δίνει τους περισσότερους βαθμούς.
    '''
    def smart(self, sak):
        n = 7
        temp = []
        while n >= 2:
            temp += self.generate_words(n, sak)
        temp.sort(key=lambda x: x[0], reverse=True)
        if len(temp) > 0:
            self.word = temp[0][0]
        else:
            self.word = "Π"
        del temp

    '''
    Ο τρόπος με τον οποίο παίζει ο υπολογιστής. Αρχικά εκτυπώνεται το όνομα και το σκόρ του.
    Στην συνέχεια εκτυπώνονται τα διαθέσιμα γράμματα και ο παίκτης δίνει την λέξη με την 
    οποία θέλει να παίξει. Αν δεν μπορεί να σχηματίσει κάποια λέξη, δίνει "Π", για να πάει πάσο.
    '''
    def play(self, sak):
        self.print_stats(sak)
        if self.algorithm == "min":
            self.min(sak)
        elif self.algorithm == "max":
            self.max(sak)
        elif self.algorithm == "smart":
            self.smart(sak)
        self.word = unicodedata.normalize('NFD', self.word).upper().translate({ord('\N{COMBINING ACUTE ACCENT}'): None})
        print("\nΠαίζω Τη Λέξη:", self.word)
        if self.word != "Π":
            self.result(sak)
        self.new_letters(sak)
        self.print_new_letters(sak)


'''
Η κλάση Play,παίζει το παιχνίδι, αφού κάνει κάποιες ορισμένες ρυθμήσεις. Επιπλέον,
αποθηκεύει τα στοιχεία του παίκτη αφού τελειώσει το παιχνίδι.
'''
class Game:

    def __init__(self):
        self.sak = SakClass()
        self.human = Human()
        self.computer = Computer()

    '''
    Απαραίτητες ρυθμίσεις πριν ξεκινήσει το παιχνίδι. Όνομα παίκτη
    '''
    def setup(self):
        self.sak.set_letters()
        self.human.name = input("Όνομα:")
        self.human.list = self.sak.get_letters(7)
        self.computer.name = "PC"
        self.computer.list = self.sak.get_letters(7)

    '''
    Ανακοινώνει τον νικητή, τον παίκτη με τις περισσότερους πόντους. Απαραίτητες ρυθμίσεις 
    αφού τελειώσει το παιχνίδι. Αποθήκευση ονόματος και σκορ παίκτη.
    '''
    def end(self):
        temp = [[self.human.name, self.human.points], [self.computer.name, self.computer.points]]
        temp.sort(key=lambda x: x, reverse=True)
        print("\n===============Results===============")
        for i in range(len(temp)):
            print("Name:", temp[i][0], "Score:", temp[i][1])
        if temp[0][1] == temp[1][1]:
            print("Ισσοπαλία!")
        else:
            print("Ο νικιτής είναι ο:", temp[0][0], "με", temp[0][1], "πόντους!")
        print("===============Results===============")
        file = open("Score.txt", encoding='utf-8')
        pos = 0
        score_list = []
        files = file.readlines()
        for line in files:
            line = line.strip()
            temp = line.split('/')
            score_list.append([temp[0], int(temp[1])])
            pos += 1
        file.close()
        p = True
        for i in range(len(score_list)):
            if score_list[i][0] == self.human.name:
                if score_list[i][1] < self.human.points:
                    score_list[i][1] = self.human.points
                p = False
                break
        if p:
            score_list.append([self.human.name, self.human.points])
        score_list.sort(key=lambda x: x[1], reverse=True)
        file = codecs.open("Score.txt", "w", encoding='utf-8')
        for i in range(len(score_list)):
            string = str(score_list[i][0]) + "/" + str(score_list[i][1]) + "\n"
            file.write(string)
        file.close()

    '''
    Ρυθμίσεις από το αρχικό μενού. Εδώ ο παίκτης μπορεί να επιλέξει τον αλγόριθμο με τον
    οποίο θα παίξει ο υπολογιστής. 
    '''
    def settings(self):
        while True:
            print("Τρόπος με τον οποίο θα παίζει ο παίκτης:")
            print("1.ΜΙΝ Letters: Το πρόγραμμα δημιουργεί όλες τις δυνατές μεταθέσεις",
                  "(permutations) των γραμμάτων που διαθέτει ο Η/Υ ξεκινώντας\nαπό 2 και",
                  "ανεβαίνοντας μέχρι τα 7 γράμματα. Για κάθε μετάθεση ελέγχει αν είναι",
                  "αποδεκτή λέξη και παίζει την πρώτη αποδεκτή\nλέξη που θα εντοπίσει.")
            print("2.ΜΑΧ Letters: Όπως και στο A αλλά το πρόγραμμα ξεκινά από τις",
                  "μεταθέσεις των γραμμάτων ανά 7 και κατεβαίνει προς το 2. Παίζει\nπάλι την",
                  "πρώτη αποδεκτή λέξη αλλά τώρα αυτή με τα περισσότερα γράμματα.")
            print("3.SMART: Όπως και στο Α αλλά εξαντλεί όλες τις μεταθέσεις 2 ως και 7",
                  "γραμμάτων χωρίς να σταματά. Βρίσκει τις αποδεκτές λέξεις\nκαι στο τέλος",
                  "παίζει τη λέξη που δίνει τους περισσότερους βαθμούς.")
            choice = input("Επιλέξτε 1, 2 ή 3:")
            if choice == "1":
                self.computer.set_algorithm("min")
                break
            elif choice == "2":
                self.computer.set_algorithm("max")
                break
            elif choice == "3":
                self.computer.set_algorithm("smart")
                break
            else:
                print("Παρακαλώ Επιλέξτε ΜΟΝΟ 1, 2 ή 3!")
        input("Enter Για Συνέχεια\n")

    '''
    παίζουμεεεε :)
    Αν υπάρχουν λιγότερα από 10 γράμματα στο σακουλάκι και κανέναν από τους 2 παίκτες δεν
    μπορεί να σχηματίσει λέξη, το παιχνίδι τελειώνει.
    '''
    def run(self):
        self.setup()
        round_to_end = 0
        print("Ο υπολογιστής θα παίξει με τον αλγόριθμο:", self.computer.algorithm)
        while True:
            self.human.play(self.sak)
            self.computer.play(self.sak)
            if self.human.word == "Π" and self.computer.word == "Π":
                round_to_end += 1
            else:
                round_to_end = 0
            if self.sak.count_letters < 10 and round_to_end == 3 and self.human.word == "Π" and self.computer.word == "Π":
                break
        self.end()
