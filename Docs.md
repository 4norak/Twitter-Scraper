# Twitter Secret API

## Endpoints

### Actication

#### Description
Returns a guest token needed for most other endpoints

#### URL
https://api.twitter.com/1.1/guest/activate.json

#### Request Method
POST

#### Parameters
None

#### Needed Headers
|Name|Value|
|----|-----|
|authorization|Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA|

### User ID and other information

#### Description
Returns a couple of user information, including the id needed for most other endpoints that require a user to be specified

#### URL
https://twitter.com/i/api/graphql/G07SmTUd0Mx7qy3Az_b52w/UserByScreenNameWithoutResults

#### Request Method
GET

#### Parameters
|Name|Value|
|----|-----|
|variables|A percentage encoded dictionary (see below)|

##### variables dictionary needed values
|Key|Value|
|---|-----|
|screen_name|The user's screen name as shown in the URL|
|withHighlightedLabel|Some boolean, no idea what it does, just set it to false|
|withSuperFollowsUserFields|Some boolean, no idea what it does, just set it to false|

#### Needed headers
|Name|Value|
|----|-----|
|x-guest-token|The token you recieved from the activation-endpoint|
|authorization|Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA|

### User's tweets

#### Description
Return a list of tweets by a specific user

#### URL
https://twitter.com/i/api/graphql/tuxTEoMUHJKKITSu6jPj4w/UserTweets

#### Request Method
GET

#### Parameters
|Name|Value|
|----|-----|
|variables|A percentage encoded dictionary (see below)|

##### variables dictionary needed values
|Key|Value|
|---|-----|
|userId|The user's id as a string (see "User ID and other information)|
|count|The number of tweets to get|
|withHighlightedLabel|Some boolean value, no idea what it does, just set it to false|
|withTweetQuoteCount|Boolean, include how often the tweet was quoted|
|includePromotedContent|Some boolean value, no idea what it does, just set it to false|
|withTweetResult|Some boolean value, no idea what it does, just set it to false|
|withReactions|Some boolean value, no idea what it does, just set it to false|
|withSuperFollowsTweetFields|Some boolean value, no idea what it does, just set it to false|
|withSuperFollowsUserFields|Some boolean value, no idea what it does, just set it to false|
|withVoice|Some boolean value, no idea what it does, just set it to false|
|withBirdwatchPivots|Some boolean value, no idea what it does, just set it to false|

#### Needed headers
|Name|Value|
|----|-----|
|x-guest-token|The token you recieved from the activation-endpoint|
|authorization|Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA|
