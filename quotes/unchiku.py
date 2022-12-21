from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
def get_unchiku(bot, m):
	pre = ""
	suf = ""
	name = m.author.name if m.author.nick is None else m.author.nick

	#元気状態なら
	if bot.dying_hp < bot.get_hp():
		#[100 , ""],
		#pre = ""
		quotes = [
			[100 , "宇宙って95%が観測出来ないなんかよくわからないエネルギーで出来てるらしいですよ。こわ・・・"],
			[100 , "精子は34度付近が一番活発になるのでタマタマは体外に出てるんですよ"],
			[100 , "板チョコの溝は別に割るために付いてるんじゃなくて、冷やし固める時表面積が増えて効率がいいからああなってるんですよ"],
			[100 , "爪楊枝の持ち手部分の溝は、製作工程で付いちゃうだけで別に意味があって付いてるんじゃないらしいですよ"],
			[100 , "絵文字は海外に輸出されてて、「emoji」で普通に通じるくらいメジャーなんですよ"],
			[100 , "BUKKAKEがエロ用語として定着しすぎたので、うどん屋さんが海外出店する時「ぶっかけうどん」って名称が使いづらいんですよ"],
			[100 , "昭和の雑誌は芸能人とか有名人の住所が普通に載ってたらしいですよ。個人情報の概念なんて無かったんですね"],
			[100 , "ルパン三世の石川五ェ門は初登場時はキャラが定まって無くて、「不二子ちゃんはそれがしのがぁるふれんど」とか言い出す上に、\n不二子のホラ話のせいでルパンに「色キチガイ」呼ばわりされたんですよ"],
			[100 , "動物には換毛期がありますが、それの名残なのか人間も春と秋は毛が抜ける量が増えるらしいですよ"],
			[100 , "WHOの調査によると、1年間習慣的に行ったセックスにおいて妊娠する確率は中出し85%外出し4%らしいですよ。あ、私で試そうとか思わないでくださいね！"],
			[100 , "女の子の乳輪の平均サイズ（300人調査）は4cmで、乳首は1.3cmらしいですよ。あと他の研究によると男性の乳首の大きさは女性の約36%だったんですって"],
			[100 , "彼氏の前でイったふりをしたことがある女の子は68%いて、その理由の1位は「恋人が傷つくと思ったから」なんですって。これぞ思いやりってやつですね"],
			[100 , "世界最年少で出産した記録は4歳で妊娠、5歳7ヶ月で出産（帝王切開）したんですって。ちなみに現在のギネスブックからは削除されてるらしいですよ。ペドなんてレベルじゃないですね"],
			[100 , "世界最多の出産記録を持つ女性は40年間で69人も産んだんですって。つまり二次元の女の子ならもっと産めるってことですよきっと！"],
			[100 , "馬の血液型は理論上3兆通りあるらしいですけど、ベースは8種だし同じように人間も細かく分けると300種とかになるらしいですよ"],
			[100 , "嘘は嘘であると見抜ける人でないと（掲示板を使うことは）難しいんですよ"],
			[100 , "短時間の睡眠で済むショートスリーパーは先天的な遺伝子の問題なので、訓練とかで短くできるものじゃないらしいですよ"],
			[100 , "ルパン三世は勝手に著作物である「アルセーヌ・ルパンの孫」ということにしてるので、フランスで発売する時名前がエドガーになったんですよ\nちなみに2011年に著作権が切れたのでもう大丈夫みたいですよ"],
			[100 , "両手を伸ばすと身長と同じ長さになると言うことがありますけど、あくまで大体同じだけでほとんどの人が数cm長かったり短かったりするんですよ"],
			[100 , "ルパン三世は不殺の怪盗だと思われてますが、アニメでも原作でも割と人殺してるんですよ"],
			[100 , "のび太は10年間無人島で生きていたことがあって、その後タイムマシンとタイムふろしきで元に戻された事があるんですよ"],
			[100 , "柿の種って商標登録されてないんですよ"],
			[100 , "クレイジーダイヤモンドは砕けませんけどダイヤモンドはハンマーで簡単に砕けるんですよ"],
			[100 , "大人は嘘つきなんじゃなくて間違いをするだけらしいですよ"],
			[100 , "小便小僧は有名ですが、実は小便少女もあるんですって。ロリコンの石化フェチだったんですかね？"],
			[100 , "黄金バットは強すぎて核攻撃を喰らっても無傷なんですよ"],
			[100 , "揖保乃糸には実は等級が7つもあるんですよ。スーパーでよく見る赤い帯のやつはランクが一番下だけど名前は「上級品」なんですよ\nちなみに内1種は「太づくり」というそうめんというよりひやむぎなんですよ"],
			[100 , "卵の白いヒモみたいなやつはカラザといって栄養豊富な部分なので、食感がよほど嫌とかじゃない限り捨てないほうがいいですよ"],
			[100 , "金星には硫酸の雨が降っているんですよ。でも地表が熱すぎて届かないらしいですよ"],
			[100 , "初代スーパーマリオブラザーズはたった40キロバイトで作られているんですよ。キロですよメガじゃなくて！"],
			[100 , "宇宙には本当に全く何も存在しない、どこの星の光も一切届かない「ヴォイド」という空間があるんですよ。エクスデスもにっこりですね"],
			[100 , "洋食は海外でもYoshokuで通じるらしいですよ"],
			[100 , "金玉は50キロとか60キロ程度の圧力で破裂しちゃうんですよ。ウケるー！"],
			[100 , "口から肛門までの長さは9mとかなんですって。けっこう長い触手を用意しないといけませんね"],
			[100 , f"血管を全部つなぎ合わせると約10万キロにもなるんですって！{name}さんで試してみてもいいですか？"],
			[100 , "人間の歯ってモース硬度が7もあるんですって。ちなみに鉄が4でダイヤが10らしいです"],
			[100 , "ドライヤーを使っていると段々溜まっていく口の部分の埃は、冷風出しながら濡れた綿棒で回すようにこするとよく取れるんですよ\n放置するとコゲたり最悪発火しちゃうからこまめにとってくださいね"],
			[100 , "サラダ油とかで「コレステロール0」とかデカデカ書いてる商品がありますが、あれは動物性脂に含まれているものなので植物油がコレステロール0なのは当たり前なんですよ"],
			[100 , "ポテトチップスは「フライドポテトが厚すぎる」というイチャモンで何度も作り直しさせられたシェフが、「じゃあ限界まで薄くしてやる」とキレて作ったのが始まりらしいですよ、殺伐としてますね"],
			[100 , "スマブラとかで有名な桜井政博さんはわずか19歳の時に星のカービィの企画を通したんですよ。ヤバイですね！"],
			[100 , "カエルのお肉って鶏肉と味が似ているんですよ"],
			[100 , "10円の物が20円になったら高く感じますけど、10000円のものが10010円になっても大して変わったように見えないのは、人間の感覚は比例（比率）で感じてるからなんですよ\nこれをウェーバー・フェヒナーの法則と言って、音とか臭いとか重さとか色々な刺激に適用できるんですよ"],
			[100 , "血液型占いとかみたいに「誰にでも当てはまる」ことを自分のことだと思い込むようなことをバーナム効果と言うんですよ"],
			[100 , "1円玉の製造費って約3.1円なんですよ。ちなみに5円玉は約10.1円で500円玉は約19.9円なんですって（2018年度の推算）"],
			[100 , "生卵の賞味期限は「生で安全に食べられる」期限であって、ちゃんと加熱するならもうちょっと経ってても食べられるんですよ。でもやっぱり早めに食べてくださいね"],
			[100 , "ペットボトルの水は「無機物」なので未開封なら理論上は何年でも腐らないんですよ。でも一応賞味期限は設定されてるんです\nそれはなんでかというと、「量が減るから」"],
			[100 , "「何が嫌いかより何が好きかで自分を語れよ!!!」というセリフはワンピースのルフィのもの・・・ではないんですけど、コラ画像に釣られて公式で言わせてしまったゲームがあるんですよ"],
			[100 , "バイオハザードシリーズの通路は90cmというこだわりがあるらしいですよ。初代バイオを作ってる時に人とすれ違う時一番ストレスな広さを日常で巻き尺持って研究した数字を今も踏襲してるんですって"],
			[100 , "排水管の耐熱温度は70とか80度なので、流しに直にお湯を捨てるのは故障の原因になるんですよ。お水も出して一緒に流しましょうね"],
			[100 , "人間の頭の堅さってカボチャと同じくらいらしいですよ。そして頭蓋骨は素焼きの鉢くらいなんですって"],
			[100 , "ゲゲゲの鬼太郎の目玉の親父は目をつぶることができるんですよ"],
			[100 , "カメの亀頭はカメの頭より大きいんですって！"],
			[100 , "アンパンマンは初出のデザインだと人間だったらしいですよ"],
			[100 , "「女体入口」とかいうバス停が長野県にあるんですって！"],
			[100 , "陰茎骨っていうおちんちんに骨がある動物は結構いっぱいいるんですよ"],
			[100 , "ガムテープを勢いよく剥がすと光るんですよ"],
			[100 , "クローン人間と一卵性双生児って内容は同じなんですよ"],
			[100 , "このサーバーのお誕生日は2021年1月11日で、私が参加したのが1月19日なんですよ。ちなみに初めて喋ったのは翌20日なんです。たまには思い出してくださいね！"]
			]
		
		#suf = ""
	else:
		#瀕死の時
		quotes = [
			[100 , "思い、つかない・・・です・・・"],
			[100 , "教えてあげま、せん・・・何も・・・"],
			[100 , "私を虐めると・・・喋れなくなる、です、よ・・・知ってます・・・？"]
			]
		
	return pre + get_quotes(quotes) + suf
