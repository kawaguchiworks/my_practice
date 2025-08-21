"""
一行ずつそれぞれの役割や性質を理解しながら進める
 (わからない箇所がないように)
"""

"""
記号の理解(随時追加)
.はオブジェクトの属性(固定された名前)にアクセスするための記号 
[]角括弧はキーやインデックスでデータを探すための記号 
()関数やクラス、メソッドを呼び出すためのもの  
"""

#関数と()はセット
print("こんにちは！") #printは()の中身を出力する関数

"""
変数(値を入れる箱)
apple_price = 100 #変数名は分かりやすく(小文字と単語は_で繋げる)
print(apple_price)
"""

#代入
x = 10
y = 100
x = y
print(x)

#変数の型
apple_price = 100 #整数型(int型)
name = "山田" #文字列型(str型)
weight = 54.5 #浮動小数点型(float型)
print(apple_price, name, weight)

#変数の型の取得
apple_price = 100 
a_type = type(apple_price)

name = "山田" 
n_type = type(name)

weight = 54.5
w_type = type(weight)

print(a_type, n_type, w_type)

"""
数値演算

演算子
足し算 +
引き算 -
かけ算 *
割り算 /
べき乗 ** べき根 √→**(1/2)
割り算の余り %
切り捨て割り算 // ※計算の優先順位は数学と同じ
"""

math = 82
japanese = 74 
english = 60
avg_score = ( math + japanese + english) / 3
print(avg_score)

#文字列の操作
surname = "山田"
given_name = "太郎"
full_name = surname + given_name #文字列を足すと並ぶ
print(full_name)

"""
文字列フォーマット

f"{変数}"
"""
#f-string(変数埋め込み)
price = 100
text = f"この商品は{price}円です"
print(text)

#ゼロ埋め
x = 123
print(f"{x:010}")#xを0で埋めて10桁表示

#金額用カンマ
x = 9000000
print(f"{x:,}")#

#小数点以下桁数
x = 0.123
print(f"{x:.5f}")


"""
リスト(一つの変数に複数の値を持つ型※リスト型)※インデックスを持つ
"""

student_name = ["斉藤", "小林","佐々木", "田中"]
student_name.append("佐藤") #追加
student_name.remove("佐々木")#削除
print(student_name)

student_name_2 = ["斉藤", "小林","佐々木", "田中"]
a = student_name_2[0:3]#インデックス(順序)の指定 ※ ,の数
b = len(student_name_2)#リストの要素の数(長さ)

print(f"０から３までの生徒は{a}",f"全生徒の数は{b}人")

x = ["a", "b", 100]
y = ["a", "f"]
z = x + y #リスト同士の結合
print(z)

#ex.3教科の平均を出すプログラム
math = 82
japanese = 74 
english = 60
avg_score = (math + japanese + english) / 3
print(avg_score)

#リストを使ったver(リストに要素を追加するだけで値が変わる)
scores = [82, 74, 60]
avg_score = sum(scores) / len(scores)
print(avg_score)

"""
辞書(keyとvalue(一つのペア)として複数持つ型※辞書型)※インデックス持たない
"""

prices = {"バナナ": 250, "みかん": 300, "いちご": 500}
x = prices["みかん"]#辞書名[key]でvalueを取り出せる
prices["ぶどう"] = 400 #新しいkeyとvalueを追加
prices["バナナ"] = 200 #既にあるkeyのvalue値を変更
print(prices)

# ※同じkeyは反映されない(後に追加のもの)
prices = {"バナナ":250, "みかん":300, "バナナ":500} 
print(prices) 

#辞書の結合
price_1 = {"バナナ":250, "みかん":300, "いちご":450} 
price_2 = {"トマト":280, "梨":150} 
price_1.update(price_2)#updateメソッドで辞書同士の結合
price_1_len = len(price_1)#lenでリスト同様、要素の数を取り出せる
print(f"結合された辞書は{price_1}、要素数は{price_1_len}")

