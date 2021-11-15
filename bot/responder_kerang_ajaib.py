import random
import discord


async def kerang_parse_petuah(message):
    desc = random.choice(["Ya", "Tidak", "Coba tanyakan lagi"])

    embed = discord.Embed(title="Kerang Ajaib bersabda...",
                          description=desc, color=0xd0a2d9)
    embed.set_thumbnail(
        url="https://gh-statis.konten.christianto.net/images/random-meme/magic-conch-shell.png")
    await message.channel.send(embed=embed)
