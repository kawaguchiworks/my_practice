#コード練習

#1
x = 1
y = "Hello"
z = "1. 2"
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
print(result_1)
result_2 = (x ** y) - (x % y)
print(result_2)

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
print(x+y)

#6
x = (1920 + 1080 + 4 + 5922
   + 999 + 1000 + 456)
print(x)

x= 1920 + 1080 + 4 + 5922 \
    + 999 + 1000 + 456 #改行
print(x)

#7
print(round(1.5)) #round関数→小数点以下を一番近い偶数にまとめられる
print(round(3.14159,2))#小数点以下を2桁に収める
print(round(2.5)) #偶数丸め(0.5の時に最も近い偶数に)

#8
x = 100
x += 100
print(x)

#9
name = "佐藤"
age = "20"
self_introduction = f"私は{name}です。{age}歳です。"
print(self_introduction)

#10
phone = "03-1111-2222" 
phone_without_hyphen = phone.replace("-","")#関数ではなくstr型(クラス)のメソッド
print(phone_without_hyphen)#replace(a,b)→aをbに置換

#11
x = "あ\nい\nう\nえ\nお" #\n→改行
print(x)

#12
x = " 鈴木太郎\n".strip()#文字列の先頭・末尾の空白、改行を取り除く
print(x)

#13
x = "Apple"
upper_x = x.upper()#"文字列".upper→大文字に
lower_x = x.lower()#"文字列".lower→小文字に
print(upper_x)
print(lower_x)

#14
fruits = ["りんご", "バナナ", "オレンジ"]
print(fruits)

#15
fruits = ["りんご", "バナナ", "オレンジ"]
fruit_len = len(fruits)
print(fruit_len)

#16
fruits = ["りんご", "バナナ", "オレンジ"]
first_fruit = fruits[0]
last_fruits = fruits[-1]
print(f"先頭は{first_fruit}です")
print(f"末尾は{last_fruits}です")

#17
phone = "03-1111-2222"
two_digit = phone[:2]
phone_len = len(phone)
print(two_digit)
print(phone_len)

#18
phone = "03-1111-2222"
fourth_to_seventh = phone[3:7]
print(fourth_to_seventh)

#19
phone = "03-1111-2222"
phone_list = phone.split("-")
print(phone_list)

#20
phone_list = ["03","1111","2222"]
phone_number = "-".join(phone_list)#文字列.joinはその文字列で連結させる
print(phone_number)

#21
numbers = [3,1,4,2,5]
sorted_numbers = sorted(numbers) #新しいリストを返す
smallest_number = sorted_numbers[:3]
print(smallest_number)

#22
numbers = [3,1,4,2,5]
numbers.reverse()#リスト.reverse().sort()
                 #※リストのメソッドでありリスト自体を変更
print(numbers)

#23
numbers = [3,1,4,2,5]
sum_numbers = sum(numbers)
print(sum_numbers)
max_numbers = max(numbers)
print(max_numbers)
min_numbers = min(numbers)
print(min_numbers)

#24
numbers = [3,1,4,2,5]
second_number = numbers.pop(1)#リスト.pop()そのインデックスの位置を指定して削除
print(numbers)        
print(second_number)

#25
odd_numbers = [1,3,5,7]
even_numbers = [2,4,6,8]
numbers = odd_numbers+even_numbers
print(numbers)

#26
odd_numbers = [1,3,5,7]
even_numbers = [2,4,6,8]

odd_numbers.append(9)
even_numbers.remove(8)
print(odd_numbers)
print(even_numbers)

#27
months = {1:"睦月", 2:"如月", 3:"弥生"}
print(months)

#28
months = {1:"睦月", 2:"如月", 3:"弥生"}
months["卯月"] = 4 
print(months)

#29
months = {1:"睦月", 2:"如月", 3:"弥生"}
value_2 = months[2]
print(value_2)

#30
months = {1:"睦月", 2:"如月", 3:"弥生"}
months[1] = "January"
print(months)

#31
months = {1:"睦月", 2:"如月", 3:"弥生"}
month_3 = months.pop(3)
print(month_3)
print(months)

