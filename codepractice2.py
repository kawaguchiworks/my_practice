#1
x = 1
y = "こんにちは"
z = 32.4
print(x,y,z)

#2
x = str(100)
y = float("100.1")
z = int(100.0)
print(x,type(x))
print(y,type(y))
print(z,type(z))

#3
x = 10
y = 2
result_1 = (x * y) + (x / y)
result_2 = (x ** y) - (x % y)
print(result_1,result_2)

#4
x = 10
y = 20
result_1 = x + y
print(result_1)
result_2 = str(x) + str(y)
print(result_2)

#5 
x = 10
y = 20
#xとyを足した結果を出力
print(x + y)

#6
x = 1920 + 1080 + 4 + 5922 + \
     2138 + 999 + 1000 + 456
print(x) 

#7
print(round(1.5))
print(round(2.5))
print(round(3.5))

#8
x = 100
x *= 100
print(x)

#9
name = "パイソン"
age = 29
print(f"私は{name}です。{age}歳です")

#10
phone = "03-1111-2222"
phone_without_hyphen = phone.replace("-","")
print(phone_without_hyphen)

#11
print("あ\nい\nう\nえ\nお")

#12
name = " 鈴木 太郎\n"
name_stripped = name.strip()
print(name_stripped)

#13
x = "Apple"
upper_x = x.upper()
lower_x = x.lower()
print(upper_x,lower_x)

#14
fruits = ["りんご", "バナナ", "オレンジ"]
print(fruits)

#15
fruits = ["りんご", "バナナ", "オレンジ"]
print(len(fruits))

#16
fruits = ["りんご", "バナナ", "オレンジ"]
first = fruits[0]
last = fruits[-1]
print(f"先頭は{first}、末尾は{last}です")

#17
phone_number = "03-1111-2222"
print(phone_number[:2])
print(len(phone_number))

#18
phone_number = "03-1111-2222"
print(phone_number[3:7])

#19
phone_number = "03-1111-2222"
phone = phone_number.split("-") #splitメソッド指定した文字で区切る
print(phone)

#20
phone_list = ['03', '1111', '2222']
phone_number = "-".join(phone_list) #joinメソッド"文字列"で連結させる
print(phone_number)

#21
numbers = [3, 1, 4, 2, 5]
sorted_numbers = sorted(numbers)#非破壊的(新しいリストを返す) ※numbers.sort()⇨破壊的
smallest_numbers = sorted_numbers[:3]
print(smallest_numbers)

#22
numbers = [3, 1, 4, 2, 5]
numbers.reverse() #破壊的 reverseメソッドはリスト自体を変更
print(numbers)

#23
numbers = [3, 1, 4, 2, 5]
total = sum(numbers)
max = max(numbers)
min = min(numbers)
print(total,max,min)

#24
numbers = [3, 1, 4, 2, 5]
second_number = numbers.pop(1) #pop(インデックス)その要素を取り出す(引く)
print(numbers)
print(second_number)

#25
odd_numbers = [1, 3, 5, 7]
even_numbers = [2, 4, 6, 8]
numbers = odd_numbers + even_numbers
print(numbers)

#26
odd_numbers = [1, 3, 5, 7]
even_numbers = [2, 4, 6, 8]
odd_numbers.append(9) #破壊的メソッド
even_numbers.remove(8)
print(odd_numbers,even_numbers)

#27
months = {1:"睦月", 2:"如月", 3:"弥生"}
print(months)

#28
months = {1:"睦月", 2:"如月", 3:"弥生"}
months[4] = "卯月" #辞書[key]="value"
print(months)

#29
months = {1:"睦月", 2:"如月", 3:"弥生"}
value_2 = months[2]
print(value_2)

#30
months = {1:"睦月", 2:"如月", 3:"弥生"}
months[1]="January"
print(months)

#31
months = {1:"睦月", 2:"如月", 3:"弥生"}
three_month = months.pop(3)#pop()その要素を取り出し削除
print(three_month)
print(months)

#32
months = {1:"睦月", 2:"如月", 3:"弥生"}
keys = list(months.keys())
values = list(months.values())
print(keys)
print(values)

#33
numbers = {1, 2, 3, 4, 5}
print(numbers)

#34
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
numbers.remove(1) 
print(numbers)

#35
numbers = [1, 1, 5, 2, 5, 3, 3]
unique_numbers = list(set(numbers))
#集合は重複した要素を持てないことを利用する set()集合に変換
print(unique_numbers)

