### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["Bradon Mull", "Jennifer A. Nielson", "J.R.R.. Tolkien", "J. Scott Savage", "C. S Lewis", "Carol Dweck", "Conan Doyle"]

# Now let's add a new author to the end with the .append() method. Type your code below.

# Code here
# Example: my_authors.append("H.G. Wells")
my_authors.append("H.G. Wells")
print(my_authors)

# Now let's remove an element in the list

# Code here
# Example: my_authors.remove("H.G. Wells")
print('===========================')
my_authors.remove("H.G. Wells")
print(my_authors)
# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here
# Example: my_authors[2]
print('===========================')
print(my_authors[-1])


# Now slice the list.

# Code here
# Example: my_authors[1:4]
print('===========================')
print(my_authors[0:7:3])

### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")

my_author_tuple = ("Bradon Mull", "Jennifer A. Nielson", "J.R.R. Tolkien", "J. Scott Savage", "C. S Lewis", "Carol Dweck", "Conan Doyle")

### Step 3 - Sets ###

# Create a set with your authors.

# Code here
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}

my_author_set = {"Bradon Mull", "Jennifer A. Nielson", "J.R.R. Tolkien", "J. Scott Savage", "C. S Lewis", "Carol Dweck", "Conan Doyle"}

# Add a new author to your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
print('===========================')
my_author_set.add("Christopher Paolini")

print(my_author_set)

# Try adding the same author again, and be sure to print your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
print('===========================')
my_author_set.add("Christopher Paolini")
print(my_author_set)

### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
# Example:

# for book in my_authors:
    # print(book)

print('===========================')
for book in my_authors:
    print(book)

# for book in my_authors_tuple:
    # print(book)
print('===========================')
for book in my_author_tuple:
    print(book)

# for book in my_authors_set:
    # print(book)
print('===========================')
for book in my_author_set:
    print(book)