#32
months = {1:"睦月", 2:"如月", 3:"弥生"}
keys_list = list(months.keys())#.keys→keyだけを取り出す辞書のメソッド
print(keys_list)
value_list = list(months.values())#.values→valueだけを取り出すメソッド
print(value_list)

#33
numbers = {1,2,3,4,5}
print(numbers)

#34
numbers = {1,2,3,4,5}
numbers.remove(1)
numbers.add(6)
print(numbers)

#35
numbers = [1,1,5,2,5,3,3]
unique_numbers = list(set(numbers))#集合は重複した要素を持てないことを利用する
print(unique_numbers)

#36
group_a = {1, 2, 3, 4, 5}
group_b = {4, 5, 6, 7, 8}
common_numbers = group_a & group_b #積集合
print(common_numbers)

#37
group_a = {1, 2, 3, 4, 5}
group_b = {4, 5, 6, 7, 8}
unique_numbers = group_a - group_b #差集合
print(unique_numbers)

#38
group_a = {1, 2, 3, 4, 5}
group_b = {4, 5, 6, 7, 8}
unique_numbers = group_a | group_b #和集合
print(unique_numbers)

#39
numbers = {1, 12, 5, 10, 13, 7, 90}
sorted_numbers = sorted(numbers)#sorted関数はリストを返す
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
print(empty_list)
print(empty_dict)
print(empty_set)

#43
x = 10
y = 10

if x == y:
    print("同じです")

#44
x = "りんご"
y = "バナナ"
if x != y:
    print("異なります")

#45
x = 1
y = 2

if x >= y:
    print("xはy以上です")
elif x < y:
    print("xはy未満です")

#46
x=85
if x >= 90:
    print("A")
elif x >= 80:
    print("B")
else :
    print("C")

#47
favorite_fruit = ["りんご", "バナナ", "みかん", "梨", "桃"]
x = "りんご"
if x in favorite_fruit:
    print("好きな果物です")

#48
allerugy_foods = ["卵", "乳", "小麦", "そば", "落花生"]
x = "牛肉"
if x not in allerugy_foods:
    print("アレルギーの食べ物ではありません")

#49
document = "私はPythonを学んでいます"
if "Python" in document:
    print("Pythonが含まれています")

#50
phone_number = "0120-1111-2222"
if phone_number.startswith("0120"):#.startwith()→引数に渡した文字列で始まる時Trueを返す
    print("フリーダイヤルです")

#51
mail_address = "python@gmail.com"
if mail_address.endswith("@gmail.com"):#.endswith()→引数に渡した文字列で終わる時Trueを返す
    print("Gmailアドレスです")

#52
math_score = 72
eng_score = 83
jpn_score = 65
if math_score >= 80 and eng_score >= 80 and jpn_score >= 80:#and→全て満たす場合
    print("合格(全て80点以上)")
else:
    print("不合格(いずれか80点未満)")
    
#53
age = 10
if age <= 12 or age >= 65: #or→いずれか満たす場合という意味
    print("割引料金")
else:
    print("通常料金")

#54
age = 20
is_student = False #bool型

if age < 18:
    print("チケット料金は500円")
else:
    if is_student:
        print("チケット料金は1000円")
    else:
        print("チケット料金は2000円")

#55
names = ["鈴木", "田中", "山田", "佐藤", "伊藤"]
for name in names: #要素を取り出す
    print(f"{name}さん")

#56
months = {1:"弥生", 2:"如月", 3:"弥生"}
for k,v in months.items():#dict.items→key,valueを取り出す
    print(f"{k}月は和風月名で{v}です")

#57
bottom_and_height =[
    [13, 40],
    [15, 30],
    [20, 25]
]

for b_and_h in bottom_and_height:
    bottom = b_and_h[0]
    height = b_and_h[1]
    area = bottom * height / 2
    print(area)

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

print(total_price)

#59
for i in range(101):
    print(i)

#60
numbers = []
for i in range(1,101):
    numbers.append(i)#.append→末尾に新しい要素を追加するリストのメソッド

print(numbers)

#61
text = "あかさたな-はまやらわ"