#36
group_a = {1, 2, 3, 4, 5}
group_b = {4, 5, 6, 7, 8}
common_number = group_a & group_b
print(common_number)

#37
group_a = {1, 2, 3, 4, 5}
group_b = {4, 5, 6, 7, 8}
unique_numbers = group_a - group_b
print(unique_numbers)

#38
group_a = {1, 2, 3, 4, 5}
group_b = {4, 5, 6, 7, 8}
all_numbers = group_a | group_b
print(all_numbers)

#39
numbers = {1, 12, 5, 10, 13, 7, 90}
sorted_numbers = sorted(numbers) # sorted()はリストを返す
second_largest_number = sorted_numbers[-2]
print(second_largest_number)

#40
screen_size = (1920, 1080)
print(screen_size)

#41
screen_size = (1920, 1080)
width = screen_size[0]
print(width)

#42
empty_list = []
empty_dict = {}
empty_set = set()
empty_tuple = ()
print(empty_list)
print(empty_dict)
print(empty_set)
print(empty_tuple)

#43
x = 10
y = 10
if x == y:
    print("同じです")

#44
x = 10
y = 20
if x != y:
    print("異なります")

#45
x = 10
y = 20
if x >= y:
    print("xはy以上")
else:
    print("xはy未満")

#46
x = 75
if x >= 90:
    print("90以上")
elif x >= 80: #ifは当てはまらない場合 
    print("90未満80以上") 
else:
    print("80未満")

#47
favorite_fruit = ["りんご", "バナナ", "みかん", "梨", "桃"]
x = "みかん"
if x in favorite_fruit:
    print("好きな果物です")

#48
allergy_foods = ["卵", "乳", "小麦", "そば", "落花生"]
x = "牛肉"
if x not in allergy_foods:
    print("アレルギーの食べ物ではありません")

#49
document = "私はpythonを学んでいます"
if "python" in document:
    print("pythonが含まれています")

#50
phone_number = "0120-1111-2222"
if phone_number.startswith("0120"):#startswith("始まりの文字列")その文字列で始まる場合Trueを返す
    print("フリーダイヤルです")

#51
mail_address = "exmaple@gmail.com"
if mail_address.endswith("@gmail.com"):#endswith("末尾の文字列")その文字列を末尾で終わる場合Trueを返す
    print("Gmailアドレスです")

#52
math_score = 83
eng_score =70
jpn_score = 80
if math_score >= 80 and eng_score >= 80  and jpn_score >= 80:
    print("合格")
else:
    print("不合格")

#53
age = 68
if age <= 12 or age >=65: 
    print("割引料金")
else:
    print("通常料金")

#54
age = 20
is_student = True
if age < 18 :
    print("500円")
else:
    if is_student:
        print("1000円")
    else:
        print("2000円")

#55
names = ["鈴木", "田中", "山田", "佐藤", "伊藤"]
for name in names:
    print(f"{name}さん")

#56
months = {1:"睦月", 2:"如月", 3:"弥生"}
for k,v in months.items():#辞書.items()で[(),(),()]として取り出す必要がある
    print(f"{k}月は和風月名で{v}です")

#57
bottom_and_height = [
    [13, 40],
    [15, 30],
    [20, 25]
]

for b_and_h in bottom_and_height:#複数のリストから一つのリストを取り出す
    bottom = b_and_h[0]
    height = b_and_h[1]
    area = bottom * height / 2
    print(f"底辺{bottom}、高さ{height}の三角形の面積は{area}です")

#58
items = [
    {"name": "りんご", "unit_price": 100, "quantity": 3},
    {"name": "みかん", "unit_price": 50, "quantity": 5},
    {"name": "バナナ", "unit_price": 80, "quantity": 2}
]   
total_price = 0

for item in items:
    price = item["unit_price"] * item["quantity"]
    total_price += price 

print(f"合計金額は{total_price}円です")

#59
for number in range(101):
    print(number)

#60
number = []
for i in range(1,101):
    number.append(i) #リスト.append()追加 or +=[]で追加

print(number)

#61
text = "あかさたな-はまやらわ"
for char in text: 
    if char == "-":
        break
    print(char)

#62
ng_numbers = [4, 9 ,13]

for number in range(1,21):
    if number in ng_numbers:
        continue
    print(number)

