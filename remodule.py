#正規表現(文字列をパターンとして表現)

import re 

s = "090333"
m = re.match(r"[0-9]{3}", s)#0-9の数字は3回繰り返しているか
print(m)#マッチオブジェクト(m)は当てはまらなければnoneになる

if m:
    print(m.group())#一致している部分を取り出し
    print(m.span())#開始インデックスと終了インデックスのタプルを返す

s = "bananaは¥300です"
m = re.search(r"¥[1-9][0-9]*", s)
print(m)
if m:
    print(m.group())
    print(m.span())

import re

s = "この洋服は$100です"
m = re.search(r"\$[0-9]+", s)
print(m)
if m:
    print(m.group())
    print(m.span())
