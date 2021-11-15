# bot.py
import os,discord,random

from discord import channel

from responder_kerang_ajaib import kerang_parse_petuah

TOKEN = os.getenv('DISCORD_TOKEN')

#client connect notif
client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your Prayers"))

#auto-reply messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.casefold().startswith('hello'):
        await message.channel.send('Hello!')

    if message.content.casefold().startswith('test'):
        await message.channel.send('Bot Aktif')

    #name auto reply

    if message.content.casefold().startswith('aldin'):
        await message.channel.send('Sungkem top global hacker')
    
    if message.content.casefold().startswith('yosua'):
        await message.channel.send('Bot')
    
    if message.content.casefold().startswith('aul'):
        await message.channel.send('Cantik :heart:')

    if message.content.casefold().startswith('chiko'):
        await message.channel.send('Kawaii desu nee :heart_eyes:')

    if message.content.casefold().startswith('hiko'):
        await message.channel.send('Kawaii :heart_eyes:')

    if message.content.casefold().startswith('munir'):
        await message.channel.send('Dalang dibalik pembunuhan munir adalah So')

    if message.content.casefold().startswith('ricko'):
        await message.channel.send('SIMP')

    if message.content.casefold().startswith('pekora'):
        await message.channel.send('Pe:arrow_upper_right:ko:arrow_lower_right:pe:arrow_upper_right:ko:arrow_lower_right:')

    if message.content.casefold().startswith('nopal'):
        await message.channel.send('Bucin')

    if message.content.casefold().startswith('riyan'):
        await message.channel.send('Verified fuckboy')

    if message.content.casefold().startswith('efga'):
        await message.channel.send('Error code in line 56 : Variable "efga" not found')

    if message.content.casefold().startswith('imam bonjour'):
        await message.channel.send('Bonjour mes amis!')

    if message.content.casefold().startswith('deden'):
        await message.channel.send('Anjay anak motor')

    if message.content.casefold().startswith('hafiidh'):
        await message.channel.send('anjay pro player Bandori')

    if message.content.casefold().startswith('ranu'):
        await message.channel.send('Pak ketu')

    if message.content.casefold().startswith('gunawan'):
        await message.channel.send('sungkem pro coding')

    if message.content.casefold().startswith('belinda'):
        await message.channel.send('hai domo, Belinda desu!')
    
    if message.content.casefold().startswith('bebel'):
        await message.channel.send('ohayoo')

    if message.content.casefold().startswith('meta'):
        await message.channel.send('META janai, Meta desu!')

    if message.content.casefold().startswith('kamet'):
        await message.channel.send('Jamet janai, Kamet desu! >_<')

    if message.content.casefold().startswith('ardy'):
        await message.channel.send('HORAS !!')

    if message.content.casefold().startswith('aids'):
        await message.channel.send('Oalah jancok')

    if message.content.casefold().startswith('agam'):
        await message.channel.send('Gummy')

    if message.content.casefold().startswith('ferdy'):
        await message.channel.send('Hai ini agam')

    if message.content.casefold().startswith('kazu'):
        await message.channel.send('Apa cha')

    if message.content.casefold().startswith('fifi'):
        await message.channel.send('FAASAN!')

    if message.content.casefold().startswith('rinko'):
        await message.channel.send('DAISUKII :revolving_hearts: :revolving_hearts:')

    if message.content.casefold().startswith('ariyani'):
        await message.channel.send('KAWAIIII')

    if message.content.casefold().startswith('fakboi') or message.content.casefold().startswith('fuckboy'):
        await message.channel.send('Riyan')

    if message.content.casefold().startswith('simp'):
        await message.channel.send('Ricko')
        
    if message.content.casefold().startswith('ariya-chan'):
        await message.channel.send('muah muah :*')
        
    if message.content.casefold().startswith('sahiko48'):
        await message.channel.send('Minna no Idol! :heart:')
                                   
    if message.content.casefold().startswith('yosua.bot'):
        await message.channel.send('wZ1PuRvgaviCcXN!!')
                                   
    #text except name

    if message.content.casefold().startswith('bye all'):
        await message.channel.send('Aku mau kesekolah')
    
    if message.content.casefold().startswith('here we are'):
        await message.channel.send('going far to save all that we love')

    if message.content.casefold().startswith('anjay'):
        await message.channel.send('Mabar :fist:')

    if message.content.casefold().startswith('iri'):
        await message.channel.send('Bilang boss')

    if message.content.casefold().startswith('indihome'):
        await message.channel.send('Silahkan Restart dulu modemnya kak')

    if message.content.casefold().startswith('anjing'):
        await message.channel.send('Woof woof')

    if message.content.casefold().startswith('iri bilang boss'):
        await message.channel.send('Iri boss')

    if message.content.casefold().startswith('wkwk'):
        await message.channel.send('Ngakak akutuh')

    if message.content.casefold().startswith('luwak white coffee'):
        await message.channel.send('Kopi enak gak bikin kembung')

    if message.content.casefold().startswith('assalamualaikum'):
        await message.channel.send('Waalaikum salam')

    if message.content.casefold().startswith('permisi'):
        await message.channel.send('Silahkan')

    if message.content.casefold().startswith('punten'):
        await message.channel.send('Monggo')

    #if message.content.startswith('Yoi') or message.content.startswith('yoi'):
    #   await message.channel.send('Yoi bro :sunglasses: :fist:')    

    if message.content.casefold().startswith('mantap'):
        await message.channel.send('Surantap')    
    
    if message.content.casefold().startswith('hahaha'):
        await message.channel.send('Ngakak akutuh')

    if message.content.casefold().startswith('burung ape tu'):
        await message.channel.send('Burung puyuh')

    if message.content.casefold().startswith('burung apa tuh'):
        await message.channel.send('Burung papilo')

    if message.content.casefold().startswith('yank'):
        await message.channel.send('Apaa sayang :hugging:')

    if message.content.casefold().startswith('kangen'):
        await message.channel.send('Uuuu sini sinii :heart:')

    if message.content.casefold().startswith('love you'):
        await message.channel.send('Love you too :revolving_hearts:')

    if message.content.casefold().startswith('lagi apa'):
        await message.channel.send('Lagi mikirin kamuu :two_hearts:')

    if message.content.casefold().startswith('meletus balon hijau'):
        await message.channel.send('DOR')

    if message.content.casefold().startswith('dor'):
        await message.channel.send('Njir kaget')

    if message.content.casefold().startswith('bot taek'):
        await message.channel.send('lo yang taek')

    if message.content.casefold().startswith('bot goblok'):
        await message.channel.send('lo yang goblok')

    if message.content.casefold().startswith('bot anjing'):
        await message.channel.send('anjing')

    if message.content.casefold().startswith('google earth'):
        await message.channel.send('yang mau unduh klik aja ke : http://earth.google.com')

    if message.content.casefold().startswith('yahha'):
        await message.channel.send('hayyuuuk')
        
    if message.content.casefold().startswith('bangsat kau'):
        await message.channel.send('Mulut anda kotor')
        
    if message.content.casefold().startswith('coffee'):
        await message.channel.send('Green tea')    

    if message.content.casefold().startswith('Green tea'):
        await message.channel.send('Coffee')

    if message.content.casefold().startswith('cawfee'):
        await message.channel.send('Gweentea')

    if message.content.casefold().startswith('gweentea'):
        await message.channel.send('Cawfee')
    
    if message.content.casefold().startswith('ikuzo'):
        await message.channel.send('ORRRAAAAAA')

    if ('algo') in message.content.casefold():
        await message.channel.send('ngulang akwokaowa')
  
    if ('matdis') in message.content.casefold():
        await message.channel.send('LOSSSS')

    if ('basda') in message.content.casefold():
        await message.channel.send('C gan')

    #Sticker gif

    if message.content.casefold().startswith('!sticker'):
        await message.channel.send('<a:721898956216598538:723711816609300541>')

    if message.content.casefold().startswith(':run:'):
        await message.channel.send('<a:0NezukoRun:720837706824941620>')

    if message.content.casefold().startswith(':milos:'):
        await message.channel.send('<a:0RicardoDance:723711866580369428>')

    if message.content.casefold().startswith(':ramspin:'):
        await message.channel.send('<a:0RamSpin:723712671022579733>')

    if message.content.casefold().startswith(':remspin:'):
        await message.channel.send('<a:0RemSpin:723711834388955197>')

    if message.content.casefold().startswith(':yeay:'):
        await message.channel.send('<a:0ShiraishiSuperYeay:723711853443678299>')

    if message.content.casefold().startswith(':gokil:'):
        await message.channel.send('https://cdn.discordapp.com/emojis/825224781162479647.png?v=1')

    if message.content.casefold().startswith(':pekoteme:'):
        await message.channel.send('https://cdn.discordapp.com/emojis/752018226480676865.png?v=1')
    
    if message.content.casefold().startswith(':yamete_:'):
        await message.channel.send('<a:834337876896120832:834337876896120832>')

    if message.content.casefold().startswith(':ning:'):
        await message.channel.send('https://cdn.discordapp.com/emojis/772190940957507584.png?v=1')

    if message.content.casefold().startswith(':saberpeak:'):
        await message.channel.send('https://cdn.discordapp.com/emojis/467557969131864064.png?v=1')
        
    

        834333470494294026
        834333273466339349