#辞書のリスト化
prices = {"バナナ":250, "みかん":300, "いちご":500}
fruit = list(prices.keys())#.keys()と.value()→その要素だけを抽出
print(fruit) #※dict_values型の為、list()でリスト化する必要あり

#ex.5教科の理科は社会より「○点」高いか抽出するプログラム
scores = {"数学": 82, "国語": 74, "英語": 60, "理科": 92, "社会": 70}
diff = scores["理科"] - scores["社会"]
print(f"{diff}点")

#ex.5教科の平均を「○点」と出力するプログラム
scores = {"数学": 82, "国語": 74, "英語": 60, "理科": 92, "社会": 70}
scores_values = list(scores.values()) #valueだけを抽出しリスト化
avg_score = sum(scores_values) / len(scores_values)
print(f"{avg_score}点")

scores = {"数学": 82, "国語": 74, "英語": 60, "理科": 92, "社会": 70}
avg_score = sum(scores.values()) / len(scores.values()) 
print(f"{avg_score}点")#sum,len関数はdict_value型をそのまま入れることが可

"""
集合(インデックスを持たない,同じ値を持てない)
set()で集合に型変換
"""

x = {1, 2, 4} 
x.add(7) #追加
x.discard(1) #削除　.discard()または.remove()※removeは対象がなければエラー
print(x)

x = {0, 1, 3, 6}
y = {0, 2, 5, 6}
a = x | y #和集合 
b = x - y #差集合
c = x & y #積集合
print(a, b, c)

"""
タプル(インデックスを持つ、同じ値を持てる※値を変更できない)
tuple()でタプルに型変換
"""

x = (1, 1, 4, "A", "B", "C") #ex.緯度経度
y = x[0:5] #リストのインデックスと同じように抽出できる
print(y)

"""
制御構文(if,for文)
インデント→コードのブロックを表すのにコードの書き始める位置を後ろに下げる
(1インデント→半角スペース4つ)
ブロックが始まりを示す:(コロン)が必要 ex.if文、for文、関数定義、クラス定義
"""

"""
条件分岐(if文)※インデントを使用

if 条件文: 
    条件分がTrueの時の処理
else:
    条件文がFalseの時の処理
   
True:
条件が満たされている ※頭文字は大文字
False:
条件が満たされていない 

TrueやFalse→Bool型(論理型)の値(どちらも変数に代入可) 
"""

#等価、不等価の条件式（==、!=）
x = "Apple"
result = x == "Apple" 
print(result)

prefecture = "ワシントン"

if prefecture == "東京":
    print("日本の首都です") 
elif prefecture == "ワシントン": 
    print("アメリカの首都です")
   
number = 0
if number % 2 == 0: 
    print("偶数です")
else:
    print("奇数です")
    
#ex.閏年の判定
year = 2024

if year % 400 == 0: #狭い条件から入れていく
    print("閏年です")
elif year % 100 == 0:
    print("平年です")
elif year % 4 ==0:
    print("閏年です")
else:
    print("平年です")

#大小比較の条件式(>= 、>、<、<=)
age = 20
if age >= 20:
    print("成人です")
elif age >= 18: #elifはいくつも書ける
    print("成人ですが飲酒できません")
elif age >= 6:
    print("こどもです")
else:
    print("乳児・幼児です")
    
#包括の条件式(in)
x = "apple"
result = x in ["apple","banana"]
print(result)

#複数の条件を組み合わせる(and:かつ、or:または)
age = 20
gender = "女性"
result = (age >= 20) and (gender == "女性")
print(result)

#否定(not:ではない)
age = 19
result = not(age >= 20)
print(result)

"""
while文(ある条件がTrueになっている間ある処理を繰り返す)
while 条件:
    繰り返したい処理
"""
x = 0
while x <= 10: #xが10以下の間ずっと繰り返す
    x += 1
    print(f"1を加算した後のx:{x}")
    
#whileとファイル読み込み
with open("text.txt") as f:
    t = f.readline() #一行読み込む
    while t != "": #空文字じゃなくなるまで
        print(t)
        t = f.readline()#次の行を読み込む(ないと無限ループ)
    
