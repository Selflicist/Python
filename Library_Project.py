import os

def show_all_books():
    try:
        with open("allbooks.txt") as book:
            for line in book:
                print(line.strip())
    except:
        print("Record could not be opened.")
    
def new_book():
    print("  Adding new Book in the record")
    print("\n\n Note : Avoid use of space while entering data. \n\n ")
    sr = input("Enter the SR number of the book : ")
    name = input("Enter the name of the book : ")
    auther = input("Enter the name of the author : ")
    issn = input("Enter the ISSN : ")
    cost = input("Enter the cost of the book : ")
    try:
        with open("allbooks.txt", "a") as bookout:
            bookout.write("\n")
            bookout.write("SR of the book : " + sr + "\n")
            bookout.write("Name of the book : " + name + "\n")
            bookout.write("Publisher of the book : " + auther + "\n")
            bookout.write("The ISSN of the books : " + issn + "\n")
            bookout.write("Cost of the book : " + cost + "\n")
            bookout.write("\n")
            bookout.write("Record entered successfully.\n")
    except:
        print("Record could not be opened.")

def issue_book():
    print("  Issuing a Book to a student")
    print("\n\n Note : Avoid use of space while entering data. \n\n ")
    stname = input("Enter the name of the student : ")
    try:
        with open(stname) as student:
            print("\n")
            print("You have already borrowed a book so please return that book and get")
            print("your name removed from the borrower list if you want to get a new one.")
    except:
        rollno = input("Enter the roll number of the student : ")
        bookname = input("Enter the name of the book that is being issued : ")
        try:
            with open(stname, "w") as newstudent:
                newstudent.write("Name of the student : " + stname + "\n")
                newstudent.write("Roll Number of the student : " + rollno + "\n")
                newstudent.write("Book issued : " + bookname + "\n")
            print("\n")
            print("Book issued successfully.")
        except:
            print("Record could not be opened.")

def search_student():
    print("  Searching for a student in the record")
    print("\n\n Note : Avoid use of space while entering data. \n\n ")
    studentname = input("Enter name of the Student whose record you want : ")
    try:
        with open(studentname) as student:
            for line in student:
                print(line.strip())
    except:
        print("Student not found in the record.")

def remove_name():
    name = input("Enter the name that you want to remove from the borrower list : ")
    try:
        os.remove(name)
        print("\n")
        print("Name removed from the list sucessfully.")
    except:
        print("Record could not be opened.")

def ask():
    ch = input("\nDo you want to continue (y or n)? : ")
    if ch == 'n':
        exit()
def main():
    while True:
        print("Library Management")
        print("")
        print("Enter any of the following choices:")
        print("1. Show the details of all books.")
        print("2. Enter a new book in the record.")
        print("3. Issue a book to a student.")
        print("4. Show the student detail record.")
        print("5. Remove a name from the book borrower list.")
        print("6. Exit")
        print("")
        choice = input("Enter your choice: ")
        if choice == "1":
            show_all_books()
            ask()
        elif choice == "2":
            new_book()
            ask()
        elif choice == "3":
            issue_book()
            ask()
        elif choice == "4":
            search_student()
            ask()
        elif choice == "5":
            remove_name()
            ask()
        elif choice == "6":
            exit(0)
        else:
            print("\n\nInvalid Choice. Press any key to continue..")
            input()
main()
