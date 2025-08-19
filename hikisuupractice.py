#可変長引数
#関数の引数の数が固定ではなく自由な数だけ設定できる引数

#1.位置引数の可変長引数
def func(*args):
    print(args)

func(1)
func(1,3,10)#複数の位置引数を一つのタプルとして出力される

def func(*args):
    result = ",".join(args)#,で複数の引数を結合
    print(result)

func("あ")
func("あ","A","a")

#可変長引数＋普通の引数
def func(x,*args):#普通の引数が先の場合
    print(args)
    print(x)

func(1, "a", "b", "c") #普通の引数を最初(位置引数で渡す)

def func(*args, x): #普通の引数が後の場合(*以降はキーワード引数で入れなければいけない)
    result = ",".join(args)
    print(f"{x}:{result}")

func("あ", x=1) #後の場合は普通の引数をキーワード引数で渡す
func("あ", "A", "a", x=2)

print(100)
print(100,"アイウエオ",True)#print関数は可変長引数の関数

#2.キーワード引数の可変長引数

def func(**kwargs):
    print(kwargs) #複数のキーワード引数を辞書として出力される

func(name="斉藤", user_id=222)#キーワード引数(引数＝値)で渡す 
func(item="牛乳",item_id=111,price=100)#key=valueで反映される

#普通の引数と可変長引数を一緒に使う場合
def func(x,**kwargs): #普通の引数を先に書く必要がある
    print(f"{x}:{kwargs}")

func(1, names="斉藤", user_id=222)
func(2, item="牛乳",item_id=111, price=100)
     



