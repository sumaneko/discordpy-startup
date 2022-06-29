from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
import re
def get_dice(bot, m, arg):
	name = m.author.name if m.author.nick is None else m.author.nick
	#元気状態なら
	if bot.get_hp() <= bot.dying_hp:
		#瀕死の時
		quotes = [
		  [100 , "そこに、サイコロ・・・ある、んで・・・勝手にやってて、ください・・・"],
		  [100 , "それどこ、じゃ・・・ないです・・・"],
		  [100 , "動けな・・・いで・・・す・・・"],
		]
		return get_quotes(quotes)

	pattern = "^\d+(d|D)\d+$"

	content = re.match(pattern, arg)

	if content:
		return content.group()
	else:
		return "マッチしてないです"

	return get_quotes(quotes)
