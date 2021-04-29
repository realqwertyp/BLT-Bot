import discord
from discord.ext import commands, tasks
import random


client = commands.Bot(command_prefix = "blt ", case_insensitive = True)


@client.event #Sends message when bot is online
async def on_ready():
  print("BLT")


@client.command(aliases = ["pic"]) 
async def picture(ctx):
  bltList = ["https://cdn.discordapp.com/attachments/748571137973288980/814691906692055060/blt.jpg"]
  message = random.choice(bltList)
  await ctx.send(message)

@client.command() 
async def gif(ctx):
  await ctx.send("https://tenor.com/view/letter-b-dancing-gif-9063746")
  await ctx.send("https://tenor.com/view/red-alphabet-letter-dancing-letter-l-cartoons-gif-12084376")
  await ctx.send("https://tenor.com/view/letter-t-gif-9063764")



@client.command()
async def mismatch(ctx, num1 : int, num2 : int, num3 : int):

    peoplelist = [['https://cdn.discordapp.com/attachments/562012213523775519/726585872585195520/seb1.jpg', 'https://cdn.discordapp.com/attachments/562012213523775519/726585874548260914/seb2.jpg', 'https://cdn.discordapp.com/attachments/562012213523775519/726585876133707836/seb3.jpg'],
                  ['https://cdn.discordapp.com/attachments/719739668840579084/726643701451063303/image_part_001.png', 'https://cdn.discordapp.com/attachments/719739668840579084/726643729007378533/image_part_002.png', 'https://cdn.discordapp.com/attachments/719739668840579084/726643754273996970/image_part_003.png'],
                  ['https://cdn.discordapp.com/attachments/719739668840579084/726647585778958438/kurtis1.png', 'https://cdn.discordapp.com/attachments/719739668840579084/726647588983537674/kurtis2.png', 'https://cdn.discordapp.com/attachments/719739668840579084/726647592653553674/kurtis3.png'],
                  ['https://cdn.discordapp.com/attachments/562012213523775519/726646188945703002/image_part_001.png', 'https://cdn.discordapp.com/attachments/562012213523775519/726646212337598464/image_part_002.png', 'https://cdn.discordapp.com/attachments/562012213523775519/726646241546731600/image_part_003.png'],
                  ['https://cdn.discordapp.com/attachments/719739668840579084/726887404639617104/image_part_001.png', 'https://cdn.discordapp.com/attachments/719739668840579084/726887430522798131/image_part_002.png', 'https://cdn.discordapp.com/attachments/719739668840579084/726887451280277564/image_part_003.png'],
                  ['https://cdn.discordapp.com/attachments/562012213523775519/726915740220915762/image_part_001.png', 'https://cdn.discordapp.com/attachments/562012213523775519/726915761485905930/image_part_002.png', 'https://cdn.discordapp.com/attachments/562012213523775519/726915781836668958/image_part_003.png'],
                  ['https://cdn.discordapp.com/attachments/719739668840579084/726919809672937472/image_part_001.png', 'https://cdn.discordapp.com/attachments/719739668840579084/726919831047110756/image_part_002.png', 'https://cdn.discordapp.com/attachments/719739668840579084/726919849636266025/image_part_003.png'],
                  ['https://cdn.discordapp.com/attachments/719739668840579084/726936978335203428/image_part_001.png', 'https://cdn.discordapp.com/attachments/719739668840579084/726936996815175700/image_part_002.png', 'https://cdn.discordapp.com/attachments/719739668840579084/726937018327629956/image_part_003.png'],
                  ['https://cdn.discordapp.com/attachments/719739668840579084/726959158670393405/image_part_001.png', 'https://cdn.discordapp.com/attachments/719739668840579084/726959178714972160/image_part_002.png', 'https://cdn.discordapp.com/attachments/719739668840579084/726959200554451014/image_part_003.png'],
                  ['https://cdn.discordapp.com/attachments/719739668840579084/727003143568752691/image_part_001.png', 'https://cdn.discordapp.com/attachments/719739668840579084/727003167338004511/image_part_002.png', 'https://cdn.discordapp.com/attachments/719739668840579084/727003187239977000/image_part_003.png']]

    image1 = peoplelist[num1-1][0]
    image2 = peoplelist[num2-1][1]
    image3 = peoplelist[num3-1][2]

    await ctx.send(image1)
    await ctx.send(image2)
    await ctx.send(image3)

@client.command()
async def mismatchhelp(ctx):
    await ctx.send("``` Num  | Person\n"
                   "------|----------------\n "
                   " 1   | Sebastian\n "
                   " 2   | Enquobahrie\n "
                   " 3   | Kurtis\n "
                   " 4   | Nikita\n "
                   " 5   | Kaleb\n "
                   " 6   | nick\n "
                   " 7   | sebastian b\n "
                   " 8   | big persian\n "
                   " 9   | Saman Safari\n "
                   " 10  | jordan```")

client.run(Token)
