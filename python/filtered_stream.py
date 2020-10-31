##
##Version 0.1 of the Social Media Map for Twitter
##Accesses Twitter APIs and executes the code 

##Uses: Twitter APIv2 
##https://developer.twitter.com/en/docs/twitter-api/early-access
##


import requests
import os
import json
import argparse

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def add_headers(expansion):
    expansiondata = 'expansions=attachments.media_keys,referenced_tweets.id,author_id'
    return expansion

def get_rules(headers, bearer_token):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", headers=headers
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(headers, bearer_token, rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(headers, delete, bearer_token, input_hashtag):
    # You can adjust the rules if needed
    rules = [
        {"value": input_hashtag, "tag": input_hashtag},
        #{"value": "cat has:images -grumpy", "tag": "cat pictures"},
    ]
    payload = {"add": rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(headers, set, bearer_token):
    payload ={'expansion': 'author_id'}
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream?expansions=geo.place_id,author_id&place.fields=contained_within,country,country_code,full_name,geo,id,name,place_type&user.fields=location&tweet.fields=geo", headers=headers,  stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=10, sort_keys=True))


def parseParameters():
    # Create the parser
    arg_parser = argparse.ArgumentParser(description='List the content of a folder')

    # Add the arguments
    arg_parser.add_argument('hashtag',
                       metavar='hashtag',
                       type=str,
                       help='Hashtag of the tweet')

    # Execute the parse_args() method
    args = arg_parser.parse_args()

    global input_hashtag 
    input_hashtag = args.hashtag

def main():
    parseParameters()
    bearer_token = os.environ.get("BEARER_TOKEN")
    headers = create_headers(bearer_token)
    rules = get_rules(headers, bearer_token)
    delete = delete_all_rules(headers, bearer_token, rules)
    set = set_rules(headers, delete, bearer_token, input_hashtag)
    get_stream(headers, set, bearer_token)


if __name__ == "__main__":
    main()
