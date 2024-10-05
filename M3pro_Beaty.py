# Ask the user what books they want to buy and display price
# 9/23/24
# CSC-121 m3Pro - Purchases
# Tristan Beaty

import M3pro_func as func

authors = ["William Shakespeare","Charles Dickens","James Joyce","Earnest Hemingway","J.K. Rowling"]

books = ["Hamlet","A Tale of Two Cities","Ulysses","The Old Man and the Sea","Harry Potter and the Philosopher's Stone"]

published = [1601, 1859, 1922, 1952, 1997]

prices = [ 14.52, 9.56, 19.97, 10.35, 16.62]

 

def main():

    func.bookDisplay()

    bookNums = []

    cont = "y"
    while cont == "y":

        valid = 2

        buy = int(input("Enter the number of the book you want to buy: "))
        bookNums.append(buy - 1)
        print()

        while valid == 2:
            cont = input("Would you like to buy another book y or n: ")
            if cont == "y" or cont == "n":
                print()
                valid = 1

            else:
                print("Invalid input, please type either y or n")

    func.showPurchase(bookNums)
    subtotal, tax, total = func.totals(bookNums)

    print()
    print("Total price (cost of book(s) + 5% tax):")
    print(f'Books cost before tax ${subtotal:.2f}')
    print(f'Tax ${tax:.2f}')
    print(f'Total after tax ${total:.2f}')


        

if __name__ == "__main__":
    main()
        
