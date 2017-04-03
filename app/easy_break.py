from ciphertext import CipherText
import re
from sys import exit

class EasyBreak:

    def __init__(self):
        self.ciphertext = None
        self.substitutions = []

        self.print_welcome_message()
        self.accept_ciphertext_file()
        self.start_options_loop()

    def print_welcome_message(self):
        print('======\n'
              'EasyBreak\n'
              '------\n'
              'A Python application to break simple monoalphabetic substitution ciphers like the Caesar Cipher\n'
              'and the general monoalphabetic cipher.\n'
              '------\n'
              '2017, Maria Candela Restless Morena Pampers etc.\n'
              '======')

    def print_ciphertext(self):
        print('------')
        print('Ciphertext:')
        print('------')
        print(self.ciphertext)

    def accept_ciphertext_file(self):
        filename = input("What's the file containing the ciphertext? ")
        try:
            with open(filename, 'r') as f:
                self.ciphertext = CipherText(f.read())
        except Exception:
            print('Oops...file not found. Check the path and try again!')
            print('------')
            self.accept_ciphertext_file()

        self.print_ciphertext()

    def print_options(self):
        print('======\n'
              'What would you like to do now?\n'
              '1: print ciphertext stats, 2: suggest substitutions, 3: add substitution(s), 4: delete substitution(s)\n'
              '5: print added substitutions, 6: print ciphertext with substitutions, 7: reset substitutions, 8: quit\n'
              '9: print partial plaintext')

    def start_options_loop(self):
        while True:
            self.print_options()
            try:
                choice = int(input('Your choice: '))
            except Exception:
                print('------\n'
                      'Oops...you picked an unknown option! Try again!')
                continue
            if choice == 1:
                self.print_stats()
            elif choice == 2:
                self.suggest_substitutions()
            elif choice == 3:
                self.add_substitutions()
                self.print_ciphertext_with_substitutions()
            elif choice == 4:
                self.delete_substitutions()
                self.print_ciphertext_with_substitutions()
            elif choice == 5:
                self.print_substitutions()
            elif choice ==6:
                self.print_ciphertext_with_substitutions()
            elif choice == 7:
                self.reset_substitutions()
            elif choice == 8:
                print('======\n'
                      'Bye bye!\n'
                      '======')
                exit(0)
            elif choice == 9:
                self.print_partial_plaintext()
            else:
                print('Oops...you picked an unknown option! Try again!')

    def print_high_freq_monograms(self):
        letter_freqs = self.ciphertext.get_monogram_freqs()
        std_freqs = CipherText.get_std_monogram_freqs()
        print('======\n'
              'Letter frequencies in ciphertext          English letter frequencies\n'
              '--------------------------------------------------------')
        for i in range(len(letter_freqs)):
            print('{0!s}: {1:.4f}'.format(letter_freqs[i][0], letter_freqs[i][1]), end='')
            print("                                ", end=" ")
            print("{0!s}: {1:.4f}".format(std_freqs[i][0], std_freqs[i][1]))
            print('--------------------------------------------------------')

    def print_high_freq_bigrams(self):
        bigram_freqs = self.ciphertext.get_bigram_freqs()
        std_freqs = self.ciphertext.get_std_bigram_freqs()
        print('======\n'
              'Bigram frequencies in ciphertext          English bigram frequencies\n'
              '--------------------------------------------------------')
        for i in range(len(bigram_freqs)):
            print('{0!s}: {1:.4f}'.format(bigram_freqs[i][0], bigram_freqs[i][1]), end='')
            print("                               ", end=" ")
            print("{0!s}: {1:.4f}".format(std_freqs[i][0], std_freqs[i][1]))
            print('--------------------------------------------------------')

    def print_high_freq_trigrams(self):
        trigram_freqs = self.ciphertext.get_trigram_freqs()
        std_freqs = self.ciphertext.get_std_trigram_freqs()
        print('======\n'
              'Trigram frequencies in ciphertext         English trigram frequencies\n'
              '--------------------------------------------------------')
        for i in range(len(trigram_freqs)):
            print('{0!s}: {1:.4f}'.format(trigram_freqs[i][0], trigram_freqs[i][1]), end='')
            print("                              ", end=" ")
            print("{0!s}: {1:.4f}".format(std_freqs[i][0], std_freqs[i][1]))
            print('--------------------------------------------------------')

    def print_high_freq_fourgrams(self):
        print('======\n'
              'Fourgram frequencies in ciphertext        English fourgram frequencies\n'
              '--------------------------------------------------------')

    def print_stats(self):
        self.print_high_freq_monograms()
        self.print_high_freq_bigrams()
        self.print_high_freq_trigrams()
        #self.print_high_freq_fourgrams()

    def suggest_substitutions(self):
        print('TODO')

    def add_substitutions(self):
        print('------')
        cchar = ''.join(input('Ciphertext character(s): ').upper().split())
        pchar = ''.join(input('Plaintext character(s) to use: ').lower().split())

        if len(cchar) != len(pchar):
            raise ValueError('Provide the same amount of ciphertext and plaintext characters!')

        for pair in zip(cchar, pchar):
            self.substitutions.append(pair)

    def delete_substitutions(self):
        print('------')
        cchar = ''.join(input('Which plaintext letter(s) do you want to undo? ').lower().split())
        for c in cchar:
            for sub in self.substitutions:
                if sub[1] == c:
                    self.substitutions.remove(sub)

    def print_substitutions(self):
        print('------')
        print('Active substitutions:')
        for sub in self.substitutions:
            print("'{}' -> '{}'".format(sub[0], sub[1]))

    def apply_substitutions(self):
        partial = self.ciphertext
        for sub in self.substitutions:
            partial = partial.replace(sub[0], sub[1])
        return partial

    def print_partial_plaintext(self):
        print('------\n'
              'Plaintext:\n'
              '------')
        partial = self.apply_substitutions()
        partial = re.sub(r"[A-Z]", " ", partial)
        print(partial)

    def print_ciphertext_with_substitutions(self):
        print('------\n'
              'Ciphertext:\n'
              '------')
        partial = self.apply_substitutions()
        print(partial)

    def reset_substitutions(self):
        self.substitutions = []

event = EasyBreak()
