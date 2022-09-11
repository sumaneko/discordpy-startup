from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
def get_job(bot, m):
	pre = ""
	suf = ""
	name = m.author.name if m.author.nick is None else m.author.nick

	#元気状態なら
	if bot.dying_hp < bot.get_hp():
		pres = [
			[100, f"{name}さんは今日から"],
			[100, f"{name}さんの新たなジョブは・・・・・・"],
			[100, f"{name}さんはー、えーっとね・・・・・・"]
		]
		pre = get_quotes(pres) + "『"

		quotes = [
			[100,"AV監督"],
			[100,"Vtuber"],
			[100,"Youtuber"],
			[100,"お花屋さん"],
			[100,"くノ一"],
			[100,"じゅじゅちゅし"],
			[100,"すっぴん"],
			[100,"はぐれメタル"],
			[100,"アイドル"],
			[100,"アコライト"],
			[100,"アサシン"],
			[100,"アスリート"],
			[100,"アナウンサー"],
			[100,"アルケミスト"],
			[100,"アルバイト"],
			[100,"アークプリースト"],
			[100,"アークメイジ"],
			[100,"イラストレーター"],
			[100,"ウエイター"],
			[100,"ウォリアー"],
			[100,"エルフ"],
			[100,"エロ博士"],
			[100,"エンジニア"],
			[100,"オールドワン"],
			[100,"カタギ"],
			[100,"カメラマン"],
			[100,"ガンスリンガー"],
			[100,"ガンナー"],
			[100,"ガーディアン"],
			[100,"キュレーター"],
			[100,"ギャンブラー"],
			[100,"クリエイター"],
			[100,"クルセイダー"],
			[100,"コマンドー"],
			[100,"ゴッドハンド"],
			[100,"サウンドコンポーザー"],
			[100,"サンシタ"],
			[100,"サーバーエンジニア"],
			[100,"サーファー"],
			[100,"シェフ"],
			[100,"シーフ"],
			[100,"スタンド使い"],
			[100,"スライムナイト"],
			[100,"スラムの花売り"],
			[100,"スーパースター"],
			[100,"スーパーヒーロー"],
			[100,"セクシーギャル"],
			[100,"セノバイト"],
			[100,"ソルジャークラス1st"],
			[100,"ソードマスター"],
			[100,"ダークナイト"],
			[100,"ディレクター"],
			[100,"デストロイヤー"],
			[100,"ドラグーン（ドラゴンと呼ばれる銃装備の騎兵）"],
			[100,"ドラゴンナイト"],
			[100,"ドラゴンライダー"],
			[100,"ナイト"],
			[100,"ニンジャ"],
			[100,"ニンベン師"],
			[100,"ニート"],
			[100,"ネクロマンサー"],
			[100,"ハンター"],
			[100,"バニーガール"],
			[100,"バーサーカー"],
			[100,"パティシエ"],
			[100,"パラディン"],
			[100,"パン屋"],
			[100,"ヒーラー"],
			[100,"ビショップ"],
			[100,"ビーストマスター"],
			[100,"ピザ屋"],
			[100,"フリーター"],
			[100,"フリーランサー"],
			[100,"ブラックスミス"],
			[100,"ブレイヴベアラー"],
			[100,"プリンセス"],
			[100,"プリースト"],
			[100,"プレデター"],
			[100,"プログラマー"],
			[100,"プロショッパー"],
			[100,"プロデューサー"],
			[100,"プロフェッサー"],
			[100,"プロレスラー"],
			[100,"ホーリーナイト"],
			[100,"マネージャー"],
			[100,"メイド"],
			[100,"メカニック"],
			[100,"メスガキ"],
			[100,"モンク"],
			[100,"ヤクザ"],
			[100,"ライフセーバー"],
			[100,"ランツクネヒト"],
			[100,"レンジャー"],
			[100,"ヲタク"],
			[100,"ヴァルキリー"],
			[100,"中学生"],
			[100,"中将"],
			[100,"仮面ライダー"],
			[100,"会計士"],
			[100,"作曲家"],
			[100,"侍"],
			[100,"傭兵"],
			[100,"僧侶"],
			[100,"兵士"],
			[100,"兵長"],
			[100,"冒険家"],
			[100,"冒険者"],
			[100,"処刑人"],
			[100,"刑事"],
			[100,"剣聖"],
			[100,"勇者"],
			[100,"医者"],
			[100,"博士"],
			[100,"占い師"],
			[100,"同人作家"],
			[100,"吟遊詩人"],
			[100,"呪術師"],
			[100,"団長"],
			[100,"土方"],
			[100,"壊し屋"],
			[100,"大将"],
			[100,"妖精さん"],
			[100,"姫騎士"],
			[100,"射手"],
			[100,"小作人"],
			[100,"小学生"],
			[100,"少将"],
			[100,"山賊"],
			[100,"工場長"],
			[100,"巫女"],
			[100,"幼稚園児"],
			[100,"弁護士"],
			[100,"弓手"],
			[100,"忍者"],
			[100,"怪盗"],
			[100,"愛玩動物"],
			[100,"戦士"],
			[100,"戦隊ヒーロー"],
			[100,"拳聖"],
			[100,"探偵"],
			[100,"提督"],
			[100,"教師"],
			[100,"教祖"],
			[100,"数学者"],
			[100,"整備士"],
			[100,"旅人"],
			[100,"時魔道士"],
			[100,"暗黒騎士"],
			[100,"木こり"],
			[100,"格闘家"],
			[100,"検事"],
			[100,"槍術士"],
			[100,"歌手"],
			[100,"武士"],
			[100,"武道家"],
			[100,"流浪人"],
			[100,"海賊"],
			[100,"漫画家"],
			[100,"無職"],
			[100,"猫"],
			[100,"王宮兵士"],
			[100,"画家"],
			[100,"白魔道士"],
			[100,"盗賊"],
			[100,"看守"],
			[100,"研ぎ師"],
			[100,"砲術士"],
			[100,"神官"],
			[100,"種付けおじさん"],
			[100,"竜騎兵"],
			[100,"算術士"],
			[100,"絵師"],
			[100,"絵描き"],
			[100,"美少女"],
			[100,"美食家"],
			[100,"義賊"],
			[100,"自販機の中の人"],
			[100,"英雄"],
			[100,"薬師"],
			[100,"裁判官"],
			[100,"覆面レスラー"],
			[100,"触手"],
			[100,"記者"],
			[100,"調律師"],
			[100,"調教師"],
			[100,"調査兵団"],
			[100,"調香師"],
			[100,"警察"],
			[100,"貴族"],
			[100,"賢者"],
			[100,"赤魔道士"],
			[100,"踊り子"],
			[100,"軽業師"],
			[100,"農家"],
			[100,"農民"],
			[100,"運転手"],
			[100,"配管工"],
			[100,"錬金術師"],
			[100,"鍛冶屋"],
			[100,"鑑定士"],
			[100,"青魔道士"],
			[100,"音楽家"],
			[100,"風来坊"],
			[100,"騎兵"],
			[100,"騎士"],
			[100,"高校生"],
			[100,"魔戒騎士"],
			[100,"魔法剣士"],
			[100,"魔術師"],
			[100,"魔道士"],
			[100,"黄金騎士"],
			[100,"黒魔道士"],
			[100,"対魔忍"],
			[100,"鑑定士"]
		]
		
		sufs = [
			[100, "として生きていきなさい"],
			[100, "・・・・・・じゃ！"],
			[100, "として使命を果たしてください"]
		]
		suf = "』" + get_quotes(sufs)
	else:
		#瀕死の時
		quotes = [
			[100 , "そんな、の・・・勝手に考えて・・・ください・・・"],
			[100 , f"{name}さんの・・・好きに、生きれば・・・いいでしょ・・・"],
			[100 , "考えられな・・・いです・・・"]
			]
		
	return pre + get_quotes(quotes) + suf