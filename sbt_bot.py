import discord
from discord.ext import commands

# Comandos


class MyClient(discord.Client):
    async def on_ready(self):
        print(
            f'Bot online!\nID: {client.user.id}\nNome: {client.user}'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}:{0.content}'.format(message))
        if message.content == '!sbt':
            await message.channel.send(f'{message.author.name} quer jogar aquela nostalgia que são os games online e gratis?\n Vem dar play em nosso site: https://gg.sbtgames.com.br/')
        elif message.content == '!bodybuilder':
            await message.channel.send(f'{message.author.name} @Gamer30mais BIRLLLLL HORA DO SHOW!!! :muscle: :sunglasses:')

# Bem-Vindo
    async def on_member_join(self, member):
        guild = member.guild
        canal = discord.utils.get(guild.channels, id=997312257035862057)
        embed = discord.Embed(
            title='Seja Bem-Vindo(a)!',
            color=0x0000CD,
            description=f'🎊 | {member.mention} Venha curtir com a galera e conversar com seus Talentos favoritos!\n\n 👮‍♂️ | **Não esquece de ir em:**\n <#996965083328548945> para evitar punições!\n\n 💎 | **Veio pela live?** Então já confere aqui em baixo um pouco sobre nossos <#997314245085642782>!'
        )

        embed.set_author(name=member.name, icon_url=member.avatar_url)

        embed.set_image(
            url='https://3.bp.blogspot.com/-vzcwGr1RDok/Wu8ID2cKtkI/AAAAAAAAEug/TOraNHUnYkEzJpCpJhLK2MN5iijArB7jwCLcBGAs/s1600/hdfPQx.gif')

        embed.set_footer(text='Acesse nosso site! https://gg.sbtgames.com.br/')

        await canal.send(embed=embed)


intents = discord.Intents.all()
intents.members = True


client = MyClient(intents=intents)
client.run('')
