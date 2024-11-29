class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo

    def kumoa(self):
        pass


class Toiminto:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        raise NotImplementedError


class Summa(Toiminto):
    def suorita(self):
        operandi = self._lue_syote()
        self._sovelluslogiikka.plus(operandi)


class Erotus(Toiminto):
    def suorita(self):
        operandi = self._lue_syote()
        self._sovelluslogiikka.miinus(operandi)


class Nollaus(Toiminto):
    def suorita(self):
        self._sovelluslogiikka.nollaa()


class Kumoa(Toiminto):
    def suorita(self):
        self._sovelluslogiikka.kumoa()
