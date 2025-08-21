"""
三項演算子:条件の結果によって返す値を変えることができる

True時に返す値 if 条件 else False時に返す値 
(if文を一行で書くイメージ)
"""

age = 20
result = "成人" if age >= 20 else "子ども" 
print(result)

age = 0.5 #elseの後に三項演算子を使うことでelifのような使い方
result = "成人" if age >= 20 else "子ども" if age >= 1 else "赤ちゃん"
print(result)