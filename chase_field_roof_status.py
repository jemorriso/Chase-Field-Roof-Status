from bs4 import BeautifulSoup
import requests

URL = "https://www.mlb.com/dbacks/ballpark/information/roof"


def gen_soup(raw):
    return BeautifulSoup(raw, features="html.parser")


def parse_game_html(html):
    table_cells = html.select("td")
    return {
        "date": table_cells[0].text,
        "time": table_cells[1].text,
        "opponent": table_cells[2].text,
        "roof status": table_cells[3].text,
    }


def get_roof_status():
    res = requests.get(URL)
    soup = gen_soup(res.text)

    # Relying on Roof Status being the only table on the page.
    games_html = soup.select("tbody > tr")

    games = []
    for g in games_html:
        games.append(parse_game_html(g))

    return games


if __name__ == "__main__":
    print(get_roof_status())
