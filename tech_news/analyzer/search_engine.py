import re
from tech_news.database import search_news

# Requisito 6


def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": re.compile(title, re.IGNORECASE)}
    filtered_news = search_news(query)
    result = []

    for news in filtered_news:
        result.append((news["title"], news["url"]))

    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
