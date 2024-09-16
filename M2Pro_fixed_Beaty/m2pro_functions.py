def getFutureValue(present, interest, months):
    """
    Param:
        present:float(references present value)
        interest:float
        mon: int(number of months that the money will be in account)
    returns future (float (value of account)
    """
    
    # Define local variable
    interest_per = interest / 100 # write the percentage as a fraction
    future = present * ((1+interest_per) ** months)
    
    return future


#menu function
#menu function
def menu():
    """
    function displays menu
    doesn't return a value
    """

    print("--------MENU--------")
    print("1)Get Future Value")
    print("2)Exit")
    print("--------------------")
    print()
