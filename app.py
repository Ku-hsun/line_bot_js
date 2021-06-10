# 載入需要的模組
import os
from datetime import datetime
from flask import Flask, abort, request
# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)
# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))
# 接收 LINE 的資訊
@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)
        print(body)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"



# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        try:
            if event.message.text == "圖片": line_bot_api.reply_message(event.reply_token,
                                                                      ImageSendMessage(original_content_url='https://firebasestorage.googleapis.com/v0/b/fast-mariner-312118.appspot.com/o/2021_06_08%2Fsleep_2021_06_08_17_54_17_481872.png?alt=media&token=2dadb535-c1c4-48f8-867c-38114db30d34',
                                                                                       preview_image_url='https://firebasestorage.googleapis.com/v0/b/fast-mariner-312118.appspot.com/o/2021_06_08%2Fsleep_2021_06_08_17_54_17_481872.png?alt=media&token=2dadb535-c1c4-48f8-867c-38114db30d34'))

        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='沒收到訊息再發送一次'))
        
    # Send To Line
    # reply =TextSendMessage(text = fun1+'$ LINE 0x100001 $', emojis=[emoji])
    line_bot_api.reply_message(event.reply_token, reply)
if __name__ == "__main__":
    app.run()
