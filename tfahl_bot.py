import time
import praw 

r = praw.Reddit("PRAW bot by /u/pizzamanzoo v 1.0")

r.login()
already_done = []

while True:
    subreddit = r.get_subreddit('scrolls')
    print "Hello"
#    for submission in subreddit.get_hot(limit=10):
    
