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
            return Multiplicacao()

class Operacao(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def executar(self, valor1, valor2):
        pass

class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado 

class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado 

class Divisao(Operacao):
    def executar(self, valor1, valor2):
        if (valor2 == 0):
            resultado = "Divisão por 0"
            return resultado
        else:
            resultado = valor1 / valor2
            return resultado 

class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado 


class testadora(TestCase):
    def teste_soma01(self):
        resultadoCalculo = Calculadora()
        resultado = resultadoCalculo.calcular(5,5, "soma")
        self.assertEqual (resultado, 10)
