from linebot.v3.messaging import (
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
    
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent

def process_text_message(event : MessageEvent, configuration : TextMessageContent):
    with ApiClient(configuration) as api_client :
        line_bot_api = MessagingApi(api_client)
        
        user_id = event.source.user_id
        profile = line_bot_api.get_profile(user_id)
        user_display_name = profile.display_name
        
        reply_message = f"Hello {user_display_name}"

        line_bot_api.reply_message(
            ReplyMessageRequest(
                replyToken = event.reply_token,
                messages= [TextMessage(text=reply_message)]
                )
        )
