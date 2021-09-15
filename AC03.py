from unittest import TestCase, main
import abc
import unittest

class Calculadora (object):
    def calcular (self, valor1, valor2, operador):
        operacaoFabrica = OperacaoFabrica ()
        operacao= operacaoFabrica.qualOperacao(operador.lower())
        if (operacao == None):
            return 0
        else:
            resultado = operacao.executar(valor1, valor2)
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
            resultado = "Divisão por zero não é permitido"
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
        print("teste_soma01 -------- Passou!")
    
    def teste_soma02(self):
        resultadoCalculo = Calculadora()
        resultado = resultadoCalculo.calcular(8,5, "soma")
        self.assertEqual (resultado, 13)
        print("teste_soma02 -------- Passou!")
    
    def teste_soma03(self):
        resultadoCalculo = Calculadora()
        resultado = resultadoCalculo.calcular(250,150, "soma")
        self.assertEqual (resultado, 400)
        print("teste_soma03 -------- Passou!")

    def teste_subtracao01(self):
        resultadoCalculo = Calculadora()
        resultado = resultadoCalculo.calcular(200,150, "subtracao")
        self.assertEqual (resultado, 50)
        print("teste_subtracao01 -------- Passou!")

    def teste_subtracao02(self):
        resultadoCalculo = Calculadora()
        resultado = resultadoCalculo.calcular(1000,1250, "subtracao")
        self.assertEqual (resultado, -250)
        print("teste_subtracao02 -------- Passou!")
    
    def teste_subtracao03(self):
        resultadoCalculo = Calculadora()
        resultado = resultadoCalculo.calcular(1, 1, "subtracao")
        self.assertEqual (resultado, 0)
        print("teste_subtracao03 -------- Passou!")

    def teste_divisao01(self):
        resultadoCalculo = Calculadora()
        resultado = resultadoCalculo.calcular(10,5, "divisao")
        self.assertEqual (resultado, 2)
        print("teste_divisao01 -------- Passou!")

    def teste_divisao02(self):
        resultadoCalculo = Calculadora()
        resultado = resultadoCalculo.calcular(1000,50, "divisao")
        self.assertEqual (resultado, 20)
        print("teste_divisao02 -------- Passou!")
    
    def teste_divisao03_comZero01(self):
        resultadoCalculo = Calculadora()
        resultado = resultadoCalculo.calcular(10,0, "divisao")
        self.assertEqual (resultado, "Divisão por zero não é permitido")
        print("teste_divisao03_comZero01 -------- Passou!")

    def teste_divisao04_comZero02_UpperCase(self):
        resultadoCalculo = Calculadora()
        resultado = resultadoCalculo.calcular(0,10, "DIVISAO")
        self.assertEqual (resultado, 0)
        print("teste_divisao04_comZero02_UpperCase -------- Passou!")

    def teste_multiplicacao01(self):
        resultadoCalculo = Calculadora()
        resultado = resultadoCalculo.calcular(1000,50, "multiplicacao")
        self.assertEqual (resultado, 50000)
        print("teste_multiplicacao01 -------- Passou!")

    def teste_multiplicacao02(self):
        resultadoCalculo = Calculadora()
        resultado = resultadoCalculo.calcular(10,10, "multiplicacao")
        self.assertEqual (resultado, 100)
        print("teste_multiplicacao02 -------- Passou!")
    
    def teste_multiplicacao03_UpperCase(self):
        resultadoCalculo = Calculadora()
        resultado = resultadoCalculo.calcular(10,0, "MUTIPLICACAO")
        self.assertEqual (resultado, 0)
        print("teste_multiplicacao03_UpperCase -------- Passou!")
    
    
    
    
    



if __name__ == '__main__':
    main()
