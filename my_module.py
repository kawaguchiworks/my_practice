#クラス

#ex.生徒のテストの点数を管理するプログラム

#設計図(インスタンス変数の初期化)
class Student:
    def __init__(self,name,math,japanese,english,science,society):
        self.name = name
        self.math = math
        self.japanese = japanese
        self.english = english
        self.science = science
        self.society = society

#５教科の平均点を計算するメソッド(クラス中で使える関数)
    def average_score(self):
        avg = (self.math + self.japanese + self.english 
               + self.science + self.society) /  5
        return avg
    

