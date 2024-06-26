from mylib.mymodule import get_quotes
from mylib.mymodule import get_nick

#慰める
def get_cheer(m):
	t = ""
	name = get_nick(m)
	if m.content == "死にたい" or m.content == "もう死にたい":
		quotes = [
			[100, "そんなこと言わないでください・・・"],
			[100, f"{name}さんに死んでほしくない人はきっとたくさんいますよ"],
			[100, "死んじゃだめですよ・・・"]
		]
		return get_quotes(quotes)

	if "褒めて" in m.content or "褒めろ" in m.content:
		quotes = [
			[100, "えらいっ"],
			[100, "すごいですね！"],
			[100, "<:iizo:805748601972195328> "],
			[100, "<:eraixtu:809118862259519548> "],
			[100, "よくやった！"]
		]
		return get_quotes(quotes)

	if m.content == "疲れた" or m.content == "もう疲れた" or "もうやだ" in m.content or "もうだめ" in m.content:
		quotes = [
			[100, "休むのは大事ですよ"],
			[100, "頑張ってください！"],
			[100, "気分転換でもしましょう？"]
		]
		return get_quotes(quotes)

	if name == "ぼっふん" and (m.content.endswith("助けて") or m.content.endswith("たすけて")):
		quotes = [
			[100, "何？ぼふんぼふんじゃ分からないですけど"],
			[100, "それは大変ですね"],
			[100, "カピバラって焼くとおいしいらしいですよ"],
			[100, "かぴばらさんを虐めないであげてください！拗ねてしまいます！"],
			[100, "助けてなんてあげませんよ♪"]
		]
		return get_quotes(quotes)

	if m.content == "たすけて" or m.content == "助けて":
		quotes = [
			[100, "何かお困りですか？"],
			[100, "困った時は周りの人を頼ってもいいんですよ！"],
			[100, "私にできることがあるならお手伝いできるんですけど・・・"],
			[100, f"誰か{name}さんを助けてあげてくださいー！"],
			[100, "私に何かできることは・・・あ、あの、尻尾くらいなら触ってもいいですよ？"]
		]
		return get_quotes(quotes)

	return t
