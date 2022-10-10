# Requisito 1

import time
import requests
from parsel import Selector
# from tech_news.database import create_news


def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if response.status_code != 200:
            return None

        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2


def scrape_novidades(html_content):
    """Seu código deve vir aqui"""

    selector = Selector(text=html_content)
    url_news = ".entry-thumbnail div.cs-overlay a::attr(href)"
    all_news_url = selector.css(url_news).getall()

    return all_news_url


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css(".pagination a.next::attr(href)").get()

    return url


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
