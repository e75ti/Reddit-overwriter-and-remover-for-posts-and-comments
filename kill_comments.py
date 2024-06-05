import praw
import pandas as pd
from wonderwords import RandomWord
from time import sleep

delete = False # Set to True if running second time after you waited 30 days for overwrite to propagate

df = pd.read_csv('comments.csv')
reddit = praw.Reddit(
    client_id="XXXX",
    client_secret="XXXX",
    password="XXXX",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/127.1",
    username="XXXX",
    ratelimit_seconds=600
)

reddit.validate_on_submit = True
file_log = open("comments_deleting_py.log","a")
counter = 0

for commentId in df['id']:
    counter += 1
    r = RandomWord()
    overwrite_string = ' '.join(r.random_words(70))
    try:
        print(str(counter) + "/" + str(len(df.index)) + " | Processing comment " + str(commentId))
        comment = reddit.comment(commentId)
        comment.edit(overwrite_string)
        if delete == True:
            sleep(3)
            comment.delete()
        print("Processed succesfully comment " + str(commentId) + "\n")
        file_log.write("OK " + str(commentId) + "\n")
    except Exception as ex:
        print("Error processing comment with id " + str(commentId) + " because: " + str(ex))
        file_log.write("Error " + str(commentId) + " because:" + str(ex) + "\n")
    sleep(3)
file_log.close()
