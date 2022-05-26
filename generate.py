import MeCab
import markovify
import re
import collect


# 正規化
def normalization(texts):
    normalized_texts = list(str())

    for text in texts:
        normalized_texts.append(re.sub(
            '\'|\"|\(|\)|\[|\]|\r|<br />|\u3000|-|\||https?://[!\?/\+\-_~=;\.,\*&@#\$%\(\)\'\[\]]+|@[\\w]{1,15}', ' ', text))

    return normalized_texts


# 形態素解析
def parse_texts(normalized_texts):
    mecab = MeCab.Tagger("-Owakati")
    parsed_texts = str()

    for text in normalized_texts:
        parsed = mecab.parse(text)
        for token in parsed:
            if token == "\n":
                continue
            parsed_texts += token
            if token == "。":
                parsed_texts += "\n"

    return parsed_texts


# 文章生成
def gen_sentence(parsed_text):
    STATE_SIZE = 2
    model = markovify.NewlineText(parsed_text, state_size=STATE_SIZE)
    sentence = None

    # 文が生成されるまで繰り返し
    while sentence == None:
        try:
            sentence = model.make_short_sentence(140)
        except Exception as e:
            print(e)

    sentence = "".join(sentence.split())

    return sentence


def main():
    # ツイートを取得
    texts , count = collect.main()
    # 正規化
    parsed_text = parse_texts(normalization(texts))
    # 文章生成
    sentence = gen_sentence(parsed_text)

    # 表示
    print(sentence, end="")
    print("["+str(len(sentence))+"文字]", end="")
    print("[解析ツイート数: "+str(count) + "]")

    return sentence


if __name__ == "__main__":
    main()
