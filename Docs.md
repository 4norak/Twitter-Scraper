# Twitter Secret API


## Endpoints


### Actication

#### Description
Returns a guest token required for most other endpoints.

#### URL
https://api.twitter.com/1.1/guest/activate.json

#### Request Method
POST

#### Parameters
None

#### Required Headers
|Name|Value|
|----|-----|
|authorization|Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA|

### User ID and other information

#### Description
Returns a couple of user information, including the id required for most other endpoints that require a user to be specified.

#### URL
https://twitter.com/i/api/graphql/G07SmTUd0Mx7qy3Az_b52w/UserByScreenNameWithoutResults

#### Request Method
GET

#### Parameters
|Name|Required|Value|
|----|--------|-----|
|variables|:heavy_check_mark:|A percentage encoded dictionary (see below)|

##### variables dictionary values
|Key|Required|Value|
|---|--------|-----|
|screen_name|:heavy_check_mark:|The user's screen name as shown in the URL|
|withHighlightedLabel|:heavy_check_mark:|Some boolean, no idea what it does, just set it to false|
|withSuperFollowsUserFields|:heavy_check_mark:|Some boolean, no idea what it does, just set it to false|

#### Required headers
|Name|Value|
|----|-----|
|x-guest-token|The token you recieved from the activation endpoint|
|authorization|Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA|


### User's tweets

#### Description
Return a list of tweets by a specific user

#### URL
https://twitter.com/i/api/graphql/tuxTEoMUHJKKITSu6jPj4w/UserTweets

#### Request Method
GET

#### Parameters
|Name|Required|Value|
|----|--------|-----|
|variables|:heavy_check_mark:|A percentage encoded dictionary (see below)|

##### variables dictionary values
|Key|Required|Value|
|---|--------|-----|
|userId|:heavy_check_mark:|The user's id as a string (see "User ID and other information")|
|count|:heavy_check_mark:|The number of tweets to get|
|withHighlightedLabel|:heavy_check_mark:|Some boolean value, no idea what it does, just set it to false|
|withTweetQuoteCount|:heavy_check_mark:|Boolean, include how often the tweet was quoted|
|includePromotedContent|:heavy_check_mark:|Some boolean value, no idea what it does, just set it to false|
|withTweetResult|:heavy_check_mark:|Some boolean value, no idea what it does, just set it to false|
|withReactions|:heavy_check_mark:|Some boolean value, no idea what it does, just set it to false|
|withSuperFollowsTweetFields|:heavy_check_mark:|Some boolean value, no idea what it does, just set it to false|
|withSuperFollowsUserFields|:heavy_check_mark:|Some boolean value, no idea what it does, just set it to false|
|withVoice|:heavy_check_mark:|Some boolean value, no idea what it does, just set it to false|
|withBirdwatchPivots|:heavy_check_mark:|Some boolean value, no idea what it does, just set it to false|

#### Required headers
|Name|Value|
|----|-----|
|x-guest-token|The token you recieved from the activation-endpoint|
|authorization|Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA|
