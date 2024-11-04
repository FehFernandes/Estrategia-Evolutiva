# Estrategia-Evolutiva

1. AlgoritmoGenético.py
Esse script implementa um algoritmo genético, que é uma técnica de otimização inspirada na evolução natural. Esse algoritmo utiliza uma população de "indivíduos" (cada um representado por uma sequência de cromossomos binários) para buscar soluções ideais para um problema. Cada indivíduo passa por processos de:

Fitness: Avaliação da adaptabilidade de um indivíduo com base em uma função objetivo, calculando quão boa é a solução.
Mutação: Pequenas alterações aleatórias nos cromossomos para introduzir diversidade genética.
Crossover: Combinação dos genes de dois indivíduos para gerar novos indivíduos.
Seleção de pais: Escolha de pares de indivíduos mais aptos para gerar uma nova geração.
Esse algoritmo é ideal para resolver problemas complexos em que a busca por uma solução ótima não é trivial e requer uma exploração de diferentes combinações de variáveis.

2. EstratégiaEvolutivaIndividuo.py
Esse código utiliza uma estratégia evolutiva, uma variação dos algoritmos genéticos com foco na otimização de uma função objetivo em um espaço de busca contínuo. Ele utiliza um indivíduo com características representadas em um intervalo contínuo, mapeado por cromossomos binários para decimal. Os principais passos são:

Conversão para decimal: Mapeia os cromossomos binários para um valor decimal, usado como a variável independente da função.
Cálculo de adaptabilidade (fitness): Avalia o indivíduo com base na função objetivo.
Mutação: Permite pequenas mudanças nos genes do indivíduo para diversificar as soluções.
Essa abordagem é adequada para otimização de funções matemáticas em espaços de busca contínuos.

3. ProgramaçãoEvolutiva.py
Este algoritmo utiliza uma abordagem de programação evolutiva, que, semelhante aos algoritmos genéticos, simula processos evolutivos para encontrar uma solução. Os principais componentes incluem:

População de indivíduos: Representada por uma lista de objetos Individuo.
Fitness: Avaliação do desempenho de cada indivíduo para determinar sua qualidade.
Mutação: Aplicada a cada indivíduo com uma taxa de mutação fixa, introduzindo diversidade.
Seleção: Processo de identificar o melhor indivíduo da população, usado para encontrar a solução mais adaptada à função objetivo.
A programação evolutiva é uma alternativa para problemas de otimização complexos, onde a solução exata não é facilmente obtida.
