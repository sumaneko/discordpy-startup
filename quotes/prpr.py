from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
def get_prpr(bot, m):
	t = ""
	name = m.author.name if m.author.nick is None else m.author.nick
	#元気状態なら
	if bot.dying_hp < bot.get_hp():
		quotes = [
			[100 , "ちょ、ちょっと！なんでいきなり舐めてくるんですか！？"],
			[100 , "だぁめですって！や、や、くすぐったい！"],
			[100 , "いーやー！ほんとにペロペロするやつがありますか！やだぁ！！"],
			[100 , "ちゃんと歯磨きとデンタルフロスとマウスウォッシュを毎日やってますか？じゃないと嫌だよ！"],
			[100 , f"女の子をペロペロしたがるとか{name}さんは変態なんですか！？"],
			[100 , f"ひいぃ・・・{name}さんにレイプされるぅぅ・・・"],
			[100 , "まさか汗の味で何か分かるとでも！？"],
			[100 , "おっぱいペロペロしないでぇ・・・吸うのもダメですぅ・・・"],
			[100 , "太もも重点的に舐めないでぇ・・・"],
			[100 , "スカートに・・・顔突っ込まない・・・でぇ・・・ひゃん！あ、あぁダメですってぇ・・・"],
			[100 , "お、お尻をペロペロしたいの！？え？穴まで！？"],
			[100 , "腋舐めないでぇ・・・！恥ずか、し・・・"],
			[100 , "膝裏にしゃぶりつかないでぇ・・・"],
			[100 , "ちょっと！尻尾舐めたら口が毛だらけになっちゃいますよ！"],
			[100 , "おへそ舐めないでぇ・・・はーなーれーてー！ち、力強っ！？"],
			[100 , "あ、アナル舐めは気持ちいいですけど、こここんなレイプみたいなやり方でやっちゃダメですぅ・・・"]
		]
	else:
		#瀕死の時
		quotes = [
			[100 , "もう・・・好きなだけ舐めればいい、でしょ・・・"],
			[100 , "傷舐めないでぇ・・・痛いぃ・・・"],
			[100 , "こん、な、状態でも・・・舐める、ですね・・・"],
			[100 , "血とか、で・・・汚、い・・・ですよ・・・？"],
			[100 , "私を・・・痛めつけてまで・・・舐めたかった・・・の・・・？"]
		]
	
	t = get_quotes(quotes)
	hp = bot.get_hp()
	#if hp < 0:

	return t
