import os

def help(msg, bot, i):
    command_files = [f for f in os.listdir('modules/commands') if f.endswith('.py') and f != 'help.py' and f != 'start.py']
    
    command_list = []
    for file in command_files:
        command_name = file[:-3]
        command_list.append(f"❖ /{command_name}")
    
    help_message = f"""
╔══════════════════╗
              𝐁𝐎𝐆𝐀𝐑𝐓'𝐁𝐎𝐓 𝐇𝐄𝐋𝐏 ✨
╚══════════════════╝
{chr(10).join(command_list)}
╚══════════════════╝
💬 Type a command to get started!
    """
    
    bot.send_message(msg.chat.id, help_message)

config = {
    "name": 'help',
    "credits": 'Joshua Apostol',
    "usage": '/help',
    "description": 'Get a list of available commands',
    "def": help
}
