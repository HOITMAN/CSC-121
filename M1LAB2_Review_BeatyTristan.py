def userInput():
    numInvestments = int(input("How many investment options are there: "))
    valInvestment = float(input("What will be the value of your investment: "))
    return numInvestments, valInvestment


def invLists(numInvestments):
    optValues = []
    pesValues = []
    for i in range(1,numInvestments+1):
        print()
        print("Option", i)
        optValue = float(input("What is the best possible return value: "))
        optValues.append(optValue)
        pesValue = float(input("What is the worst possible return value: "))
        pesValues.append(pesValue)
    return optValues, pesValues


def valCalcs(valInvestment, optValues, pesValues):
    bestEndReturn = float(0)
    for i in range(len(pesValues)):
        expVal = (optValues[i] + pesValues[i]) / 2
        expReturn = (expVal - valInvestment) / valInvestment
        if expReturn > bestEndReturn:
            bestEndReturn = expReturn
            bestInvest = i+1
            risk = (optValues[i] - pesValues[i]) / 2
    return bestInvest, bestEndReturn , risk


def userReturn(bestInvest, bestEndReturn, risk):
    print()
    print("Best investment: " , bestInvest)
    bestExpReturn = bestEndReturn * 100
    print(f'Best average return = {bestExpReturn:.1f} %')
    print(f'Risk = {risk:.1f}')



def main():
    numInvestments, valInvestment = userInput()
    optValues, pesValues = invLists(numInvestments)
    bestInvest, bestEndReturn, risk = valCalcs(valInvestment, optValues, pesValues)
    userReturn(bestInvest, bestEndReturn, risk)

main()
