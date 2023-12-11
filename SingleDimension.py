import numpy;
import simpy;
import matplotlib.pyplot as plt;

intervalSize = 0.01
intervalStart = 0
intervalEnd = 10
thermalDiff = 0.01

def NormalInitialialDistribution():
    distribution = []
    size = numpy.floor((intervalEnd - intervalStart) / intervalSize).astype(int)
    for i in range(size):
        distribution.append(numpy.exp(-((i*intervalSize-5)**2)))
    return distribution

def QuadraticInitialialDistribution():
    distribution = []
    size = numpy.floor((intervalEnd - intervalStart) / intervalSize).astype(int)
    for i in range(size):
        distribution.append(((intervalSize+intervalStart)*i)**2)
    return distribution

def StepInitialDistribution():
    distribution = []
    size = numpy.floor((intervalEnd - intervalStart) / intervalSize).astype(int)
    for i in range(size):
        if i < size / 2 : 
            distribution.append(0)
        else:
            distribution.append(1)
    return distribution

def iterateTime(distribution):
    firstOrderDerivative = []
    for i in range(len(distribution)):
        firstOrderDerivative.append(calculateDerivative(distribution, i))
    iteratedDistribution = []
    # iteratedDistribution.append(0)
    # for i in range(1, len(firstOrderDerivative)-1):
    for i in range(len(firstOrderDerivative)):
        iteratedDistribution.append(distribution[i] + thermalDiff*calculateDerivative(firstOrderDerivative, i))
    # iteratedDistribution.append(0)
    # print("At x=0.2:")
    # print("u(0.2) = " + str(distribution[20]))
    # print("u'(0.2) = " + str(firstOrderDerivative[20]))
    # print("u''(0.2) = " + str(iteratedDistribution[20]))
    return iteratedDistribution
    

def calculateDerivative(distribution, i):
    if i == 0:
        # return (distribution[i+1]-distribution[i])/(intervalSize)
        return 0
    elif i == len(distribution)-1:
        # return (distribution[i] - distribution[i-1])/(intervalSize)
        return 0
    else:
        return (distribution[i+1] - distribution[i-1])/(2*intervalSize)

# dist = StepInitialDistribution()
# dist = QuadraticInitialialDistribution()
dist = NormalInitialialDistribution()
plt.plot(dist)
for j in range(6):
    dist = iterateTime(dist)
    plt.plot(dist)
plt.show()

    