from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
def get_erabe(bot, m, *args):
	pre = ""
	suf = ""
	name = m.author.name if m.author.nick is None else m.author.nick

	if  bot.get_hp() <= bot.dying_hp:
		#瀕死の時
		quotes = [
			[100 , "今それどこ、ろじゃ・・・ないです・・・"],
			[100 , "勝手に・・・やっててくだ・・・さい・・・"],
			[100 , "選べ・・・と言われ・・・ても・・・"]
			]
	else:
		#元気の時
		choices = list(args)
		quotes = [[]]

		if len(choices) < 0:
			return "えっ、選択肢が無いです・・・"

		if len(choices) == 1:
			return choices[0] + "しか選べないじゃないですか！"

		for i in choices:
			qoutes.append([100, choices[i]])

	return get_quotes(quotes)

"""

		text = vote_text_prefix + choices.pop(0)
		if len(choices) <= 0:
			#マルバツ
			vote = await ctx.send(text)
			for emoji in vote_emoji_on_no_choice:
				await vote.add_reaction(emoji)
		else:
			for index in range(len(commands)):
				if index < len(vote_emoji_on_some_choice):
					text += "\n" + vote_emoji_on_some_choice[index] + ":" + commands[index]
				else:
					text += "\n" + vote_text_choice_overflow_message
					break
			vote = await ctx.send(text)
			for index in range(len(commands)):
				if index < len(vote_emoji_on_some_choice):
					await vote.add_reaction(vote_emoji_on_some_choice[index])

	return choices[0] + choices[1]
	#return pre + get_quotes(quotes) + suf
"""