from pyrogram import Client, filters

API_ID = 12345678
API_HASH = "ضع_API_HASH_هنا"
BOT_TOKEN = "ضع_BOT_TOKEN_هنا"

app = Client(
    "yousef_music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "🎵 أهلاً بك في بوت يوسف ميوزك\n\n"
        "استخدم /play لطلب أغنية 🎶"
    )

@app.on_message(filters.command("help"))
async def help_command(client, message):
    await message.reply_text(
        "🎵 أوامر البوت:\n\n"
        "/start - تشغيل البوت\n"
        "/play - تشغيل أغنية\n"
        "/help - المساعدة"
    )

app.run()
