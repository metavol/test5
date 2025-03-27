import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


# タイトル
st.title("株価チャート表示アプリ")

# テキストボックス
ticker = st.text_input("銘柄（ティッカーシンボルを入力してください）", value="AAPL")

# ボタン
if st.button("株価取得"):
    try:
        # 株価データ取得
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1mo")  # 過去1か月のデータ

        if hist.empty:
            st.error("データが見つかりませんでした。正しいティッカーを入力してください。")
        else:
            # チャートの描画
            st.subheader(f"{ticker} の株価推移")
            fig, ax = plt.subplots()
            ax.plot(hist.index, hist["Close"], label="Close Price", color="blue")
            ax.set_xlabel("日付")
            ax.set_ylabel("株価")
            ax.legend()
            st.pyplot(fig)

    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
