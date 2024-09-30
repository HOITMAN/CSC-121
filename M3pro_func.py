import M3pro_Beaty

authors = ["William Shakespeare","Charles Dickens","James Joyce","Earnest Hemingway","J.K. Rowling"]

books = ["Hamlet","A Tale of Two Cities","Ulysses","The Old Man and the Sea","Harry Potter and the Philosopher's Stone"]

published = [1601, 1859, 1922, 1952, 1997]

prices = [ 14.52, 9.56, 19.97, 10.35, 16.62]

def bookDisplay():

    print(f'{"Num":<5}{"Book":<50}{"Author":<25}{"Year":<7}{"Price"}')
    print("-"*100)

    for i in range(len(authors)):

        print(f'{i+1:<5}{books[i]:<50}{authors[i]:<25}{published[i]:<7}${prices[i]}')

    print("-"*100)


def showPurchase(bookNums):

    print(f'{"Book":<50}{"Author":<25}{"Year":<7}{"Price"}')
    print("-"*100)

    for i in range(len(bookNums)):
        print(f'{books[bookNums[i]]:<50}{authors[bookNums[i]]:<25}{published[bookNums[i]]:<7}${prices[bookNums[i]]}')
        

def totals(bookNums):

    subtotal = 0.00
    for i in range(len(bookNums)):
        subtotal += prices[bookNums[i]]
    tax = subtotal * 0.05
    total = subtotal + tax

    return subtotal, tax, total
