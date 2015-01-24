#!/usr/bin/env python
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
prawWords = ['test', 'second tes t']
#Opens the post file and reads it into a var
post_file = open("test.md", "r+")
post_text = post_file.read(2955)

while True:
    print "Looking for posts to reply to"
    #Set the subreddit name here
    subreddit = r.get_subreddit('newbie_bot_test')
    #looks at the 10 newest posts
    for submission in subreddit.get_new(limit=10):
        #Looks to see if words are in each submission
        op_text = submission.selftext.lower()
        has_praw = any(string in op_text for string in prawWords)
        #If the words are there, post reply
        if submission.id not in already_done and has_praw:
            #post reply
            print "Posting reply"
            submission.add_comment(post_text)
            #Add this post to the already done list
            already_done.append(submission.id)   
            pass
    print "Sleeping"
    time.sleep(600)
    print "Done sleeping"

    
