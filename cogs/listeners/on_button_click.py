import disnake
import variables
from disnake.ext import commands
from aiofiles import open


class OnButtonClick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        
        if inter.component.custom_id == "dph_highlighter_on":
            button = disnake.ui.Button(
                style=disnake.ButtonStyle.red,
                custom_id="dph_highlighter_off",
                label="Disable"
            )
        
            embed = disnake.Embed(
                title="`mcfunction` Highlighter (ENABLED)",
                description="The **`mcfunction` Highlighter** adds syntax highlighting to all **mcfunction code in codeblocks**. This is achvieved by **deleting** the message originally sent and **replacing it using a webhook** (with the original senders name and profile picture). \nYou always can **re-enable** this option at any time after disabling it!\n**Does not apply retroactively to already sent messages**",
                color=disnake.Colour.blue()
            )
            
            if inter.guild is None:
                embed = disnake.Embed(
                    title="Error!",
                    description="Something went wrong, report this to the developer! (on_button_click.py:29)",
                )
                await inter.send(embed=embed, ephemeral=True)
                return
            
            async with open(file=f"{variables.full_path}/highlighter_servers.txt", mode="a") as file:
                await file.write(f"\n{inter.guild.id}")
            
            await inter.response.edit_message(embed=embed,components=button)

        elif inter.component.custom_id == "dph_highlighter_off":
            button = disnake.ui.Button(
                style=disnake.ButtonStyle.green,
                custom_id="dph_highlighter_on",
                label="Enable"
            )
        
            embed = disnake.Embed(
                title="`mcfunction` Highlighter (DISABLED)",
                description="The **`mcfunction` Highlighter** adds syntax highlighting to all **mcfunction code in codeblocks**. This is achvieved by **deleting** the message originally sent and **replacing it using a webhook** (with the original senders name and profile picture). \nYou can always **disable** this option at any time after enabling it!\n**Does not apply retroactively to already sent messages**",
                color=disnake.Colour.blue()
            )
                    
            async with open(file=f"{variables.full_path}/highlighter_servers.txt") as file:
                lines = await file.readlines()
                
            async with open(f"{variables.full_path}/highlighter_servers.txt", "w") as file: 
                if inter.guild is None:
                    embed = disnake.Embed(
                        title="Error!",
                        description="Something went wrong, report this to the developer! (on_button_click.py:29)",
                    )
                    await inter.send(embed=embed, ephemeral=True)
                    return
                
                for line in lines:
                    if str(inter.guild.id) not in line:
                        await file.write(line)
                
            await inter.response.edit_message(embed=embed,components=button)
            
        else:
            print(inter.component.custom_id)