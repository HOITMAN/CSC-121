bookInventory = {"William Shakespear":[
        {"bookName": "Hamlet", "yearPub": 1601, "price": 14.52, "quantity": 43},
        {"bookName": "Macbeth", "yearPub": 1606, "price": 13.45, "quantity": 50},
        {"bookName": "Othello", "yearPub": 1604, "price": 15.30, "quantity": 37},
        {"bookName": "Romeo and Juliet", "yearPub": 1597, "price": 12.99, "quantity": 60}
        ],

        "Charles Dickens": [
        {"bookName": "A tale of Two Cities", "yearPub": 1859, "price": 9.56, "quantity": 75},
        {"bookName": "Great Expectations", "yearPub": 1861, "price": 12.50, "quantity": 60},
        {"bookName": "Oliver Twist", "yearPub": 1837, "price": 9.75, "quantity": 50},
        {"bookName": "David Copperfield", "yearPub": 1850, "price": 11.25, "quantity": 40}
        ],
        
        "James Joyce": [
        {"bookName": "Ulysses", "yearPub": 1922, "price": 19.99, "quantity": 30},
        {"bookName": "A Portrait of the Artist as a Young Man", "yearPub": 1916, "price": 13.20, "quantity": 25},
        {"bookName": "Dubliners", "yearPub": 1914, "price": 12.00, "quantity": 35},
        {"bookName": "Finnegans Wake", "yearPub": 1939, "price": 16.50, "quantity": 20},
        ],
        
        "Ernest Hemingway": [
        {"bookName": "The Old Man and the Sea", "yearPub": 1952, "price": 10.35, "quantity": 80},
        {"bookName": "A Farewell to Arms", "yearPub": 1929, "price": 14.75, "quantity": 45},
        {"bookName": "For Whom the Bell Tolls", "yearPub": 1940, "price": 13.50, "quantity": 50},
        {"bookName": "The Sun Also Rises", "yearPub": 1926, "price": 12.99, "quantity": 55},
        ],

        "J.K. Rowling": [
        {"bookName": "Harry Potter and the Philosopher's Stone", "yearPub": 1997, "price": 16.62, "quantity": 100},
        {"bookName": "Harry Potter and the Chamber of Secrets", "yearPub": 1998, "price": 22.99, "quantity": 90},
        {"bookName": "Harry Potter and the Prisoner of Azkaban", "yearPub": 1999, "price": 23.99, "quantity": 85},
        {"bookName": "Harry Potter and the Goblet of Fire", "yearPub": 2000, "price": 25.99, "quantity": 80},
        ]
                 
}

def menu():
    print(f'{"-" * 8}Menu{"-" * 8}')
    print("1) Display Book Inventory and Calculate Total")
    print("2) Lookup by Author and Get Total")
    print("3) Lookup by Book Name and Get Total")
    print("4) Lookup by Price Range")
    print("5) Exit")
    print("-" * 20)
    print()
    userMenu = int(input("Select a menu number: "))
    return userMenu


def totalDisplay():
    priceSum = 0.00
    print(f'{"Author":<25} {"Book":<50} {"Year":<10} {"Price":<10} {"Quantity"}')
    print("-" * 120)
    for author, info in bookInventory.items():
        for item in info:
            print(f'{author:<25} {item["bookName"]:<50} {item["yearPub"]:<10} {item["price"]:<10.2f} {item["quantity"]}')
            priceSum += item["price"] * item["quantity"]
    print("-" * 120)
    print(f'{"Overall Total":<86} ${priceSum:,.2f}')
    print()


def authorLookup():
    priceSum = 0.00
    validAuthor = "False"
    while validAuthor == "False":
        authorName = input("Enter author name (name is case sensitive): ")
        print()
        for author, info in bookInventory.items():
            if author == authorName:
                print(f'{"Book":<50} {"Year":<10} {"Price":<10} {"Quantity"}')
                print("-" * 85)
                for item in info:
                    print(f'{item["bookName"]:<50} {item["yearPub"]:<10} {item["price"]:<10.2f} {item["quantity"]}')
                    priceSum += item["price"] * item["quantity"]
                    validAuthor = "True"
                print("-" * 85)
                print(f'{"Overall Total":<60} ${priceSum:.2f}')
        if validAuthor == "False":
            print("Invalid author. Make sure you used correct capitalization")
            print()
    print()


def bookLook():
    priceSum = 0.00
    validBook = "False"
    while validBook == "False":
        book = input("Enter book name (book name is case sensitive): ")
        print()
        for author, info in bookInventory.items():
            author = author
            for item in info:
                if item["bookName"] == book:
                    print(f'{"Author":<25} {"Book":<50} {"Year":<10} {"Price":<10} {"Quantity"}')
                    print("-" * 120)
                    print(f'{author:<25} {item["bookName"]:<50} {item["yearPub"]:<10} {item["price"]:<10.2f} {item["quantity"]}')
                    priceSum += item["price"] * item["quantity"]
                    print("-" * 120)
                    print(f'{"Overall Total":<86} ${priceSum:,.2f}')
                    validBook = "True"
        if validBook == "False":
            print("Invalid book name. (Make sure you use correct capitalization.)")
            print()
    print()


def priceRange():
    inRange = 0
    validRange = "False"
    while validRange == "False":
        validLow = "False"
        validHigh = "False"
        while validLow == "False":
            try:
                lower = float(input("Enter the smaller value: "))
            except ValueError:
                print()
                print("Invalid number")
                print()
            else:
                validLow = "True"
                print()

        while validHigh == "False":
            try:
                higher = float(input("Enter the larger value: "))
            except ValueError:
                print()
                print("Invalid number")
                print()
            else:
                validHigh = "True"
                print()

        if higher < lower:
            print("ERROR, the larger value is smaller than the smaller value, please reinput values")
            print()
        else:
            validRange = "True"

    print(f'{"Author":<25} {"Book":<50} {"Year":<10} {"Price":<10} {"Quantity"}')
    print("-" * 120)
    for author, info in bookInventory.items():
        for item in info:
            if item["price"] >= lower and item["price"] <= higher:
                print()
                print(f'{author:<25} {item["bookName"]:<50} {item["yearPub"]:<10} {item["price"]:<10.2f} {item["quantity"]}')
                inRange += item["quantity"]
    print("-" * 120)
    print(f'{"Number of books between"} ${lower} {"and"} ${higher}{":":<60} {inRange}')
    print()


def exit():
    exitValue = 0
    userExit = "placeholder"
    while userExit != "rerun" and userExit != "exit":
        userExit = input("Would you like to rerun the program or exit the program? (rerun/exit) ")
        if userExit == "rerun":
            exitValue = 0
            print()
            print()
        elif userExit == "exit":
            exitValue = 1
        else:
            print("INVALID RESPONSE. Please type either rerun or exit")
            print()
    return exitValue

                


       