#63
for number in range(1,21):
    if number % 3 == 0:
        print(f"{number}は3の倍数")
    else:
        print(number)

#64
addresses = {
    "鈴木": "suzuki@example.com",
    "田中": "tanaka@example.com",
    "山田": "yamada@example.com",
    "佐藤": "satou@gmail.com"
    }

gmail_addresses = {}
for name,address in addresses.items(): #辞書のkey,value取り出し
    if address.endswith("@gmail.com"): #末尾""で終わる時
        gmail_addresses[name] = address #辞書の追加

print(gmail_addresses)

#65
for a in range(1,10):
    for b in range(1,10):
        c = a * b
        print(f"{a} × {b} = {c}")

#66
def print_string(text):
    print(text)

print_string("Hello,Python!")

#67
a = 10
b = 20

def add(x,y):
    return x + y 

result = add(a,b)
print(result)

#68
numbers = [14, 32, 80, 1, 9]

def sum_and_avg(nums):
    sum_numbers = sum(nums)
    avg_numbers = sum_numbers / len(nums)
    return sum_numbers,avg_numbers #(,)で返している

total,avg = sum_and_avg(numbers)
print(total)
print(avg)

#69
numbers = [14, 32, 80, 1, 9]

def is_even(x):
    return x % 2 == 0 #Trueを返す

for num in numbers:
    if is_even(num): #Trueを返してる
        print(f"{num}は偶数")
    else:
        print(f"{num}は奇数")

#70
def drink_price(drink_size,has_whip = False):
    price = 0
    if drink_size == "S":
        price += 100
    elif drink_size == "M":
        price += 200
    elif drink_size == "L":
        price += 300
    
    if has_whip:
        price += 100
    return price #結果を返す(返さないとnoneが出てしまう)

result_1 = drink_price("L")
result_2 = drink_price("M",True)
print(result_1)
print(result_2)

#71
JP_MONTHS = {1: "睦月", 2: "如月", 3: "弥生",4: "卯月",5: "皐月", 
             6: "水無月", 7:"文月", 8: "葉月", 9: "長月", 10: "神無月",
               11: "霜月", 12: "師走" }

def print_jp_month(month):
    print(f"{month}月は和風月名で{JP_MONTHS[month]}です")

print_jp_month(3)
print_jp_month(12)

#72
words = ["Apple", "banana", "Cherry", "lemon"]

def modify_words(word):
    first_char = word[0]
    if first_char.isupper(): #isupperメソッドで頭文字が大文字かチェック
        return word.upper() #upperメソッドで全て大文字に変換
    else:
        return word

modified_words = []
for word in words: #要素を取り出す
    m_word = modify_words(word) #定義した関数で変換
    modified_words.append(m_word) #空のリストに追加
print(modified_words)

#73
class Student:
    def __init__(self):
        self.name = ""
        self.grade = 1
        self.section = "A"
        self.scores = {}

#74
class Student:
    def __init__(self, name, grade, section):
        self.name = name
        self.grade = grade
        self.section = section
        self.scores = {}

student = Student("鈴木", 2, "B")
print(student.name) #studentのnameという属性にアクセス※メソッドではない

#75
class Student:
    def __init__(self, name, grade, section):
        self.name = name
        self.grade = grade
        self.section = section
        self.scores = {}
    def add_score(self, subject, score):#メソッドにはselfが必須
        self.scores[subject] = score #空の辞書(self.scores)に追加

student = Student("鈴木", 2, "B")
student.add_score("数学", 80) 
student.add_score("英語", 70)
student.add_score("国語", 90)
print(student.scores)

#76
class Student:
    def __init__(self, name, grade, section):
        self.name = name
        self.grade = grade
        self.section = section
        self.scores = {}
    def add_score(self, subject, score):
        self.scores[subject] = score #辞書に追加するだけだからreturnいらない
    def total_score(self):
        return sum(self.scores.values()) #辞書(self.scores)のvalue(点数)のみ取り出してその合計を返す

student = Student("鈴木", 2, "B")
student.add_score("数学", 80) 
student.add_score("英語", 70)
student.add_score("国語", 90)
print(student.total_score())

#77
class Student:
    def __init__(self, name, grade, section):
        self.name = name
        self.grade = grade
        self.section = section
        self.scores = {}
    def add_score(self, subject, score):
        self.scores[subject] = score 
    def total_score(self):
        return sum(self.scores.values())

