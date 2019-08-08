import praw
import config
import re
import urlextract
import time
import os

def bot_login():
	print("Logging in...")
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = config.user_agent)
	print("Logged in!")

	return r
  
from urlextract import URLExtract
extractor = URLExtract()

llb = "youtube.com"
slb = "youtu.be"

linksearch = [llb, slb]

inv = "invidio.us"

lowerlink = []
newlink = []
comments_replied_to = []

file = open('comments_replied_to.txt', 'r')
commentlist = file.readlines()

def run_bot(r, comments_replied_to):
	print("Searching last 10 comments")
	for linkbase in linksearch:
		for comment in r.subreddit('Trolysis').comments(limit=10):
			if linkbase in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me() and comment.id not in commentlist:
				print("String with " + linkbase + " found in comment " + comment.id)
				links = extractor.find_urls(comment.body)
				print(links)
				for link in links:
					lowerlink.append(link.lower())
				for link in lowerlink:
					if link.startswith("http"):
						if llb in link:
							newlink.append(re.sub(llb, inv, link))
						elif slb in link:
							newlink.append(re.sub(slb, inv, link))
					else:
						if llb in link:
							newlink.append("https://" + re.sub(llb, inv, link))
						elif slb in link:
							newlink.append("https://" + re.sub(slb, inv, link))
				comment.reply("Hey, I noticed you linked a YouTube video in your comment. For privacy, here are your links converted to invidio.us: \n" + (' \n \n'.join(newlink)) + "\n" + "\nI am a bot. This comment was performed automatically.")
				print("Replied to comment " + comment.id)
				newlink.clear()
				links.clear()
				lowerlink.clear()
				commentlist.append(comment.id)
				with open ("comments_replied_to.txt", "a") as f:
					f.write(comment.id + "\n")

		print("Search Completed.")

		print(comments_replied_to)

		print("Sleeping for 10 seconds...")
		#Sleep for 10 seconds...
		time.sleep(10)

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = filter(None, comments_replied_to)

	return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
	run_bot(r, comments_replied_to)
