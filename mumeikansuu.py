"""
無名関数:
ラムダ式で作った関数オブジェクト
名前をつけるほどではない小さい関数を使う時に使う

lambda 引数: 処理 (改行できない、一行で書く)
lambda 引数1,引数2: 処理 
"""

func = lambda x, y: print(f"{x}さんは{y}です")
func("鈴木","学生")

"""
map関数:
繰り返しオブジェクトの全ての要素にある処理を行う

map(関数,繰り返しオブジェクト)
"""
#map関数とラムダ関数との組み合わせ

#ラムダ関数の引数が1つの場合
names = ["鈴木", "斉藤", "田中"]
result = list(map(lambda x: x + "さん",names))#namesリスト全てにラムダ関数を適用
print(result)

#ラムダ関数の引数が複数ある場合
n1 = ["鈴木", "斉藤", "田中"]
n2 = ["めい", "ゆづき", "ひなた"]
result = list(map(lambda x,y : x + y + "さん",n1,n2))
print(result)

"""
filter関数:
繰り返しオブジェクトの中である条件がTrueになる要素だけを抽出する関数

filter(関数,繰り返しオブジェクト)
"""

#filter関数とラムダ関数との組み合わせ
numbers = [5, 8, 10, 12, 30]
result = list(filter(lambda x:x >= 10, numbers))
print(result)

#リスト内包表記で書いた場合
result_1 = [x for x in numbers if x >= 10] 
print(result_1)

#※ラムダ式は対象がリストだけじゃなくてタプルや集合とかも使える



