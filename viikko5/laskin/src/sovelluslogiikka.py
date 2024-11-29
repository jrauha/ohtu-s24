class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._historia = []

    def miinus(self, operandi):
        self.aseta_arvo(self._arvo - operandi)

    def plus(self, operandi):
        self.aseta_arvo(self._arvo + operandi)

    def nollaa(self):
        self.aseta_arvo(0)

    def aseta_arvo(self, arvo):
        self._historia.append(self._arvo)
        self._arvo = arvo

    def arvo(self):
        return self._arvo

    def kumoa(self):
        self._arvo = self._historia.pop()


class Toiminto:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        raise NotImplementedError

    def kumoa(self):
        raise NotImplementedError


class Summa(Toiminto):
    def suorita(self):
        operandi = self._lue_syote()
        self._sovelluslogiikka.plus(operandi)

    def kumoa(self):
        self._sovelluslogiikka.kumoa()


class Erotus(Toiminto):
    def suorita(self):
        operandi = self._lue_syote()
        self._sovelluslogiikka.miinus(operandi)

    def kumoa(self):
        self._sovelluslogiikka.kumoa()


class Nollaus(Toiminto):
    def suorita(self):
        self._sovelluslogiikka.nollaa()

    def kumoa(self):
        self._sovelluslogiikka.kumoa()
