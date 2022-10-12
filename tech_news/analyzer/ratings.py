from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    all_news = find_news()

    all_sorted_news = sorted(
        all_news, key=lambda news: (-news["comments_count"], news["title"])
    )

    result = []

    for news in all_sorted_news[:5]:
        result.append((news["title"], news["url"]))

    return result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    all_news = find_news()
    all_categories = []

    for news in all_news:
        all_categories.append(news["category"])
    list_5_categories = Counter(all_categories).most_common(5)

    result = []

    for category in sorted(
        list_5_categories, key=lambda category: (-category[1], category[0])
    ):
        result.append(category[0])

    return result
