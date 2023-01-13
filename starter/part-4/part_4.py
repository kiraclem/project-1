book_list = {
'my_book':{
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}, 
'my_book2':{
   "title": "FableHaven",
    "author": "Brandon Mull",
    "year": 2006,
    "rating": 4.1,
    "pages": 368
}
, 
'my_book3':{
   "title": "FarWorld",
    "author": "J. Scott Savage",
    "year": 2012,
    "rating": 3.9,
    "pages": 432
}}

### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

def new_book_input():
    title = input( 'The title of book you would like to add: ')
    author = input('The author name of the book you would like to add: ')
    pages = input( "The number of pages of the book you would like to add: ")
    year = input("The year of the book you would like to add: ")
    rating = input("The rating of the book you would like to add: ")

    book_dictionary = {
        'title': title,
        'author': author,
        'pages': pages,
        'year': year,
        'rating': rating
    }

    return book_dictionary



### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
{'title': 'The Lost Hero', 'author': 'Rick Riordan', 'pages': '557', 'year': '2010', 'rating': '4.8'}

def string_to_int(book_dictionary):
    for key,item in book_dictionary.items():
        if key == 'pages':
            book_dictionary['pages'] = int(item)
        elif key == 'year':
            book_dictionary['year'] = int(item)
        elif key == 'rating':
            book_dictionary['rating'] = float(item)
    return book_dictionary


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

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

    return book_dictionary

# new_book = new_book_input()
# print(new_book)


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here


def menu():
    print('Menu:')
    print('1: add a book')
    print('2: library')
    print('3: exit')

    result = input('input number for menu option: ')

    if result == '1':
        new_book = new_book_input()
        print('')
        print(new_book['title'])
        print('by')
        print(new_book['author'])
        print('added to library')  
        print('')
        menu()
    elif result == '2':
        def get_books():
            book_titles = []
            for book in book_list:
                book_titles.append(book_list[f'{book}']['title'])
            print('Books in library: ')
            print(book_titles)
            print('')
            menu()

        books = get_books()
        print(books)
    elif result == '3':
        print('exited menu')
    else:
        return "not a valid input, please enter 1 or 2"


menu()



