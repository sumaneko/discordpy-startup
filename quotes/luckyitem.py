from mylib.mymodule import get_quotes_with_damage
from mymodule.ryonage_bot import RyonageBot
def get_lucky(bot, m):
    pre = ""
    suf = ""
    #元気状態なら
    if bot.dying_hp < bot.get_hp():
      pre = m.author.name + "さんのラッキーアイテムは・・・・・・『"
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
            [100 , "わ・た・し"],
            [100 , "javascript"],
            [100 , "Unity"],
            [100 , "RPGツクール"],
            [100 , "カピバラ"],
            [100 , "手袋"],
            [100 , "掃除機"],
            [100 , "箒"],
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
            [100 , "リュックサック"]
            ]
        suf = "』っ！ですっ！"
    else:
        #瀕死の時
        quotes = [
            [100 , "知りま、せん・・・そんなの・・・"],
            [100 , "私、を・・・虐める" + m.author.name + "さんに・・・ラッキーアイテムなん、て・・・無いです・・・"],
            [100 , "私が欲しい、ですよ・・・そんなの・・・"]
            ]
        
    return pre + get_quotes(quotes) + suf