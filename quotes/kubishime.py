from mylib.mymodule import get_quotes_with_damage
from mymodule.ryonage_bot import RyonageBot
from quotes.omorashi import get_omorashi
from mylib.mymodule import get_nick

def get_kubishime(bot, m):
	t = ""
	name = get_nick(m)
	l = []
	sikko = ""
	#元気状態なら
	if bot.dying_hp < bot.get_hp():
		quotes = [			
			[100 , "ちょ、がっ・・・！？ぐ、ぐぅぅうう・・・ぐぇ、う゛ぅ゛ぅ゛うう！！", 30],
			[100 , "首、絞めな・・・や゛、うぐぅ゛ぅあ゛あぁ！", 30],
			[100 , "突然何す、ぎぇっ・・・！がっ・・・かはっ！？", 30],
			[100 , "苦゛し゛・・・、あ゛・・・！・・・かはっ！げほっごほっ！な、何てこと、げぇ゛ぇ・・・", 30],
			[100 , "やめ、や゛・・・はなし・・・がぁ・・・", 30],
			[100 , "あぐ・・・あ゛う゛・・・がが・・・ぷはっ！な、んか・・・別の、せか・・・が・・・見えま・・・した・・", 30],
			[100 , "ぐっ゛・・・が、あ゛・・・ヒューヒュー・・・あっ！・・・アハ・・・しゅご・・・", 30]
			]
	else:
		#瀕死の時
		quotes = [
			[100 , "ほん、どに・・・死んじゃ、ぐぁ・・・あ゛・・・", 30],
			[100 , "か゛ぁ゛・・・い゛ゃ・・・殺さな゛・・・で・・・", 30],
			[100 , "苦し゛・・・ぐぇ・・・ヒュー、ヒュー・・・", 30],
			[100 , "やだ・・・や゛・・・死んじゃ・・・！あ゛・・・・・", 30],
			[100 , "いや゛・・・ぐぁ・・・・・・・う・・・", 30],
			[100 , "おねが・・・です・・・やめ゛・・・", 30],
			[100 , "・・・・・・・あ゛・・・・・・・ぐ、う゛ぅ・・・", 30]
			]
	
	l = get_quotes_with_damage(quotes)
	#ダメージ前しっこ
	sikko = get_omorashi(bot, 20)
	#おしっこ判定後にダメージ
	hp = bot.damage(l[1])
	
	#if hp < 0:
	
	return l[0] + sikko
