from televisao import Televisao
from classe_calcula import  Calculadora

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calcula = Calculadora(10, 5)
    print(calcula.multiplicacao())

