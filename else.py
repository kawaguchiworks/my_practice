"""
elseの使い方まとめ 
※文法によって意味が異なる
"""

#ifとelse

x = 5

if x > 10:
    print("大きい")
else: #条件がFalseの時に実行
    print("小さい")
    
#forとelse(ループ+breakチェック)

for i in range(5):
    if i == 3:
        print("3回目で見つけた")
        break #breakない場合 elseが最後に実行
else: #for文が全て回った時に実行(※breakがなければelse実行)
    print("全部見たけどなかった")

#whileとelse(forと同じ)

n = 0 
while n < 3: #Trueであれば繰り返す
    if n == 5:
        break #5に到達したら強制終了
    print(n)
    n += 1 #ないと0のままから増えず無限ループ
else: #n=2のループが終わった時点で実行される
    print("正常にループ終了")
    
#tryとelse(エラーがなければ実行)

try:
    x = int("123")
except ValueError:
    print("整数に変換できません")
else: #tryが成功した場合に実行される
    print("変換成功！")

