"""
datetimeモジュール:
日付と時間の操作

"""
"""
dateオブジェクト
(年,月,日を含む)
"""
#todayメソッド:今日の日付を取得
from datetime import date
t = date.today() #dateオブジェクト(年と月と日を持つ)
print(t) 
t.year #年
t.month#月
t.day  #日

t.weekday() #曜日
#月→0 火→1 水→2 木→3 金→4 土⇨5 日→6 と出力される

#引数を指定する
from datetime import date #dateはクラス
d = date(2020,12,24)#dateはクラス→インスタンス化している
print(d)
print(d.weekday())#weekdayメソッドは曜日(数字)を出力

"""
timeオブジェクト
(時,分,秒,マイクロ秒を含む)
"""
#引数を指定をする
from datetime import time
t = time(12,15,30,0)
t.hour #時
t.minute #分
t.second #秒
t.microsecond #マイクロ秒

"""
datetimeオブジェクト
(年,月,日,時,分,秒,マイクロ秒を含む)

"""
#nowメソッド:現在の時間を取得
from datetime import datetime
n = datetime.now()
print(n)
print(n.year,n.month,n.day)
print(n.hour,n.minute,n.second,n.microsecond)

#datetimeオブジェクト
from datetime import datetime
d = datetime(2020,12,24,12,11,10)
#最低、年と月と日を指定する(時間は指定しないと0になる)
print(d)
print(d.date()) #dateメソッドでdateオブジェクト(日付だけ)が生成される

#datetimeオブジェクト同士の計算

#日数の差を計算
from datetime import datetime,timedelta
d1 = datetime(2020,12,25,0,0,0)
d2 = datetime(2020,11,25,0,0,0)
result = d1 - d2 
print(result)
print(result.days)

from datetime import datetime,timedelta
d = datetime(2020,12,25,3,0,0)
result = d + timedelta(days=10)#timedeltaクラスで10日間という差を表す
print(result)

"""
timezoneオブジェクト

タイムゾーン:
同じ標準時間が使われている地域

協定世界時(UTC):
世界の時間の基準になる時間 
日本の時刻よりも9時間遅い→日本はUTCより9時間早い
"""

from datetime import datetime,timedelta,timezone
JST = timezone(timedelta(hours=+9))#日本標準時間を指定
result = datetime(2020,1,1,12,15,30, tzinfo=JST)
#datetimeの引数にtzinfoを指定
print(result)


