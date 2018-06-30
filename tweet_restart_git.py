# Make sure you have Tweepy installed in order to run the program
# If you get a request error, wait 15 minutes and run program again.


import tweepy
from tweepy import OAuthHandler

# Testing

test_mode = True # Set to False for the program to run

# Auth

consumer_key = '' # Replace with your key
consumer_secret = '' # Replace with your consumer secret
access_token = '' # Replace with your token
access_token_secret = '' # Replace with your Token Secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Delete Options

delete_tweets = True
delete_favs = True
delete_messages = True
unfollow = True

# What not to delete

keep_following = [] # Put in a list of people you want to keep following by using their twitter ID's

# delete tweets

if delete_tweets:
	print ("Gathering Tweets")
	my_tweets = tweepy.Cursor(api.user_timeline).items()
	deletion_count = 0

	for tweet in my_tweets:
		if not test_mode:
			api.destroy_status(tweet.id)
		deletion_count += 1
	print ("Deleted %d Tweets!") % (deletion_count)
else:
	print ("Not Deleting Tweets")


# Unfavorite Tweets

if delete_favs:
	print ("Gathering Favorites")
	unfave_count = 0
	fav = tweepy.Cursor(api.favorites).items()

	for hearts in fav:
		if not test_mode:
			api.destroy_favorite(hearts.id)
		unfave_count += 1
	print ("Unfavorited %d Tweets") % (unfave_count)
else:
	print ("Not Unfavoriting Tweets")

# Unfollow

if unfollow:
	print ("Gathering Friends")
	unfollow_count = 0
	keep_follow_count = 0
	friend = tweepy.Cursor(api.friends).items()

	for person in friend:
		if person.id not in keep_following:
			if not test_mode:
				api.destroy_friendship(person.id)
			unfollow_count += 1
		else:
			keep_follow_count += 1
	print ("Unfollowed %d people and kept following %d") % (unfollow_count, keep_follow_count)
else:
	print ("Not unfollowing anyone")

# Delete Messages

if delete_messages:
	print ("Gathering Messages")
	message_delete_count = 0
	message = tweepy.Cursor(api.direct_messages).items()
	for dm in message:
		if not test_mode:
			api.destroy_direct_message(dm.id)
		message_delete_count += 1
	print ("Deleted %d Messages") % (message_delete_count)
else:
	print ("Not Deleting Messages")













