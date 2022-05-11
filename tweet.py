import tweepy
from dotenv import load_dotenv
import os
import generate


def tweet(sentence):
    # 環境変数の読み込み
    load_dotenv()
    client = tweepy.Client(bearer_token=os.environ["BT"], consumer_key=os.environ["CK"],
                           consumer_secret=os.environ["CS"], access_token=os.environ["AT"],
                           access_token_secret=os.environ["AS"])

    # ツイートする
    client.create_tweet(text=sentence)


def main():
    # 文章を生成
    sentence = generate.main()
    # ツイートする
    tweet(sentence)


if __name__ == "__main__":
    main()
