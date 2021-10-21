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

### User ID and other User Information

#### Description
Returns a couple of user information, including the id required for most other endpoints that require a user to be specified.

#### URL
https://twitter.com/i/api/graphql/G07SmTUd0Mx7qy3Az_b52w/UserByScreenNameWithoutResults

#### Request Method
GET

#### Parameters
|Name|Required|Type|Value|
|----|:------:|----|-----|
|variables|:heavy_check_mark:|String|A percentage encoded json dictionary (see below)|

##### variables dictionary values
|Key|Required|Type|Value|
|---|:------:|----|-----|
|screen_name|:heavy_check_mark:|String|The user's screen name as shown in the URL|
|withHighlightedLabel|:heavy_check_mark:|Boolean|No idea what it does, just set it to false|
|withSuperFollowsUserFields|:heavy_check_mark:|Boolean|No idea what it does, just set it to false|

#### Required Headers
|Name|Value|
|----|-----|
|x-guest-token|The token you recieved from the activation endpoint|
|authorization|Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA|


### User's Tweets

#### Description
Return a list of tweets by a specific user

#### URL
https://twitter.com/i/api/graphql/tuxTEoMUHJKKITSu6jPj4w/UserTweets

#### Request Method
GET

#### Parameters
|Name|Required|Type|Value|
|----|:------:|----|-----|
|variables|:heavy_check_mark:|String|A percentage encoded json dictionary (see below)|

##### variables dictionary values
|Key|Required|Type|Value|
|---|:------:|----|-----|
|count|:heavy_check_mark:|Integer|The number of tweets to get|
|userId|:heavy_check_mark:|String|The user's id (see "User ID and other User Information")|
|withVoice|:heavy_check_mark:|Boolean|No idea what it does, just set it to false|
|withReactions|:heavy_check_mark:|Boolean|No idea what it does, just set it to false|
|withTweetResult|:heavy_check_mark:|Boolean|No idea what it does, just set it to false|
|withTweetQuoteCount|:heavy_check_mark:|Boolean|Include how often the tweet was quoted|
|withBirdwatchPivots|:heavy_check_mark:|Boolean|No idea what it does, just set it to false|
|withHighlightedLabel|:heavy_check_mark:|Boolean|No idea what it does, just set it to false|
|includePromotedContent|:heavy_check_mark:|Boolean|No idea what it does, just set it to false|
|withSuperFollowsUserFields|:heavy_check_mark:|Boolean|No idea what it does, just set it to false|
|withSuperFollowsTweetFields|:heavy_check_mark:|Boolean|No idea what it does, just set it to false|

#### Required Headers
|Name|Value|
|----|-----|
|x-guest-token|The token you recieved from the activation-endpoint|
|authorization|Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA|


### Search

#### Description
Search twitter

#### URL
https://twitter.com/i/api/2/search/adaptive.json

#### Request Method
GET

#### Parameters
|Name|Required|Type|Values|
|----|:------:|------|
|q|:heavy_check_mark:|String|The search string|
|pc| |Boolean|Seems to do nothing|
|ext| |String|Percentage encoded comma separated fields to include in "ext" field|
|count| |Integer|The number of results|
|tweet_mode| |String|Defines the verbosity of information about tweets. Twitter's website uses "extended"|
|skip_status| |Boolean|Seems to do nothing|
|query_source| |String|?. Twitter's website uses "typed_query"|
|include_cards| |Boolean|Include tweet cards (link previews)|
|cards_platform| |String|Platform for tweet cards fields (link previews). Twitter's website uses "Web-12"|
|include_can_dm| |Boolean|Include some can_dm parameter for users included in the answer|
|include_blocking| |Boolean|Include the users a user included in the answer has blocked|
|include_entities| |Boolean|Include tweets' entities (hashtags,symbols,user mentions,urls,media)|
|include_mute_edge| |Boolean|Include some muting parameter for users included in the answer|
|include_blocked_by| |Boolean|Include the users a user included in the answer has been blocked by|
|include_error_codes| |Boolean|?|
|include_followed_by| |Boolean|Include the users following a user included in the answer|
|include_quote_count| |Boolean|Include tweets' quote counts|
|include_reply_count| |Boolean|Include tweets' reply count|
|simple_quoted_tweet| |Boolean|?|
|include_ext_alt_text| |Boolean|Include alt text for extended entities|
|spelling_corrections| |Boolean|Seems to do nothing|
|include_can_media_tag| |Boolean|Seems to do nothing|
|include_want_retweets| |Boolean|Include some want_retweets parameter for users included in the answer|
|include_ext_media_color| |Boolean|Include extensions media colors|
|include_ext_media_availability| |Boolean|Include extensions media availability (seems to always be null)|
|include_profile_interstitial_type| |Boolean|Include some profile_interstitial_type parameter for users included in the answer|

#### Required Headers
|Name|Value|
|----|-----|
|x-guest-token|The token you recieved from the activation-endpoint|
|authorization|Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA|
