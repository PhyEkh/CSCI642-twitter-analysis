# -*- coding: utf-8 -*-


import re
def replace_retweet(tweet, default_replace=""):
    tweet = re.sub('RT\s+', default_replace, tweet)
    return tweet

def replace_user(tweet, default_replace="twitteruser"):
    tweet = re.sub('\B@\w+', default_replace, tweet)
    return tweet

# pip install emoji --upgrade
import emoji
def demojize(tweet):
    tweet = emoji.demojize(tweet)
    return tweet

def replace_url(tweet, default_replace=""):
    tweet = re.sub('(http|https):\/\/\S+', default_replace, tweet)
    return tweet

def replace_hashtag(tweet, default_replace=""):
    tweet = re.sub('#+', default_replace, tweet)
    return tweet

def to_lowercase(tweet):
    tweet = tweet.lower()
    return tweet

def word_repetition(tweet):
    tweet = re.sub(r'(.)\1+', r'\1\1', tweet)
    return tweet

def punct_repetition(tweet, default_replace=""):
    tweet = re.sub(r'[\?\.\!]+(?=[\?\.\!])', default_replace, tweet)
    return tweet

# replace contraction example: who's -> who is, you'll -> you will
# pip install contractions
import contractions
def fix_contractions(tweet):
    tweet = contractions.fix(tweet)
    return tweet


import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# nltk.download('stopwords')
def custom_tokenize(tweet, keep_punct = False, keep_alnum = False, keep_stop = False):
    token_list = word_tokenize(tweet)

    if not keep_punct:
        token_list = [token for token in token_list if token not in string.punctuation]

    if not keep_alnum:
        token_list = [token for token in token_list if token.isalpha()]
  
    if not keep_stop:
        stop_words = set(stopwords.words('english'))
        stop_words.discard('not')
        token_list = [token for token in token_list if not token in stop_words]

    return token_list


# Lemmatization
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
# nltk.download('wordnet')

def lemmatize_tokens(tokens, lemmatizer):
    token_list = []
    for token in tokens:
        token_list.append(lemmatizer.lemmatize(token))
    return token_list

#################################################################

def process_tweet(tweet, verbose=False):
    if verbose: print("Initial tweet: {}".format(tweet))
      
    ## Twitter Features
    tweet = replace_retweet(tweet) # replace retweet
    tweet = replace_user(tweet, "") # replace user tag
    tweet = replace_url(tweet) # replace url
    tweet = replace_hashtag(tweet) # replace hashtag
    if verbose: print("Post Twitter processing tweet: {}".format(tweet))
      
    ## Word Features
    tweet = to_lowercase(tweet) # lower case
    tweet = fix_contractions(tweet) # replace contractions
    tweet = punct_repetition(tweet) # replace punctuation repetition
    tweet = word_repetition(tweet) # replace word repetition
    tweet = demojize(tweet) # replace emojis
    if verbose: print("Post Word processing tweet: {}".format(tweet))
      
    ## Tokenization & Stemming
    tokens = custom_tokenize(tweet, keep_alnum=False, keep_stop=False) # tokenize
    lemmatizer = WordNetLemmatizer() # define lemmatizer
    stem = lemmatize_tokens(tokens, lemmatizer) # lemmatize tokens
      
    return stem


###########################################################

tweet = "RT @AIOutsider I love this! 👍😀 https://AIOutsider.com #NLP #Fun"
print(process_tweet(tweet))

def process_
____