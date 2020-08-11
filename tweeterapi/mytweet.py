import tweepy
import time

auth = tweepy.OAuthHandler( 'lC3t8FRu2zLBjD5R7RYfzm1GW', '3sQ1t8agxtBAGWPs1RMkCgkoYQjxW58E9fD26QMVWe0QIqH5GT' );
auth.set_access_token( '418337382-bJJPxWYhqm9iU7KroowKeiIM4UEAufqXnIuPUv5f', 'GPb9U2ljRFjRF0NtmpG8ZGehZUc9uiGhaApSXxoDQjxg8' );

api = tweepy.API( auth )

public_tweets = api.home_timeline()

for tweet in public_tweets:
	print( tweet.text )


def limit_handler( cursor ):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)
	except tweepy.TweepError as e:
		print( e.reason )
	except StopIteration:
		print( 'finished' )

search_string = 'evo morales'
numbersOfTweets = 2

for tweet in limit_handler( tweepy.Cursor( api.search, search_string ).items( numbersOfTweets ) ):
	print( tweet.text )
	