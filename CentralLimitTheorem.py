import math
import matplotlib.pyplot as plt
import numpy.random


def getMean(list: list) -> float:
    return sum(list) / len(list)


def getVariance(list: list) -> float:
    mean = getMean(list)
    return sum([(i - mean) ** 2 for i in list]) / len(list)


def getDeviation(list: list) -> float:
    mean = getMean(list)
    return math.sqrt(sum([(i - mean) ** 2 for i in list]) / len(list))


def getUniformMean(n):
    return n / 2


def getUniformVariance(n):
    return n / 12


def getUniformDeviation(n):
    return math.sqrt(n / 12)


def getNormalDistributionFunction(mean: float, deviation: float, x: float) -> float:
    return (1 / (deviation * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mean) / deviation) ** 2)


def generateASample(n: int) -> list:
    return [numpy.random.uniform() for i in range(n)]


def sumTheList(list: list) -> float:
    return sum(list)


def makeExperiment(experimentNum: int, valueNum: int) -> list:
    return [sumTheList(generateASample(valueNum)) for i in range(experimentNum)]


def generateASampleFour(n: int) -> list:
    result = []
    result.append(numpy.random.uniform(0, 200))  # first value is always uniform
    while len(result) < n:
        if result[-1] < 99:
            result.append(numpy.random.uniform(0, 200))
        else:
            result.append(numpy.random.uniform(98, 102))
    return result


def makeExperimentFour(experimentNum: int, valueNum: int) -> list:
    return [sumTheList(generateASampleFour(valueNum)) for i in range(experimentNum)]


def generateASampleFive(n: int) -> list:
    result = []  # list to store the result
    for i in range(n):
        while True:
            a = numpy.random.uniform()
            b = numpy.random.uniform()
            if a < b:
                result.append(numpy.random.uniform(a, b - a))
                break
    return result


def makeExperimentFive(experimentNum: int, valueNum: int) -> list:
    return [sumTheList(generateASampleFive(valueNum)) for i in range(experimentNum)]


def experiment1():
    result = makeExperiment(200000, 2)
    x = numpy.linspace(0, 2, 200000)
    mean = getUniformMean(2)
    deviation = getUniformDeviation(2)
    y = [getNormalDistributionFunction(mean, deviation, i) for i in x]
    print(f"Experiment 1"
          f"\nMean: {mean}"
          f"\nVariance: {getUniformVariance(2)}"
          f"\nDeviation: {deviation}")

    plt.plot(x, y, label="Theoratical")
    plt.hist(result, bins=100, density=True)
    plt.title("Histogram of the samples1")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()


def experiment2():
    result = makeExperiment(200000, 4)
    x = numpy.linspace(0, 4, 200000)
    mean = getUniformMean(4)
    deviation = getUniformDeviation(4)
    y = [getNormalDistributionFunction(mean, deviation, i) for i in x]
    print(f"Experiment 2"
          f"\nMean: {mean}"
          f"\nVariance: {getUniformVariance(4)}"
          f"\nDeviation: {deviation}")
    plt.plot(x, y, label="Theoretical")
    plt.hist(result, bins=100, density=True)
    plt.title("Histogram of the samples2")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()


def experiment3():
    result = makeExperiment(200000, 50)
    x = numpy.linspace(0, 50, 200000)
    mean = getUniformMean(50)
    deviation = getUniformDeviation(50)
    y = [getNormalDistributionFunction(mean, deviation, i) for i in x]
    print(f"Experiment 3"
          f"\nMean: {mean}"
          f"\nVariance: {getUniformVariance(50)}"
          f"\nDeviation: {deviation}")
    plt.plot(x, y, label="Theoretical")
    plt.hist(result, bins=100, density=True)
    plt.title("Histogram of the samples3")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()


def experiment4():
    result = makeExperimentFour(200000, 50)
    x = numpy.arange(3000, 7000, 15)
    mean = getMean(result)
    deviation = getDeviation(result)
    y = [getNormalDistributionFunction(mean, deviation, i) for i in x]
    print(f"Experiment 4"
          f"\nMean: {mean}"
          f"\nVariance: {getVariance(result)}"
          f"\nDeviation: {deviation}")
    plt.plot(x, y, label="Theoretical")
    plt.hist(result, bins=100, density=True)
    plt.title("Histogram of the samples4")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()


def experiment5():
    result = makeExperimentFive(200000, 50)
    x = numpy.linspace(0, 50, 200000)
    mean = getMean(result)
    deviation = getDeviation(result)
    y = [getNormalDistributionFunction(mean, deviation, i) for i in x]
    print(f"Experiment 5"
          f"\nMean: {mean}"
          f"\nVariance: {getVariance(result)}"
          f"\nDeviation: {deviation}")
    plt.plot(x, y, label="Theoretical")
    plt.hist(result, bins=100, density=True)
    plt.title("Histogram of the samples5")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()


experiment1()
experiment2()
experiment3()
experiment4()
experiment5()