for char in text:
    if char == "-":
        break
    print(char)

#62
ng_numbers = [4,9,13]

for numbers in range(1,21):
    if numbers in ng_numbers:
        continue
    print(numbers)

#63
for number in range(1,21):
    if number % 3 == 0:
        print(f"{number}は３の倍数です")
    else:
        print(number)

#64
addresses = {
    "鈴木": "suzuki@example.com",
    "田中": "tanaka@example.com",
    "山田": "yamada@example.com",
    "佐藤": "sato@gmail.com"
}

gmail_addresses = {}

for name,address in addresses.items():
    if address.endswith("@gmail.com"):#.endswithは文字列が特定の文字列が終わっているかチェックする
        gmail_addresses[name] = address #dict[key]=valueで追加

print(gmail_addresses)

#65
for i in range(1,10):
    for j in range(1,10):
        print(f"{i} × {j} = {i * j}")

#66
def print_string(text):
    print(text)

print_string("Hello,Python!")

#67
a = 10
b = 20

def add(x,y):
    z = x + y
    return z

result = add(a,b)
print(result)

#68
numbers = [14,32,80,1,9]

def sum_and_avg(nums):
    total = sum(nums)
    avg = total / len(nums)
    return total,avg

total,avg = sum_and_avg(numbers)
print(total)
print(avg)

#69
numbers = [14,32,80,1,9]

def is_even(n):
    return n % 2 == 0 #※結果がTrueかFalseしかない場合、return 条件式 で返せる

for num in numbers:
    if is_even(num):
         print(f"{num}は偶数")
    else:
        print(f"{num}は奇数")

#70
def drink_price(drink_size,has_whip=False):#引数に=でデフォルト値を与える
    price = 0
    if drink_size == "S":
        price += 100
    elif drink_size == "M":
        price += 200
    elif drink_size == "L":
        price += 300
    
    if has_whip:
        price += 100
    return price

drink_price_M_whip = drink_price("M",True)
drink_price_L = drink_price("L") #デフォルト値あるため、引数を省略できる
print(drink_price_M_whip)
print(drink_price_L)

#71
JP_MONTHS = {1:"睦月", 2:"如月", 3:"弥生", 4:"卯月", 5:"皐月",
              6:"水無月", 7:"文月", 8:"葉月", 9:"長月", 10:"神無月",
              11:"霜月", 12:"師走"}

def print_jp_month(month):
    print(f"{month}月は{JP_MONTHS[month]}です")

print_jp_month(3)
print_jp_month(12)

#72
words = ["Apple", "banana", "Cherry", "lemon"]

def modify_words(word):
    first_char = word[0]
    if first_char.isupper():#.isupper()は大文字の時、Trueを返すメソッド
        return word.upper()#.upperは全て大文字に変える
    else:
        return word #False(それ以外)の場合は、変換しない
    
modified_words = []
for word in words:#リストから要素を取り出す
    new_word = modify_words(word)#抽出した要素を作った関数で変換
    modified_words.append(new_word)#空のリストに追加していく

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
print(student.name)

#75
class Student:
    def __init__(self, name, grade, section):
        self.name = name
        self.grade = grade
        self.section = section
        self.scores = {}

    def add_score(self, subject, score):
        self.scores[subject] = score #辞書に要素を加える

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
        self.scores[subject] = score 
    
    def total_score(self):
        return sum(self.scores.values())#dict.valuesでvalueのみ引き出すメソッド

student = Student("鈴木", 2, "B")
student.add_score("数学", 80)
student.add_score("英語", 70)
student.add_score("国語", 90)
print(f"合計{student.total_score()}点です")

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

for student in [student_1, student_2, student_3]:#[]でリストを作る
    print(f"{student.name}さんの合計点数は{student.total_score()}点です")

#79
class Card: #設計図(カード一枚)
    def __init__(self,suit,number):#引数にマークと数字の設定
        self.suit = suit
        self.number = number
    
