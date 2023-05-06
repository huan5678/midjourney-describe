# Midjourney describe transform prompt

[English](./README_EN.md) | 繁體中文

## Midjourney Describe
Midjourney Describe 是一個簡單好用的 Python Flask Web 應用程式，幫助大家快速地處理和轉換所提供的文本。
它讓您能輸入一段帶有 --ar *:* 語法的字串，同時也可以自定義 ar 的值。
---

## 功能介紹
在Midjourney使用命令/describe將取得的result帶emoji數字的文字一起複製，
輸入字串中的數字 emoji 會被自動移除，
可以自定義 ar 值，讓您有更多彈性，
與Prefix可以，讓您輸入在Midjourney中定義的prefix，
可在input欄位中用,分開不同的參數，
按下 "Process" 按鈕後，結果會顯示在下方的文字框中，
提供 "CopyResult" 和 "ClearInput" 兩個實用按鈕，
---

## 安裝和使用說明
請先確保您的電腦已安裝 Python 3.10 或更新的版本

安裝所需的套件：
```
pip install -r requirements.txt
```
執行
```
python3 main.py
```
用瀏覽器打開：http://127.0.0.1:5000
---

## 注意事項
本應用程式僅適用於教學和學習目的，不建議在生產環境中使用
若遇到問題，歡迎提出 Issue 或 Pull Request
祝您使用愉快！