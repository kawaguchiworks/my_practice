"""
命名規則
変数名や関数名をつけるときのルール ※PEP8

変数名
スネーク型:小文字+_ ex.user_name,address

定数名
アッパースネーク型:大文字+_ ex.FILE_NAME

クラス名
CapWard方式:単語の先頭だけ大文字 ex.UserClass

関数名・メソッド名
スネーク型:小文字+_ ex.update_password()

ファイル名
スネーク型:小文字+_ ex.validation_util.py

変数名のつけ方のコツ
①意味を持たない変数名をつけない
②対になっている対義語・反対語を使う 
ex.start⇄stop、top⇄bottom
③Bool型はどちらがTrueでFalseかわかるように 
ex.is_student = True、has_card = True、 can_login = True
④型情報を持つシステムハンガリアン記法をむやみに使わない
ex.strやintを変数名にしない

"""