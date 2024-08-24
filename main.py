####--------------------------------####
#--# Author:   by Umbrellla777      #--#
#--# Telegram: @Umbrellla777        #--#
#--# VK:       @Umbrellla777        #--#
####--------------------------------####

###########################
## Importing libraries
###########################
import sys
import asyncio
import random
from collections import deque
from telethon.sync import TelegramClient
from telethon import events

###########################
## Console color
###########################
red = [206, 76, 54]
green = [68, 250, 123]
blue = [253, 127, 233]
yellow = [241, 250, 118]
orange = [255, 184, 107]

def colored(color, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(color[0], color[1], color[2], text)

###########################
## Settings
###########################
api_id = int(sys.argv[1])
api_hash = str(sys.argv[2])

## Connect
client = TelegramClient('users/current_user', api_id, api_hash)
client.start()

###########################
## Account Information
###########################
async def print_account_info():
    entity = await client.get_me()
    MY_ID = entity.id
    print(
        "["
        + colored(green, "PROFILE: ")
        + str(entity.first_name)
        + " | " + colored(orange, "Id: ") + str(MY_ID)
        + " | " + colored(orange, "Uname: ") + "@" + str(entity.username)
        + "]"
    )

asyncio.run(print_account_info())

###########################
## Help by commands
###########################
@client.on(events.NewMessage(pattern='.help'))
async def help(event):
    help_text = (
        "Hi! I am a bot with animated messages.\n"
        "With me, you can send a beautiful animated message.\n"
        "List of commands:\n"
        ".ping - checking the bot for operability.\n"
        ".8 animation - is a gift for March 8th.\n"
        ".lv animation - is the heart.\n"
        "@all mentioning all the chat participants.\n"
        ".coin A coin with options for falling out - Heads, tails, edges.\n"
        ".rtext a running strip of text.\n"
        ".roll randomly the number between the two entered.\n"
        ".type animation of writing text.\n"
        ".moon Good night, with the moon phase changing.\n"
        ".bunny animation with a rabbit.\n\n"
        "Commands will also be added, follow the news in our telegram channel t.me/umbrellla777bot \n"
        "Author Umbrellla777 \n"
        "VK @Umbrellla777\n"
        "TG @Umbrellla777"
    )
    await event.message.edit(help_text)

###########################
## Checking the bot
###########################
@client.on(events.NewMessage(pattern='.ping'))
async def pong(event):
    await event.message.edit("pong")

##########################
## Animation .8|5×10
###########################
@client.on(events.NewMessage(pattern='.8'))
async def draw_matrix(event):
    message = event.message
    matrix = '12221\n21112\n21112\n21112\n12221\n21112\n21112\n21112\n21112\n12221'
    end = '00000000\n00000000\n00000000\n0Happy holidays!0\n00000000\n00000000\n00000000'

    matrix = matrix.replace('1', '⬜️').replace('2', '⬛️')

    for _ in range(4):
        await message.edit(matrix)
        await asyncio.sleep(1)
        matrix = matrix.replace('⬜️', '◻️').replace('⬛️', '◼️')
        matrix = matrix.replace('◻️', '◽️').replace('◼️', '◾️')
        matrix = matrix.replace('◽️', '▫️').replace('◾️', '▪️')
    
    motivational_messages = [
        'This is your day!', 'Shine!', 'Take action!',
        'Nothing is impossible.!', 'Never give up!', 'Be yourself!',
        '✨✨✨✨✨✨✨✨', 'And just...'
    ]
    
    for msg in motivational_messages:
        await message.edit(msg)
        await asyncio.sleep(2)
    
    end = end.replace('0', '❤️')
    await message.edit(end)
    await asyncio.sleep(2)
    end = end.replace('❤️', '❤️‍🔥')
    await message.edit(end)

##########################
## Animation .lv
##########################
@client.on(events.NewMessage(pattern=r"\.lv", outgoing=True))
async def lv_animation(event):
    message = event.message
    arr = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫", "⬛️", "🔳"]
    h = "⬜️"
    first = ""

    for i in "".join([h*9, "\n", h*2, arr[0]*2, h, arr[0]*2, h*2, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h*2, arr[0]*5, h*2, "\n", h*3, arr[0]*3, h*3, "\n", h*4, arr[0], h*4]).split("\n"):
        first += i + "\n"
        await message.edit(first)
        await asyncio.sleep(0.2)

    for color in arr:
        await message.edit(
            "".join([
                h*9, "\n", h*2, color*2, h, color*2, h*2, "\n",
                h, color*7, h, "\n", h, color*7, h, "\n",
                h, color*7, h, "\n", h*2, color*5, h*2, "\n",
                h*3, color*3, h*3, "\n", h*4, color, h*4, "\n",
                h*9
            ])
        )
        await asyncio.sleep(0.3)

    for _ in range(8):
        rand = random.choices(arr, k=34)
        await message.edit(
            "".join([
                h*9, "\n", h*2, rand[0], rand[1], h, rand[2], rand[3], h*2, "\n",
                h, rand[4], rand[5], rand[6], rand[7], rand[8], rand[9], rand[10], h, "\n",
                h, rand[11], rand[12], rand[13], rand[14], rand[15], rand[16], rand[17], h, "\n",
                h, rand[18], rand[19], rand[20], rand[21], rand[22], rand[23], rand[24], h, "\n",
                h*2, rand[25], rand[26], rand[27], rand[28], rand[29], h*2, "\n",
                h*3, rand[30], rand[31], rand[32], h*3, "\n",
                h*4, rand[33], h*4, "\n", h*9
            ])
        )
        await asyncio.sleep(0.3)

    fourth = "".join([h*9, "\n", h*2, arr[0]*2, h, arr[0]*2, h*2, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h*2, arr[0]*5, h*2, "\n", h*3, arr[0]*3, h*3, "\n", h*4, arr[0], h*4, "\n", h*9])
    await message.edit(fourth)

    for _ in range(47):
        fourth = fourth.replace("⬜️", "🟥", 1)
        await message.edit(fourth)
        await asyncio.sleep(0.1)

    for i in range(8):
        await message.edit((arr[0] * (8 - i) + "\n") * (8 - i))
        await asyncio.sleep(0.4)

    final_messages = ["I", "I ❤️", "I ❤️ U", "I ❤️ U!", 'i ❤️ U', 'I ❤️ u', 'I ❤️ U']
    for msg in final_messages:
        await message.edit(f"<b>{msg}</b>", parse_mode='html')
        await asyncio.sleep(0.5)

##########################
## Animation .rtext
##########################
@client.on(events.NewMessage(pattern=r"\.rtext", outgoing=True))
async def rtext(event):
    try:
        text = event.message.text.split('.rtext ')[1]
    except IndexError:
        return

    deq = deque(text)
    for _ in range(len(text)):
        deq.rotate(1)
        await event.edit(''.join(deq))
        await asyncio.sleep(0.1)

###########################
## Run Bot
###########################
client.run_until_disconnected()