student = Student("鈴木", 2, "B")
student.grade = 3
student.section = "C"
print(student.grade)
print(student.section)

#78
class Student:
    def __init__(self, name, grade, section, scores):
        self.name = name
        self.grade = grade
        self.section = section
        self.scores = scores
    def add_score(self, subject, score):
        self.scores[subject] = score 
    def total_score(self):
        return sum(self.scores.values())

student_1 = Student("鈴木", 2, "B", {"数学": 80, "英語": 70, "国語": 90})
student_2 = Student("田中", 2, "B", {"数学": 70, "英語": 80, "国語": 75})
student_3 = Student("斉藤", 2, "B", {"数学": 90, "英語": 85, "国語": 80})

for student in [student_1, student_2, student_3]: #生徒のリスト化しfor文で回す
    print(f"{student.name}さんの合計点数は{student.total_score()}点です")
    #nameのような変数・属性は()いらない.total_scoreのようなメソッド(関数)必ずつける

#79
class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["ハート", "ダイヤ", "スペード", "クラブ"]:
            for number in range(1,14):
                card = Card(suit, number) 
                self.cards.append(card)
    
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    
    def draw_card(self):
        return self.cards.pop(0)
    
#80
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
for card in deck.cards: #リストから一枚ずつ取り出す ※cardsはリストだからアクセス
    print(f"{card.suit}{card.number}")

 #deckはリストではない（Deckというクラスのオブジェクト）
 #だから for card in deck.cards: はOKだけど、
 #for card in deck: は NG（イテラブルじゃないから）
    
#81
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
print("5枚引く:")
for _ in range(5): #_→数字の部分は使わないことを示す
    card = deck.draw_card()#ドローしたカード一枚(インスタンス)を示す 
    print(f"{card.suit}{card.number}")

#82
from module import add

result = add(1,2)
print(result)

#83
from module import Card,URL

card = Card("ハート", 1)
print(f"{card.suit}{card.number}")
print(URL)

#84
import module

result = module.add(1, 2)#importで指定していない場合、プレフィックス(接頭辞)が必要
print(result)
print(module.URL)

#85
from my_packages.testmodule import add,URL

result = add(1, 2)
print(result)
print(URL)

#86
text = "こんにちは!" #withはブロックを抜けると自動的に閉じる
with open("doc.txt", "w") as f: # open→ファイルオブジェクトを呼び出す "w"は上書き
    f.write(text)

#87
with open("doc.txt","a") as f:
    f.write("\nさようなら!")#"a"は新規作成または末尾に追加

#88
with open("doc.txt","r") as f: #"r" 読み込みモード
    text = f.read() 
print(text)

#89
with open("doc.txt","r") as f:
    lines = f.readlines() #readlinesメソッドはファイルの中身一行ずつが要素のリスト
    
new_lines = []    
for line in lines:
    new_lines.append(line.strip())
print(new_lines)

#90
x = 2
#result = x % 0  例外
#print(result)

#91
x = 2 
try:
    result = x % 0
    print(result)
except ZeroDivisionError:
    print("0で割ることができません")

#92
x = 2
y = 10
numbers = [1, 4, 0, 12, 6]

try:
    result = y / numbers[x]
    print(result)
except IndexError:
    print("リストの範囲を超えるインデックスです")
except ZeroDivisionError:
    print("0で割ることはできません")

#93
x = 6
y = 10
numbers = [1, 4, 0, 12, 6]

try:
    result = y / numbers[x]
    print(result)
except(IndexError,ZeroDivisionError):
    print("エラーが発生しました")

#94
import math #標準モジュール

r = 3
circle_area = r ** 2 * math.pi #円周率
print(circle_area)

#95
import os

home_pass = os.getenv("HOME") #getenv()環境変数を取得
print(home_pass)

#96
from datetime import date #dateクラス

today = date.today()#date.をつけ呼び出す必要がある
print(today)

#97
import time 

for number in range(1,2):
    print(number) #まず1を表示
    time.sleep(1)#1表示させてから1秒停止

#98
from pathlib import Path 

current_dic = Path.cwd()
print(current_dic)

#99
import art #外部ライブラリ(モジュール集合体)
result = art.text2art("PYTHON")
print(result)

#100
import qrcode 

URL = "https://chatgpt.com/"
img = qrcode.make(URL)
img.save("chatGPT.png")




    

    















