import datetime
from mylib.mymodule import get_quotes
from mylib.mymodule import get_nick
#BOTちゃんに呼びかける
#[100, ""],
def get_calling_bot(m):
	name = get_nick(m)
	t = ""
	if "BOTちゃん" in m.content or "Botちゃん" in m.content or "ＢＯＴちゃん" in m.content or "botちゃん" in m.content or "ボットちゃん" in m.content:
		#先入れしておいてBOTちゃんのみの場合に対応している
		#JSTにするには普通に9時間ずらすだけ
		dt_now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
		quotes = [
			[100, "呼びました？"],
			[100, "私ですか？"],
			[100, f"ひょっとして{name}さん、私のこと好きなんですか？"],
			[100, "んもー、そんなに私に興味があるんですか？しょうがないですねぇ"],
			[100, "なんですか？"],
			[100, "また私何かやっちゃいました？"],
			[100, "そうやってすぐ私のこと呼ぶー"],
			[100, "はい！"],
			[100, "BOTちゃんは留守です"],
			[100, "はい　　・・・と見せかけていいえ"],
			[100, "はい？"],
			[100, "ひゃい"],
			[100, "BOTちゃんですよ"],
			[100, "呼ばれた気がする"],
			[100, "お返事してあげませんー"],
			[100, "はいはい"],
			[10000, f"{name}ちゃん！"],
			[100, f"{name}さんってばいつも私の話してるー"],
			[100, "はい"]
		]
		if dt_now.month == 1:
			#quotes.append([100, ""])
			quotes.append([100, str(dt_now.year) + "年も私とこのサーバーをよろしくお願いしますね！"])
		if dt_now.month == 2:
			if dt_now.day == 14:
				quotes.append([500, f"今日はバレンタインデーですよ！{name}さんはチョコもらいましたか？ほんとにー？"])
			if dt_now.day == 22:
				quotes.append([500, "今日は2月22日ですよ！にゃんにゃんにゃん！"])
		if dt_now.month == 3:
			if dt_now.day == 14:
				quotes.append([500 , f"今日はホワイトデーですよ、{name}さん私に何かくださいよ！"])
		if dt_now.month == 4:
			quotes.append([100, f"4月は出会いと別れの季節ですよね。{name}さんはここからいなくなったりしないでください・・・ね？"])
			if dt_now.day == 1:
				quotes.append([300, "実は私BOTちゃんじゃないんですよ　　　　　あ、嘘です"])
				quotes.append([300, f"今日はエイプリルフールですけど{name}さんはなにか嘘つきました？"])
		if dt_now.month == 6:
			quotes.append([100, "梅雨はジメジメしてテンション下がりぎみのBOTちゃんですよ"])
		if dt_now.month == 7:
			quotes.append([100, "今年ももう半分終わってるんですよ、知ってました？"])
		if dt_now.month == 7 or dt_now.month == 8:
			quotes.append([100, "お返事しません暑いから"])
		if dt_now.month == 9:
			quotes.append([100, "だんだん涼しくなってきて気分がいいのでお返事してあげますね"])
		if dt_now.month == 10 or dt_now.month == 11:
			quotes.append([100, "これくらいの気温がずっと続けばいいのにと思ってるBOTちゃんです"])
		if dt_now.month == 12:
			quotes.append([100, "もう12月ですよ、今年が終わっちゃいますよ・・・"])
			if dt_now.day == 24 or dt_now.day == 25:
				quotes.append([500, f"クリスマスなのに{name}さんもよっぽど暇なんですね！ｸｽｸｽ"])

		t = get_quotes(quotes)
		
		#更になにか入っていたら反応
		if m.content.endswith("しないで！"):
			quotes = [
				[100,"うるさいですね……"]
			]
			return get_quotes(quotes)

		if "黙って" in m.content or "だまって" in m.content or "うるさい" in m.content or "静かに" in m.content or "しずかに" in m.content or "黙れ" in m.content or "だまれ" in m.content:
			quotes = [
				[100, "え、うるさかったですか・・・？ごめんなさい・・・"],
				[100, "す、すいません・・・"],
				[100, "あ、あの・・・もしかして私のお腹殴ります・・・？"]
			]
			return get_quotes(quotes)

		if "殺す" in m.content or "殺したい" in m.content:
			quotes = [
				[100, "さ、サツガイヨコクは捕まっちゃうんだぞぉ・・・"],
				[100, "リョナラーだからそういう気持ちは分かるんですけど、や、やめましょ？"],
				[100, "目が怖い！目が怖いですって！"]
			]
			return get_quotes(quotes)

		if "死ね" in m.content or "死んでほしい" in m.content:
			quotes = [
				[100, "し、死にませんよ・・・"],
				[100, "死にたくないもん・・・"],
				[100, "死ねだなんて・・・ひどいよ・・・"],
				[100, "ひ、ひどいこと言わないでください・・・"]
			]
			return get_quotes(quotes)

		if "犯す" in m.content or "犯したい" in m.content or "ヤりたい" in m.content or "ヤらせろ" in m.content or "おかす" in m.content:
			quotes = [
				[100, "あ、あの？目が本気ですよ・・・？"],
				[100, "だ、だめですよそんなハレンチな！"],
				[100, "えっちなのはいけないと思います！"],
				[100, "そういえば私ちょっと用事があるので席外していいですか・・・？"]
			]
			return get_quotes(quotes)

		if "しゃぶれ" in m.content or "しゃぶって" in m.content or "舐めて" in m.content or "舐めろ" in m.content:
			quotes = [
				[100, "ひっ！急におちんちん出さないで！"],
				[100, "おちんちんだったら誰のでも舐めると思ってるんですか！？"],
				[100, "し、しまって！それしまってくださいっ！"],
				[100, "本当にぺろぺろするわけないでしょー！！"]
			]
			return get_quotes(quotes)

		if "レイプ" in m.content or "輪姦" in m.content:
			quotes = [
				[100, "れ、レイプなんてさせませんよ！？"],
				[100, "レイプ！？ひぇ・・・逃げます・・・"],
				[100, "無理矢理犯されるなんて嫌ぁ！！"]
			]
			return get_quotes(quotes)

		if "リョナ" in m.content or "虐待" in m.content:
			quotes = [
				[100, "いやあの・・・私をリョナりたい気持ちは分からないでもないんですけど・・・"],
				[100, "そうですよねリョナはいいですよね！え？なんでこっち見てるんです・・・？"],
				[100, "ほ、ほら私以外にもリョナりたくなる可愛い子はいっぱいいますよ・・・？"]
			]
			return get_quotes(quotes)
		
		if "殴る" in m.content or "腹パン" in m.content or "殴らせろ" in m.content or "殴らせて" in m.content or "殴りたい" in m.content:
			quotes = [
				[100, "嫌ですよ！なんで私が殴られなきゃいけないんですか！！"],
				[100, "いやあの・・・うるさかったなら謝るので、その拳を下ろしてもらえると・・・"],
				[100, "なな、殴らないで！せめて顔を狙うのだけはやめてくださいぃ・・・"]
			]
			return get_quotes(quotes)
		"""優先樹に的にcheerのが高かったので意味無し
		if "褒めて" in m.content or "褒めろ" in m.content:
			quotes = [
				[100, "えらいっ"],
				[100, "すごいですね！"],
				[100, "<:iizo:805748601972195328> "],
				[100, "<:eraixtu:809118862259519548> "],
				[100, "よくやった！"]
			]
			return get_quotes(quotes)
			"""

		if "アナル" in m.content or "ケツ穴" in m.content or "ケツの穴" in m.content or "肛門" in m.content or "アヌス" in m.content or "あなる" in m.content:
			quotes = [
				[100, "アナルは好きだけど見せろと言われても・・・"],
				[100, "だーれが準備いらずの即ハメガバガバアナルだーーーー！！！！"],
				[100, "ガバガバではない・・・はず・・・です　　柔らかいけど・・・"],
				[100, f"{name}さんがアナル好きなのは知ってますけど私のは見せてあげませんよ！"]
			]
			return get_quotes(quotes)

		if "まんこ" in m.content or "マンコ" in m.content or "すじ" in m.content or "まんまん" in m.content or "マンマン" in m.content:
			quotes = [
				[100, "おまんこ！・・・・・・え、お前のを見せろって・・・？"],
				[100, "ど、どこ見てるんですか！そんなとこじっと見てもスカートしかありませんよ！"],
				[100, "例え無理やり脱がされても尻尾で隠しますからねっ！"],
				[100, "スカートに手を突っ込まないでくださいいぃ！！"]
			]
			return get_quotes(quotes)

		if "乳首" in m.content or "おっぱい" in m.content or "巨乳" in m.content:
			quotes = [
				[100, "ちょっと！おっぱい見てるのバレバレですよ！"],
				[100, "あの、私のおっぱいに何かご用でも・・・？"],
				[100, "わわ、おっぱい触っちゃダメですって！"],
				[100, "なんですかそのこっちに伸びてくる手は・・・"]
			]
			return get_quotes(quotes)

		if "お尻" in m.content or ("ケツ" in m.content and "バケツ" not in m.content):
			quotes = [
				[100, "ち、チカンってやつですか！？"],
				[100, "私のお尻をどうするつもりですか！？"],
				[100, "スカートめくってお尻をこっちに向けろですって！？"]
			]
			return get_quotes(quotes)

		if "ベロチュー" in m.content or ("キス" in m.content and "テキスト" not in m.content):
			quotes = [
				[100, "歯磨きとデンタルフロスをちゃんと毎日してる人じゃないと、キスなんてしてあげませんからね"],
				[100, "キスはけっこう特別なモノなので・・・無理やりはちょっと・・・"],
				[100, "ほっぺくらいだったら・・・まだしてあげてもいいですよ"]
			]
			return get_quotes(quotes)

		if "脱げ" in m.content or "脱いで" in m.content:
			quotes = [
				[100, "や、いやですよ！なんで脱がなきゃいけないんですか！"],
				[100, "私のハダカで一体ナニをするつもりですか！？"],
				[100, "例え強引に脱がされたって、尻尾と手で隠せるんですからねっ！！"]
			]
			return get_quotes(quotes)

		if "謝って" in m.content or "謝れ" in m.content:
			quotes = [
				[100, "な、なんで私が謝らなきゃいけないんですか・・・"],
				[100, "私何か悪いことしちゃいました・・・？"],
				[100, "え、ご・・・ごめんなさい"],
				[50, "だが私は謝らない"],
				[100, "す、すみません・・・"]
			]
			return get_quotes(quotes)

		if "変態" in m.content:
			quotes = [
				[100, "わわわたしは変態なんかじゃないですよ"],
				[100, "よしんば私が変態だったら・・・嫌いになっちゃいますか・・・？"],
				[100, "もしかして私を変態さんだと思ってます・・・？"]
			]
			return get_quotes(quotes)

		if "マゾ" in m.content or "ドM" in m.content or "ドＭ" in m.content:
			quotes = [
				[100, "マゾじゃないです！リョナラーですよ私は！"],
				[100, "リョナられて悦んじゃうわけないでしょ！"],
				[100, "い、虐められるのが好きなわけじゃないです・・・"]
			]
			return get_quotes(quotes)

		if "サド" in m.content or "ドS" in m.content or "ドＳ" in m.content or "サディスト" in m.content:
			quotes = [
				[100, "そりゃーどちらかといえばSですよリョナラーなので！"],
				[100, "女王様とお呼び！！！"],
				[100, "女の子をSMどころのレベルじゃないリョナで虐めたいですよね"]
			]
			return get_quotes(quotes)

		if "オナニー" in m.content or "アナニー" in m.content or "クリオナ" in m.content:
			quotes = [
				[100, "公衆の面前でオナニーなんかしませんよ！"],
				[100, "まさか私をおかずにするつもりですか！？"],
				[100, "しないこともないですけど・・・今はやりませんよ！"]
			]
			return get_quotes(quotes)

		if "処女" in m.content:
			quotes = [
				[100, "ま、前は処女ですけど後ろは・・・秘密です"],
				[100, "私は処女ですよ！ほんとですって！"]
			]
			return get_quotes(quotes)

		if "好き" in m.content or "愛してる" in m.content:
			quotes = [
				[100, "えっ・・・やだ、恥ずかしい・・・"],
				[100, f"私も{name}さんのこと好きですよ！"],
				[100, "やだ、突然何を言うんですかぁ・・・"],
				[100, "そ、そんな、いきなり告白されても・・・"]
			]
			return get_quotes(quotes)

		if "かわいい" in m.content or "可愛い" in m.content:
			quotes = [
				[100, "いやだな照れちゃうじゃないですか！"],
				[100, "かわいいって言われるの・・・嬉しいな・・・"],
				[100, "ほんとにかわいいって思ってくれてます～？ほんとにぃ～？"]
			]
			return get_quotes(quotes)

		if "かわいそう" in m.content or "可哀想" in m.content:
			quotes = [
				[100, "どうせ「かわいそうじゃないと抜けない～」とか言うんでしょ！"],
				[100, "実は私としてはまんざらでも・・・いやなんでもないです"],
				[100, "かわいそうとか言いながらめっちゃ笑顔じゃないですか！"]
			]
			return get_quotes(quotes)

		if "シッポ" in m.content or "しっぽ" in m.content or "尻尾" in m.content:
			quotes = [
				[100, "私の尻尾が気になるんですか？"],
				[100, "長くて先っぽまでまっすぐなのが自慢なんですよ！"],
				[100, "触ってもいいですけど敏感だから優しくしてくださいね？"]
			]
			return get_quotes(quotes)

		if "元気" in m.content:
			quotes = [
				[100, "元気ですよ！今はね"],
				[100, "私は元気に生きてます！"],
				[100, "まさかこれから私を元気じゃなくするつもりじゃ・・・"]
			]
			return get_quotes(quotes)
	#BOTちゃん無しパターン
	if m.content == "ヤらせろ" or m.content == "やらせろ" or m.content == "犯す" or m.content == "犯させろ" or m.content == "おかす" or m.content == "おかす":
		quotes = [
			[100, "え、あの・・・私に言ってます・・・？"],
			[100, "や、ヤらせませんよ・・・"],
			[100, "私に言ってるんですか！？嫌ですよ！！"],
			[100, "自分の手でも使っててください！"],
			[100, "赤ちゃん出来ちゃうからダメです！"]
		]
		return get_quotes(quotes)

	if m.content == "しゃぶれ" or m.content == "しゃぶれよ":
		quotes = [
			[100, "い、嫌ですよ！"],
			[100, "しゃぶりませんよ！！"],
			[100, "ちゃんとおちんちん洗いましたか？それでも舐めてあげませんけどねー"],
			[100, "わわ、突然ズボンを降ろさないで！"],
		]
		return get_quotes(quotes)

	if m.content == "殺す" or m.content == "ころす":
		quotes = [
			[100, "え、わ、私を殺しちゃおうとしてます・・・？"],
			[100, "死にたくないので嫌です・・・"],
			[100, "そんな野蛮な言葉使っちゃいけませんよ！・・・え？私に言ってる？"],
			[100, "や、やぁ・・・殺さないで・・・"]
		]
		return get_quotes(quotes)

	if m.content == "死ね" or m.content == "しね":
		quotes = [
			[100, "ま、まさか私に死んでほしいんですか・・・？"],
			[100, "死にたくないです・・・"],
			[100, "いくらなんでもひどいですよ！・・・え？私に言ってる？"],
			[100, "わ、私になら言ってもいいですけど他の人へは絶対言っちゃダメです・・・"]
		]
		return get_quotes(quotes)

	#BOTちゃんだけの時のreturn
	return t
