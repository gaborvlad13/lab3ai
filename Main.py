
from Read import readGML
from Modularity import modularity
from NrComunitati import nrComunitati
from random import randint
from IntegerChromosome import Chromosome

class GA:
    def __init__(self, param=None, problParam=None):
        self.__param = param
        self.__problParam = problParam
        self.__population = []

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        for _ in range(0, self.__param['popSize']):
            c = Chromosome(self.__problParam)
            self.__population.append(c)

    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__problParam['function'](c.repres, net)

    def worstChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness < best.fitness):
                best = c
        return best

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness > best.fitness):
                best = c
        return best

    def selection(self):
        pos1 = randint(0, self.__param['popSize'] - 1)
        pos2 = randint(0, self.__param['popSize'] - 1)
        if (self.__population[pos1].fitness > self.__population[pos2].fitness):
            return pos1
        else:
            return pos2

    def oneGeneration(self):
        # generational
        newPop = []
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()



net = readGML("data/lesmiserables.gml")
MIN = 1
if net['noNodes'] <= 10:
    MAX = net["noNodes"]
else:
    MAX = 10
noDim = net["noNodes"]
# initialise de GA parameters
gaParam = {'popSize': 100, 'noGen': 100, 'pc': 0.8, 'pm': 0.1}
# problem parameters
problParam = {'min': MIN, 'max': MAX, 'function': modularity, 'noDim': noDim, 'noBits': 8}

# store the best/average solution of each iteration (for a final plot used to anlyse the GA's convergence)
allBestFitnesses = []
allAvgFitnesses = []
generations = []
ga = GA(gaParam, problParam)
ga.initialisation()
ga.evaluation()
maximFitness = -1
bestRepres = []
fileName_output = "miserables.txt"
f = open(fileName_output, 'w')
for g in range(gaParam['noGen']+1):
    bestSolX = ga.bestChromosome().repres
    bestSolY = ga.bestChromosome().fitness
    if bestSolY > maximFitness:
        maximFitness = bestSolY
        bestRepres = bestSolX
    allBestFitnesses.append(bestSolY)
    ga.oneGeneration()

    bestChromo = ga.bestChromosome()
    f.write('Best solution in generation ' + str(g) + ' is: x = ' + str(bestChromo.repres) + ' f(x) = ' + str(
        bestChromo.fitness))
    f.write('\n')
f.write("Best repres&fitness: " + str(bestRepres) + " " + str(maximFitness))
f.write('\n')
f.write("Nr. de comunitati: " + str(nrComunitati(bestRepres)))
f.write('\n')
f.write("Node - culoare comunitate: \n")
for i in range(len(bestRepres)):
    f.write(str(i) + " - " + str(bestRepres[i]))
    f.write('\n')

f.close()