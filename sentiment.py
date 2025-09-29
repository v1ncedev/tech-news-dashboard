from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(headlines):
    results = []
    for h in headlines:
        score = analyzer.polarity_scores(h)
        results.append({"headline": h, "compound": score["compound"]})
    return results

if __name__ == "__main__":
    sample = ["AI is transforming the future", "Tech stocks crash amid fears"]
    print(analyze_sentiment(sample))
