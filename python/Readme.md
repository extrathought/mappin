
# Version 0.1 of the Social Media Map for Twitter

Accesses Twitter APIs and extracts the locations of the tweets

Uses: Twitter APIv2
https://developer.twitter.com/en/docs/twitter-api/early-access

# Pre-requistes: 
1. Twitter Developer Account 
2. BEARER_TOKEN from the twitter developer account 
3. Python3.7

# Instructions
Details of the help menu:
usage: filtered_stream.py [-h] hashtag

Lists Location of the tweets based on the Hashtag

positional arguments:
  hashtag     Hashtag of the tweet

optional arguments:
  -h, --help  show this help message and exit


# To execute: 
run
1. Configure ENV: BEARER_TOKEN
To set your enviornment variables in your terminal run the following line:
export 'BEARER_TOKEN'='<your_bearer_token>'

2. Execute: 
python filtered_stream.py <hashtag>





