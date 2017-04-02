from collections import OrderedDict
from string import ascii_uppercase

class CipherText:

    def __init__(self, string):
        self.text = string
        self._monogram_freqs = None
        self._bigram_probs = None
        self.trigram_probs = None
        self.quadram_probs = None

    def __str__(self):
        return self.text

    def replace(self, cchar, pchar):
        return self.text.replace(cchar, pchar)

    def text_without_whitespace(self):
        return ''.join(self.text.split())

    def get_monogram_freqs(self):
        if self._monogram_freqs is not None:
            return self._monogram_freqs

        stripped_text = self.text_without_whitespace().upper()
        textlen = len(stripped_text)

        freqs = {}
        for ch in stripped_text:
            if ch in ascii_uppercase:
                freqs[ch] = freqs.get(ch, 0) + 1
        for ch, n in freqs.items():
            freqs[ch] = n / textlen

        for ch in ascii_uppercase:
            if freqs.get(ch) is None:
                freqs[ch] = 0

        sorted_freqs = OrderedDict(sorted(freqs.items(), key=lambda t: t[1], reverse=True))
        self._monogram_freqs = sorted_freqs
        return sorted_freqs

    def get_std_monogram_freqs(self):
        freqs = {
            'E': 0.1209652247516903,
            'T': 0.08938126949659495,
            'A': 0.08551690673195275,
            'O': 0.07467265410810447,
            'I': 0.0732511860723129,
            'N': 0.07172184876283856,
            'S': 0.06728203117491646,
            'R': 0.0633271013284023,
            'H': 0.04955707280570641,
            'L': 0.04206464329306453,
            'D': 0.03871183735737418,
            'C': 0.03164435380900101,
            'U': 0.026815809362304373,
            'M': 0.025263217360184446,
            'F': 0.021815103969122528,
            'G': 0.020863354250923158,
            'P': 0.020661660788966266,
            'W': 0.018253618950416498,
            'Y': 0.017213606152473405,
            'B': 0.016047959168228293,
            'V': 0.01059346274662571,
            'K': 0.008086975227142329,
            'J': 0.002197788956104563,
            'X': 0.0019135048594134572,
            'Q': 0.0010402453014323196,
            'Z': 0.001137563214703838
        }

        return OrderedDict(sorted(freqs.items(), key=lambda t: t[1], reverse=True))