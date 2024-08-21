# Ask user for height and weight, then calc BMI
# 7-21-2004
# CSC121 m1Lab1– Review
# Tristan Beaty

def main():

    again = "yes"
    while again == "yes":
        
        #Ask user for height and weight

        height = float(input("What is your height in inches: "))
        weight = float(input("What is your weight in pounds: "))

        #calc BMI
        heightSqrd = height * height
        BMI = (weight / heightSqrd) * 703
        
        print()
        print(f'Your BMI is {BMI:.1f}')
        print()
        
        U_Bound = 18.5
        L_Bound = 24.9
        
        if L_Bound <= BMI <= U_Bound:
            print("You are within healthy BMI range")

        else:

            if BMI < 18.5:
                lowWeight = (heightSqrd * 18.5) / 703
                weightGain = lowWeight - weight
            
                print(f'You need to gain {weightGain:.2f} pounds to have a healty BMI')
                print()
                
            else:

                if BMI > 24.9:
                    highWeight = (heightSqrd * 24.9) / 703
                    weightLoss = weight - highWeight

                    print(f'You need to lose {weightLoss:.2f} pounds to have a healty BMI')
                    print()
                    

        again = input("Would you like to run the program again? Enter yes or no: ")

main()
input("The program has ended. Press enter/return to exit")
