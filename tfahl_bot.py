#Newbie Bot created by pizzamanzoo
import time
import praw 

#Set the message for reddit
r = praw.Reddit("Newbie Bot for newbie_bot_test by /u/pizzamanzoo v 1.0")

#login with u/p combo
r.login()
#Initialize list of posts
already_done = []

#Words the bot will look for
prawWords = ['test']


while True:
    #Set the subreddit name here
    subreddit = r.get_subreddit('newbie_bot_test')
    #looks at the 10 newest posts
    for submission in subreddit.get_new(limit=10):
        #Looks to see if words are in each submission
        op_text = submission.selftext.lower()
        has_raw = any(string in op_text for string in prawWords)
        #If the words are there, post reply
        if submission.id not in already_done and has_praw:
            #post reply
            pass
        time.sleep(2000)

    
