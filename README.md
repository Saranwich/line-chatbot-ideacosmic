# 🤖 LINE Chatbot (IdeaCosmic)

Hello there! Welcome to my practice project. This is a LINE Chatbot built with Python. 
I created this project to master LINE Bot development and learn how to write clean, modular code using best practices.

## 📂 1. Project Structure

Here is how the project is organized to keep everything neat and easy to manage:

```text
line-chatbot-ideacosmic/
├── app/
│   ├── __init__.py
│   ├── main.py          # Entry point (LINE Webhook receiver)
│   ├── config.py        # Settings and environment variables
│   ├── handlers/        # Message logic (e.g., text, images)
│   ├── services/        # Connect to LINE Messaging API & outside APIs
│   ├── models/          # Database schema and models
│   ├── utils/           # Helper functions (e.g., math, date formats)
│   └── database/        # Database connection management
├── tests/               # For writing code tests
├── .env                 # Secret Keys (DO NOT upload to GitHub!)
├── .gitignore
├── requirements.txt
└── README.md
```

## 🛠️ 2. Environment Setup

Want to run this bot? Just follow these simple steps!

### Step 1: Virtual Environment
Use your existing venv to keep this project's libraries separate from your main computer system.

### Step 2: Install Dependencies
Open your terminal and run this command to install all the tools we need:

```Bash
pip install line-bot-sdk fastapi uvicorn python-dotenv
```

### Step 3: Environment Variables
Create a file named .env in the main folder and add your secret keys like this:

```code
LINE_CHANNEL_SECRET=<your_secret_here>
LINE_CHANNEL_ACCESS_TOKEN=<your_token_here>
```