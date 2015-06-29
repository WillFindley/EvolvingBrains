import random
import copy

def runEvolution(generationSize,selectionPressure,sensoryInput,motorOutput):

    generation = Generation(generationSize,selectionPressure)
    
    currentPerformance = generation.generationAveragePerformance()
    generationNumber = 1
    print str(generationNumber) + "\t" + str(currentPerformance)
    while True:
        previousPerformance = currentPerformance
        generation.runGeneration(sensoryInput,motorOutput)
        currentPerformance = generation.generationAveragePerformance()
        generationNumber += 1
        if previousPerformance == currentPerformance:
            break
    print str(generationNumber) + "\t" + str(currentPerformance)


class Generation:

    def __init__(self,generationSize,selectionPressure):
        self.neuralNets = [NeuralNet() for whichNet in xrange(generationSize)]
        self.toKillOffEachGen = int(round(selectionPressure*generationSize))

    def generationAveragePerformance(self):
        generationAverageLocation = 0.0
        for neuralNet in self.neuralNets:
           generationAverageLocation += neuralNet.net[0].location 
        return generationAverageLocation/len(self.neuralNets)

    def runGeneration(self,sensoryInput,motorOutput):
        for neuralNet in self.neuralNets:
            neuralNet.runNet(sensoryInput,motorOutput)
        self.neuralNets.sort(key = lambda x: x.performance)
        for toKill in xrange(self.toKillOffEachGen):
            self.neuralNets[toKill] = copy.deepcopy(self.neuralNets[random.randint(self.toKillOffEachGen,len(self.neuralNets)-1)])


class NeuralNet:
    
    def __init__(self):
        self.net = [Neuron()]
        self.performance = 0
    
    def runNet(self,sensoryInput,motorOutput):
        for whichTest in xrange(len(sensoryInput)):
            for neuron in self.net:
                if motorOutput[whichTest] == neuron.run(sensoryInput[whichTest]):
                    self.performance += 1


class Neuron:
    
    def __init__(self):
        self.location = random.randint(0,1)
    
    def run(self,sensoryInput):
        if sensoryInput == self.location:
            return 1
        else:
            return 0


generationSize = 1000
selectionPressure = 0.2 # proportion killed off without offspring at end of generation
sensoryInput = [0,1]    # which pixel is on
motorOutput = [0,1]     # should I act
runEvolution(generationSize,selectionPressure,sensoryInput,motorOutput)
