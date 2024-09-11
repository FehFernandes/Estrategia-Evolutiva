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
        self.yx = self.calcularx() ** 2 - 5 * self.calcularx() + 6
        return self.yx

    def mutacao(self, taxa_mutacao=0.1):
        for i in range(len(self.cromossomos)):
            if random.random() < taxa_mutacao:
                self.cromossomos[i] = 1 - self.cromossomos[i]
        print(f"Mutação realizada. Novos cromossomos: {self.cromossomos}")

    def crossover(self, outro_individuo, taxa_recombinacao=0.7):
        filho1_cromossomos = self.cromossomos[:]
        filho2_cromossomos = outro_individuo.cromossomos[:]
        
        if random.random() < taxa_recombinacao:
            for i in range(len(self.cromossomos)):
                if random.random() < 0.5:
                    filho1_cromossomos[i], filho2_cromossomos[i] = filho2_cromossomos[i], filho1_cromossomos[i]
        
        # Criar filhos com cromossomos combinados
        filho1 = Individuo(self.xmin, self.xmax)
        filho2 = Individuo(self.xmin, self.xmax)
        filho1.cromossomos = filho1_cromossomos
        filho2.cromossomos = filho2_cromossomos
        
        # Exibir detalhes do crossover
        print("\nCrossover:")
        print(f"  Pai 1 Cromossomos: {self.cromossomos}")
        print(f"  Pai 2 Cromossomos: {outro_individuo.cromossomos}")
        print(f"  Filho 1 Cromossomos: {filho1.cromossomos}")
        print(f"  Filho 2 Cromossomos: {filho2.cromossomos}")
        
        return filho1, filho2

class Populacao:
    def __init__(self, tamanho, xmin=0, xmax=6):
        self.individuos = [Individuo(xmin, xmax) for _ in range(tamanho)]

    def avaliar_populacao(self):
        for individuo in self.individuos:
            individuo.fitness()

    def selecionar_pais(self):
        """Seleciona pares de pais usando seleção por torneio."""
        pais = []
        for _ in range(len(self.individuos) // 2):
            torneio = random.sample(self.individuos, 3)
            torneio.sort(key=lambda ind: ind.fitness())
            pai, mae = torneio[0], torneio[1]
            pais.append((pai, mae))
        return pais

    def gerar_nova_geracao(self, taxa_mutacao=0.1, taxa_recombinacao=0.7):
        nova_geracao = []
        pais = self.selecionar_pais()
        for pai, mae in pais:
            filho1, filho2 = pai.crossover(mae, taxa_recombinacao)
            filho1.mutacao(taxa_mutacao)
            filho2.mutacao(taxa_mutacao)
            
            # Avaliar fitness dos filhos e exibir resultados
            print("\nApós Mutação:")
            print(f"  Filho 1 Fitness: {filho1.fitness()}")
            print(f"  Filho 2 Fitness: {filho2.fitness()}")
            
            nova_geracao.extend([filho1, filho2])
        self.individuos = nova_geracao

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
    taxa_mutacao = float(input("Digite a taxa de mutação: "))
    taxa_recombinacao = float(input("Digite a taxa de recombinação: "))
    '''significa que há uma chance de que cada bit do cromossomo seja alterado durante o processo de mutação'''
    populacao = Populacao(tamanho_populacao)
    populacao.avaliar_populacao()

    while True:
        print("\nMenu:")
        print("1. Mostrar População")
        print("2. Encontrar Melhor Indivíduo")
        print("3. Realizar Mutação em Todos os Indivíduos")
        print("4. Recombinação")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_populacao(populacao)
        elif opcao == "2":
            encontrar_melhor_individuo(populacao)
        elif opcao == "3":
            for individuo in populacao.individuos:
                individuo.mutacao(taxa_mutacao)
            print("Mutação realizada em todos os indivíduos.")
        elif opcao == "4":
            populacao.gerar_nova_geracao(taxa_mutacao, taxa_recombinacao)
            populacao.avaliar_populacao()
            '''Dois indivíduos (pais) são selecionados da população para gerar novos indivíduos (filhos)'''
            print("Nova geração criada.")
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    menu()
