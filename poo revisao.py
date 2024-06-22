# #Jeito de programar - Serve para facilitação de compreensão(abstração-pegar do real)
# #class são os atributos que são caracteristicas
# #o método é uma funcão dentro de uma classe
# #objeto são as instâncias


# #Método construtor:
# class Carro: 
#     def __init__(self,marca,modelo,n_portas):
#         self.marca = marca
#         self.modelo = modelo
#         self.n_portas = n_portas 
#         self.ligado = False
#         self.velocidade = 0

#     def ligar(self):
#         if self.ligado:
#             print("O carro já está ligado")
#         else:
#             print("ligando carro")
#             self.ligado = True

#     def desligar(self):
#         if not self.ligado:
#             print("O carro está desligado")
#         else:
#             print("desligadno o carro")
#             self.ligado = False

#     def acelerar(self):
#         if self.ligado:
#             self.velocidade += 10
#             print(f"Velocidade atual do carro {self.velocidade}")
#         else:
#             print("O carro não está ligado")

# carro1.ligar()
# carro1.ligar()
# carro1.desligar()
# carro1.desligar()
# carro1.acelerar()
# carro1.acelerar()


#Encapsulamento = restrição de acesso
class PEssoa:
    def __init__(self,nome, idade, altura):
        self.nome = nome
        self.__idade = idade
        self.__altura = altura


    def get_altura(self):
        return self.__altura
    
    def set_altura(self, nova_altura):
        self.__altura = nova_altura

pessoa1 = PEssoa("eduardo", 31, 1.67,)
pessoa1.set_altura(1.72)
print(pessoa1.get_altura())