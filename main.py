# -*- coding: utf-8 -*-
import json
import config
from requests_oauthlib import OAuth1Session

# OAuth認証
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

# Twitter Endpoint(検索結果を取得する)
url = 'https://api.twitter.com/1.1/search/tweets.json'


def search_tweet(keyword):
    params = {
             'count': 20,  # 取得するtweet数
             'q': keyword  # 検索キーワード
             }

    req = twitter.get(url, params=params)

    if req.status_code == 200:
        res = json.loads(req.text)
        for line in res['statuses']:
            print(line['text'])
    else:
        print("Failed: %d" % req.status_code)


# Enedpointへ渡すパラメーター
lis = [chr(i) for i in range(12353, 12436)]
search_words = [a+b+c+d for a in lis for b in lis for c in lis for d in lis]

for word in search_words:
    print(word+":")
    search_tweet(word)
    sleep(3)
