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

                #Compare BMI to scale
                L_Bound = 18.5
                U_Bound = 24.9

                #BMI healthy
                if L_Bound <= BMI <= U_Bound:
                    print("You are within healthy BMI range")
                    print()

                else:
                    #BMI low
                    if BMI < 18.5:
                        lowWeight = (heightSqrd * 18.5) / 703
                        weightGain = lowWeight - weight
                    
                        print(f'You need to gain {weightGain:.2f} pounds to have a healty BMI')
                        print()
                        
                    else:
                        #BMI high
                        if BMI > 24.9:
                            highWeight = (heightSqrd * 24.9) / 703
                            weightLoss = weight - highWeight

                            print(f'You need to lose {weightLoss:.2f} pounds to have a healty BMI')
                            print()


                
                #ask user to repeat or not

                yn = "invalid"
                while yn == "invalid":
                        again = input("Would you like to run the program again? Enter yes or no: ")

                        if again != "yes" and again != "no":
                            yn = "invalid"
                            print()
                            print("Invalid Response, please type either yes or no.")
                            print()
                
                        else:
                            yn = "valid"
                            print()
                            if again == "yes":
                                print()
                  

#Run program
main()

