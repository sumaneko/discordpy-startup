from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
def get_momimomi(bot, m):
	t = ""
	name = m.author.name if m.author.nick is None else m.author.nick
	#元気状態なら
	if bot.dying_hp < bot.get_hp():
		quotes = [
			[100, "なっ！なんでいきなり胸に手を伸ばしてきたんですか！？"],
			[100, "やだ！お尻を揉もうとしないでくださいーっ！！"],
			[100, "肩を揉んでくれるんですか？私、肩こりってあんまりなったこと無いんですよね"],
			[100, "おっぱいを揉ませろだなんて言われても困るんですけど！"],
			[100, "け、ケツを揉ませろですって！？"],
			[100, f"私のこと揉みたいだなんて{name}さん、エッチですよね！！"],
			[100, "お腹を揉みたい？うん・・・まあ、別にいいですけど・・・"],
			[100, "お尻は嫌だけど、太ももならまあ・・・揉ませてあげても"],
			[100, "お尻もおっぱいも揉ませてあげませんよ！！"],
			[100, "そ、そんなにおっぱい揉みたいんですか・・・？うーん・・・。痛くしないっていうならちょっと・・・だけ・・・揉ませてあげてもいいですよ"],
			[100, "そこまでしてお尻を揉みたいの・・・？うーん・・・す、スカート越しで、ちょっとだけなら・・・"],
			[50, "いやっ！お尻をそんなに乱暴に揉まないで！！だ、ダメ、変なスイッチ入っちゃ・・・ぅからぁ・・・"],
			[50, "ひゃん！おっぱい、そんなに強く揉みしだいちゃダメですって！！あっ！ちょっと！乳首いじるのまで、は、許可してな・・・ないですよぉ！"],
			[100, "肩とか二の腕とかなら・・・揉んでもいいですよ"]
			]
	else:
		#瀕死の時
		quotes = [
			[100 , "そんな、に・・・揉みたければ・・・も、好きにして・・・"],
			[100 , "動けなくなっ、た・・・女の子なん、か、揉んで・・・楽し・・・ですか・・・？"],
			[100 , "死ぬほど痛い、のに・・・おっぱい、弄られると・・・ムラッとする、ですね・・・"],
			[100 , "それ、で・・・気が済むなら・・・好きな、だけ・・・揉んでくだ、さい・・・"],
			[100 , "き、傷口触らないで！痛いぃ・・・やめてぇ・・・"],
			[100 , "ほら・・・揉みたければ・・・揉めばいい、でしょ・・・"],
			[100 , "お腹、ぐちゃぐちゃなのに・・・いじらない、でぇ！痛い・・・痛いよぉ・・・"],
			[100 , "柔らかい、でしょ・・・？いっぱい、殴られたから、ね・・・"],
			[100 , "楽しそ、ですね・・・私の、お尻・・・気持ちいです、か・・・？"]
			]
		
	t = get_quotes(quotes)
	hp = bot.get_hp()
	#if hp < 0:

	return t