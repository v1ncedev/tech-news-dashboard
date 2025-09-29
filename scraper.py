import requests
from bs4 import BeautifulSoup

def scrape_hackernews(n=20):
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    headlines = []
    for row in soup.select(".titleline a")[:n]:   # updated selector
        headlines.append(row.text)
    return headlines

if __name__ == "__main__":
    print(scrape_hackernews(10))
