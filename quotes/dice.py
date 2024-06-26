from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
import re
import random
from mylib.mymodule import get_nick

def get_dice(bot, m, *arg):
	name = get_nick(m)
	#元気状態なら
	if bot.get_hp() <= bot.dying_hp:
		#瀕死の時
		quotes = [
		[100 , "そこに、サイコロ・・・ある、んで・・・勝手にやってて、ください・・・"],
		[100 , "それどこ、じゃ・・・ないです・・・"],
		[100 , "動けな・・・いで・・・す・・・"],
		]
		return get_quotes(quotes)

	miss_quotes = [
		[100 , "フォーマットが違います！「数字d数字」か「数字D数字」です！"],
		[100 , "フォーマットは「数字d数字」か「数字D数字」ですよ？"],
		[100 , "「数字d数字」か「数字D数字」で入力してください～"],
		]
	target = list(arg)
	#引数の数がおかしい
	if len(target) != 1:
		return get_quotes(miss_quotes)

	pattern = "^[1-9]\d*(d|D)[1-9]\d*$"
	#コンパイル
	repatter = re.compile(pattern)
	content = repatter.match(target[0])

	#マッチしてない
	if content is None:
		return get_quotes(miss_quotes)

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