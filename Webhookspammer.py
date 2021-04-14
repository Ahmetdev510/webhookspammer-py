from discord_webhook import DiscordWebhook,DiscordEmbed


url = input('Webhook url giriniz : ')
embed1 = input('Webhook embed spam atsınmı e veya h : ')
webhook = DiscordWebhook(url=url)

if(embed1 == "e"):
    print("""

    1) Başlık 
    2) açıklama
    3) Başlık ve açıklama
    4) Başlık açıklama ve renk
    5) Resim
    
    """)
    secim = input("Lütfen seçim yapınız: ")
    if(secim == "1"):
        title = input("Başlıkta ne yazıcak: ")
        embed = DiscordEmbed(title=title)
        webhook.add_embed(embed)
        while True:
            webhook.execute()
    elif(secim == "2"):
        aciklama = input("Açıklamada ne yazıcak: ")
        embed = DiscordEmbed(description=aciklama)
        webhook.add_embed(embed)
        while True:
            webhook.execute()
    elif(secim == "3"):
        title = input("Başlıkta ne yazıcak: ")
        aciklama = input("Açıklamada ne yazıcak: ")
        embed = DiscordEmbed(title=title,description=aciklama)
        webhook.add_embed(embed)
        while True:
            webhook.execute()
    elif(secim == "4"):
        title = input("Başlıkta ne yazıcak: ")
        aciklama = input("Açıklamada ne yazıcak: ")
        renk = input("Renk kodu gir: ")
        embed = DiscordEmbed(title=title,description=aciklama,color=renk)
        webhook.add_embed(embed)
        while True:
            webhook.execute()
    elif(secim == "5"):
        resim = input("Resim url Gir: ")
        embed = DiscordEmbed()
        embed.set_image(url=resim)
        webhook.add_embed(embed)
        while True:
            webhook.execute()

elif(embed1 == "h"):
    yazı = input("Webhook ne spamı atıcak: ")
    webhook = DiscordWebhook(url=url, content=yazı)
    while True:
        webhook.execute()


else:
    print("Lütfen seçim yapın.")