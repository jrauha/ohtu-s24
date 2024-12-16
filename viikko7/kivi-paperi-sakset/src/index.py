from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


def luo_peli(tyyppi):
    if tyyppi == "a":
        return KPSPelaajaVsPelaaja()
    elif tyyppi == "b":
        return KPSTekoaly()
    elif tyyppi == "c":
        return KPSParempiTekoaly()


def main():
    while True:
        print(
            "Valitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
        )

        vastaus = input()
        peli = luo_peli(vastaus)
        if peli is None:
            break
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )
        peli.pelaa()


if __name__ == "__main__":
    main()
