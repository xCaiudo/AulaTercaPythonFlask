from unittest import TestCase, main
import abc

class Caculadora (object):
    def calcular (self, valor1, valor2, operador):
        operacaoFabrica = operacaoFabrica ()
        operacao= operacaoFabrica.qualOperacao(operador.lower())
        if (operacao == None):
            return 0
        else:
            resultado = coperacao.executar(valor1, valor2)
            return resultado

class OperacaoFabrica (object):
    def qualOperacao(self, operador):
        if (operador == "soma"):
            return Soma()
        elif (operador == "subtracao"):
            return Subtracao()
        elif (operador == "divisao"):
            return Divisao()
        elif (operador == "multiplicacao"):
            return Mutiplicacao()

class Operacao(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def executar(self, valor1, valor2):
        pass

class Soma(Operacao):
    resultado = valor1 + valor2
    return resultado

    
