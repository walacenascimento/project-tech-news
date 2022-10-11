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

    selector = Selector(text=html_content)
    result = {}

    result["url"] = selector.css("head link[rel*=canonical]::attr(href)").get()

    header = selector.css("div.entry-header-inner")
    result["title"] = header.css("h1.entry-title::text").get().rstrip()
    result["timestamp"] = header.css("li.meta-date::text").get()
    result["writer"] = header.css("ul.post-meta a.fn::text").get()

    comments = selector.css("ol.comment-list").getall()
    result["comments_count"] = len(comments)

    sumary_path = ".entry-content > p:first-of-type *::text"
    summary = selector.css(sumary_path).getall()
    result["summary"] = "".join(summary).strip()

    result["tags"] = []
    for tag in selector.css("a[rel*=tag]::text").getall():
        result["tags"].append(tag)

    result["category"] = header.css("div.meta-category span.label::text").get()

    return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
