import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents = discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def ecoinfo(ctx):
     await ctx.send("1. Покупайте продукты в упаковках большого объема\n2. Покупайте товары длительного пользования\n3. Посещайте магазины подержанных товаров\n4. Берите взаймы или напрокат, а не покупайте\n5. Ходите за продуктами с многоразовой сумкой и покупайте меньше полиэтиленовых пакетов\n6. Ремонтируйте изделия, а не покупайте новые\n7. Берите обед на работу в многоразовых контейнерах\n8. Используйте меньше бумаги на кухне и проявляйте заботу об окружающей среде\n9. Сократите количество ненужных почтовых материалов\n10. Используйте устройства, работающие от сети\n11. В столовой используйте многоразовые стаканы, тарелки и чашки\n12. Утилизируйте пищевые отходы\n13. Продавайте или отдавайте на благотворительность старую мебель и технику\n14. Подвозите друг друга на работу, используйте общественный транспорт и велосипеды\n15. Экономьте бумагу")

@bot.command()
async def ecoprac(ctx):
     await ctx.send(file=discord.File("eco.pdf"))

bot.run("MTE1NTUwMDI1ODMzMjI1MDIyMg.GIpQlM.PwJys2031ixRjbT0MF5uhrp9y3_yUxcG9MIw-Y")
