from ciphertext import CipherText
import re
from sys import exit

class EasyBreak:

    def __init__(self):
        self._ciphertext = None
        self._substitutions = []

        self.run()

    def print_welcome_message(self):
        print('======\n'
              'EasyBreak\n'
              '------\n'
              'A Python application to break simple monoalphabetic substitution ciphers like the Caesar Cipher\n'
              'and the general monoalphabetic cipher.\n'
              '------\n'
              '2017, Maria Candela Restless Morena Pampers etc.\n'
              '======')

    def run(self):
        self.print_welcome_message()
        self.accept_ciphertext_file()
        self.print_ciphertext()
        while True:
            try:
                command = input('>>> ')
                self.parse_command(command)
            except ValueError as err:
                print('------\n' +
                      str(err) + 'Try again!')
                continue

    def accept_ciphertext_file(self):
        filename = input("What's the file containing the ciphertext? ")
        try:
            with open(filename, 'r') as f:
                self._ciphertext = CipherText(f.read())
        except Exception:
            print('Oops...file not found. Check the path and try again!')
            print('------')
            self.accept_ciphertext_file()

    def print_help(self):
        print('------')
        print('Help:\n'
              '(Note: uppercase is CIPHERTEXT, lowercase is plaintext)\n'
              "'a X y' : add the substitution rule X~y\n"
              "'d y'   : delete the substitution rule for y\n"
              "'r'     : reset the substitution rules\n"
              "'p s'   : print the substitution rules\n"
              "'s'     : print the ciphertext statistics from frequency analysis\n"
              "'p'     : print the ciphertext with the substitution rules\n"
              "'p p'   : print only the plaintext letters substituted so far\n"
              "'#'     : show substitution hints from frequency analysis\n"
              "'?'     : print this list\n"
              "'q'     : quit")
        print('------')

    def parse_command(self, string):
        string = ''.join(string.split())
        command = string[0].lower()

        if command == 'a':  # add
            self.add_substitutions(string[1:])
            self.print_ciphertext_with_substitutions()
        elif command == 'r':  # reset
            self.reset_substitutions()
            self.print_ciphertext()
        elif command == 'd':  # delete
            self.delete_substitutions(string[1:])
            self.print_ciphertext_with_substitutions()
        elif command == 's':  # stats
            self.print_stats()
        elif command == 'p':  # print
            if len(string) == 2 and string[1] == 'p':
                self.print_partial_plaintext()
            elif len(string) == 2 and string[1] == 's':
                self.print_substitutions()
            else:
                self.print_ciphertext_with_substitutions()
        elif command == '#':
            self.suggest_substitutions()
        elif command == '?':  # help
            self.print_help()
        elif command == 'q':  # quit
            self.quit()
        else:
            raise ValueError('')

    def quit(self):
        print('======\n'
              'Bye bye!\n'
              '======')
        exit(0)

    def print_high_freq_monograms(self):
        letter_freqs = self._ciphertext.get_ngram_freqs(1)
        std_freqs = CipherText.get_std_monogram_freqs()
        print('======\n'
              'Monograms (cipher)          English\n'
              '-------------------------------------')
        for i in range(len(letter_freqs)):
            print('{0!s}: {1:.4f}'.format(letter_freqs[i][0], letter_freqs[i][1]), end='')
            print("                  ", end=" ")
            print("{0!s}: {1:.4f}".format(std_freqs[i][0], std_freqs[i][1]))
            print('-------------------------------------')

    def print_high_freq_bigrams(self):
        bigram_freqs = self._ciphertext.get_ngram_freqs(2)
        std_freqs = self._ciphertext.get_std_bigram_freqs()
        print('======\n'
              'Bigrams (cipher)            English\n'
              '--------------------------------------')
        for i in range(len(bigram_freqs)):
            print('{0!s}: {1:.4f}'.format(bigram_freqs[i][0], bigram_freqs[i][1]), end='')
            print("                 ", end=" ")
            print("{0!s}: {1:.4f}".format(std_freqs[i][0], std_freqs[i][1]))
            print('--------------------------------------')

    def print_high_freq_trigrams(self):
        trigram_freqs = self._ciphertext.get_ngram_freqs(3)
        std_freqs = self._ciphertext.get_std_trigram_freqs()
        print('======\n'
              'Trigrams (cipher)           English\n'
              '---------------------------------------')
        for i in range(len(trigram_freqs)):
            print('{0!s}: {1:.4f}'.format(trigram_freqs[i][0], trigram_freqs[i][1]), end='')
            print("                ", end=" ")
            print("{0!s}: {1:.4f}".format(std_freqs[i][0], std_freqs[i][1]))
            print('---------------------------------------')

    def print_high_freq_fourgrams(self):
        fourgram_freqs = self._ciphertext.get_ngram_freqs(4)
        std_freqs = self._ciphertext.get_std_fourgram_freqs()
        print('======\n'
              'Fourgrams (cipher)          English\n'
              '----------------------------------------')
        for i in range(len(fourgram_freqs)):
            print('{0!s}: {1:.4f}'.format(fourgram_freqs[i][0], fourgram_freqs[i][1]), end='')
            print("               ", end=" ")
            print("{0!s}: {1:.4f}".format(std_freqs[i][0], std_freqs[i][1]))
            print('----------------------------------------')

    def print_stats(self):
        self.print_high_freq_monograms()
        self.print_high_freq_bigrams()
        self.print_high_freq_trigrams()
        self.print_high_freq_fourgrams()

    def suggest_substitutions(self):
        print('TODO')

    def add_substitutions(self, string):
        cchar = re.sub(r"[a-z ]", '', string)
        pchar = re.sub(r"[A-Z ]", '', string)
        if len(cchar) != len(pchar):
            raise ValueError('Provide the same amount of ciphertext and plaintext characters!')

        for pair in zip(cchar, pchar):
            self._substitutions.append(pair)

    def delete_substitutions(self, string):
        pchar = re.sub(r"[A-Z ]", '', string)
        for p in pchar:
            for sub in self._substitutions:
                if sub[1] == p:
                    self._substitutions.remove(sub)

    def print_substitutions(self):
        print('------')
        print('Active substitutions:')
        for sub in self._substitutions:
            print("'{}' -> '{}'".format(sub[0], sub[1]))

    def apply_substitutions(self):
        partial = self._ciphertext.get_text()
        for sub in self._substitutions:
            partial = partial.replace(sub[0], sub[1])
        return partial

    def print_ciphertext(self, subs=False):
        print('------')
        print('Ciphertext:')
        print('------')
        if subs:
            print(self.apply_substitutions())
        else:
            print(self._ciphertext.get_text())
        print('------')

    def print_ciphertext_with_substitutions(self):
        self.print_ciphertext(subs=True)

    def print_partial_plaintext(self):
        print('------\n'
              'Plaintext:\n'
              '------')
        partial = re.sub(r"[A-Z]", " ", self.apply_substitutions())
        if not partial.isspace():
            print(partial)
            print('------')

    def reset_substitutions(self):
        self._substitutions = []

app = EasyBreak()
