import os
import uvicorn
from app import config

from dotenv import load_dotenv

from fastapi import FastAPI, Request, HTTPException, Header

from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import (
    MessageEvent, 
    TextMessageContent,
    FollowEvent)

from linebot.v3.messaging import (
    ApiClient, 
    MessagingApi, 
    Configuration, 
    ReplyMessageRequest, 
    TextMessage, 
    # FlexMessage, 
    # Emoji,
)
from app.database import init_db
from app.handlers.message_handler import process_text_message
from app.handlers.follow_handler import process_follow_message

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    print(f"String building the table...")
    init_db()
    yield
    print(f"Shutting down")

app = FastAPI(lifespan=lifespan)

load_dotenv(override=True)

# LINE Access Key
get_access_token = config.LINE_CHANNEL_ACCESS_TOKEN
configuration = Configuration(access_token=get_access_token)
# LINE Secret Key
get_channel_secret = config.LINE_CHANNEL_SECRET
handler = WebhookHandler(channel_secret=get_channel_secret)

@app.post("/callback")
async def callback(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    body_str = body.decode('utf-8')
    try:
        handler.handle(body_str, x_line_signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        raise HTTPException(status_code=400, detail="Invalid signature.")

    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event: MessageEvent):
    
    process_text_message(event, configuration)
    
@handler.add(FollowEvent)
def handle_follow(event: MessageEvent):
    process_follow_message(event, configuration)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")