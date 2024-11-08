import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN:\n")
    fin_players = filter(lambda p: p.nationality == "FIN", players)
    for player in fin_players:
        print(player)


if __name__ == "__main__":
    main()
