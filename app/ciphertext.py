from collections import OrderedDict
from string import ascii_uppercase

class CipherText:

    _HIGH_FREQ_RANGE = 12

    def __init__(self, string):
        self.text = string

        self._monogram_freqs = None
        self._bigram_freqs = None
        self._trigram_freqs = None
        self._quadram_freqs = None

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

        mfreqs = {}
        for c in stripped_text:
            mfreqs[c] = mfreqs.get(c, 0) + 1
            #if ch in ascii_uppercase:
            #    freqs[ch] = freqs.get(ch, 0) + 1
        for c, n in mfreqs.items():
            mfreqs[c] = n / textlen

        mfreqs_list = list(mfreqs.items())
        mfreqs_list.sort(key=lambda tup: tup[1], reverse=True)
        self._monogram_freqs = mfreqs_list[:CipherText._HIGH_FREQ_RANGE]
        return self._monogram_freqs
        #for ch in ascii_uppercase:
        #    if freqs.get(ch) is None:
        #        freqs[ch] = 0
        #sorted_freqs = OrderedDict(sorted(freqs.items(), key=lambda t: t[1], reverse=True))
        #self._monogram_freqs = sorted_freqs
        #return sorted_freqs

    @staticmethod
    def get_std_monogram_freqs():
        return [
            ('E', 0.1209652247516903),
            ('T', 0.08938126949659495),
            ('A', 0.08551690673195275),
            ('O', 0.07467265410810447),
            ('I', 0.0732511860723129),
            ('N', 0.07172184876283856),
            ('S', 0.06728203117491646),
            ('R', 0.0633271013284023),
            ('H', 0.04955707280570641),
            ('L', 0.04206464329306453),
            ('D', 0.03871183735737418),
            ('C', 0.03164435380900101),
            ('U', 0.026815809362304373),
            ('M', 0.025263217360184446),
            ('F', 0.021815103969122528),
            ('G', 0.020863354250923158),
            ('P', 0.020661660788966266),
            ('W', 0.018253618950416498),
            ('Y', 0.017213606152473405),
            ('B', 0.016047959168228293),
            ('V', 0.01059346274662571),
            ('K', 0.008086975227142329),
            ('J', 0.002197788956104563),
            ('X', 0.0019135048594134572),
            ('Q', 0.0010402453014323196),
            ('Z', 0.001137563214703838)
        ][:CipherText._HIGH_FREQ_RANGE]
        # return OrderedDict(sorted({
        #     'E': 0.1209652247516903,
        #     'T': 0.08938126949659495,
        #     'A': 0.08551690673195275,
        #     'O': 0.07467265410810447,
        #     'I': 0.0732511860723129,
        #     'N': 0.07172184876283856,
        #     'S': 0.06728203117491646,
        #     'R': 0.0633271013284023,
        #     'H': 0.04955707280570641,
        #     'L': 0.04206464329306453,
        #     'D': 0.03871183735737418,
        #     'C': 0.03164435380900101,
        #     'U': 0.026815809362304373,
        #     'M': 0.025263217360184446,
        #     'F': 0.021815103969122528,
        #     'G': 0.020863354250923158,
        #     'P': 0.020661660788966266,
        #     'W': 0.018253618950416498,
        #     'Y': 0.017213606152473405,
        #     'B': 0.016047959168228293,
        #     'V': 0.01059346274662571,
        #     'K': 0.008086975227142329,
        #     'J': 0.002197788956104563,
        #     'X': 0.0019135048594134572,
        #     'Q': 0.0010402453014323196,
        #     'Z': 0.001137563214703838
        # }.items(), key=lambda t: t[1], reverse=True))

    def get_bigram_freqs(self):
        if self._bigram_freqs is not None:
            return self._bigram_freqs

        stripped_text = self.text_without_whitespace().upper()
        textlen = len(stripped_text)

        bfreqs = {}
        for i in range(textlen):
            bgram = stripped_text[i:i+2]
            if len(bgram) == 2:
                bfreqs[bgram] = bfreqs.get(bgram, 0) + 1

        tot_bgrams = textlen if textlen % 2 == 0 else textlen - 1
        for bgram, n in bfreqs.items():
            bfreqs[bgram] = n / tot_bgrams

        # keep only the most frequent 8
        bfreqs_list = list(bfreqs.items())
        bfreqs_list.sort(key=lambda tup: tup[1], reverse=True)
        #sorted_freqs = OrderedDict(sorted(freqs.items(), key=lambda t: t[1], reverse=True))
        #self._monogram_freqs = sorted_freqs
        self._bigram_freqs = bfreqs_list[:CipherText._HIGH_FREQ_RANGE]
        return self._bigram_freqs

    @staticmethod
    def get_std_bigram_freqs():
        return [
            ('TH', 0.027056980400061274),
            ('HE', 0.0232854497343354),
            ('IN', 0.020275533912479046),
            ('ER', 0.017838136076634363),
            ('AN', 0.016136243079947415),
            ('RE', 0.014089222456964019),
            ('ES', 0.013198141738779546),
            ('ON', 0.013162249877258834),
            ('ST', 0.012492322191729358),
            ('NT', 0.011725158252060271),
            ('EN', 0.011329747191802887),
            ('AT', 0.011164000013278053),
            ('ED', 0.010787830752016612),
            ('ND', 0.010682918499219806),
            ('TO', 0.010664621630644244),
            ('OR', 0.010574430727766728),
            ('EA', 0.010020473709826474),
            ('TI', 0.009918454525937884),
            ('AR', 0.009794636726918318),
            ('TE', 0.009781351042209434),
            ('NG', 0.008919108277644921),
            ('AL', 0.008836830184180957),
            ('IT', 0.008773684503494425),
            ('AS', 0.008735606073905992),
            ('IS', 0.00863757543993427),
            ('HA', 0.008318866088601775),
            ('ET', 0.007602122951633152),
            ('SE', 0.00729216912299171),
            ('OU', 0.007195042486331116),
            ('OF', 0.0070629048594105116),
            ('LE', 0.007026448490998915),
            ('SA', 0.0069563462630839205),
            ('VE', 0.006780783001195525),
            ('RO', 0.006759922609930308),
            ('RA', 0.006624590581664445),
            ('RI', 0.006390801475057014),
            ('HI', 0.0063585866555539395),
            ('NE', 0.006320736942604214),
            ('ME', 0.006299011868313592),
            ('DE', 0.006250933272000211),
            ('CO', 0.0061832354595479444),
            ('TA', 0.006046905542206225),
            ('EC', 0.005960924043027139),
            ('SI', 0.005957002558656506),
            ('LL', 0.005697536135740754),
            ('SO', 0.005527965758559595),
            ('NA', 0.005445612274171245),
            ('LI', 0.005386327487603231),
            ('LA', 0.005360229277177168),
            ('EL', 0.005340324916836537)
        ][:CipherText._HIGH_FREQ_RANGE]

    def get_trigram_freqs(self):
        if self._trigram_freqs is not None:
            return self._trigram_freqs

        stripped_text = self.text_without_whitespace().upper()
        textlen = len(stripped_text)

        tfreqs = {}
        for i in range(textlen):
            tgram = stripped_text[i:i+3]
            if len(tgram) == 3:
                tfreqs[tgram] = tfreqs.get(tgram, 0) + 1

        tot_tgrams = textlen - 2
        for tgram, n in tfreqs.items():
            tfreqs[tgram] = n / tot_tgrams

        # keep only the most frequent 8
        tfreqs_list = list(tfreqs.items())
        tfreqs_list.sort(key=lambda tup: tup[1], reverse=True)
        #sorted_freqs = OrderedDict(sorted(freqs.items(), key=lambda t: t[1], reverse=True))
        #self._monogram_freqs = sorted_freqs
        self._trigram_freqs = tfreqs_list[:CipherText._HIGH_FREQ_RANGE]
        return self._trigram_freqs

    @staticmethod
    def get_std_trigram_freqs():
        return [
            ('THE', 0.019763959760977716),
            ('AND', 0.009650407245601894),
            ('ING', 0.007854080839603726),
            ('HER', 0.0056470407038060385),
            ('THA', 0.004855105985442601),
            ('HAT', 0.004574924943704365),
            ('ERE', 0.004355914031936269),
            ('HIS', 0.003905057404343844),
            ('ENT', 0.003585006545750069),
            ('DTH', 0.0032777904912125286),
            ('WAS', 0.0031721081684516145),
            ('ETH', 0.0030656066028786006),
            ('NTH', 0.0030265560288351622),
            ('TTH', 0.002848780338609439),
            ('YOU', 0.002843591800799472),
            ('THI', 0.0028334878061169037),
            ('ITH', 0.002777233133019363),
            ('OTH', 0.0027245285121075893),
            ('FOR', 0.002674281619632116),
            ('ION', 0.002657077520578014),
            ('HES', 0.002657077520578014),
            ('NOT', 0.0025912650146726387),
            ('INT', 0.0025246332659551634),
            ('WIT', 0.0024989636578426934),
            ('SHE', 0.0024219548335052835),
            ('TER', 0.002406389220075381),
            ('EDT', 0.002393008254144413),
            ('ALL', 0.002368157888844043),
            ('ERS', 0.0023531384372888742),
            ('FTH', 0.002306714677936535),
            ('OFT', 0.0022712141560788635),
            ('NCE', 0.0022428137385927267),
            ('VER', 0.0021748165851884177),
            ('ESS', 0.002172085775814751),
            ('EAN', 0.0021554278386353817),
            ('STH', 0.0021273005020866114),
            ('HAD', 0.002105454027097275),
            ('TIO', 0.002048926273062368),
            ('EST', 0.0020483801111876344),
            ('ATT', 0.002017521965265197),
            ('REA', 0.002002229432772662),
            ('STO', 0.0019790175530964922),
            ('ATI', 0.001956897997169789),
            ('EAR', 0.001910201156880083),
            ('GHT', 0.0019044664571953823),
            ('HIN', 0.0019028279715711822),
            ('HIM', 0.0018850777106423464),
            ('ONT', 0.0018823469012686795),
            ('RES', 0.0018812545775192125),
            ('ONE', 0.0018686928544003442),
            ('RIN', 0.001864323559402477),
            ('EVE', 0.0018528541600330755),
            ('OUT', 0.0018012418628707688),
            ('SAN', 0.0017971456488102683),
            ('EDA', 0.0017914109491255674),
            ('TIN', 0.001757002751017363),
            ('NDT', 0.0017512680513326623),
            ('NGT', 0.001736794761652227),
            ('OME', 0.0017053904538550564),
            ('HEM', 0.0016797208457425862),
            ('BUT', 0.0016401241098244145),
            ('MAN', 0.0016316586007660467),
            ('RTH', 0.001629473953267113),
            ('HEC', 0.0016117236923382774),
            ('OUN', 0.0016005273739062426),
            ('ECO', 0.001593700350472075),
            ('OUL', 0.001590969541098408),
            ('TED', 0.0015803193845411066),
            ('HOU', 0.0015743116039190392),
            ('HEW', 0.001570761551733272),
            ('DIN', 0.0015704884707959054),
            ('TAN', 0.0015683038232969717),
            ('HEA', 0.0015562882620528368),
            ('ERA', 0.001545091943620802),
            ('ESA', 0.0015224262258193657),
            ('DTO', 0.001515599202385198),
            ('ATH', 0.0015128683930115312),
            ('HED', 0.0015071336933268303),
            ('HEN', 0.0015033105602036965),
            ('THO', 0.001488291108648528),
            ('NDE', 0.0014768217092791264),
            ('AST', 0.001475183223654926),
            ('ULD', 0.0014618022577239577),
            ('RED', 0.0014440519967951222),
            ('EDI', 0.0014394096208598882),
            ('NTO', 0.0014388634589851549),
            ('EOF', 0.0014314902736762539),
            ('ATE', 0.001425755573991553),
            ('AVE', 0.0014181093077452855),
            ('AID', 0.0014167439030584518),
            ('RAN', 0.0014159246602463518),
            ('YTH', 0.001413740012747418),
            ('ANT', 0.0014112822843111179),
            ('CON', 0.0014096437986869175),
            ('EWA', 0.0014063668274385173),
            ('ILL', 0.001400085965879083),
            ('TOT', 0.0013976282374427828),
            ('ARE', 0.0013905281330712485),
            ('ORE', 0.0013897088902591484),
            ('IST', 0.0013847934333865476)
        ][:CipherText._HIGH_FREQ_RANGE]