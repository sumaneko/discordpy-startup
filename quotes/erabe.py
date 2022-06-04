from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
def get_erabe(bot, m, *args):
    pre = ""
    suf = ""
    name = m.author.name if m.author.nick is None else m.author.nick

    #元気状態なら
    if  bot.get_hp() <= bot.dying_hp:
        #瀕死の時
        quotes = [
            [100 , "知りま、せん・・・そんなの・・・"],
            [100 , f"私、を・・・虐める{name}さんに・・・ラッキーアイテムなん、て・・・無いです・・・"],
            [100 , "私が欲しい、ですよ・・・そんなの・・・"]
            ]
    else:
        choices = list(args)

     return choices[0], choices[1]   
    #return pre + get_quotes(quotes) + suf
