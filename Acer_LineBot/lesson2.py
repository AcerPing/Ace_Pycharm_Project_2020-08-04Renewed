#引用套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

#準備素材
app = Flask(__name__)
#注意開頭及結尾的單引號
line_bot_api = LineBotApi('EHs7+foRB5Ucx23bz14MKwzAePKbJDeonDsOMOlcksS1MFk1cZ3jFjdbQz5iHFUsi1RpecUtZCGfn25PWkM8Ftz2e3zSE9KttGtXMxULdKUlI/Hk9czu5BYm+uZzjdITSY2j7w+QMDZX950H4ML7dwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('aea331bd7df6b63d486271a43028bf8c')

'''
總機收信的流程：
1.驗證信件
2.信件轉發給部門
3.處理不合規的信件

handler如何處理傳來的消息
1.驗證消息
2.轉發
3.處理不合規的信件
'''

@app.route("/callback", methods=['POST'])
def callback():

    #取出驗證所需的東西(不需修改)
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)

    #把寄過來的消息都印出來
    #app.logger.info("Request body: " + body)
    print(body)

    # handle webhook body
    try:
        #handler將body跟signature拿來確認消息的合法性
        #另外還有一用途，轉發給後續的業務邏輯
        handler.handle(body, signature)

    #若訊息不合法，做下面的處理
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        #忽略訊息，並告知Line 400的狀態
        abort(400)

    #若都無問題，就回傳ok
    return 'OK'

#客戶自製的邏輯
#handler收到消息事件，而且是文字消息的時候，做下面的def
@handler.add(MessageEvent, message=TextMessage)

#請line_bot_api回覆用戶，我們剛傳過來的文字
#event指用戶傳來的消息
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

#伺服器啟動
if __name__ == "__main__":
    app.run(host="0.0.0.0")