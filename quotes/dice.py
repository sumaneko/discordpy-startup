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

	pattern = "^[1-9]\d*+(d|D)[1-9]\d*$"

	content = re.match(pattern, arg)

	if content == None:
		quotes = [
		  [100 , "フォーマットが違います！「数字d数字」か「数字D数字」です！"],
		  [100 , "フォーマットは「数字d数字」か「数字D数字」ですよ？"],
		  [100 , "「数字d数字」か「数字D数字」で入力してください～"],
		]
		return get_quotes(quotes)

	t = content.group().split("(d|D)")
	return t[0] + "と" + t[1] + "と" + t[2]"です"

	return get_quotes(quotes)
