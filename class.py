class SchoolReport:
    def __init__(self,student_name):
        self.student_name = student_name
        print("イニシャライザの中です")

sr_a = SchoolReport("田中 A")
sr_b = SchoolReport("鈴木 B")
sr_c = SchoolReport("斉藤 C")
print(sr_a.student_name)
print(sr_b.student_name)
print(sr_c.student_name)

#インスタンス変数(self)
class SchoolReport:
    def __init__(self,student_name, math_score, jp_score, en_score):
        self.student_name = student_name
        self.math_score = math_score
        self.jp_score = jp_score
        self.en_score = en_score
    def calc_avg_score(self):
        sum_score = (self.math_score + self.jp_score + self.en_score)
        avg_score = sum_score / 3
        return avg_score

sr_a = SchoolReport("田中A",100,30,50)
avg_a = sr_a.calc_avg_score()
print(f"Aさんの3教科平均は{avg_a}点です")

sr_b = SchoolReport("鈴木B",20,59,50)
avg_b = sr_b.calc_avg_score()
print(f"Bさんの3教科平均は{avg_b}点です")

sr_c = SchoolReport("斉藤C", 19, 22, 19)
avg_c = sr_c.calc_avg_score()
print(f"Cさんの3教科平均は{avg_c}点です")

#クラス変数(オブジェクト同士の共通の値)
class SchoolReport:
    school_name = "第五小学校" #クラス変数はクラスの下に書く
    def __init__(self,student_name, math_score, jp_score, en_score):
        self.student_name = student_name

#オブジェクト作らない場合のアクセス
print(SchoolReport.school_name)#クラスに直接書かれている変数なのでオブジェクト作らずにアクセスできる

#オブジェクト作った場合のアクセス
sr_a = SchoolReport("田中A",100,30,50)
print(sr_a.school_name)#オブジェクトにクラス変数にアクセス
SchoolReport.school_name = "第五中学校" # ※通常は更新しないが更新できる
print(SchoolReport.school_name) #変更された値を出力

#メソッド内の一時的な変数(def内のselfなしの変数、外からアクセスできない ex.sum_score)
class SchoolReport:
    def __init__(self,student_name, math_score, jp_score, en_score):
        self.student_name = student_name
        self.math_score = math_score
        self.jp_score = jp_score
        self.en_score = en_score
    def calc_avg_score(self):
        self.sum_score = (self.math_score + self.jp_score + self.en_score)
        avg_score = self.sum_score / 3 #sum_scoreにselfをつけると後からアクセスできる
        return avg_score

sr_a = SchoolReport("田中A",100, 30, 50)
sr_a.calc_avg_score()
print(sr_a.sum_score)#selfをつけた為、アクセスできている