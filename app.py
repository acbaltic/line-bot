from flask import Flask, request, abort  # 用flask來架設伺服器

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('k/02zjAjk1+VSpd4N6FoWQVWUSzjq0CJYZ69svC89qL4jtT3KuiL+Jb0pw0ziNyj4Sm2yaK/ukZwX27LU9+nVwt+REY2NRQSoNyYmQOKNAmi3/BJ1nscnmKur6mkY8N3u7CgUfL1oFTZudb8dnk1LAdB04t89/1O/w1cDnyilFU=')  # YOUR_CHANNEL_ACCESS_TOKEN
handler = WebhookHandler('3081173db182a0d90db68206ad70ada1')  # YOUR_CHANNEL_SECRET


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text  # 將使用者傳來的訊息存在msg
    s = '你吃飯了嗎？'  # 擬回復的訊息
    line_bot_api.reply_message(
        event.reply_token,
        # TextSendMessage(text=event.message.text))
        TextSendMessage(text= s))


if __name__ == "__main__":
    app.run()
