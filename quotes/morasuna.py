from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
from mylib.mymodule import get_nick

#[100 , ""],
def get_morasuna(bot, m):
	t = ""
	name = get_nick(m)
	#元気状態なら
	if bot.dying_hp < bot.get_hp():
		quotes = [
			[100 , "そりゃあそうでしょ！"],
			[100 , "漏らすわけないでしょ！"],
			[100 , "もらしませーん"],
			[100 , "当たり前ですよ"],
			[100 , "漏らしませんよ！"],
			[100 , "土下座して頼まれても嫌です～・・・ってあれ？"],
			[100 , "漏らすなと言われると・・・ちょっとおもらししたく・・・な、なるわけないでしょ"],
			[100 , "ちょっとおしっこしたくなってきたような・・・"],
			[100 , "漏らしまーす"],
			[100 , "はい"],
			[100 , "本当にもらしませーん、0%でーす"],
			]
	else:
		#瀕死の時
		quotes = [
			[100 , "ごめん・・・なさい・・・我慢、できない、よ・・・"],
			[100 , "もう痛くって　全然動けなくてェ・・・"],
			[100 , "もう、立てな・・・おしっこ・・・でちゃう・・・"],
			[100 , "もうちょっと・・・だけ、我慢・・・できま・・・す"],
			[100 , "んん・・・おトイレまで・・・我慢、しな・・・きゃ・・・"]
			]
		
	return get_quotes(quotes)
