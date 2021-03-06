# -*- coding: utf-8 -*-
from TwitterSearch import *
import sys
from keys import *
from bayes import classify

reload(sys)
sys.setdefaultencoding('utf8')


def twitter_fetch(keyword):
	
	tso = TwitterSearchOrder()

	tso.set_keywords([keyword])
	tso.set_language('en')
	tso.set_include_entities(False)
	tso.set_count(100)

	key = key1
	ts = TwitterSearch(
		key.consumer_key,
		key.consumer_secret,
		key.access_token,
		key.access_token_secret
	)

	csv = open('tweets.csv','w+')

	limit = 0
	tweet_array = []

	for tweet in ts.search_tweets_iterable(tso):
	
		limit += 1
		print limit

		each_tweet = tweet['text'].replace('\t',' ').replace('\n',' ').encode("ascii", "ignore")
	 
		tweet_array.append(each_tweet)

		csv.write(each_tweet+"\n")

		if limit == 500: break

	csv.close()
	return tweet_array

def main(keyword):

	
	
	pos, neg, net = 0, 0, 0
	try:
		tweets = twitter_fetch(keyword)
	
	except:
		print "Connection Error"

	for each_tweet in tweets:
		result = classify(each_tweet)

		if result < 0.35:
			pos = pos + 1
		elif result>0.65:
			neg = neg + 1
		else:
			net = net + 1


	return pos,neg,net

if __name__ == '__main__':
	main()
