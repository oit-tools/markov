import tweepy
from dotenv import load_dotenv
import os
import unicodedata
import re


# ツイートを取得する
def get_tweets():
    # 環境変数の読み込み
    load_dotenv()
    client = tweepy.Client(bearer_token=os.environ["BT"])
    OITWC_LIST_ID = "1516921724033728512"
    token = None
    count = 0
    text_list = list()
    # GET_TWEET_LIMIT = 100  # 取得するツイートの上限

    while True:
        tweets = client.get_list_tweets(
            id=OITWC_LIST_ID, pagination_token=token)

        for i in range(len(tweets[0])):
            # ツイートの文字列を取得
            text = (tweets[0][i].text)
            # リツイートを除外
            if "RT" in text:
                continue
            # 質問箱を除外
            if "みんなからの匿名" in text:
                continue
            # 文字列を整える
            text = format_text(text)
            # リストに追加
            text_list.append(text)
            # 取得したツイート数をカウント
            count += 1

            # ツイート取得数が上限に達したらループを抜ける
            # if i >= GET_TWEET_LIMIT:
            #     break

        # ツイート取得数が上限に達していない場合は次のページを取得
        try:
            token = ((tweets[3])["next_token"])
        except KeyError:
            break

    return text_list , count


# 文字列を整える
def format_text(text):
    # NG.txtを読み込む
    with open("ng.txt", "r", encoding="utf-8") as f:
        ng_word = f.read().splitlines()
    breaking_chars = ["(", ")", "[", "]", '"', "'"]

    # 正規化
    text = unicodedata.normalize("NFKC", text)
    # 改行、半角スペース、全角スペース、URL、メンション、ハッシュタグを除外
    text = re.sub(r"\r|\n| |\u3000|http\S+|@\S+|#\S+", "", text)
    # breaking_charsを除外
    for char in breaking_chars:
        text = text.replace(char, "")
    # NGワードを除外
    for ng in ng_word:
        text = text.replace(ng, "")

    return text


def main():
    # ツイートを取得
    text_list , count = get_tweets()

    return text_list , count


if __name__ == "__main__":
    main()
