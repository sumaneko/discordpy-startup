from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
def get_nadenade(bot, m):
	t = ""
	#元気状態なら
	if bot.dying_hp < bot.get_hp():
		quotes = [
			[100, "えへへ、どうしたんですか急に？"],
			[100, "ひっ・・・虐めないで！\n・・・あれ？なでてくれるんですか？"],
			[100 ,"やだな、急に優しくしないでくださいよ"],
			[100 , "お返しですよ！なでなでー"],
			[100 , m.author.name + "さんって優しいんですね・・・"],
			[100 , m.author.name + "さんの手、あったかいです"],
			[100 , "傷のところさすってくれるんですか？"],
			[100 , "さっきのがすごく痛かったんですけどちょっと楽になりました・・・"],
			[100 , "誰にでも触らせてあげるわけじゃないんですからね"],
			[100 , "あっ！そ、そこは・・・っ！んっ、まあ痛くされないのなら、いいかぁ・・・"]
		]
	else:
		#瀕死の時
		quotes = [
			[100 , "ひっ・・・こ、来ないで！"],
			[100 , "怖いよ・・・どうせまた虐めるんでしょう・・・？"],
			[100 , "心配するふりをしてまた殴るんでしょ・・・？"],
			[100 , "誰か・・・助けてぇ・・・"],
			[100 , "もう殴らないでぇ・・・"],
			[100 , "お、お願いです許して！"],
			[100 , "もう・・・痛いのは・・・嫌だよ・・・"],
			[100 , "ごめんなさいごめんなさいごめんなさい！"],
			[100 , "なんでもしますからもう痛いことしないで！"]
		]
	
	t = get_quotes(quotes)
	hp = bot.damage(l[1])
	#if hp < 0:

	return t
