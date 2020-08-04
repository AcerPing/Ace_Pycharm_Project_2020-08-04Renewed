from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,ImageMessage,FollowEvent,
    TemplateSendMessage,ButtonsTemplate,MessageAction,URIAction,PostbackAction,PostbackEvent,QuickReply,QuickReplyButton,
    LocationAction,VideoMessage,AudioMessage)

import json

app = Flask(__name__)

line_bot_api = LineBotApi('EHs7+foRB5Ucx23bz14MKwzAePKbJDeonDsOMOlcksS1MFk1cZ3jFjdbQz5iHFUsi1RpecUtZCGfn25PWkM8Ftz2e3zSE9KttGtXMxULdKUlI/Hk9czu5BYm+uZzjdITSY2j7w+QMDZX950H4ML7dwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('aea331bd7df6b63d486271a43028bf8c')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    print(body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

'''
告知handler
若收到關注事件，
    則取人家個資，並打印出來
        打印出來太low，準備存成檔案
            引用json模組
                把python的變數轉換成json格式
                    用with存入檔案內
    送文字消息給用戶
        引入文字消息套件
        生成文字消息
        交給Line_bot_api做信息回覆
    送圖片消息給用戶
        引入圖片消息套件
        生成圖片消息
            要準備兩張圖片的https link
        交給Line_bot_api做信息回覆
        
    訟按鍵範本消息給用戶
        引入按鍵範本消息按鍵
        生成範本消息
            準備很多，簇繁不及備載
        交給Line_bot_api做信息回覆
        
'''
@handler.add(FollowEvent)
def handle_message(event):
    #TODO:取得用戶個資
    user_profile = line_bot_api.get_profile(event.source.user_id)
    # print(user_profile)
    # print(user_profile.user_id)
    # print(user_profile.picture_url)

    #TODO:開啟一個檔案，將用戶個資轉成json格式，存入檔案內
    with open("./user.txt","a") as myfile:
        myfile.write(
            json.dumps(
                vars(user_profile)))
        #TODO:新資料換行
        myfile.write('\r\n')

    #TODO:建立文字消息
    follow_text_send_message = TextSendMessage("LineBot機器人－山岸逢花")

    #TODO:建立圖片消息
    follow_image_send_message = ImageSendMessage(
        original_content_url='https://cdn2.ettoday.net/images/4913/d4913197.jpg',
        preview_image_url='https://cdn-origin.cool-style.com.tw/cool/2020/04/91810013_442464159886024_3948554206271952495_n.png'
    )

    #TODO:建立範本消息
    # alt_text:消息在Line聊天列表的替代文字
    # template:Carousel,Button,Confirm,ImageCarousel
    # title:標題
    # text:描述
    # actions:按鍵
    #   MessageAction:
    #       label:按鍵的字樣
    #       text:當用戶點擊時，以用戶身分發出的文字，串接場景
    #   URIAction:
    #       label:按鍵的字樣
    #       uri:網址
    #   PostbackAction:
    #       label:
    #       text:會發一個MessageEvent，且為TextMessage
    #       data:會發一個PostbackEvent給我們
    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://example.com/image.jpg',
            title='Menu',
            text='Please select',
            actions=[
            MessageAction(label='message',
                          text='message text'),
            # URIAction(label="網址按鍵", uri="https://www3.nhk.or.jp/news/easy/")
            URIAction(label="立即聯絡TRE購票",uri="tel://0958365"),
            URIAction(label="分享你的女優",uri="https://line.me/R/nv/camera/"),
            #PostbackAction(label='以後常用的回傳動作', text='以用戶身分發話', data="special")
            #如何解析 多欄位的data
            #python querystring parser
            PostbackAction(label='以後常用的回傳動作',text='以用戶身分發話',data="itme=123&brand=asus&log=ec2")]))

    '''
    用json生成模板消息
        讀取本地的json檔案-json.load 取得json物件
        將json物件放入TemplateSendMessage的new_from_json_dict方法，並存在變數內即可
    '''
    with open("./sendmessage.json","r",encoding="utf8") as jsonfile:
        json_object = json.load(jsonfile)
    template_message_from_json = TemplateSendMessage.new_from_json_dict(json_object)


    #TODO:麻煩line_bot_api，把文字消息交給line
    line_bot_api.reply_message(event.reply_token,[follow_text_send_message,follow_image_send_message,buttons_template_message,template_message_from_json])


