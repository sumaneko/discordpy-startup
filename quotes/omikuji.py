
from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
def get_morase(bot, m):
    t = ""
    #元気状態なら
    if bot.dying_hp < bot.get_hp():
        quotes = [
            [100 , "嫌ですよ・・・なんでお漏らしなんてしなきゃいけないんですか・・・"],
            [100 , "漏らしませんよ！"],
            [100 , "いきなり漏らせだなんて言われても・・・"],
            [100 , "おしっこするならトイレでしますよ！"],
            [100 , "嫌ですよお掃除大変だし・・・"],
            [100 , "そんなに私がおしっこするとこ見たいんですか！？"],
            [100 , "そんな恥ずかしいことしませんよ！"],
            [50 , "わ、分かりましたよ・・・すればいいんでしょ？すれば！ちょっと待ってくださいね\n・・・・\nんっ・・・！あああ・・・パンツ履きながらだから　すっっごい気持ち悪いですぅ・・・\n・・・・\nはぁ・・・お掃除と替えのパンツもってこなきゃ"]
            ]
    else:
        #瀕死の時
        quotes = [
            [100 , "ほんとは漏らしたくなんて・・・ないのに・・・おトイレまで行けそうにありません・・・ははは"],
            [100 , "お漏らしでもなんでもするから　もう殴らないで・・・・・・んんっ・・・"],
            [100 , "んんん・・・恥ずかし・・・です・・・ほんとに・・・"],
            [100 , "ごめんなさいごめんなさい・・・臭いですよね・・・でも動けなく、って・・・"],
            [100 , "気持ち悪い・・・です・・・パンツもスカートも　ぐちゃぐちゃになってる・・・"],
            [100 , "出しちゃいけないのに・・・出ちゃう・・・よ・・・"]
            ]
        
    return get_quotes(quotes)
