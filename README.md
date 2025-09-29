#  Tech News Sentiment Dashboard

##  Overview
This project scrapes the latest **tech news headlines** (currently from Hacker News), performs **sentiment analysis** using the VADER NLP model, and displays results in an **interactive Streamlit dashboard**.  

It demonstrates:
- Web scraping with **BeautifulSoup**
- Text sentiment analysis with **VADER**
- Data processing with **pandas**
- Interactive dashboard visualisation with **Streamlit**

---

##  How It Works
1. **Scraper** (`scraper.py`)  
   - Fetches latest headlines from Hacker News (can be extended to other sources).  

2. **Sentiment Analysis** (`sentiment.py`)  
   - Uses VADER to score headlines from -1 (negative) → +1 (positive).  

3. **Dashboard** (`dashboard.py`)  
   - Displays:
     - A table of headlines with sentiment scores  
     - A bar chart of sentiment distribution  

---

##  Usage

### 1. Clone the repo
```bash
git clone https://github.com/YOURUSERNAME/tech-news-sentiment.git
cd tech-news-sentiment