'''
收到文字消息的時候
他打啥，我就回傳啥
'''
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    #TODO:把用戶的話轉成文字發送消息
    reply_text_message = TextSendMessage(event.message.text)

    '''
    QuickReply:
    我方發消息的時候，可以順道寄一排會消失的按鍵給用戶使用
    '''

    #TODO:創造一個QuickReplyButton
    text_quickreply = QuickReplyButton(action=MessageAction(label="A",text="123"))
    location_quickreply = QuickReplyButton(action=LocationAction(label="助教在哪裡"))

    #TODO:創造一個QuickReply，並把剛剛創建的button放進去
    quick_reply_array = QuickReply(items=[text_quickreply,location_quickreply])

    #TODO:生成一個文字消息
    #把用戶的話轉成文字發送消息
    reply_text_message = TextSendMessage(event.message.text,quick_reply=quick_reply_array)

    #TODO:line_bot_api 傳送回去
    line_bot_api.reply_message(event.reply_token,reply_text_message)

'''
告知handler收到Postback event 做~事情
    判斷Postback的data
        若為specific，則取牠個資
'''
@handler.add(PostbackEvent)
def handle_postback_event(event):
    if event.postback.data == "special":
        user = line_bot_api.get_profile(event.source.user_id)
        print(user)

'''
當用戶發出圖片消息的時候，我們回應她，把他的消息編號傳給他。
'''
@handler.add(MessageEvent,message=ImageMessage)
def handle_image_message(event):
    #用戶的圖片消息id
    message_id=event.message.id

    #TODO:變成文字消息
    image_id_text_send_message = TextSendMessage(text=message_id)

    #TODO:將該文字消息傳回給用戶
    line_bot_api.reply_message(event.reply_token, image_id_text_send_message )

    #TODO:請line_bot_api拿照片回來，娶回一個檔案
    # 得自己存在硬碟內
    #
    content_file = line_bot_api.get_message_content(message_id=message_id)
    #TODO:存圖片必須以二進制的方式存(wb)
    # 但content_file不是二進制的格式，所以得用iter_content()轉成二進制，再寫入到檔案
    # 圖片等多媒體檔案，多以二進制存檔
    with open(message_id+".jpg","wb") as tempfile:
        for chunk in content_file.iter_content():
            tempfile.write(chunk)

'''
用戶傳影片給我們，我們把影片存回給本地端
1.引用套件
2.handler.add
3.客制化logic
'''
@handler.add(MessageEvent,message=VideoMessage)
def handle_video_message(event):
    #TODO:line_bot_api向line取回影片
    video_content = line_bot_api.get_message_content(event.message.id)

    #TODO:開啟一個以message_id為名的影片檔案，並要求line_bot_api把影片轉成二進制檔案，寫入
    with open(event.message.id+".mp4","wb") as video_file:
        for chunk in video_content.iter_content():
            video_file.write(chunk)

'''
用戶傳聲音檔給我們，我們把影片存回給本地端
'''
@handler.add(MessageEvent,message=AudioMessage)
def handle_audio_message(event):
    #TODO:line_bot_api向line取回影片
    audio_content = line_bot_api.get_message_content(event.message.id)

    #TODO:開啟一個以message_id為名的影片檔案，並要求line_bot_api把影片轉成二進制檔案，寫入
    with open(event.message.id+".mp3","wb") as audio_file:
        for chunk in audio_content.iter_content():
            audio_file.write(chunk)


if __name__ == "__main__":
    app.run(host="0.0.0.0")