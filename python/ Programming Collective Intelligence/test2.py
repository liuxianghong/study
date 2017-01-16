from pydelicious import get_popular,get_userposts,get_urlposts
import time
import random

def initiallizeUserDict(tag, count = 5):
	user_dict = {}
	redic = get_popular(tag = tag)[0:count]
	print redic
	for p1 in redic:
		print p1['href']
		for p2 in get_urlposts('https://shop.icio.us/sales/the-limited-edition-black-hawk-drone-hd-camera?utm_source=del.icio.us&utm_medium=referral&utm_campaign=the-limited-edition-black-hawk-drone-hd-camera'):
			user = p2['user']
			user_dict[user] = {}
	return user_dict


def  fillItems(user_dict):
	all_items = {}

	for user in user_dict:
		posts = {}
		for i in xrange(3):
			try:
				posts = get_userposts(user)
				break
			except Exception as e:
				print "Failed user " + user + " , retrying "
				time.sleep(3)
		for post in posts:
			url = post['href']
			print url
			user_dict[user][url] = 1.0
			all_items[url] = 1

	for ratings in user_dict.values():
		for item in all_items:
			if item not in ratings:
				ratings[item] = 0.0

def randomUser(user_dict):
	user = user_dict.keys()[random.randint(0, len(user_dict) - 1)]
	return user
	
