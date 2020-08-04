from linebot import (LineBotApi)
from linebot.models import (
    TextSendMessage,QuickReplyButton,QuickReply,MessageAction)


#TODO:創造line_bot_api
line_bot_api = LineBotApi('EHs7+foRB5Ucx23bz14MKwzAePKbJDeonDsOMOlcksS1MFk1cZ3jFjdbQz5iHFUsi1RpecUtZCGfn25PWkM8Ftz2e3zSE9KttGtXMxULdKUlI/Hk9czu5BYm+uZzjdITSY2j7w+QMDZX950H4ML7dwdB04t89/1O/w1cDnyilFU=')

'''
#TODO:推播給指定用戶
line_bot_api.push_message(
    to="Ufceff163313e89e97b772ecd525c35d1",
    messages=[TextSendMessage("Line的Push推播")])
'''
'''
#TODO:全體廣播
line_bot_api.broadcast(TextSendMessage("全體廣播"))
'''
''''''
#TODO:指定多位用戶
#Quick
message_qnb = QuickReplyButton(action=MessageAction(label="(1)",text="1."))
message_qnb2 = QuickReplyButton(action=MessageAction(label="(2)",text="2. "))
quick_reply_list = QuickReply(items=[message_qnb,message_qnb2])
text_demo_message = TextSendMessage("意圖",quick_reply=quick_reply_list)
line_bot_api.multicast(to=["Ufceff163313e89e97b772ecd525c35d1"],messages=[text_demo_message])
