"""
継承:基底クラスの性質を派生クラスが引き継ぐ

"""
#継承
class HumanClass:
    def defend(self):
        print("防御をしました")

class WizardClass(HumanClass):#基底クラスを継承
    pass

wizard = WizardClass()
wizard.defend()

class HumanClass:
    def __init__(self):
        print("HumanClassのinit")
        self.hp = 100

class WizardClass(HumanClass):
    def __init__(self):
        super().__init__() #基底クラスのイニシャライザーを呼び出し
        self.mp = 50
    def output_info(self):
        print(f"現在のHPは{self.hp}で、MPは{self.mp}です")

wizard = WizardClass()
print(wizard.mp)
wizard.output_info()

#多重継承
class WizardClass:
    def __init__(self):
        self.mp = 100
        print("WizardClassのinit")
    
    def cast_spell(self):
        print("呪文を唱える")

class SwordFighterClass:
    def attack_with_sword(self):
        print("剣で攻撃する")

class MagicSwordFighterClass(WizardClass,SwordFighterClass):
    pass

msf = MagicSwordFighterClass()
msf.cast_spell()
msf.attack_with_sword()