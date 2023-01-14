#### Step 1 - Store data in a .txt

### This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and 
## call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

# with open('library.txt','a') as file:
#     file.write('FableHaven2, BradonMull, 2011, 4.2, 402\n')

#### Step 2 - Read data from a .txt

### Now take your previously create function which prints info about all the books in your library, but gets the info from a list, 
## and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python 
# application finished!

# THIS WORKS!!!!

# def get_book_dictionary():
#     with open('library.txt', 'r') as file:
#         file = file.readlines()

#         for line in file:
#             title, author, pages, year, rating = line.split(',')

#             book_dictionary = {
#                 'title': title,
#                 'author': author,
#                 'pages': int(pages),
#                 'year': int(year),
#                 'rating': float(rating)
#             }

#             print(book_dictionary)
#             return book_dictionary


#BOOK INFO

def get_book_list():
    with open('library.txt', 'r') as file:
        file = file.readlines()
        num = 0
        book_list = {}
        for line in file:
            title, author, pages, year, rating = line.split(',')

            book_dictionary = {
                'title': title,
                'author': author,
                'pages': int(pages),
                'year': int(year),
                'rating': float(rating)
            }

            num += 1

            book_list[num] = book_dictionary
        
        return book_list


# get_book_list()



def get_book_list_title_author(dictionary):
    for value in dictionary.values():
        print(value['title'] + ' by' + value['author'])

def get_book_title(dictionary):
       for value in dictionary.values():
        print(value['title'])




# 4 BOOK TITLE SEARCH

def book_title_input():
    search = input("please enter key letters or words of the title your looking for ")
    return search



def book_title_search(string, books):
    for value in books.values():
        bk = value['title'].lower()
        if string in bk:
            print(f'found the following matching results: {bk}')

# 5 BOOK AUTHOR SEARCH

def book_author_input():
    search = input("please enter key letters, or name of the author your looking for ")
    return search



def book_author_search(string, books):
    for value in books.values():
        bk = value['author'].lower()
        if string in bk:
            print(f'found the following matching results: {bk}')

    # for book in books:
    #     bk = book.lower()
    #     if string in bk:
    #         print(f'found the following matching results: {bk}')



# 2 ADD A BOOK 

def new_book_input():
    
    title = input( 'The title of book you would like to add: ')
    author = input('The author name of the book you would like to add: ')

    try:
        pages = int(input( "The number of pages of the book you would like to add: "))
    except:
        return print("Invalid input, please enter a number")
   
    try:
        year = int(input("The year of the book you would like to add: "))
    except:
        return print("Invalid input, please enter a number")
  
    try:
        rating = float(input("The rating of the book you would like to add: "))
    except:
        return print("Invalid input, please enter a number")


    book_dictionary = {
        'title': title,
        'author': author,
        'pages': pages,
        'year': year,
        'rating': rating
    }

    with open('library.txt','a') as file:
        file.write(f'{title}, {author}, {pages}, {year}, {rating}\n')

    return book_dictionary


# MAIN MENU


if __name__ == '__main__':
    def menu():
        print('Menu:')
        print('1: exit')
        print('2: add a book')
        print('3: library')
        print('4: search by title')
        print('5: search by author')
        print('')
        result = input('input number for menu option: ')
        print('')
        while not result == '1':


            if result == '2':
                new_book = new_book_input()
                print(new_book['title'])
                print('by')
                print(new_book['author'])
                print('added to library')  
    

            elif result == '3':
                print('The library contains these books:')
                print('')
                get_book_list_title_author(get_book_list())

            elif result == '4':
                book_string = book_title_input()
                books = get_book_list()
                print('you searched ' + book_string)
                book_title_search(book_string, books)               

            elif result == '5':
                book_string = book_author_input()
                books = get_book_list()
                print('you searched ' + book_string)
                book_author_search(book_string, books)    

            else:
                print("not a valid input, please enter a number for menu: ")

            print('')
            menu()
            break
        
        if result == '1':
            print('exited menu')

    menu()    


