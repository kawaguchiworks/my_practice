"""
リスト内包表記
リストを簡単に生成するための表記

forを使って一行でリストを書ける
[式 for 変数 in 繰り返しオブジェクト]
"""

#基本
x = [i + 1000 for i in range(6)]
print(x)

names = ["斉藤", "山田", "田中"]
x = [i + "さん" for i in names]
print(x)

#条件つき
x = [i for i in range(11) if i % 2 != 0]#奇数の時だけ10回繰り返す
print(x)

foods = ["apple", "banana", "lemon"]
x = [i for i in foods if "a" in i]
print(x)

#三項演算子を使用
x = ["偶数" if i%2 == 0 else i for i in range(11)]
print(x)

kanto = ["千葉", "栃木", "東京", "埼玉", "茨城", "群馬", "神奈川"]
x = [i + "都" if i == "東京" else i + "県" for i in kanto]
print(x)