"""
繰り返し処理(for~in文)※コレクションから要素を取り出し繰り返す
for 変数 in 繰り返しオブジェクト(リスト・辞書・range等):
    処理
"""

#[リスト](タプル){集合}の場合
x_list = [100, 190 , 2980]
for x in x_list:
    x_yen = str(x) + "円"
    print(x_yen)
    
scores = [90, 30, 40] 
for x in scores:#要素を取り出す
    print(x + 1)

#辞書の場合
fruit = {"apple": 130, "banana": 350, "lemon": 100} 
for name,price in fruit.items(): #.items()はキーと値のペアを取り出す関数
    print(f"{name}は{price}円です") 

#range関数(回数が決まっていてfor文回したい時)
for x in range(5): #range関数は連番の整数を作れる※最後の数字は含まれない
    print(x) 

for i in range(1,11): #:ではなく,に注意
    print(i)

#break(繰り返しを強制終了)
numbers = [10, 21, 100, 18, 2]
for n in numbers:
    if n >= 100: #ここで終了
        break

#continue(スキップして次の繰り返し処理を続ける)
number = [10, 21, 32, 65]
for n in numbers:
    if n % 2 == 0: 
        continue #continueが発動したらそれ以降のコード
                 #(同じブロック内)は実行されない

#ex.名前に「さん」をつけるプログラム
names = ["斉藤", "佐藤", "鈴木"]
for x in names:
    print(f"{x}さん")

#ex.教科の名前と点数を表示させるプログラム
scores = {"数学":82, "国語":74, "英語":60, "理科":92, "社会":78}

for k,v in scores.items():
    print(f"{k}は{v}点です")

#fizzbuzz問題(for,if組み合わせ)
for number in range(1,101): 
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
        

"""
関数(処理を一つにまとめて定義する)

関数定義
def 関数名(引数1,引数2,…): 
    処理…
    処理…
    return 戻り値  

引数:関数に渡された値 戻り値:関数が返す値
"""

#関数呼び出し
def add_sub_numbers (a, b): 
    #関数の処理の部分
    c = a + b
    d = a - b
    return c, d #return(戻り値)が結果になる※外でその値を使う時に必要(処理だけしたい時はいらない)

x,y = add_sub_numbers(10,100)
print(x)
print(y)

def is_leep_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False 

year = 2024
result = is_leep_year(year) #returnが設定した変数に代入される
print(result)

"""
クラス

クラス:設計図(実体はない空)
メソッド:クラスの中にある関数 ※引数がない場合は()のみつける
引数:材料(材料がないと動かない関数、メソッド、クラスには()の中に引数を入れる)
オブジェクト(インスタンス)→実体化したもの ※クラス名()でインスタンス化できる
インスタンス変数→オブジェクトの具体的な値や名前
クラス変数→クラスで共通した値

クラスの定義

class クラス名:
    変数名 = 値 ⇦クラス変数
    def __init__(self,引数,…):
        self.変数名 = 引数 ⇦インスタンス変数
    def メソッド名(self,引数,…):
        #処理
"""

#ex.生徒のテストの点数を管理するプログラム

class Student:
    def __init__(self,name,math,japanese,english,science,society):
        self.name = name
        self.math = math
        self.japanese = japanese
        self.english = english
        self.science = science
        self.society = society

    def average_score(self):
        #５教科の平均点を計算するメソッド
        avg = (self.math + self.japanese + self.english 
               + self.science + self.society) /  5
        return avg

student_1 = Student("斉藤そうま", 82, 74, 60, 92, 72)
s1_avg = student_1.average_score()
print(f"斉藤さんの５教科の点数は{s1_avg}点です")

student_2 = Student("田中かえで", 75, 78, 80, 85, 68)
s2_avg = student_2.average_score()
print(f"田中さんの５教科の平均は{s2_avg}点です")

#ex.アパレルのネット通販で商品クラスを作るケース
class Item:
    def __init__(self,id,name,price,purchase_price):
        self.id = id
        self.name = name 
        self.price = price
        self.purchase_price = purchase_price

    def cost_rate(self):
        rate = self.purchase_price / self.price
        return rate

