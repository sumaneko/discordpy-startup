from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
from mylib.mymodule import get_nick

#[100 , ""],
def get_omanko(bot, m):
	t = ""
	name = get_nick(m)
	#元気状態なら
	if bot.dying_hp < bot.get_hp():
		quotes = [
			[100 , "おまーんこ"],
			[100 , "やだ・・・この人突然/omankoとか言い始めた・・・"],
			[100 , "急にどうしたんですか？"],
			[100 , "オマーン湖"],
			[100 , "おまんこ！！"],
			[100 , "女性器のことですか？"],
			[100 , "急におまんことか言わないでくださいよ・・・"],
			[100 , "おまんこに何かご用事でも？"],
			[100 , ":suji:"],
			[100 , "日々のストレスで急におまんことか言いたくなる気持ちも分かりますよ"],
			[100 , "Coochieっておまんこって意味なんですよ"],
			[100 , "おまんこ！"]
			]
	else:
		#瀕死の時
		quotes = [
			[100 , "おま・・・んこ・・・"],
			[100 , "な、なんですか・・・、煽ってる・・・ですか・・・？"],
			[100 , "い、や・・・おまんこ、殴ら・・・ない、でぇ・・・"]
			]
		
	return get_quotes(quotes)
