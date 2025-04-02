import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

tweets = ["I love my phone", "I hate my phone", "I don't like my phone"]

for tweet in tweets:  
    print(tweet)
    print(sia.polarity_scores(tweet))
    print()


messages = [
    "The package I received was damaged.",
    "I love the product!",
    "I don't like the product.",
    "I can't believe you call this customer service.",
    "I fell down the stairs",
    "I am eating a sandwich.",
    "I am agree but you are a liar and a crook, But that's okaaaaaaaay, please continue,."
]

for message in messages:
    score = sia.polarity_scores(message)['compound']
    if score > 0.2:
        print(f"{message} -> Positive")
    elif score < -0.2:
        print(f"{message} -> Negative")
    else:
        print(f"{message} -> Neutral")