item_1 = Item("A0001", "半袖クールTシャツ", 5000, 2250)
item_1.price = 6000
rate = item_1.cost_rate()
print(rate)

#ex.生徒のクラス
class Student:
    def __init__(self, name, grade, section, scores):
        self.name = name
        self.grade = grade
        self.section = section
        self.scores = scores
    def add_score(self, subject, score):
        self.scores[subject] = score #辞書に追加するだけだからreturnいらない
    def total_score(self):
        return sum(self.scores.values()) #辞書(self.scores)のvalue(点数)のみ取り出してその合計を返す


student_1 = Student("鈴木", 2, "B", {"数学": 80, "英語": 70, "国語": 90})
student_2 = Student("田中", 2, "B", {"数学": 70, "英語": 80, "国語": 75})
student_3 = Student("斉藤", 2, "B", {"数学": 90, "英語": 85, "国語": 80})

for student in [student_1, student_2, student_3]: #生徒のリスト化しfor文で回す
    print(f"{student.name}さんの合計点数は{student.total_score()}点です")
    #nameのような変数・属性は()いらない.total_scoreのようなメソッド(関数)必ずつける

#ex.トランプゲーム(カードクラスとデッキクラス)
class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["ハート", "ダイヤ", "スペード", "クラブ"]:
            for number in range(1,14):
                card = Card(suit, number)#一枚のカードを表す
                self.cards.append(card)
    
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    
    def draw_card(self):
        return self.cards.pop(0)#先頭を要素を取り出し"返してから"消す
    
deck = Deck() #山札を作る設計図から作られた山札の実物(※この時点でリストではない→オブジェクト=インスタンス)
deck.shuffle() #山札の実物をシャッフル
for card in deck.cards: #リストの状態から一枚ずつ取り出す ※cardsはリストだからアクセス
    print(f"{card.suit}{card.number}")

"""
モジュール(クラスや関数が書かれたスクリプトファイル)

パッケージ:モジュールが存在するディレクトリ(pip install パッケージ名)
ライブラリ:パッケージを1つにまとめたもの

import モジュール名 #読み込み
      または
from モジュール名 import 関数名,クラス名

モジュール名.クラス名 #呼び出し
モジュール名.関数名
モジュール名.変数名
"""

#予め用意したモジュール
from my_module import Student #〇〇.ファイル名で〇〇フォルダから呼び出せる
#my_module(ファイル名)からStudent(クラス)を呼び出し

student_1 = Student("斉藤そうま", 82, 74, 60, 92, 72)
s1_avg = student_1.average_score()
print(f"s1の平均点は{s1_avg}点")

#標準モジュール(元々搭載されている)
from datetime import datetime #現在の日時

t = datetime.today()
print(t)

#外部ライブラリ(モジュールを複数まとめてパッケージ化したもの)
"""
ex.Matplotlib(グラフを書くことに特化)
ex.Excelファイルを操作できるOpenpyxl
ex.PDFファイルを操作できるpypdf 等 Pythonは外部ライブラリが豊富

パッケージ管理ツール pip (pipコマンドをターミナルに入力)
PyPlに登録されている外部ライブラリをpip越しにインストールできる
"""

#仮想環境の構築
"""
※Macの場合→homebrew経由のpythonだとpipコマンド等使えなかった
仮想環境(python)を作る手順
python3 -m venv venv(仮想環境フォルダ作る※ターミナル入力)
source venv/bin/activate(仮想環境に入る※ターミナル左側にvenv出たらok)
pip install 〇〇(ターミナル入力でインストール)
"""
#ex.Matplotlibの使用(グラフ特化)

import matplotlib.pyplot as plt

label = ["A", "B", "C", "D"]
num = [20, 17, 25, 9]
plt.bar(label, num)
plt.savefig("./bar.png")

#PDF出力
"""
pythonファイル→PDF出力する方法
py→html化→PDF保存(以下コマンド)
pygmentize -f html -O full -o ファイル名.html ファイル名.py(ターミナル入力)
"""



