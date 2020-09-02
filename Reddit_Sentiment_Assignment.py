# Import all the necessary libraries
import praw # Import the Praw library: https://praw.readthedocs.io/en/latest/code_overview/reddit_instance.html
import pandas as pd # Import Pandas library: https://pandas.pydata.org/
import datetime as dt # Import datetime library
import matplotlib.pyplot as plt # Import Matplot lib for plotting
from tqdm.notebook import tqdm  # progress bar used in loops

import credentials as cred  # make sure to enter your API credentials in the credentials.py file

# Praw (Python Reddit API Wrapper) is used to communicate with Reddit
reddit = praw.Reddit(client_id='5IhZscpEj4ULow',
                     client_secret='hauiAFMbEQgoAQA0N8IioYNB8ZU',
                     user_agent='MSDS600 Scrape')

number_of_posts = 200
time_period = 'all'  # use posts from all time

# .top() can use the time_period argument
# subreddit = reddit.subreddit('').top(time_filter=time_period, limit=number_of_posts)

subreddit = reddit.subreddit('nba').hot(limit=number_of_posts)

# Create an empty list to store the data
subreddit_comments = []

# go through each post in our subreddit and put the comment body and id in our dictionary
# the value for 'total' here needs to match 'limit' in reddit.subreddit().top()
for post in tqdm(subreddit, total=number_of_posts):
    submission = reddit.submission(id=post)
    submission.comments.replace_more(limit=0)  # This line of code expands the comments if “load more comments” and “continue this thread” links are encountered
    for top_level_comment in submission.comments:
        subreddit_comments.append(top_level_comment.body)  # add the comment to our list of comments

print("test TEST")
##subreddit_comments
print(subreddit_comments)
print("...end TESTing")

# This is an example of how we split up the comments into individual words.
# This technique will be used again to get the scores of each individual word.
for comment in subreddit_comments_df['comment']:  # loop over each word
        comment_words = comment.split()  # split comments into individual words
        for word in comment_words:  # loop over idndividual words in each comment
            word = word.strip('?:!.,;"!@()#-')  # remove extraneous characters
            word = word.replace("\n", "")  # remove end of line
            print(word)

        break  # end the loop after one comment

# We load the AFINN sentiment table into a Python dictionary

sentimentfile = open("AFINN-en-165.txt", "r")  # open sentiment file
scores = {}  # an empty dictionary
for line in sentimentfile:  # loop over each word / sentiment score
    word, score = line.split("\t")  # file is tab-delimited
    scores[word] = int(score)  # convert the scores to intergers

sentimentfile.close()

# print out the first 10 entries of the dictionary
counter = 0
for key, value in scores.items():
    print(key, ':', value)
    counter += 1
    if counter >= 10:
        break

####
# we create a dictionary for storing overall counts of sentiment values
##sentiments = {"-5": 0, "-4": 0, "-3": 0, "-2": 0, "-1": 0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0}

##for word in subreddit_comments_df['comment']:  # loop over each word
##        comment_words = word.split()  # split comments into individual words
##        for word in comment_words:  # loop over individual words in each comment
##            word = word.strip('?:!.,;"!@()#-')  # remove extraneous characters
##            word = word.replace("\n", "")  # remove end of line
##            if word in scores.keys():  # check if word is in sentiment dictionary
##                score = scores[word]  # check if word is in sentiment dictionary
##                sentiments[str(score)] += 1  # add one to the sentiment score

# Print the scores
#### for sentiment_value in range(-5, 6):
    # this uses string formatting, more on this here: https://realpython.com/python-f-strings/
    ####### print(f"{sentiment_value} sentiment:", sentiments[str(sentiment_value)])

# this would be equivalent, but obviously much less compact and elegant
# print("-5 sentiments ", sentiments["-5"])
# print("-4 sentiments ", sentiments["-4"])
# print("-3 sentiments ", sentiments["-3"])
# print("-2 sentiments ", sentiments["-2"])
