import tweepy
from textblob import TextBlob
from .NLPutilities import clean_text


class Twitter(object):
    """
    Twitter Class for getting tweets
    """

    def __init__(self, apikey, apikey_secret, access_token, access_token_secret):
        try:
            # create client object
            auth = tweepy.OAuth1UserHandler(apikey, apikey_secret)
            auth.set_access_token(access_token, access_token_secret)
            # tweepy API object to get tweets
            self.api = tweepy.API(auth)

            self.tweets = []
        except Exception as e:
            print("Authentication Failed with Twitter!")

    def _preprocess_text(self, tweet):
        """
        Data cleaning of texts
        """
        # return clean_text(tweet)
        return tweet

    def _get_sentiment(self, tweet):
        """
        Sentiment analysis on tweets
        """
        try:
            blob = TextBlob(self._preprocess_text(tweet))
            # setting sentiment
            if blob.sentiment.polarity > 0:
                return 'positive'
            elif blob.sentiment.polarity == 0:
                return 'neutral'
            else:
                return 'negative'
        except Exception as e:
            raise ValueError("Sentiment Analysis failed!")

    def get_tweets(self, query, count=10):
        """
        Search function to fetch tweets based on query
        """
        try:
            result = self.api.search_tweets(q=query, count=count, lang='en')
        except Exception as e:
            raise ValueError("Tweet Search Failed!")

        tweets = [
            {"id": tw.id, "user": tw.user.screen_name, "tweet": tw.text, "sentiment": self._get_sentiment(tw.text)}
            for tw in result
        ]
        return tweets
