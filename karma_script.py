import praw

user_agent = ("Tfahl's Reddit Test bot 1.0 by /u/pizzamanzoo")
r = praw.Reddit(user_agent=user_agent)

user_name = "pizzamanzoo"
user = r.get_redditor(user_name)

thing_limit = 99
gen = user.get_submitted(limit=thing_limit)

karma_by_subreddit = {}
for thing in gen:
    subreddit = thing.subreddit.display_name
    karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit,0)
                                     + thing.score)
import pprint
pprint.pprint(karma_by_subreddit)


