import requests
from bs4 import BeautifulSoup
from googlesearch import search

from bot import config


class GoogleSearch:
    def __init__(self) -> None:
        self.results = []

    async def get_search_results(self, query: str) -> list[tuple[str, str]]:
        for url in search(query, stop=config.MAX_SEARCH_RESULTS):
            print(url)
            try:
                reqs = requests.get(url)
                soup = BeautifulSoup(reqs.text, 'html.parser')
                for title in soup.find_all('title'):
                    self.results.append((title.get_text(), url))
            except Exception:
                continue

        return self.results
