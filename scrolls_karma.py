import praw

user_agent = ("Tfahl's Reddit Test bot 1.0 by /u/pizzamanzoo")
r = praw.Reddit(user_agent=user_agent)

print("Enter Reddit User Name")
user_name = raw_input()
user = r.get_redditor(user_name)

print("Enter subreddit")
sub = raw_input()

thing_limit = 99
gen = user.get_submitted(limit=thing_limit)


karma_by_subreddit = {}
for thing in gen:
    subreddit = thing.subreddit.display_name
    if subreddit == sub:
        karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit,0)
                                         + thing.score)
    
import pprint
pprint.pprint(karma_by_subreddit)




