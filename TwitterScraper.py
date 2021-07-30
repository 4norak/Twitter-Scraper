import requests
from urllib import parse
import json
from typing import List

class TwitterResources:
    BEARER_TOKEN = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
    ENDPOINT_ACTIVATION = "https://api.twitter.com/1.1/guest/activate.json"
    ENDPOINT_USER = "https://twitter.com/i/api/graphql/G07SmTUd0Mx7qy3Az_b52w/UserByScreenNameWithoutResults"
    ENDPOINT_TWEETS = "https://twitter.com/i/api/graphql/tuxTEoMUHJKKITSu6jPj4w/UserTweets"

def get_guest_token() -> str:
    r = requests.post(TwitterResources.ENDPOINT_ACTIVATION, headers={"authorization": TwitterResources.BEARER_TOKEN})
    return r.json()["guest_token"]

def get_user_id(guestToken: str, screenName: str, *kwargs) -> str:
    params = {"screen_name": screenName,
            "withHighlightedLabel": False,
            "withSuperFollowsUserFields": False}
    params.update(kwargs)
    r = requests.get(f"{TwitterResources.ENDPOINT_USER}?variables={parse.quote(json.dumps(params))}",
            headers={"authorization": TwitterResources.BEARER_TOKEN, "x-guest-token": guestToken})
    return r.json()["data"]["user"]["rest_id"]

def get_user_tweets(guestToken: str, userId: str, count: int, **kwargs) -> List[str]:
    params = {"userId": userId,
            "count": str(count),
            "withHighlightedLabel": False,
            "withTweetQuoteCount": False,
            "includePromotedContent": False,
            "withTweetResult": False,
            "withReactions": False,
            "withSuperFollowsTweetFields": False,
            "withSuperFollowsUserFields": False,
            "withVoice": False,
            "withBirdwatchPivots": False}
    params.update(kwargs)
    r = requests.get(f"{TwitterResources.ENDPOINT_TWEETS}?variables={parse.quote(json.dumps(params))}",
            headers={"authorization": TwitterResources.BEARER_TOKEN, "x-guest-token": guestToken})
    tweetIds = [tweet["content"]["itemContent"]["tweet"]["rest_id"] for tweet in r.json()["data"]["user"]["result"]["timeline"]["timeline"]["instructions"][0]["entries"][:count]]
    return tweetIds
