import discord
from discord.ext import commands as cmds

import logging

log = logging.getLogger("red.example518")


class Example518:
    def __init__(self, bot):
        self.bot = bot
        self.conf = bot.get_conf(self.__class__.__name__, 23894723987423987)

        self.conf.register_global("is_ready", False)
        self.conf.register_server("is_server_enabled", False)
        self.conf.register_channel("is_channel_enabled", False)
        self.conf.register_role("is_role_enabled", False)
        self.conf.register_member("is_member_enabled", False)
        self.conf.register_user("is_user_enabled", False)

    @cmds.command()
    async def botready(self):
        txt = "is" if self.conf.is_ready else "is not"
        await self.bot.say("Bot {} ready.".format(txt))

    @cmds.command(pass_context=True)
    async def serverenablecheck(self, ctx, set: bool=None):
        if set is not None:
            self.conf.server(ctx.message.server).set("is_server_enabled", set)
        txt = "is" if self.conf.server(ctx.message.server).is_server_enabled \
            else "is not"
        await self.bot.say("Bot {} server enabled.".format(txt))

    @cmds.command(pass_context=True)
    async def channelenablecheck(self, ctx, set: bool=None):
        if set is not None:
            self.conf.channel(ctx.message.channel).set(
                "is_channel_enabled", set)
        txt = "is" if self.conf.channel(
            ctx.message.channel).is_channel_enabled \
            else "is not"
        await self.bot.say("Bot {} channel enabled.".format(txt))

    @cmds.command(pass_context=True)
    async def roleenablecheck(self, ctx, role: discord.Role, set: bool=None):
        log.debug("{}: {}".format(role.name, role.id))
        if set is not None:
            self.conf.role(role).set(
                "is_role_enabled", set)
        txt = "is" if self.conf.role(
            role).is_role_enabled \
            else "is not"
        await self.bot.say("Bot {} role enabled.".format(txt))

    @cmds.command(pass_context=True)
    async def memberenablecheck(self, ctx, member: discord.Member,
                                set: bool=None):
        if set is not None:
            self.conf.member(member).set(
                "is_member_enabled", set)
        txt = "is" if self.conf.member(
            member).is_member_enabled \
            else "is not"
        await self.bot.say("Bot {} member enabled.".format(txt))

    @cmds.command(pass_context=True)
    async def userenablecheck(self, ctx, user: discord.Member, set: bool=None):
        if set is not None:
            self.conf.user(user).set(
                "is_user_enabled", set)
        txt = "is" if self.conf.user(
            user).is_user_enabled \
            else "is not"
        await self.bot.say("Bot {} user enabled.".format(txt))

    async def on_ready(self):
        self.conf.set("is_ready", True)


def setup(bot):
    bot.add_cog(Example518(bot))
