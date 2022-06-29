from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
import re
def get_dice(bot, m, *arg):
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

	miss_quotes = [
		  [100 , "フォーマットが違います！「数字d数字」か「数字D数字」です！"],
		  [100 , "フォーマットは「数字d数字」か「数字D数字」ですよ？"],
		  [100 , "「数字d数字」か「数字D数字」で入力してください～"],
		]
	target = list(arg)
	#引数の数がおかしい
	if len(target) != 1:
		return get_quotes(miss_quotes)

	pattern = "^[1-9]\d*+(d|D)[1-9]\d*$"

	content = re.match(pattern, str(target[0]))
	return "テスト"
	#マッチしてない
	if content is None:
		return get_quotes(miss_quotes)

	return content.group()
	t = re.split("(d|D)", content.group())
	return t
#	return t[0] + "と" + t[1] + "と" + t[2] + "です"

	return get_quotes(quotes)