from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
from mylib.mymodule import get_nick

def get_syabette(bot, m):
	name = get_nick(m)
	#元気状態なら
	if bot.dying_hp < bot.get_hp():
		quotes = [
		  [100 , "もー、しょうがないなー"],
		  [100 , "そんなに私に喋ってほしいんですか？"],
		  [100 , "私も忙しいんだけどなぁ～"],
		  [100 , "しょうがないにゃあ"],
		  [100 , "いやでプー"],
		  [100 , "別に私は喋りたくないんですけどねー！"],
		  [100 , f"いいでしょう！このBOTちゃんが{name}さんのために喋ってあげましょう！"]
		]
	else:
		#瀕死の時
		quotes = [
		  [100 , "・・・・・・"],
		  [100 , "無理・・・です・・・"],
		  [100 , "こんな・・・状態、で・・・何か喋れ・・・ると、でも・・・？"],
		]
	return get_quotes(quotes)
