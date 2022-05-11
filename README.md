# OIT Markov

save.pyでツイートを収集した後、generate.pyでマルコフ連鎖による文章生成を行います。  
生成された文章をtweet.pyでTwitterに投稿しています。  
全てTwitter API v2で動かすことができます。

## Usage

必要に応じてvenv作成

```bash
pip install -r requirements.txt
```

UniDicをダウンロードする

```bash
python -m unidic download
```

generate.pyと同じディレクトリに```.env```ファイルを作成  
```.env```ファイルに  

```text
CK=取得したAPI Key
CS=取得したAPI Key Secret
AT=取得したAccess Token
AS=取得したAccess Token Secret
BT=取得したBearer token
```

をそれぞれ記入し保存する。

```bash
python ./generate.py
```

generate.pyを動作させるとtweets.txtを読み込み、マルコフ連鎖による文章の自動生成を行う。  
生成された文章は標準出力に表示される。

## Misc

Tweetの取得は
[Tweepy](https://github.com/tweepy/tweepy)
を使用し、取得先のリストは
[これ](https://twitter.com/i/lists/1516921724033728512)
を利用。  
形態素解析は
[MeCab](https://github.com/taku910/mecab)
と
[UniDic](https://clrd.ninjal.ac.jp/unidic/)
を使用。  
マルコフ連鎖は
[Markovify](https://github.com/jsvine/markovify)
を利用。
