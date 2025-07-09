import telebot
import threading
import time

# === CONFIG ===
BOT_TOKEN = "7832911275:AAGqXqBScHOOMyBf8yxSmJmPxenzEBhpFNo"
VIP_CHAT_ID = -1002526774762
FREE_CHAT_ID = -1002717425469
DELAY_SECONDS = 3600  # 1 hour

bot = telebot.TeleBot(BOT_TOKEN)

# === HANDLERS ===

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "✅ Nova Signal Delay Bot is running.\nSend your signals using /signal")

@bot.message_handler(commands=['signal'])
def handle_signal(message):
    signal_text = message.text.replace("/signal", "").strip()
    if not signal_text:
        bot.reply_to(message, "⚠️ Please add signal text after /signal\nExample:\n/signal Sell BTCUSDT at 110000")
        return

    # Send to VIP group immediately
    bot.send_message(VIP_CHAT_ID, f"📢 VIP Signal:\n{signal_text}")
    bot.reply_to(message, "✅ Sent to VIP group.\n⏳ Will send to Free group in 1 hour.")

    # Create a delayed task
    threading.Thread(target=delayed_send, args=(signal_text,)).start()

def delayed_send(text):
    time.sleep(DELAY_SECONDS)
    bot.send_message(FREE_CHAT_ID, f"📢 Free Signal (Delayed 1h):\n{text}")

# === RUN ===
print("🚀 Nova Delay Bot is running...")
bot.polling()
