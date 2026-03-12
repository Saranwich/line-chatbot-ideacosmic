from linebot.v3.messaging import (
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
    
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent

def process_follow_message(event : MessageEvent, configuration : TextMessageContent):
    with ApiClient(configuration) as api_client :
        line_bot_api = MessagingApi(api_client)
        
        user_id = event.source.user_id
        profile = line_bot_api.get_profile(user_id)
        user_display_name = profile.display_name
        
        reply_message = (
            f"สวัสดี {user_display_name}! ดีใจที่ได้เป็นเพื่อนกันนะครับ "
            "ผมชื่อ IdeaCosmic เป็นผู้ช่วยที่จะคอยช่วยจำงานต่างๆ ให้คุณครับ\n\n"
            "วิธีใช้ง่ายๆ แค่พิมพ์บอกผมว่า 'เตือนให้ซื้อนมตอน 8 โมง' ผมก็จะจำไว้ให้ทันทีเลยครับ!"
        )

        line_bot_api.reply_message(
            ReplyMessageRequest(
                replyToken = event.reply_token,
                messages= [TextMessage(text=reply_message)]
                )
        )