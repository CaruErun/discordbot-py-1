from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import time
import math
from datetime import datetime, timedelta
import os
load_dotenv()

global startTime
global endTime
startTime=""
PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    global startTime
    global endTime
    
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!')

    if message.content.startswith(f'{PREFIX}start'):
        startTime = datetime.now()
        await message.channel.send("시작시간 : "+startTime.strftime("%H시 %M분 %S초"))
        
    if message.content.startswith(f'{PREFIX}end'):
        endTime = datetime.now()
        if(startTime=="") :
            await message.channel.send('#start를 먼저 진행해주세요')
        else :
            minusTime = endTime - startTime
            startTime=""
            await message.channel.send('종료시간 : '+endTime.strftime("%H시 %M분 %S초")+'\n총 시간 : '+ str(datetime.utcfromtimestamp(minusTime.total_seconds()).strftime("%H시 %M분 %S초")))             

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
