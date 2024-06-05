# Overwrite and delete all your Reddit data using Python Reddit API Wrapper (PRAW):
Hello. This program uses the *wonderwords* python library to first generate a collection of random words to edit your comments and posts with. The python scripts are ran individually for posts and comments. You also need *pandas* and *praw* python libraries.

Said libraries can be installed with pip -> `pip3 install -r requirements.txt` or `pip3 install wonderwords pandas praw`

## Running the program
It's suggested you run the programs first with with delete disabled and then wait 30 days before running the full program (with overwrite and delete enabled) to allow the edited posts and comments to propagate into backup.

You run the program with Python 3:
```
$ python3 kill_comments.py
$ python3 kill_posts.py
```
After the program runs successfully you will have a log file with all processed comments 
You will need to either run a venv in which you will install with pip3 the wonderwords library or you could install it globally if your system supports such also with pip3.

## Running prerequisites and warnings:
_Warning: Use it at your own risk. Will remove all data. The editing behaviour will get you banned from some subs, which may not be reversible. Tested working on Debian._

### SETUP:

Request your data export here: https://www.reddit.com/settings/data-request and wait for a link.

Create a new app here: `https://www.reddit.com/prefs/apps/` -- select "script". You have to enter a redirect URI; you can use `http://localhost:8080`

- Register to use the API as described here: `https://www.reddit.com/wiki/api` -- you need to create the app first (see above), because you need the ID from the app for the registration form. Wait for the confirmation email.
- Install the praw and pandas Python libraries with pip.
- Add the plaintext reddit username and password to code (there are more secure ways to prompt for this, but you should only need to run this script once, and can then delete it or overwrite the value).
- Add the ID and secret from the app you created.
- Copy the comments.csv and posts.csv file to the directory.
- Run the script, and wait for it to finish.

This script will log when an attempt to edit a comment returned an error response, and continue. This seems to happen when a comment in the backup is part of a deleted thread (this results in a 403).

_Inspiration and text is originally from [here](https://gist.github.com/confluence/3c9637a679ce4e65cfe9df9acee8796a)_
