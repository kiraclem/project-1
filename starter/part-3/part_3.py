my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_book2 = {
   "title": "FableHaven",
    "author": "Brandon Mull",
    "year": 2006,
    "rating": 4.1,
    "pages": 368
}

my_book3 = {
   "title": "FarWorld",
    "author": "J. Scott Savage",
    "year": 2012,
    "rating": 3.9,
    "pages": 432
}

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


# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def get_book_info(book_dictionary):
    t = book_dictionary['title']
    a = book_dictionary['author']
    y = book_dictionary['year']
    r = book_dictionary['rating']
    p = book_dictionary['pages']

    book_string = f"{t} is a book written by {a} that contains {p} pages, has a rating of {r}, and was written in {y}."
    print(book_string)
    return book_string

get_book_info(my_book)

print('================================================')
# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def get_book_title(book_dictionary):
     print(book_dictionary['title'])
     return book_dictionary['title']

get_book_title(my_book)

# ===============================================

def get_book_author(book_dictionary):
     print(book_dictionary['author'])
     return book_dictionary['author']

get_book_author(my_book)

# ===============================================

def get_book_pages(book_dictionary):
     print(book_dictionary['pages'])
     return book_dictionary['pages']

get_book_pages(my_book)

# ==================================================

def get_book_year(book_dictionary):
     print(book_dictionary['year'])
     return book_dictionary['year']

get_book_year(my_book)

# ==================================================

def get_book_rating(book_dictionary):
     print(book_dictionary['rating'])
     return book_dictionary['rating']

get_book_rating(my_book)

print('================================================')

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps think of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

# function 1 gets titles of all books in library

def get_books():
    book_titles = []
    for book in book_list:
        book_titles.append(book_list[f'{book}']['title'])

    return book_titles

books = get_books()
print(books)
print('================================================')

# function 2 gets multiple books at once

def get_multi_book_info(*args):
         for item in args:
            t = item['title']
            a = item['author']
            y = item['year']
            r = item['rating']
            p = item['pages']
            book_string = f"{t} is a book written by {a} that contains {p} pages, has a rating of {r}, and was written in {y}."
            print(book_string)
            print('================================================')
            

get_multi_book_info(my_book, my_book2)


# function 3 reutrns book searched for

def book_title_input():
    search = input("please enter key letters or words of the title your looking for")
    return search



def book_title_search(string, books):
    for book in books:
        bk = book.lower()
        if string in bk:
            print(f'found the following matching results: {bk}')


book_string = book_title_input()
print('you searched ' + book_string)

book_title_search(book_string, books)