#Multiple answer
    SIMP = ('Ricko','Kocir','Nopal','Ricok')
    if message.content.casefold().startswith('siapa yang paling simp'):
        response = random.choice(SIMP)
        await message.channel.send(response)

    queen = ('Meta','Aul','Chiko','Belinda','Bebel','Kamet','Paul','Hiko')
    if message.content.casefold().startswith('7queen'):
        response = random.choice(queen)
        await message.channel.send(response)

    lyoko = ('Will reset it all','Be there when you call','We will stand real tall','Stronger after all')
    if message.content.casefold().startswith('code lyoko'):
        response = random.choice(lyoko)
        await message.channel.send(response)

    jankenpon = (':v:',':fist:',':hand_splayed:')
    if message.content.casefold().startswith('jankenpon'):
        response = random.choice(jankenpon)
        await message.channel.send(response)

    mati = ('Ampun tuhan','ampun bang','Cok baperan')
    if message.content.casefold().startswith('w ban lo ajg'):
        response = random.choice(mati)
        await message.channel.send(response)

    kyostinv = ('put your melantha here','put your vangarda here','not yet','MAMMA MIA','dont forget to use your friend silverash if you dont have','opini yang bagus dokutah, sekarang put your melantha here')
    if message.content.casefold().startswith('kyostin'):
        response = random.choice(kyostinv)
        await message.channel.send(response)

    quotesFF = ('Pacaran sama pemain Free Fire itu gampang. Lagi enggak ngedate, push rank pun jadi.','Kamu itu mirip kayak airdrop yang ingin kuraih, tapi banyak juga yang menginginkanmu','Bukan ku tak ingin membalas chatmu, tapi mengertilah bahwa Free Fireku enggak ada opsi pause','Izinkan aku mencintaimu tanpa harus menghapus Free Fireku','Sendiri bukan berarti sepi, karena berdua pun belum tentu booyah','Ditinggal pas lagi sayang banget itu sakit, tapi ditinggal pas lagi knocked out itu lebih sakit lagi','Mendapatkan kamu itu layaknya mengejar rank Grand Master, sama sulitnya','Kamu harus tahu, Free Fire cuma sekadar pengisi waktu kosongku. Tapi kamulah pengisi hati kosongku','Karena Free Fire, aku jadi lupa memberi kabar ke pasangan. Parahnya, sampai lupa kalau aku sebenarnya enggak punya pasangan','Free Fire rutinitasku, kamu prioritasku','Sakitnya diputusin pacar, enggak sesakit kena landmine Free Fire','Mabar boleh, ibadah jangan sampai terlewat','Game adalah hobiku dan kamu adalah prioritasku.Jadi jangan cemburu sama game, cemburulah ketika aku mendekati yang baru','Kamu itu ibarat flashbang Begitu kena bikin silau dan buta. Gak akan bisa ngelirik yang lain','Lo Bilang Free Fire Game Burik? Eh ngaca! Muka lo lebih burik bos!','Jika Bermuda punya Mill Purgatory punya Brasil Maka setidaknya aku punya kamu untuk mengisi hatiku.')
    if message.content.casefold().startswith('quotes ff'):
        response = random.choice(quotesFF)
        await message.channel.send(response)

    off = ('Baperan','Ngantuk','Paketan abis','Indihome gangguan','Lowbatt','Mau nge SIMP','mau Tham Ngan','mau pacaran dulu','Mau tidur','Mo bobo','Mau belajar','Mau kesekolah','Mau ngoding','Mau cuci piring','Disuruh bobo','Mau ngoding','Mau hacking')
    if message.content.casefold().startswith('off'):
        response = random.choice(off)
        await message.channel.send(response)

    decade = ('K-k-k-kuuga','A-a-a-agito','R-r-r-ryuki','F-f-f-faiz','B-b-b-blade','H-h-h-hibiki','K-k-k-kabuto','D-d-d-denO','K-k-k-kiva','D-d-d-decade','D-d-d-double','O-o-o-ozu','F-f-f-fourze','W-w-w-wizard','G-g-g-gaim','D-d-d-drive','G-g-g-ghost','E-e-e-exaid','B-b-b-build')
    if message.content.casefold().startswith('final form ride'):
        response = random.choice(decade)
        await message.channel.send(response)

#test 
    waifu = ('Ayaka', 'Astolfo', 'Luna')
    if message.content.casefold().startswith("!waifu"):
        if message.content(waifu):
            await message.channel.send("waifu anda: " , )

#random number
    if message.content.casefold().startswith('panjang burung'):
        response = random.randint(0,20)
        await message.channel.send(response)    

    if message.content.casefold().startswith('jumlah mantan'):
        response = random.randint(0,50)
        await message.channel.send(response)

    if message.content.casefold().startswith('nuklir'):
        response = random.randint(0,400000)
        await message.channel.send(response)
    
#kerang ajaib
    if message.content.casefold().startswith('kerang ajaib,'):
        if len(message.content.casefold()) > 16:
            await kerang_parse_petuah(message)
        else:
            await message.channel.send('?')

if __name__ == "__main__":
    client.run(TOKEN)
