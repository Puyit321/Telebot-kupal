from time import time

def uptime(msg, bot, i):
  uptime = int(f"{time() - i.bot.start_time:.0f}")
  h,m,s = uptime//3600, (uptime%3600) // 60, uptime%60
  
  tid = msg.chat.id
  text = f"{i.font('bold', 'BOT UPTIME')}\n{h}h {m}m {s}s"
  bot.send_message(tid, text)

config = {
  "name": 'uptime',
  "credits": 'Greegmon',
  "description": 'Get the bot\'s uptime',
  "def": uptime
}