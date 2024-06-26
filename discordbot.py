import discord
from discord.ext import commands
import os
import traceback

#汎用モジュール
import random
import datetime
import asyncio

#自作モジュール
from mymodule.bot_reaction import get_bot_reaction
from mymodule.ryonage_bot import RyonageBot
from quotes.harapan import get_harapan
from quotes.dengeki import get_dengeki
from quotes.yakigote import get_yakigote
from quotes.nadenade import get_nadenade
from quotes.morase import get_morase
from quotes.morasuna import get_morasuna
from quotes.omanko import get_omanko
from quotes.omikuji import get_omikuji
from quotes.luckyitem import get_lucky
from quotes.playchu import get_playchu
from quotes.syabette import get_syabette
from quotes.momimomi import get_momimomi
from quotes.feint import get_feint
from quotes.kubishime import get_kubishime
from quotes.penpen import get_penpen
from quotes.erabe import get_erabe
from quotes.dice import get_dice
from quotes.keisan import get_keisan
from quotes.jobchange import get_job
from quotes.prpr import get_prpr
from quotes.unchiku import get_unchiku
from quotes.gpt import get_gpt

#デフォのintentではmemberにアクセスできないので、ここでTrueに（app画面からのserver members intent設定も必要）
inte = discord.Intents.default()
inte.members = True
inte.message_content = True

#BOTをコンストラクト
bot = commands.Bot(command_prefix='/', intents=inte)
#動かすにはトークンが必要
token = os.environ['DISCORD_BOT_TOKEN']

#BOTクールタイム（秒）
ct = 60
#BOT前回の発言イベント時間（初期ct秒黙るためあらかじめ引く）
prev_time = datetime.datetime.now() - datetime.timedelta(seconds=ct)
#プレイ中のターン数
playing_turn = 0

#ボットちゃん
bot_chan = RyonageBot()


#エラーだけど吐かせないでコメントで終わり
@bot.event
async def on_command_error(ctx, error):
	orig_error = getattr(error, "original", error)
	error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
	print(error_msg)
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send("そんなの知らないです・・・")
#await ctx.send(error_msg)

#自分でコマンドを作れる helpなどはオーバライドできない
#@commands.cooldown(1, 30, commands.BucketType.user（とかchannelとかserver）)でクールダウン仕込める
@bot.command()
async def ping(ctx):
	await ctx.send("_chinpong_")
	#botはカスタムステータス使えないらしい
	#await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, state="NAMEOFMYACTIVITY"))

@bot.command()
async def syabutte(ctx):
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send("私に喋って欲しい時は/syabetteですよ？\nえ？本当にしゃぶれ・・・？")
		
@bot.command()
async def aisatsu(ctx):
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		name = ctx.message.author.name if ctx.message.author.nick is None else ctx.message.author.nick
		await ctx.send(f"ドーモ、{name}＝サン。リョナゲボットです。")
		
@bot.command()
async def oppai(ctx):
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send("おっぱいおっぱい！")
		
@bot.command()
async def anal(ctx):
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send("アナルの話しました？")
		
@bot.command()
async def anus(ctx):
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send("本当はアヌスでもアナルはもはや名詞になってますよね")
		
@bot.command()
async def sex(ctx):
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send("せっくす！")
@bot.command()
async def test(ctx):
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send("今はテストはしてないです")

@bot.command()
async def jikan(ctx):
	#瀕死じゃないなら喋る
	dt_now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send(f"日本時間で{dt_now}です")

@bot.command()
async def harapan(ctx):
	global prev_time
	#殴るとCT延長
	prev_time = datetime.datetime.now() + datetime.timedelta(minutes=10)
	await ctx.send(get_harapan(bot_chan, ctx.message))
	
@bot.command()
async def dengeki(ctx):
	global prev_time
	#スタンガンでCT延長
	prev_time = datetime.datetime.now() + datetime.timedelta(minutes=20)
	await ctx.send(get_dengeki(bot_chan, ctx.message))

@bot.command()
async def yakigote(ctx):
	global prev_time
	#焼きごてでCT延長
	prev_time = datetime.datetime.now() + datetime.timedelta(minutes=60)
	await ctx.send(get_yakigote(bot_chan, ctx.message))

@bot.command()
async def kubishime(ctx):
	global prev_time
	#首絞めでCT延長
	prev_time = datetime.datetime.now() + datetime.timedelta(minutes=10)
	await ctx.send(get_kubishime(bot_chan, ctx.message))

@bot.command()
async def penpen(ctx):
	global prev_time
	#お尻ペンペンでCT延長
	prev_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
	await ctx.send(get_penpen(bot_chan, ctx.message))

@bot.command()
async def feint(ctx):
	global prev_time
	#フェイントでCT延長
	prev_time = datetime.datetime.now() + datetime.timedelta(minutes=10)
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send(get_feint(bot_chan, ctx.message))
	
@bot.command()
async def nadenade(ctx):
	bot_chan.heal(15)
	await ctx.send(get_nadenade(bot_chan, ctx.message))
	
@bot.command()
async def momimomi(ctx):
	bot_chan.heal(5)
	await ctx.send(get_momimomi(bot_chan, ctx.message))

@bot.command()
async def prpr(ctx):
	await ctx.send(get_prpr(bot_chan, ctx.message))

@bot.command()
async def morase(ctx):
	await ctx.send(get_morase(bot_chan, ctx.message))
	
