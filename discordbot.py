from cmath import log
from distutils.sysconfig import PREFIX
import discord, random
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']
ACCCHANNEL = os.environ['ACCCHANNEL']
ACSCHANNEL = os.environ['ACSCHANNEL']
INCHANNEL = os.environ['INCHANNEL']
ADDGUIDEC = os.environ['ADDGUIDEC']
intents = intents=discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("^도움말ㅣ서버 관리"))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == f'{PREFIX}핑':
        await message.channel.send(f'퐁! {round(round(client.latency, 4)*1000)}ms')
        
    if message.content == f'{PREFIX}도움말':
        embed = discord.Embed(title="에루의 간단 도움말!", description= "^주사위 (숫자) : 주사위를 굴립니다!\n――――――――――――――――――――――――――――\n^골라 (단어1) (단어2)... : 단어 중에서 하나를 골라줍니다!", color=0xFFFF00)
        await message.channel.send (embed=embed)

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith (f'{PREFIX}공지'):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(f'{ACCCHANNEL}')
            embed = discord.Embed(title="**공지사항**", description="\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Ouro Mumi | 관리자 : {}".format(message.author), icon_url="https://cdn.discordapp.com/attachments/1081144519531180052/1092046236770631812/698bee4b003363ca.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1081144519531180052/1092045992624406548/88f091914ec7771e.png")
            await channel.send ("<@&1093841975666552872>", embed=embed)
            await message.author.send("*[ BOT 자동 알림 ]* | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))
    if message.content == (f'{PREFIX}규칙'):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(f'{ACSCHANNEL}')
            embed = discord.Embed(title="**규칙**: 이 서버의 기본적인 규칙", description="\n――――――――――――――――――――――――――――\n\n1. 욕설, 도배, 비하 발언 금지입니다.\n\n――――――――――――――――――――――――――――\n\n2. 테러는 당연히 안됩니다.\n\n――――――――――――――――――――――――――――\n\n채팅방에서 홍보는 안됩니다.\n\n――――――――――――――――――――――――――――\n\n쓸데없는 멘션을 하면 안됩니다.\n\n――――――――――――――――――――――――――――\n\n이러한 기본적인 규칙만 지켜주신다면 서버에서 잘 지낼 수 있습니다\n\n――――――――――――――――――――――――――――\n\n**주의: 기본으로 이 규칙을 어길 시 경고 1회가 되지만 수위에 따라 다를 수 있음**".format(notice), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Ouro Mumi | 관리자 : {}".format(message.author), icon_url="https://cdn.discordapp.com/attachments/1081144519531180052/1092046236770631812/698bee4b003363ca.jpg")
            await channel.send ("<@&1093841975666552872>", embed=embed)
            await message.author.send("*[ BOT 자동 알림 ]* | 정상적으로 규칙이 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

            
    if message.content.startswith(f'{PREFIX}골라'):
        choices = message.content.split()[1:]  
        if len(choices) < 2:  
            embed = discord.Embed(title="고를 수 있는 단어가 2가지 이상이여야 합니다", color=0xFFFF00)
            await message.channel.send (embed=embed)
        else:
            selected = random.choice(choices)  
            embed = discord.Embed(title='선택 결과', description=f'"{selected}" 선택되었습니다.', color=0x00ff00)
            await message.channel.send(embed=embed)

    if message.content.startswith(f'{PREFIX}주사위'):
        try:
            num = int(message.content.split()[1])  
            if num < 2:  
                embed = discord.Embed(title='입력 오류', description='주사위 눈의 수는 2 이상이어야 합니다.', color=0xff0000)
                await message.channel.send(embed=embed)
            else:
                result = random.randint(1, num) 
                embed = discord.Embed(title='주사위 결과', description=f'{result}이(가) 나왔습니다.', color=0x00ff00)
                await message.channel.send(embed=embed)
        except ValueError:  
            embed = discord.Embed(title='입력 오류', description='주사위 눈의 수는 정수여야 합니다.', color=0xff0000)
            await message.channel.send(embed=embed)
            
    if message.content == ('^authenticate1'):
        embed = discord.Embed(title="인증을 완료하세요", description="이모지를 눌러주세요.", color=0x00ff00)
        channel = client.get_channel(f'{INCHANNEL}')
        msg = await channel.send(embed=embed)
        await msg.add_reaction("<:check:1046316929561935934>")

    if message.content == ('^authenticate2'):
        embed = discord.Embed(title="아래 역할을 받고싶다면 아래 이모지를 눌러주세요", description=":one: : 공지 알림 :two: : 봇 가동 알림", color=0x00ff00)
        channel = client.get_channel(f'{ADDGUIDEC}')
        msg = await channel.send(embed=embed)
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")

        
@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.author == client.user and str(reaction.emoji) == "<:check:1046316929561935934>":
        role = discord.utils.get(user.guild.roles, name="유저")
        await user.add_roles(role)
    if reaction.message.author == client.user and str(reaction.emoji) == "1️⃣":
        role = discord.utils.get(user.guild.roles, name="공지 알림")
        await user.add_roles(role)
    if reaction.message.author == client.user and str(reaction.emoji) == "2️⃣":
        role = discord.utils.get(user.guild.roles, name="봇 가동 알림")
        await user.add_roles(role)
            
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
