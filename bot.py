from discord import app_commands
from discord.utils import get # New import
from discord.ext import commands
import os
import discord
import random
import time

intents = discord.Intents.all()
intents.members = True
COMMIT = 'TESTING_VERSION'
TOKEN = 'YOUR TOKEN HERE'
SYS_PIT_DIR_PATH = "YOUR LOG PATH"
bot = commands.Bot(command_prefix="(", intents=intents)
tree = bot.tree

#Guild ID
server_id = 938728183203758080

#Channels
channel_joinleave = 943602154428571708 # join and leave channel
channel_pplofthepit = 1243174332293976095
channel_pit = 1057343199888285786

#Roles
role_admin = 938787942657327114
role_mod = 977248936148500550
role_owner = 938732039207809025
role_bot_smileyface = 938795313815240734
role_bot2 = 998594848582025269
role_pitted = 1057342828205846538
role_member = 938804320026099742
role_swagballer = 1003732468370776125

@bot.event
async def on_ready():
        await tree.sync(guild=discord.Object(id=server_id))
        print("The bot has successfully started.")
        print(SYS_PIT_DIR_PATH)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(channel_joinleave)
    await channel.send(f"{member.mention} ({member}) joined the server!\nhttps://tenor.com/view/snsdmongus-dog-sideye-gif-21272558")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(channel_joinleave)
    await channel.send(f"{member.mention} ({member}) left the server!\nhttps://media.discordapp.net/attachments/1096276589743972386/1096665886779261068/attachment.gif")

@tree.command(
name='hello',
description='haii',
guild=discord.Object(id=server_id)
)
async def hello (interaction: discord.Interaction):
		await interaction.response.send_message("Hiiiii haiii haiiii :3")
		
@tree.command(
name='bye',
description='baii',
guild=discord.Object(id=server_id)
)
async def bye (interaction: discord.Interaction):
		await interaction.response.send_message("baii... :(")
    
# SWAGIFICATION

@tree.command(
    name="swagify",
    description="swagifies a user",
    guild=discord.Object(id=server_id)
)
async def swag(interaction: discord.Interaction, user: discord.Member):
    if not interaction.user.guild_permissions.manage_roles:
        await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.")
        return

    if user.guild_permissions.manage_roles:
        await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.", ephemeral=True)
        return
    bot_member = interaction.guild.get_member(bot.user.id)
    bot_top_role = bot_member.top_role
    user_top_role = user.top_role

    if bot_top_role <= user_top_role:
        await interaction.response.send_message("I do not have permission to modify roles for this user.", ephemeral=True)
        return

    try:
        if interaction.user.guild_permissions.manage_roles:
            ylwrole = discord.Object(id=role_swagballer)
            await user.add_roles(ylwrole)
            await interaction.response.send_message(f"{user.mention} is now a swagballer!!!!!!!!!!!!!!!")
        else:
            await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.", ephemeral=True)
    except discord.Forbidden:
            await interaction.response.send_message("403. I need to be higher in the role hiearchy.", ephemeral=True)
    except Exception as e:
            await interaction.response.send_message(f"An unexpected error occurred: {str(e)}", ephemeral=True)
    
@tree.command(
    name="unswagify",
    description="unswagifies a user",
    guild=discord.Object(id=server_id)
)
async def unswag(interaction: discord.Interaction, user: discord.Member):
    if not interaction.user.guild_permissions.manage_roles:
        await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.")
        return

    if user.guild_permissions.manage_roles:
        await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.", ephemeral=True)
        return
    bot_member = interaction.guild.get_member(bot.user.id)
    bot_top_role = bot_member.top_role
    user_top_role = user.top_role

    if bot_top_role <= user_top_role:
        await interaction.response.send_message("I do not have permission to modify roles for this user.", ephemeral=True)
        return

    try:
        if interaction.user.guild_permissions.manage_roles:
            ylwrole = discord.Object(id=role_swagballer)
            await user.remove_roles(ylwrole)
            await interaction.response.send_message(f"{user.mention} had their swag privilleges revoked.")
        else:
            await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.", ephemeral=True)
    except discord.Forbidden:
            await interaction.response.send_message("403. I need to be higher in the role hiearchy.", ephemeral=True)
    except Exception as e:
            await interaction.response.send_message(f"An unexpected error occurred: {str(e)}", ephemeral=True)

@tree.command(
	name="version",
	description="bot version",
        guild=discord.Object(id=server_id)
)
async def ver(interaction: discord.Interaction):
    await interaction.response.send_message(f"Version: {COMMIT}")

