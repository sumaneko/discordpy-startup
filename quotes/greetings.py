import datetime
from mylib.mymodule import get_quotes
from mylib.mymodule import get_nick

#挨拶
def get_greetings(m):
	t = ""
	name = get_nick(m)
	#JSTにするには普通に9時間ずらすだけ
	dt_now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
	if "おやす" in m.content:
		quotes = [
			[100, "おやすみなさい～"],
			[100, "寝るんですか？私も寝たい！おやすみ！"],
			[100, "睡眠は大事ですよ！"],
			[100, "寝るおやす！"]
		]
		return get_quotes(quotes)

	if "落ちます" in m.content or "おちます" in m.content:
		quotes = [
			[100, "落ちるんですか？おつかれー"],
			[100, "お疲れ様です"],
			[100, "おつー"]
		]
		return get_quotes(quotes)

	if "こんば" in m.content:
		quotes = [
			[100, "こんばんは！"],
			[100, "こんばんはー"],
			[100, "こん～"]
		]
		return get_quotes(quotes)

	if "こんにち" in m.content:
		quotes = [
			[100, "こんにちは！"],
			[100, "こんにちー"]
		]
		return get_quotes(quotes)

	if m.content == "こんー":
		quotes = [
			[100, "こんー"],
			[100, "こんこん"],
			[100, "こん～"]
		]
		return get_quotes(quotes)

	if m.content == "おはー" or "おはよ" in m.content:
		quotes = [
			[100, "おはー"],
			[100, f"{name}さんおはー"],
			[100, "おはよ～"]
		]
		return get_quotes(quotes)

	if m.content == "あけおめ" or "あけましておめでとう" in m.content or "明けましておめでとう" in m.content:
		if dt_now.month == 1:
			quotes = [
				[100, "あけおめですよ！"],
				[100, "あけましておめでとうございます！"],
				[100, "あけおめ～"]
			]
		elif dt_now.month == 12:
			quotes = [
				[100, "あけおめにはちょっと早いですよ？"],
				[100, "それは来月でしょ！"],
				[100, "まだあけてないです・・・"]
			]
		else:
			quotes = [
				[100, "はいはいあけおめあけおめ"],
				[100, "まだ" + str(dt_now.month) + "月ですよ、からかってます？"],
				[100, "あけませんよ！"]
			]
		return get_quotes(quotes)

	return t
