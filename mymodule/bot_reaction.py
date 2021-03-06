#汎用モジュール
import random
#セリフモジュール
from quotes.greetings import get_greetings
from quotes.shimoneta import get_shimoneta
from quotes.cheer import get_cheer
from quotes.ryona import get_ryona
from quotes.hobby import get_hobby
from quotes.calling_bot import get_calling_bot

def get_bot_reaction(msg):
	reaction = ""
	#CTセットするかどうか
	ct_flag = True
	#挨拶
	reaction = get_greetings(msg)
	#中身入ったら終了
	if reaction != "":
		return reaction, ct_flag

	#慰める
	reaction = get_cheer(msg)
	#中身入ったら終了
	if reaction != "":
		return reaction, ct_flag

	#BOTちゃんの反応
	reaction = get_calling_bot(msg)
	if reaction != "":
		ct_flag = False
		return reaction, ct_flag

	#リョナ
	reaction = get_ryona(msg)
	#中身入ったら終了
	if reaction != "":
		return reaction, ct_flag

	#下ネタは確率操作して下げることも可能
	if random.randint(0, 100) < 101:
		reaction = get_shimoneta(msg)
	#中身入ったら終了
	if reaction != "":
		return reaction, ct_flag

	#趣味関連
	reaction = get_hobby(msg)
	#中身入ったら終了
	if reaction != "":
		return reaction, ct_flag

	#一応絶対に通るreturn
	return reaction, ct_flag
