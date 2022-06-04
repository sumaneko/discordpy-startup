from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
def get_erabe(bot, m, *args):
	pre = ""
	suf = ""
	name = m.author.name if m.author.nick is None else m.author.nick

	if  bot.get_hp() <= bot.dying_hp:
		#瀕死の時
		quotes = [
			[100 , "今それどこ、ろじゃ・・・ないです・・・"],
			[100 , "勝手に・・・やっててくだ・・・さい・・・"],
			[100 , "選べ・・・と言われ・・・ても・・・"]
			]
		return get_quotes(quotes)
	else:
		#元気の時
		choices = list(args)

		if len(choices) <= 0:
			return "えっ、選択肢が無いです・・・"

		if len(choices) == 1:
			return choices[0] + "しか選べないじゃないですか！"

		#ここから本題
		pre = [
			[100, "そうですね・・・"],
			[100, "私は"],
			[100, "私なら"],
			[100, "どうしても選べというなら・・・"],
			[100, "え、うーん・・・"],
			[100, ""],
			[100, "私だったら"]
			]
		suf = [
			[100, "がいいと思います"],
			[100, "にします"],
			[100, "ですかね・・・"],
			[100, "！"],
			[100, "を選びます"]
			]
		#中身をquotesにつっこんでいく
		quotes = list(list())
		for choice in choices:
			quotes.append([100, choice])

		return get_quotes(pre) + "「" + get_quotes(quotes) + "」" + get_quotes(suf)
	return