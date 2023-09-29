import disnake
from disnake.ext import commands
import variables

invites = commands.option_enum(
    [
        "datapack hub",
        "minecraft commands",
        "shader labs",
        "bot",
        "smithed",
        "blockbench",
        "optifine",
        "fabric",
        "minecraft",
        "dataworld (fr)"
    ]
)


class InviteCommand(commands.Cog, name="invite"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="invite",
        description="Shows discord invite for a discord server relevant to datapacks",
    )
    async def invite(
        self, inter: disnake.ApplicationCommandInteraction, invite: invites
    ):
        match invite:
            case "datapack hub":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪 Datapack Hub Invite**"),
                    description="Join Datapack Hub for help with your Datapacks and support regarding this bot using this link: https://dsc.gg/datapack",
                )

            case "minecraft commands":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪Minecraft Commands Invite**"),
                    description="Join Minecraft Commands for help regarding your Datapacks using this link: https://discord.gg/QAFXFtZ",
                )

            case "shader labs":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪ShaderLABS Invite**"),
                    description="Join ShaderLABS for help regarding shaders using this link: https://discord.gg/Ayav9YPQra",
                )
            case "bot":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪Datapack Helper Invite**"),
                    description="Add the Datapack Helper bot to your server using this link: *COMING SOON*",
                )
            case "smithed":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪Smithed Invite**"),
                    description="Join Smithed for information/help regarding the smithed datapacking conventions using this link: https://smithed.dev/discord",
                )
            case "blockbench":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪Blockbench Invite**"),
                    description="Join Blockbench for help regarding modeling and Blockbench using this link: https://discord.gg/blockbench",
                )
            case "optifine":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪Optifine Invite**"),
                    description="Join Optifine for help regarding (problems with) Optifine using this link: https://discord.gg/optifine",
                )
            case "fabric":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪Fabric Invite**"),
                    description="Join The Fabric Project for information/help regarding Fabric using this link: https://discord.gg/DtevV9NmaR",
                )
            case "minecraft":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪Minecraft Invite**"),
                    description="Join the official minecraft discord server using this link: https://discord.gg/minecraft",
                )
            case "dataworld (fr)":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪Data World Invite**"),
                    description="Rejoins Data World pour obtenir de l'aide sur les datapacks avec le lien: https://discord.gg/5y5FBz5",
                )
        await inter.response.send_message(embed=embed)
        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**`/invite` Command**"),
            description=(
                str(inter.user.name) + " looked up the invite of `" + str(invite) + "`(Server: **" + inter.guild.name + "**)"
            ),
        )
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)