@bot.command()
async def morasuna(ctx):
	await ctx.send(get_morasuna(bot_chan, ctx.message))

@bot.command()
async def omanko(ctx):
	await ctx.send(get_omanko(bot_chan, ctx.message))

@bot.command()
async def omikuji(ctx):
	await ctx.send(get_omikuji(bot_chan, ctx.message))
	
@bot.command()
async def lucky(ctx):
	await ctx.send(get_lucky(bot_chan, ctx.message))

@bot.command()
async def jobchange(ctx):
	await ctx.send(get_job(bot_chan, ctx.message))

@bot.command()
async def gpt(ctx):
	await ctx.send(get_gpt(bot_chan, ctx.message))
	
@bot.command()
async def rkey(ctx):
	bot_chan.heal(9999)

@bot.command()
async def keisan(ctx, *arg):
	await ctx.send(get_keisan(bot_chan, ctx.message, *arg))
	#await ctx.send("今は使えません・・・")
	
@bot.command()
async def syabette(ctx):
	global prev_time
	#CTを大袈裟な数でリセット
	prev_time = datetime.datetime.now() - datetime.timedelta(days=1)
	await ctx.send(get_syabette(bot_chan, ctx.message))
	
@bot.command()
async def okiro(ctx):
	global prev_time
	#CTを大袈裟な数でリセット
	prev_time = datetime.datetime.now() - datetime.timedelta(days=1)

@bot.command()
async def erabe(ctx, *args):
	await ctx.send(get_erabe(bot_chan, ctx.message, *args))

@bot.command()
async def dice(ctx, *arg):
	await ctx.send(get_dice(bot_chan, ctx.message, *arg))

@bot.command()
async def unchiku(ctx):
	line = await ctx.send(get_unchiku(bot_chan, ctx.message))
	#何故かカスタム絵文字はフェッチしないと使えなくなった
	emoji = await ctx.guild.fetch_emoji(1031502459652280320)
	await line.add_reaction(emoji)
	emoji = await ctx.guild.fetch_emoji(1031502489717059694)
	await line.add_reaction(emoji)
	#await line.add_reaction("<:hee:1031502459652280320>")
	#await line.add_reaction("<:sitteru:1031502489717059694>")
	#await line.add_reaction("🇾")
	#await line.add_reaction("🇳")

#発言に反応する
@bot.event
async def on_message(message):
	#プレイ中（生きてる時の◯◯をプレイ中ってやつ）を処理する
	global playing_turn
	#健康ならプレイ中
	if bot_chan.dying_hp < bot_chan.get_hp():
		playing_turn -= 1
		#プレイ中の更新
		if playing_turn < 0:
			playing_turn = random.randint(10,60)
			await bot.change_presence(activity=discord.Game(name=get_playchu()))
	else:
		#瀕死になったらやめる
		playing_turn = 0
		await bot.change_presence(activity=None)

	#発言処理パート
	#botならスルー
	if message.author.bot:
		pass
	else:
		bot_chan.heal(1)
		#瀕死じゃないなら喋る
		if bot_chan.dying_hp < bot_chan.get_hp():
			#コマンドなら何もしないためのif
			if message.content[0] != "/":
				global prev_time
				t = prev_time

				if bot.user in message.mentions:
					#メンション（リプ）された時のやつ
					await message.reply(f"何かご用ですか？")
				else:
					#セリフの文字列取得["セリフ", flag]で返る　BOTちゃん反応のために仕方なく順序をずらす
					msg = get_bot_reaction(message)
					
					#ct経ってないかつflagがTrue（通常の反応）なら落とす
					if datetime.datetime.now() < t + datetime.timedelta(seconds=ct) and msg[1]:
						return
					
					if msg[0] != "":
						await message.channel.send(msg[0])
						prev_time = datetime.datetime.now()
	await bot.process_commands(message)


#メンバー加入
@bot.event
async def on_member_join(member):
	#何故か加入メッセージより先に流れるのでスリープでごまかす
	await asyncio.sleep(0.5)
	#玄関チャンネルで発言　多分ニックネームは入った瞬間は付いていないからnameだけでいい
	await bot.get_channel(928650405246824488).send(f"{member.name}さんはじめまして！お暇なときに<#798192857327992882>を一読しておいてくださいね！")
	
	
#アンケートゾーン*************************************************************************************************************
@bot.command()
async def vote(ctx, *args):
	if bot_chan.get_hp() <= bot_chan.dying_hp:
		await ctx.send("いま・・・そんな状態じゃ・・・ないです・・・")
		return
	# 前文句
	name = ctx.message.author.name if ctx.message.author.nick is None else ctx.message.author.nick
	vote_text_prefix = name + "さんのアンケートです！\n:regional_indicator_q:"
	# 選択肢未指定の場合の絵文字
	vote_emoji_on_no_choice = ["⭕","❌"]
	# 選択肢指定の場合の絵文字
	vote_emoji_on_some_choice = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
	# 選択肢の数が↑のやつより多かった場合のメッセージ
	vote_text_choice_overflow_message = "選択肢はしよーじょー10個までです！"
	
	commands = list(args)
	
	if len(commands) <= 0:
		await ctx.send("あの、本文がないとアンケート出来ませんケド・・・")
		return

	text = vote_text_prefix + commands.pop(0)
	if len(commands) <= 0:
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
#アンケート終わり*************************************************************************************************************


#起動
bot.run(token)
