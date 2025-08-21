"""
ファイル操作
※今回はtxtファイルが対象

f = open("ファイルパス", "モード") 
ファイルオープン(ファイルオブジェクト生成)

with open("ファイルパス","モード") as 変数名:
変数名としてファイルオープンしてブロック終わりに閉じる

モード
"r" :読み込み(デフォルト)
"w" :書き込み(ファイルなし→新規作成orファイルあり→上書き) 
"a" :追記
"r+":読み込み＋書き込み

ファイルオブジェクトのメソッド
read() 読み込み
readline() 一行ずつ読み込み
readlines() 読み込みリストで取得
write(改行は\n) 書き込み
writelines() リストを書き込み
 
"""

#読み込みモード(デフォルト)
with open("text.txt") as f:
    s = f.read() #readメソッドは内容全て読み込む
    print(s)

with open("text.txt") as f:
    for _ in range(4):
        s_line = f.readline() #readlineメソッドは1行だけ読み込む
        print(s_line)
        if s_line == "":
            print("終了です") # ※3行しかない為、4行目は終了と出力

with open("text.txt") as f:
    s_lines = f.readlines() #readlinesメソッドはリスト化して読み込む
    print(s_lines)#改行コードも反映される

#書き込みモード
with open("text2.txt", "w") as f:
    f.write("あああ\nいいい\nううう") #新規作成される

x_list = ["apple", "orange", "banana"]
with open("text3.txt","w") as f:
    f.writelines(x_list) #writelinesメソッドはリストのデータを書き込み(改行なしでそのまま連結している状態)

x_list = ["apple", "orange", "banana"]
s = "\n".join(x_list)#join(文字列のメソッド)でそれぞれの要素を""で結合させる

with open("text3.txt","w") as f:
    f.write(s)

#追記モード
with open("text2.txt","a") as f:
    f.write("\nえええ\nおおお") 




