from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
import re
import random
def get_keisan(bot, m, *arg):
	name = m.author.name if m.author.nick is None else m.author.nick
	#元気状態なら
	if bot.get_hp() <= bot.dying_hp:
		#瀕死の時
		quotes = [
		[100 , "今あた、ま、回ら・・・ないです・・・"],
		[100 , "電卓で、も・・・使っててく・・・ださ・・・い"],
		[100 , "なんで、わたし・・・が・・・そんな、の・・・答えなく、ちゃ、いけない・・・ですか・・・"],
		]
		return get_quotes(quotes)

	formula = "".join(arg)
	miss_quotes = [
		[100 , "フォーマットが違うんじゃないですか？数字と+-/*とカッコだけにしてくださいね"],
		[100 , "これフォーマット違います！何か変なコマンド入れようとしたりしてないでしょうね？エッチ！！"],
		[100 , "何か変ですよこれ"],
		]

	pattern = "[\d\s\(\)\+\-\*\/]+"

	#コンパイル
	repatter = re.compile(pattern)
	content = repatter.match(formula)

	#マッチしてない
	if content is None:
		return get_quotes(miss_quotes)

	result = eval(formula)
	quotes = [
		[100 , f"「{formula}」の結果は・・・「{result}」っです！"],
		[100 , f"{name}さんの代わりに私が「{formula}」の答えを教えてあげましょう！「{result}」です！！"],
		[100 , f"「{formula}」の答えはなんだと思いますか？・・・ふふふ、「{result}」ですよ！"],
		[100 , f"「{formula}」は「{result}」です！暗算なら得意なんですよ！"],
		]

	return get_quotes(quotes)
"""
	t = re.split("(d|D)", content.group())

	#振る回数
	num = int(t[0])
	if num > 10:
		return "振る回数が多すぎです！10回までにしてください！！"
	#賽の目
	d_roll = int(t[2])
	if d_roll >999999:
		return "100万以上の数はちょっと・・・"
	#出た目
	result = 0
	#出た目の羅列
	r_text = ""
	#合計
	d_sum = 0

	#最初の1回はカンマつかない
	result = random.randint(1, d_roll)
	d_sum += result
	r_text += str(result)
	for i in range(num-1):
		r_text += "、"
		result = random.randint(1, d_roll)
		d_sum += result
		r_text += str(result)

	quotes = [
		[100 , f"{r_text}だったので{d_sum}です！"],
		[50 , f"{r_text}ですって。{name}さん代わりに足しといてください（{d_sum}）"],
		[100 , f"{r_text}！合計{d_sum}です！多分！"],
		]
	return get_quotes(quotes)
"""