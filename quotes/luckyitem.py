from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
from mylib.mymodule import get_nick

def get_lucky(bot, m):
	pre = ""
	suf = ""
	name = get_nick(m)

	#元気状態なら
	if bot.dying_hp < bot.get_hp():
		pre = f"{name}さんのラッキーアイテムは・・・・・・『"
		quotes = [
			[100 , "アナルバイブ"],
			[100 , "湯呑"],
			[100 , "ビニール傘"],
			[100 , "ギロチン台"],
			[100 , "ローター"],
			[100 , "ペンタブ"],
			[100 , "プロテイン"],
			[100 , "疑似精子"],
			[100 , "マヨネーズ"],
			[100 , "鶏むね肉"],
			[100 , "ゆで卵"],
			[100 , "銀のスプーン"],
			[100 , "生首"],
			[100 , "包丁"],
			[100 , "チェーンソー"],
			[100 , "Steamの積みゲー"],
			[100 , "プラスチックのコップ"],
			[100 , "バナナ"],
			[100 , "ゴールデンキウイ"],
			[100 , "爪楊枝"],
			[100 , "アナルパール"],
			[100 , "エロフィギュア"],
			[100 , "javascript"],
			[100 , "Unity"],
			[100 , "RPGツクール"],
			[100 , "アクションゲームツクール"],
			[100 , "カピバラ"],
			[100 , "手袋"],
			[100 , "掃除機"],
			[100 , "ホウキ"],
			[100 , "ツヴァイヘンダー"],
			[100 , "日本刀"],
			[100 , "ハルバード"],
			[100 , "メッサー（グロスメッサー）"],
			[100 , "プレートアーマー"],
			[100 , "クロスボウ"],
			[100 , "ロングボウ"],
			[100 , "牛刀"],
			[100 , "肩ロース肉"],
			[100 , "エロ漫画"],
			[100 , "アナルもののAV"],
			[100 , "手鏡"],
			[100 , "イラスト参考書"],
			[100 , "猫のぬいぐるみ"],
			[100 , "耳掛け型イヤホン"],
			[100 , "ブックスタンド"],
			[100 , "レモン"],
			[100 , "トマト"],
			[100 , "スピーカー"],
			[100 , "ミネラルウォーター"],
			[100 , "アジャスタブルダンベル"],
			[100 , "ゲーミングマウス"],
			[100 , "液タブ"],
			[100 , "コピー用紙"],
			[100 , "プリン"],
			[100 , "ハイカカオチョコレート"],
			[100 , "アーモンド"],
			[100 , "彫刻刀"],
			[100 , "ハサミ"],
			[100 , "手首"],
			[100 , "足首"],
			[100 , "スカート"],
			[100 , "コスプレグッズ"],
			[100 , "ラブドール"],
			[100 , "カチューシャ"],
			[100 , "ヘアピン"],
			[100 , "お寿司"],
			[100 , "冷凍マグロ"],
			[100 , "しいたけ"],
			[100 , "折りたたみ椅子"],
			[100 , "シャーペン"],
			[100 , "ボールペン"],
			[100 , "ピンセット"],
			[100 , "浣腸用のシリンジ"],
			[100 , "サバイバルナイフ"],
			[100 , "遮光カーテン"],
			[100 , "大福"],
			[100 , "練乳"],
			[100 , "キッチンカー"],
			[100 , "脚立"],
			[100 , "歯ブラシ"],
			[100 , "デンタルフロス"],
			[100 , "デッサン人形"],
			[100 , "30cm定規"],
			[100 , "接着剤"],
			[100 , "USBメモリ"],
			[100 , "電卓"],
			[100 , "カレンダー"],
			[100 , "コーヒー"],
			[100 , "おっぱい"],
			[100 , "おまんこ"],
			[100 , "Suica"],
			[100 , "C++"],
			[100 , "薙刀"],
			[100 , "段ボール箱"],
			[100 , "ティッシュ"],
			[100 , "片手鍋"],
			[100 , "乳首に刺す名札"],
			[100 , "片手斧"],
			[100 , "ショートソード"],
			[100 , "アーミングソード"],
			[100 , "ロングソード"],
			[100 , "アルテマウェポン"],
			[100 , "ロトの剣"],
			[100 , "チェインメイル"],
			[100 , "三色ボールペン"],
			[100 , "焼き鳥の缶詰"],
			[100 , "乾パン"],
			[100 , "駆逐艦"],
			[100 , "石"],
			[100 , "コンクリートブロック"],
			[100 , "レンガ"],
			[100 , "豆腐"],
			[100 , "スライム"],
			[100 , "ローション"],
			[100 , "うさみみバンド"],
			[100 , "バニースーツ"],
			[100 , "バイアグラ"],
			[100 , "媚薬"],
			[100 , "ぷっちょのケース"],
			[100 , "たけのこの里"],
			[100 , "きのこの山"],
			[100 , "チョコモナカジャンボ"],
			[100 , "バトルドーム"],
			[100 , "砥石"],
			[100 , "リオレウス"],
			[100 , "超大型巨人"],
			[100 , "ミギー"],
			[100 , "バキSAGA"],
			[100 , "雀牌"],
			[100 , "足の爪"],
			[100 , "ジャポニカ学習帳"],
			[100 , "DXライブラリ"],
			[100 , "Godot"],
			[100 , "ドラえもん（のぶ代ボイス）"],
			[100 , "ポニーテール"],
			[100 , "ボンデージ"],
			[100 , "新しいPC"],
			[100 , "5円玉"],
			[100 , "1万円札"],
			[100 , "サングラス"],
			[100 , "ブルーライトカットメガネ"],
			[100 , "チョコパフェ"],
			[100 , "堅揚げポテト"],
			[100 , "お団子"],
			[100 , "A4ファイル"],
			[100 , "野太刀"],
			[100 , "エアコン"],
			[100 , "バランスボール"],
			[100 , "算数ドリル"],
			[100 , "殺虫スプレー"],
			[100 , "ベープマット"],
			[100 , "虫取り網"],
			[100 , "ロープ"],
			[100 , "Tシャツ"],
			[100 , "エッチな下着"],
			[100 , "魚雷"],
			[100 , "かつおぶし"],
			[100 , "パンツ"],
			[100 , "心霊写真"],
			[100 , "ハンガー"],
			[100 , "爪切り"],
			[100 , "お米"],
			[100 , "唐揚げ"],
			[100 , "漂白剤"],
			[100 , "湯たんぽ"],
			[100 , "シャンプーのボトル"],
			[100 , "After Effects"],
			[100 , "Photoshop"],
			[100 , "クリップスタジオ"],
			[100 , "触手"],
			[100 , "消臭スプレー"],
			[100 , "消毒用エタノール"],
			[100 , "自転車"],
			[100 , "ビー玉"],
			[100 , "ハイパーヨーヨー"],
			[100 , "ミニ四駆"],
			[100 , "緑茶"],
			[100 , "紅茶"],
			[100 , "野菜ジュース"],
			[100 , "トマト"],
			[100 , "懐中時計"],
			[100 , "懐中電灯"],
			[100 , "防災リュック"],
			[100 , "ハンドガン"],
			[100 , "トミーガン"],
			[100 , "ロケットランチャー"],
			[100 , "四次元ポケット"],
			[100 , "1.5Lのペットボトル"],
			[100 , "方位磁針"],
			[100 , "羅針盤"],
			[100 , "漢字ドリル"],
			[100 , "ファミコン"],
			[100 , "カセットテープ"],
			[100 , "呪いのビデオ"],
			[100 , "ニプレス"],
			[100 , "猫のヒゲ"],
			[100 , "ゲームボーイ"],
			[100 , "ガントレット"],
			[100 , "サバトン"],
			[100 , "アーメット"],
			[100 , "バルビュート"],
			[100 , "アナルフック"],
			[100 , "ベーコン"],
			[100 , "パンの耳"],
			[100 , "高級食パン"],
			[100 , "甘酒"],
			[100 , "ガチャポンのカプセル"],
			[100 , "木刀"],
			[100 , "お土産の剣型キーホルダー"],
			[100 , "幸運を呼ぶツボ"],
			[100 , "硯"],
			[100 , "筆"],
			[100 , "電極"],
			[100 , "スタンガン"],
			[100 , "キャットナインテイル"],
			[100 , "レイピア"],
			[100 , "こんにゃく"],
			[100 , "黒マテリア"],
			[100 , "コメドプッシャー（ニキビ潰し）"],
			[100 , "毛抜き"],
			[100 , "山芋"],
			[100 , "海老の天ぷら"],
			[100 , "食塩"],
			[100 , "ブランデー"],
			[100 , "ビール"],
			[100 , "バファリン"],
			[100 , "モンエナ"],
			[100 , "オロナミンC"],
			[100 , "アクエリアス"],
			[100 , "ポカリスエット"],
			[100 , "パトランプ"],
			[100 , "へぇボタン"],
			[100 , "チャージマン研DVDBOX"],
			[100 , "蹄鉄"],
			[100 , "バスターソード"],
			[100 , "バスタードソード"],
			[100 , "蛇口"],
			[100 , "ネジ"],
			[100 , "六角ボルト"],
			[100 , "餃子"],
			[100 , "肉まん"],
			[100 , "ピザマン"],
			[100 , "伊達メガネ"],
			[100 , "バンダナ"],
			[100 , "ラブレター"],
			[100 , "紐水着"],
			[100 , "スクール水着"],
			[100 , "アナル型オナホール（非貫通タイプ）"],
			[100 , "妖精さん"],
			[100 , "猫耳美少女"],
			[100 , "マスカラ"],
			[100 , "ランニングシューズ"],
			[100 , "懸垂スタンド"],
			[100 , "バスタオル"],
			[100 , "塩麹"],
			[100 , "ケチャップ"],
			[100 , "クリピアス"],
			[100 , "乳首ピアス"],
			[100 , "手錠"],
			[100 , "足枷"],
			[100 , "珪藻土コースター"],
			[100 , "ワカメ"],
			[100 , "昆布"],
			[100 , "だしパック"],
			[100 , "ウニ"],
			[100 , "ピッケル"],
			[100 , "ツルハシ"],
			[100 , "ギター"],
			[100 , "リュート"],
			[100 , "レオタード"],
			[100 , "ドラム缶"],
			[100 , "フライパン"],
			[100 , "三角コーナー"],
			[100 , "マニキュア"],
			[100 , "洗濯バサミ"],
			[100 , "ピカチュウ"],
			[100 , "スーパーマリオ"],
			[100 , "ドラえもん（CV：大山のぶ代）"],
			[100 , "ハローキティ"],
			[100 , "ラップの芯"],
			[100 , "トイレットペーパー"],
			[100 , "かまぼこの板"],
			[100 , "ストロー"],
			[100 , "針金"],
			[100 , "豚骨ラーメン"],
			[100 , "レバー"],
			[100 , "変身ステッキ"],
			[100 , "メイス"],
			[100 , "お馬さんのおちんちん"],
			[100 , "栗おこわ"],
			[100 , "アナルプラグ"],
			[100 , "セミの抜け殻"],
			[100 , "マイクロファイバーの雑巾"],
			[100 , "サランラップ"],
			[100 , "お箸"],
			[100 , "スタンド使い"],
			[100 , "紙粘土"],
			[100 , "つけまつげ"],
			[100 , "おろし金"],
			[100 , "グランドピアノ"],
			[100 , "リコーダー"],
			[100 , "月の石"],
			[100 , "万華鏡"],
			[100 , "畳"],
			[100 , "虫眼鏡"],
			[100 , "利尿剤"],
			[100 , "大胸筋矯正サポーター"],
			[100 , "おちんぽミルク"],
			[100 , "ベニヤ板"],
			[100 , "スレッジハンマー"],
			[100 , "五寸釘"],
			[100 , "そうめん"],
			[100 , "カツオのたたき"],
			[100 , "藁人形"],
			[100 , "セーター"],
			[100 , "金塊"],
			[100 , "梅干し"],
			[100 , "チェダーチーズ"],
			[100 , "チャーシュー"],
			[100 , "上履き"],
			[100 , "ブルマ"],
			[100 , "バファリン"],
			[100 , "単2電池"],
			[100 , "鎖鎌"],
			[100 , "ひまわりの種"],
			[100 , "母乳"],
			[100 , "おしっこ"],
			[100 , "リュックサック"]
			]
		#わ・た・しの確率を２％にするためあとから追加
		num = len(quotes) * 0.02 * 100
		quotes.append([num , "わ・た・し♥"])
		
		suf = "』っ！ですっ！"
	else:
		#瀕死の時
		quotes = [
			[100 , "知りま、せん・・・そんなの・・・"],
			[100 , f"私、を・・・虐める{name}さんに・・・ラッキーアイテムなん、て・・・無いです・・・"],
			[100 , "私が欲しい、ですよ・・・そんなの・・・"]
			]
		
	return pre + get_quotes(quotes) + suf