@tree.command(name="length", description="Convert cm to feet and vica versa", guild=discord.Object(id=server_id))	
@app_commands.describe(value="Value of length", system="The measurement system used for the value parameter. Options: cm, in, m, ft (Case sensitive)")
async def calculate(interaction: discord.Interaction, value: str, system: str):
    try:
        if "'" not in value or system != "ft":
                number = float(value)
        embed = discord.Embed(title="Calculation Result", color=discord.Color.yellow())

        if system == 'cm':
            embed.add_field(name="Input", value=value + system, inline=True)
            embed.add_field(name="Inches", value=round(number * 0.3937, 2), inline=True)
            embed.add_field(name="Meters", value=round(number / 100, 2), inline=True)
            embed.add_field(name="Feet", value=(str(int((number/2.54)//12))) + "'" + str(round((number/2.54)%12, 2)) + "\"", inline=True)
        elif system == 'in':
            embed.add_field(name="Input", value=value + system, inline=True)
            embed.add_field(name="Feet", value=round(number / 12, 2), inline=True)
            embed.add_field(name="Meters", value=round(number * 0.0254, 2), inline=True)
            embed.add_field(name="Centimeters", value=round(number * 2.54, 2), inline=True)
        elif system == 'm':
            embed.add_field(name="Input", value=value + system, inline=True)
            embed.add_field(name="Inches", value=round(number / 0.0254, 2), inline=True)
            embed.add_field(name="Centimeters", value=round(number * 100, 2), inline=True)
            embed.add_field(name="Feet", value=round(number * 3.280839895, 2), inline=True)
        elif system == 'ft':
                if "'" in value:
                        value = value.split("'")
                        embed.add_field(name="Input", value=(value[0] + "'" + value[1] + '"'), inline=True)
                        embed.add_field(name="Inches", value=round(int(value[0]) * 12 + float(value[1]), 2), inline=True)
                        embed.add_field(name="Centimeters", value=round((int(value[0]) * 12 + float(value[1])) * 2.54, 2), inline=True)
                        embed.add_field(name="Meters", value=round((int(value[0]) * 12 + float(value[1])) * 0.0254, 2), inline=True)
                else:
                        embed.add_field(name="Input", value=value + system, inline=True)
                        embed.add_field(name="Inches", value=round(number * 12, 2), inline=True)
                        embed.add_field(name="Centimeters", value=round(number * 30.48, 2), inline=True)
                        embed.add_field(name="Meters", value=round(number * 0.3048, 2), inline=True)
        # https://preview.redd.it/zh4z7cem9kg51.png?auto=webp&s=90ff37f3925e3d8dfe41a88aafcf8f35a414d5b7
        await interaction.response.send_message(embed=embed)
    except ValueError:
        await interaction.response.send_message("Invalid input! Please provide a valid number.")

@tree.command(
    name="temperature",
    description="Convert kelvin, fahrenheit and celsius.",
    guild=discord.Object(id=server_id)
)
@app_commands.describe(value="Value", system="The system that you inputted the value in. Options: k, c, f. (Case sensitive)")
async def calc(interaction: discord.Interaction, value: str, system: str):
    try:
        number = float(value)
        embed = discord.Embed(title="Calculation Result", color=discord.Color.yellow())

        if system == "k":
            embed.add_field(name="Input", value=value + system, inline=True)
            embed.add_field(name="Celsius", value=round(number - 273.15, 2), inline=True)
            embed.add_field(name="Fahrenheit", value=round(1.8 * (number - 273.15) + 32, 2))
        elif system == "c":
            embed.add_field(name="Input", value=value + system, inline=True)
            embed.add_field(name="Kelvin", value=round(number + 273.15, 2), inline=True)
            embed.add_field(name="Fahrenheit", value=round(number * 1.8 + 32, 2))
        elif system == "f":
            embed.add_field(name="Input", value=value + system, inline=True)
            embed.add_field(name="Kelvin", value=round((number - 32) * 5 / 9 + 273.15, 2), inline=True)
            embed.add_field(name="Celsius", value=round((number - 32) / 1.8, 2))
            
        await interaction.response.send_message(embed=embed)
    except ValueError:
        await interaction.response.send_message("Invalid input")
        
# PITTING SYSTEM
async def generic_pit(interaction, user): # Use this when pitting someone in another function. Does not include reason.
        
        user_id = str(user.id) # gets user id
        user_roles_ids = user.roles # gets list of roles user has
        list_len = len(user_roles_ids) 
        file = open(f"{SYS_PIT_DIR_PATH}/{user_id}", "w") 
        iterate = 0
        while iterate < list_len:
                file.write(str(user_roles_ids[iterate].id)+"\n") # write each role ID in to file
                iterate = iterate + 1
                
        file.close()
        pit_role = discord.Object(id=role_pitted)  # pit role
        await user.edit(roles=[pit_role])

@tree.command(
    name="pit",
    description="pits someone",
    guild=discord.Object(id=server_id)
)
@app_commands.describe(reason="Reason will be posted in the public logging channel.")
async def pit(interaction: discord.Interaction, user: discord.Member, reason: str = ""):
    if not interaction.user.guild_permissions.manage_roles:
        await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.")
        return

    if user.guild_permissions.manage_roles:
        await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.", ephemeral=True)
        return
    bot_member = interaction.guild.get_member(bot.user.id)
    bot_top_role = bot_member.top_role
    user_top_role = user.top_role

    if bot_top_role <= user_top_role:
        await interaction.response.send_message("I do not have permission to modify roles for this user.", ephemeral=True)
        return

    try:
        pit = bot.get_channel(channel_pit)
        if interaction.user.guild_permissions.manage_roles and reason != "":
            await generic_pit(interaction, user)
            await interaction.response.send_message(f"{user.mention} has been pitted.\nhttps://media.discordapp.net/attachments/1091036967199834112/1129035100915511376/attachment.gif")
            channel = bot.get_channel(channel_pplofthepit)
            await user.send(f'You have been pitted in 69SwagBalls420 cord for undisclosed reasons.')
            await channel.send(f"{user.mention} ({user}) was pitted by {interaction.user.mention} for {reason}.")
            await pit.send (f"A loud thud shakes the depths of the Pit as {user.mention} ({user}) falls to the ground... Welcome your new friend.")
        elif interaction.user.guild_permissions.manage_roles and reason == "":
            await generic_pit(interaction, user)
            channel = bot.get_channel(channel_pplofthepit)
            await interaction.response.send_message(f"{user.mention} has been pitted.\nhttps://media.discordapp.net/attachments/1091036967199834112/1129035100915511376/attachment.gif")
            await user.send(f'You have been pitted in 69SwagBalls420 cord for undisclosed reasons.')
            await channel.send(f"{user.mention} ({user}) was pitted by {interaction.user.mention} for unknown reasons! :DEVIL:")
            await pit.send (f"A loud thud shakes the depths of the Pit as {user.mention} ({user}) falls to the ground... Welcome your new friend.")
        else:
            await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.", ephemeral=True)
    except discord.Forbidden:
            await interaction.response.send_message("403. I need to be higher in the role hiearchy.", ephemeral=True)
    except Exception as e:
            await interaction.response.send_message(f"An unexpected error occurred: {str(e)}", ephemeral=True)

async def generic_unpit(interaction, user):
        
        user_id = str(user.id)
        file_list = os.listdir(f"{SYS_PIT_DIR_PATH}")
        fl_len = len(file_list)
        iterator = 0;
        found = False
        while iterator < fl_len:
                if user_id == file_list[iterator]:
                        found = True
                        break;
                iterator = iterator + 1
            
        if found == False:
                await interaction.response.send_message("Could not find role ID's, applying greenrole")
                greenrole = discord.Object(id=role_member)
                await user.edit(roles=[greenrole])
                return False
        
        full_path = SYS_PIT_DIR_PATH+"/"+file_list[iterator]
        role_ids = open(full_path, "r").read().split('\n')
        role_ids_int = [int(role_id) for role_id in role_ids if role_id.strip().isdigit()]
        roles_list_objects = [discord.Object(id=role_id) for role_id in role_ids_int]
        await user.edit(roles=roles_list_objects)
        os.remove(full_path)
            
@tree.command(
    name="unpit",
    description="unpits someone",
    guild=discord.Object(id=server_id)
)

@app_commands.describe(reason="Reason will be posted in the public logging channel.")
async def unpit(interaction: discord.Interaction, user: discord.Member, reason: str = ""):
    if not interaction.user.guild_permissions.manage_roles:
        await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.")
        return

    if user.guild_permissions.manage_roles:
        await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.", ephemeral=True)
        return
    bot_member = interaction.guild.get_member(bot.user.id)
    bot_top_role = bot_member.top_role
    user_top_role = user.top_role

    if bot_top_role <= user_top_role:
        await interaction.response.send_message("I do not have permission to modify roles for this user.", ephemeral=True)
        return

    try:
        if interaction.user.guild_permissions.manage_roles and reason != "":
            if await generic_unpit(interaction, user) == False:
                    return
            
            await interaction.response.send_message(f"{user.mention}, who crawled through a river of shit and came out clean on the other side.\nhttps://cdn.discordapp.com/attachments/938728183203758082/1129104885154074704/attachment.gif")
            channel = bot.get_channel(channel_pplofthepit) 
            await channel.send(f"{user.mention} ({user}) was unpitted by {interaction.user.mention} for reason: {reason}")
            
        elif interaction.user.guild_permissions.manage_roles and reason == "":
            if await generic_unpit(interaction, user) == False:
                    return
            await interaction.response.send_message(f"{user.mention}, who crawled through a river of shit and came out clean on the other side.\nhttps://cdn.discordapp.com/attachments/938728183203758082/1129104885154074704/attachment.gif")
            channel = bot.get_channel(channel_pplofthepit) 
            await channel.send(f"{user.mention} ({user}) was unpitted by {interaction.user.mention} for unknown reasons!")
        else:
            await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.", ephemeral=True)
    except discord.Forbidden:
            await interaction.response.send_message("403. I need to be higher in the role hiearchy.", ephemeral=True)
    except Exception as e:
            await interaction.response.send_message(f"An unexpected error occurred: {str(e)}", ephemeral=True)

@tree.command(
	name="roulette",
	description="@someone with cooler features",
	guild=discord.Object(id=server_id)
)
@app_commands.describe(pit="If random user shall be failed. Type YUP! case senstive if you want to do this!", russian="blanks for no kick and kick for kicking upon death")

async def roulette(interaction: discord.Interaction, pit: str = "", russian: str = ""):
		guild = bot.get_guild(server_id)
		channel = bot.get_channel(channel_pplofthepit)
		# God give me strength
		# UPD: I'm going to hang myself'
		# UPD: we are so back
		# UPD: BRO
		if pit == "" and russian == "":
			randoms = random.choice(guild.members)
			await interaction.response.send_message(f"{randoms.mention} has won the roulette!")
		elif pit == "YUP!" and russian == "" and interaction.user.guild_permissions.manage_roles:
			randoms = random.choice(guild.members)
			pitted = discord.Object(id=role_pitted) # What the fuck am I doing I swear to god/Oh i think i got it lemme try
			await interaction.response.send_message(f"{randoms.mention} has won the justin bieber concert tickers! Congratulations!")
			await randoms.edit(roles=[pitted])
			await randoms.send("You have been by random chosen to be pitted in Ragecord! You can be unpitted upon request.")
			await channel.send(f"{randoms.mention} was failed by {interaction.user.mention} in the result of a pit roulette. Epic fail!")
		elif pit == "YUP!" and (russian == "blanks" or russian == "kick"):
			await interaction.response.send_message(f"You can not activate both pit and russian at the same time!")
		elif pit == "" and russian == "blanks":
			rng = random.randint(1, 6)
			await interaction.response.send_message("You pick up the gun, swirl the chamber and point it at your head... You will be killed if it lands on 1...")
			time.sleep(4)
			if rng != 1:
				await interaction.followup.send("-# *click*")
				time.sleep(2)
				await interaction.followup.send(f"You open your eyes... You are still standing... (Your rolled is: damn {rng})")
			elif rng == 1:
				await interaction.followup.send("-# *click*")
				time.sleep(1)
				await interaction.followup.send("# BANG.\n Your head suddenly starts resembling a red daisy. You are dead.")
		elif pit == "" and russian == "kick":
			rng = random.randint(1, 6)
			await interaction.response.send_message("You pick up the gun, swirl the chamber and point it at your head.... You will be kicked if it lands on 1...")
			time.sleep(4)
			if rng != 1:
				await interaction.followup.send("-# *click*")
				time.sleep(2)
				await interaction.followup.send(f"You open your eyes... You are still standing... (Your rolled is: damn {rng})")
			elif rng == 1:
				await interaction.followup.send("-# *click*")
				time.sleep(1)
				await interaction.followup.send("# BANG.\n Your head suddenly starts resembling a red daisy. You are dead.")
				await interaction.user.send("You are kicked from 69SwagBalls420 Cord for dying to a russian roulette.\n You can join back here: https://discord.gg/NUWJZPsy5f")
				await interaction.user.kick(reason = "Swagbot: Russian roulette death")
				

		
		elif pit == "YUP!" or russian == "blanks" or russian == "kick" and not interaction.user.guild_permissions.manage_roles:
			await interaction.response.send_message("https://cdn.discordapp.com/attachments/1239258065988222999/1261509266208981073/RDT_20240712_2224291177474633641757631.jpg?ex=6696834e&is=669531ce&hm=b441f6ee1d35f9e6e00823f493b26e7c859377ddf5a6f7c1930cb5ee7d21bcc8&.")
			
@tree.command(
	name="cowsay",
	description="The iconic CLI tool now on Discord!",
	guild=discord.Object(id=server_id)
)
async def cowsay(interaction: discord.Interaction, text: str):
	if len(text) <= 40:
       
          response = f"""
  {"_" * len(text)}
< {text} >
  {"-" * len(text)}
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
                          
"""
          await interaction.response.send_message(content=f"```{response}```")
	elif len(text) > 40:
	      chars = len(text)
	      await interaction.response.send_message(f"Please type in a phrase less than 40 characters. You currently used {chars} characters.")

bot.run(TOKEN)
