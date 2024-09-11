import random
import math

class Individuo:
    def __init__(self, xmin=0, xmax=6):
        self.cromossomos = [random.randint(0, 1) for _ in range(10)]
        self.xy = 0  # Fenótipo
        self.yx = 0  # Adaptabilidade
        self.xmin = xmin  # Mínimo do intervalo
        self.xmax = xmax  # Máximo do intervalo

    def converter_para_decimal(self):
        decimal = 0
        for i, gene in enumerate(reversed(self.cromossomos)):
            decimal += gene * (2 ** i)
        return decimal

    def calcularx(self):
        decimal = self.converter_para_decimal()
        self.xy = self.xmin + (decimal / (2 ** len(self.cromossomos) - 1)) * (self.xmax - self.xmin)
        return self.xy

    def fitness(self):
        self.yx = self.xy ** 2 - 5 * self.xy + 6
        return self.yx

    def mutacao(self, taxa_mutacao):
        if random.random() < taxa_mutacao:
            indice = random.randint(0, len(self.cromossomos) - 1)
            self.cromossomos[indice] = 1 - self.cromossomos[indice]

class Populacao:
    def __init__(self, tamanho):
        self.individuos = [Individuo() for _ in range(tamanho)]

    def avaliar_populacao(self):
        for individuo in self.individuos:
            individuo.calcularx()
            individuo.fitness()

    def selecionar_e_mutar(self, taxa_mutacao):
        for individuo in self.individuos:
            individuo.mutacao(taxa_mutacao)

def mostrar_populacao(populacao):
    for i, individuo in enumerate(populacao.individuos):
        print(f"Indivíduo {i + 1}:")
        print(f"  Cromossomos: {individuo.cromossomos}")
        print(f"  Decimal: {individuo.converter_para_decimal()}")
        print(f"  x: {individuo.calcularx()}")
        print(f"  f(x): {individuo.fitness()}\n")

def encontrar_melhor_individuo(populacao):
    melhor = min(populacao.individuos, key=lambda ind: ind.fitness())
    print("Melhor Indivíduo:")
    print(f"  Cromossomos: {melhor.cromossomos}")
    print(f"  Decimal: {melhor.converter_para_decimal()}")
    print(f"  x: {melhor.calcularx()}")
    print(f"  f(x): {melhor.fitness()}")

def menu():
    tamanho_populacao = int(input("Digite o número de indivíduos na população: "))
    taxa_mutacao = 0.1

    populacao = Populacao(tamanho_populacao)

    while True:
        print("\nMenu:")
        print("1. Mostrar População")
        print("2. Encontrar Melhor Indivíduo")
        print("3. Realizar Mutação em Todos os Indivíduos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_populacao(populacao)
        elif opcao == "2":
            encontrar_melhor_individuo(populacao)
        elif opcao == "3":
            populacao.selecionar_e_mutar(taxa_mutacao)
            print("Mutação realizada em todos os indivíduos.")
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    menu()
