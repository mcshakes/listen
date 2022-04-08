import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    user_agent = "Comment Extraction (by u/butterbutt)",
    client_id = os.getenv("CLIENT_ID"),
    client_secret = os.getenv("CLIENT_SECRET"),
)

# Go through all the new posts and collect the titles
short_squeeze = reddit.subreddit("Shortsqueeze")

for post in short_squeeze.new(limit=25):
    print(post.title)


#  Check for capitalizations
#  Check for money $XCUR


#  Dictionary