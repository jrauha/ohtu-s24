from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

SEASONS = ["2023-24", "2022-23", "2021-22", "2020-21", "2019-20", "2018-19"]
NATIONALITIES = [
    "AUT",
    "CZE",
    "AUS",
    "SWE",
    "GER",
    "DEN",
    "SUI",
    "SVK",
    "NOR",
    "RUS",
    "CAN",
    "LAT",
    "BLR",
    "SLO",
    "USA",
    "FIN",
    "GBR",
]


def get_season():
    return Prompt.ask("Select season", default="2023-24", choices=SEASONS)


def get_nationality():
    return Prompt.ask("Select nationality", default="FIN", choices=NATIONALITIES)


def create_table(players):
    table = Table(title="Top NHL Players")
    table.add_column("Name", justify="left", style="cyan", no_wrap=True)
    table.add_column("Team", justify="left", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points),
        )
    return table


def main():
    season = get_season()
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationality = get_nationality()
        players = stats.top_scorers_by_nationality(nationality)

        console = Console()
        table = create_table(players)
        console.print(table)


if __name__ == "__main__":
    main()
