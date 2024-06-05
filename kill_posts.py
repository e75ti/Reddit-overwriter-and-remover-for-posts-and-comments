import praw
import pandas as pd
from wonderwords import RandomWord
from time import sleep

delete = True # Set to False if running first time and wait 30 days for overwrite to propagate

df = pd.read_csv('posts.csv')
reddit = praw.Reddit(
    client_id="XXXX",
    client_secret="XXXX",
    password="XXXX",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/127.1",
    username="XXXX",
    ratelimit_seconds=600
)

reddit.validate_on_submit = True
file_log = open("posts_deleting_py.log","a")
counter = 0

for postId in df['id']:
    counter += 1
    r = RandomWord()
    overwrite_string = ' '.join(r.random_words(70))
    try:
        print(str(counter) + "/" + str(len(df.index)) + " | Processing post " + str(postId))
        post = reddit.submission(postId)
        post.edit(overwrite_string)
        if delete == True:
            sleep(3)
            post.delete()
        print("Processed succesfully post " + str(postId) + "\n")
        file_log.write("OK " + str(postId) + "\n")
    except Exception as ex:
        print("Error processing post with id " + str(postId) + " because: " + str(ex))
        file_log.write("Error " + str(postId) + " because:" + str(ex) + "\n")
    sleep(3)
file_log.close()