class Deck: #設計図(カードの山)
    def __init__(self):
        self.cards = [] #空のリスト
        for suit in ["ハート", "ダイヤ", "スペード", "クラブ"]: 
            for number in range(1,14):#それぞれのカードの組み合わせを作る
                card = Card(suit, number)#カードを作る
                self.cards.append(card)#空のリストに追加

    def shuffle(self):
        import random #import random(標準ライブラリ)→このライブラリを使うという合図
        random.shuffle(self.cards)
    
    def draw_card(self):
        return self.cards.pop(0)#.pop→リストの先頭(0番目)を取り出すメソッド

#80
class Card: 
    def __init__(self,suit,number):
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

deck = Deck()
deck.shuffle()
for card in deck.cards:
    print(f"{card.suit}{card.number}")

#81
class Card: 
    def __init__(self,suit,number):
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

deck = Deck()
deck.shuffle()
for _ in range(5):
    card = deck.draw_card()
    print(f"{card.suit}{card.number}")

#82
from module import add #from ファイル名 import 特定の関数

result = add(1, 2)
print(result)

#83
from module import Card, URL #from ファイル名 import クラスやURL

card = Card("ハート", 1)
print(f"{card.suit}{card.number}")
print(URL)

#84
import module #import ファイル名→モジュール全体を読み込む

result = module.add(1, 2)# ※ファイル名.が必要(見づらい)
print(result)
print(module.URL)

#85
from my_packages.testmodule import add,URL 

result = add(1, 2)
print(result)
print(URL)

#86
text = "こんにちは！"
#with open(ファイル名, モード, エンコーディングなど) as 変数名:
    # この中でファイルを操作

with open("doc.txt", "w") as f: #with open("ファイルパス","書き込みモード")"w"新規作成or上書き
    f.write(text) # .write() ファイル(doc.txt)に書き込み

#87
with open("doc.txt","a") as f: #"a"だと末尾に追記モード(前の行は消えない)
    f.write("\nさようなら！")

#88
with open("doc.txt", "r") as f: #"r"読み込みモード
    text = f.read() #readメソッドで読み込み
    
print(text)

#89   
with open("doc.txt", "r") as f:
    lines = f.readlines() #readlinesメソッドで要素を返す
    clean_lines = [] #空のリスト
    for line in lines: #for文で要素取り出す
        clean_lines.append(line.strip())#改行を取ったものを空のリストに追加していく

print(clean_lines)

#90
x = 10
#print(x / 0) #ZeroDivisionErrorが起きる⇨例外という

#91
x = 10
try:
    result = x / 0 
    print(result)
except ZeroDivisionError:
    print("ゼロで割ることはできません")

#92
x = 2
y = 10
numbers = [1, 4, 0 ,12, 6]

try:
    result = y / numbers[x]
    print(result)

except IndexError:
    print("リストの範囲を超えるインデックスです")
except ZeroDivisionError:
    print("ゼロで割ることができません")

#93
x = 2
y = 10
numbers = [1, 4, 0 ,12, 6]

try:
    result = y / numbers[x]
    print(result)

except (IndexError, ZeroDivisionError): # ,区切りでエラー名を入れることができる
    print("エラーが発生しました")

#94
import math #標準モジュールを読み込む

r = 3
circle_area = r ** 2 * math.pi #pi=円周率
#モジュール名.関数名or定数名で使える 

print(circle_area)

#95
import os #標準モジュール

x = os.getenv("HOME") #getenv("環境変数名")を取得するメソッド
print(x)

#96
from datetime import date #from 標準モジュール import クラス名

today = date.today()
print(today)

#97
import time #標準モジュール

for n in range(0,1):
    print(n)
    time.sleep(1) #time.sleep("秒")秒数だけ処理を中断

#98
from pathlib import Path

current_dir = Path.cwd() #Path.cwd()現在の作業ディレクトリのパスを取得
print(current_dir)

#99
from art import text2art #外部ライブラリ pip install 外部ライブラリ名

result = text2art("PYTHON")
print(result)

#100
import qrcode #QRコードを作る外部ライブラリ

url = "https://www.youtube.com/"#urlを設定
img = qrcode.make(url)#make(URL)
img.save("youtube.png")#save(保存するファイル名)



















