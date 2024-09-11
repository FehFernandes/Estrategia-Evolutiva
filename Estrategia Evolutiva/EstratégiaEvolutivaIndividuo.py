import random
import math

class Individuo:
    def __init__(self, xmin=0.0, xmax=6.0):
        self.cromossomos = [random.randint(0, 1) for _ in range(10)]
        self.xy = 0  # Fenótipo
        self.yx = 0  # Adaptabilidade
        self.xmin = xmin  # Mínimo do intervalo
        self.xmax = xmax  # Máximo do intervalo

    def converter_para_decimal(self):
        """Converte o valor binário do cromossomo para decimal."""
        return sum(gene * (2 ** idx) for idx, gene in enumerate(reversed(self.cromossomos)))

    def calcularx(self):
        """Calcula o valor de x mapeado para o intervalo [xmin, xmax]."""
        decimal = self.converter_para_decimal()
        self.xy = self.xmin + (decimal / (2 ** len(self.cromossomos) - 1)) * (self.xmax - self.xmin)
        return self.xy

    def fitness(self):
        """Calcula o indivíduo baseada na função objetivo."""
        self.yx = self.xy ** 2 - 5 * self.xy + 6
        return self.yx

    def mutacao(self, taxa_mutacao=0.1):
        """Realiza a mutação no cromossomo com base na taxa de mutação."""
        for i in range(len(self.cromossomos)):
            if random.random() < taxa_mutacao:
                self.cromossomos[i] = 1 - self.cromossomos[i]

def main():
    xmin = 0
    xmax = 6
    individuo = Individuo(xmin, xmax)
    
    while True:
        print("\nMenu:")
        print("1. Exibir cromossomos do indivíduo")
        print("2. Realizar mutação")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("Cromossomos:", individuo.cromossomos)
            print("Valor decimal:", individuo.converter_para_decimal())
            print("x:", individuo.calcularx())
            print("f(x):", individuo.fitness())
        elif opcao == "2":
            individuo.mutacao()
            print("Mutação realizada. Novos cromossomos:", individuo.cromossomos)
            print("Valor decimal:", individuo.converter_para_decimal())
            print("x:", individuo.calcularx())
            print("f(x):", individuo.fitness())
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
