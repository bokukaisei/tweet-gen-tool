
import streamlit as st

st.set_page_config(page_title="煽り系ツイート生成ツール", layout="centered")

st.title("1ツイート煽り系ジェネレーター")
st.caption("URLと特徴を入れるだけ。1行構成＋TinyURL付きで出力されます。")

# 入力欄
url = st.text_input("動画URL（例：https://gofile.io/d/xxxxxx）")
note1 = st.text_input("特徴1（例：自撮りでコレはハマる）")
note2 = st.text_input("特徴2（例：自撮りしながら放出）")

tiny_choices = [
    "ランダムにする",
    "リンクを付けない",
    "http://tiny.cc/gyo1",
    "http://tiny.cc/gyo2",
    "http://tiny.cc/penyo",
    "http://tiny.cc/penyo2",
    "http://tiny.cc/mute1",
    "http://tiny.cc/mute2",
    "http://tiny.cc/re858",
    "http://tiny.cc/re8582",
    "http://tiny.cc/zoryo",
    "http://tiny.cc/zoryo2",
    "http://tiny.cc/kuna663",
    "http://tiny.cc/kuna6634",
    "http://tiny.cc/chap2",
    "http://tiny.cc/chap1",
    "http://tiny.cc/m4vf001",
    "http://tiny.cc/o4vf001",
    "http://tiny.cc/w4vf001",
    "http://tiny.cc/y4vf001",
    "http://tiny.cc/haruka694",
    "http://tiny.cc/05vf001"
]

selected_tiny = st.selectbox("TinyURLを選んでください（または付けない）", tiny_choices)

def get_final_tiny():
    if selected_tiny == "ランダムにする":
        import random
        return random.choice(tiny_choices[2:])
    elif selected_tiny == "リンクを付けない":
        return ""
    else:
        return selected_tiny

def generate_tweet(url, note1, note2, tiny):
    templates = [
        f"{note1}、{note2}とかガチで反則すぎる {url} {tiny}",
        f"{note1}で{note2}、こんなん見たら止まらん {url} {tiny}",
        f"{note1}だけでも強いのに{note2}までやってくる {url} {tiny}",
        f"{note2}ってるのに{note1}とか、天才か？ {url} {tiny}",
        f"{note1}の時点でやばいのに{note2}までしてくるの草 {url} {tiny}"
    ]
    import random
    tweet = random.choice(templates)
    return tweet.strip()

# ボタン
if st.button("ツイート文を生成する"):
    if url and note1 and note2:
        tiny_url = get_final_tiny()
        tweet = generate_tweet(url, note1, note2, tiny_url)
        st.success("生成されたツイート文：")
        st.code(tweet, language="markdown")
    else:
        st.error("全ての入力欄を埋めてください。")
