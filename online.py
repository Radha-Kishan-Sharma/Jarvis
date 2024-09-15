import requests
import wikipedia
import pywhatkit as kit

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results


def search_on_google(query):
    kit.search(query)

def youtube(video):
    kit.playonyt(video)

def get_news():
    news_headline = []
    result =requests.get(f"https://newsapi.org/v2/everything?q=apple&from=2024-09-12&to=2024-09-12&sortBy=popularity&apiKey=bbb9e8a7e93844e6ac49368723ac43f9").json()
    articles = result["articles"]
    for article in articles:
        news_headline.append(article["title"])
    return news_headline[:6]

