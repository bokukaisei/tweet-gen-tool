import streamlit as st
import random

st.set_page_config(page_title="煽り系ツイート生成ツール", layout="centered")

st.title("1ツイート煽り系ジェネレーター")
st.caption("URLと特徴を入れるだけ。1行構成＋TinyURL付きで出力されます。")

# 入力欄
url = st.text_input("動画URL（例：https://gofile.io/d/xxxxxx）")
note1 = st.text_input("特徴1（例：自撮りでコレはハマる）")
note2 = st.text_input("特徴2（例：自撮りしながら放出）")

tiny_urls = [
    "http://tiny.cc/gyo1",
    "http://tiny.cc/gyo2",
    "http://tiny.cc/mute1",
    "http://tiny.cc/mute2"
]

def generate_tweet(url, note1, note2):
    templates = [
        f"{note1}、{note2}とかガチで反則すぎる {url} {{tiny}}",
        f"{note1}で{note2}、こんなん見たら止まらん {url} {{tiny}}",
        f"{note1}だけでも強いのに{note2}までやってくる {url} {{tiny}}",
        f"{note2}ってるのに{note1}とか、天才か？ {url} {{tiny}}",
        f"{note1}の時点でやばいのに{note2}までしてくるの草 {url} {{tiny}}"
    ]
    template = random.choice(templates)
    tiny = random.choice(tiny_urls)
    return template.replace("{tiny}", tiny)

# ボタン
if st.button("ツイート文を生成する"):
    if url and note1 and note2:
        tweet = generate_tweet(url, note1, note2)
        st.success("生成されたツイート文：")
        st.code(tweet, language="markdown")
    else:
        st.error("全ての入力欄を埋めてください。")
