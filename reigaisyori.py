#例外処理(コンピューターが命令を実行した時に起きる問題を処理)
"""
try:
例外が発生する可能性のある処理
except 例外型;
例外型と同じ例外発生時の処理

例外型→例外用のクラス(ex.MemoryError,AttributeError,〇〇Error等)
※大元はExceptionクラスから派生したもの
例外オブジェクト→例外型のクラスから作られたオブジェクト

"""

x = 1
y = 2

try:
    result = x / y
except ZeroDivisionError as e: # 例外オブジェクトを as 変数名で代入できる
    print("ゼロでは割ることはできません")
    print(e)
except NameError as e: 
    print("変数が定義されていません")
    print(e)
else: #例外ではない場合
    print(result)
    print("正常に終了しました")
finally: #例外の発生有無に関わらず最後に実行される処理 
    print("割り算を終了します")

x = 1
y = 0

try:
    result = x / y
except Exception as e: #Exception→システム終了以外の全例外
    print("例外が発生しました")
    print(e)

#意図的に例外を発生させる方法(raise)
# raise 例外クラス(メッセージ※なくてもいい)

#ex.ファイル読み込み時のデータチェック

import pandas as pd
import numpy as np

df = pd.read_csv("items.csv")

# quantity列が整数型かどうかチェック（int系ならOK）
if df["quantity"].dtype != np.int64:
    raise TypeError("quantityに整数ではないデータがあります")

# price列が整数型かどうかチェック（int系ならOK）
if df["price"].dtypes != np.int64:
    raise TypeError("priceに整数ではないデータがあります")


print(sum(df["quantity"] * df["price"]))

#例外クラス
#TypeError(変数の方に問題がある場合に発生)

#ValueErrot(変数の値に問題がある場合に発生)

#RuntimeError(実行時の例外(上記以外)※サーバーの障害)
















 

