from mylib.mymodule import get_quotes_with_damage
from mymodule.ryonage_bot import RyonageBot
from quotes.omorashi import get_omorashi
from mylib.mymodule import get_nick

def get_dengeki(bot, m):
	t = ""
	name = get_nick(m)
	l = []
	sikko = ""
	#元気状態なら
	if bot.dying_hp < bot.get_hp():
		quotes = [			
			[100 , "ななな、なにをバチバチさせてるんですか！？スタンガンでしょそれ！？やめて、当てな、ギャん！！！", 20],
			[100 , "や、やめて！スタンガンなんか近づけないでよ！？やだ、やあだ！や　が、ァ゛ァア゛ア！！", 20],
			[100 , "え、急に抱きついてきてどうし・・・ひ゛！？イギイィィア゛ア゛ァァア゛ア゛ア゛！！！！離゛し゛でえ゛え゛え゛え゛！！！！！！グゥウぅぅぁガッ、ア゛ア゛ア゛アァァアアア！！！！", 40],
			[100 , "それすっごく痛いんですよ！？たくさんの針で貫かれたような痛みが走るんですから！だからお願いやメ゛ン゛！！！", 20],
			[100 , "せ、せめて手とか足とかにしてください！お腹はシャレになってないんですって！やだ！やだやだや　ア゛グン゛ッ゛！！！", 20],
			[100 , "やだっ押さえつけないで！やだやあだっ！スタンガン当て続けるのだけは　ギッッ！！痛゛いイダいイダイイ痛゛イ゛ィィイ！！！ギャア゛アア゛ァ゛ア！！！", 40],
			[100 , "ちょちょちょ、おっぱい狙ってるでしょ！？やめてやめてお願い！おね　キ゛ヤンッッ！！！", 30],
			[100 , "嘘でしょ！？お股にスタンガンなんて死んじゃうよぉ！！ヤダやめてやめて！ツ゛ッ゛ッッ゛！！？ア、アギア゛ア゛アッ゛ッ！？！？", 40],
			[100 , "どうしました？何かご用で ア゛ガッ！？・・・・・・う、うぅ・・・痛ぁい・・・痛いよお・・・", 20]
			]
	else:
		#瀕死の時
		quotes = [
			[100 , "それ、当てたい、の・・・？嫌だ・・・なぁ・・・うク゛ぅうん！", 20],
			[100 , "バチバチ嫌ぁ・・・痛い、の、グぅウ゛ン゛っ！！", 20],
			[100 , "痛゛い゛痛゛い゛イタ゛イ！！や、やあアあ゛あ痛゛い゛ぃィィ！！", 40],
			[100 , "あ、あ゛！？あ、ガ、カ゛アア゛ァ゛ああぁ゛ぁぁあ゛あ゛！？", 40],
			[100 , "今、おまんこ、に・・・バチバチされた、ら・・・死んじゃ・・・ヅア゛ッッ！！ア、アア゛ァァ！！", 40],
			[100 , f"{name}さん・・・お願い・・・バチバチするの嫌・・・なの・・・　グァああ゛あ゛！！", 20],
			[100 , f"スタンガ・・・持った{name}さんなん、て・・・嫌、い・・・　ア゛ギャッ゛ッ゛！！", 20]
			]
	
	l = get_quotes_with_damage(quotes)
	#回避があるのでダメージで場合分け
	if 0 < l[1]:
		sikko = get_omorashi(bot, 20)
	#おしっこ判定後にダメージ
	hp = bot.damage(l[1])
	
	#if hp < 0:
	
	return l[0] + sikko
