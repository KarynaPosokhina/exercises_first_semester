def read_books():
    list = []
    with open("books.txt", encoding="utf-8") as file:
        line = file.readline().strip()
        while line:
            list.append(line)
            line = file.readline().strip()
    return list

def menu():
    choice = '?'
    while choice not in 'abcsABCS':
        print("\ta - Overview")
        print("\tb - Longest title")
        print("\tc - 5 letters on a row")
        print("\ta - Stop")
        choice = input('\tMake your choice: ').lower()
    return choice

def print_list(books):
    print("\nList of books:\n")
    for i in range(len(books)):
        print(i+1, books[i])
    print()

books = read_books()
choice = menu()

while choice != 's':
    match choice:
        case 'a':
            print_list(books)
        case 'b':
            print_list(books)
            max_length = len(books[0])
            for book in books:
                if len(book) > max_length:
                    max_length = len(book)
            print(f'The longest title has {max_length} characters\n')
        case 'c':
            booknumber = int(input("Enter book number max " + str(len(books)) + ": "))
            book = books[booknumber - 1]

            for i in range(len(book)):
                if i % 5 == 0:
                    print()
                print(book[i], end=' ')
            print()
    choice = menu()