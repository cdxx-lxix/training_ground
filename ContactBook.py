# Python Project Ideas: Beginners Level
# 6. Contact Book
# https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/

import sqlite3
import sys

conn = sqlite3.connect('contactbook.db')  # Connection
cur = conn.cursor()  # Cursor
run = True


# Table VALUES - INTEGER[PK,AI,U](id) TEXT(first_name) TEXT(last_name) TEXT(address) TEXT(number) / Table name:contacts
def showAll():
    cur.execute("SELECT * FROM contacts")
    show = cur.fetchall()
    print("ID" + "\t" + "NAME" + "\t\t" + "ADDRESS" + "\t\t\t" + "NUMBER")
    for s in show:
        print(str(s[0]) + " " + s[1] + " " + s[2] + "\t" + s[3] + "\t" + s[4])


def addNew():
    print("---------------------------------")
    print("Creating a new contact")
    while True:
        try:
            addID = input("Enter ID (numbers only): ")
            addID = int(addID)
            break
        except ValueError:
            print("NUMBERS ONLY | this is the only step you cant go back from")
    addName = input("First name: ")
    if addName == '<':
        menu()
    addLast = input("Last name: ")
    if addLast == '<':
        menu()
    addRess = input("Address: ")
    if addRess == '<':
        menu()
    addNum = input("Number: ")
    if addNum == '<':
        menu()
    cur.execute(
        f'''INSERT INTO contacts VALUES ("{addID}", "{addName}", "{addLast}", "{addRess}", "{addNum}")''')
    conn.commit()
    print("Done")
    cur.execute(f'SELECT * FROM contacts WHERE number = "{addID}"')
    print(cur.fetchall())
    print("---------------------------------")


def editCont():
    print("------------------------------------------")
    idfilter = input("Please enter contact ID you want to edit: ")
    cur.execute(f'SELECT * FROM contacts WHERE id = "{idfilter}"')
    print(cur.fetchall())
    asurance = input("Is this the right contact?: y / n: ")
    if asurance.lower() == 'y':
        editfilter = input(
            "What do you want to edit? (name, lastname, address, number): ")
        if editfilter.lower() == 'name':
            newname = input("Enter a new name: ")
            cur.execute(
                f'''UPDATE contacts SET first_name = "{newname}" WHERE id = "{idfilter}"''')
            print("Updated. Here is how it looks now: ")
            cur.execute(f'SELECT * FROM contacts WHERE id = "{idfilter}"')
            print(cur.fetchall())
            print("------------------------------------------")
        elif editfilter.lower() == 'lastname':
            newname = input("Enter a new lastname: ")
            cur.execute(
                f'''UPDATE contacts SET last_name = "{newname}" WHERE id = "{idfilter}"''')
            print("Updated. Here is how it looks now: ")
            cur.execute(f'SELECT * FROM contacts WHERE id = "{idfilter}"')
            print(cur.fetchall())
            print("------------------------------------------")
        elif editfilter.lower() == 'address':
            newname = input("Enter a new address: ")
            cur.execute(
                f'''UPDATE contacts SET address = "{newname}" WHERE id = "{idfilter}"''')
            print("Updated. Here is how it looks now: ")
            cur.execute(f'SELECT * FROM contacts WHERE id = "{idfilter}"')
            print(cur.fetchall())
            print("------------------------------------------")
        elif editfilter.lower() == 'number':
            newname = input("Enter a new number: ")
            cur.execute(
                f'''UPDATE contacts SET number = "{newname}" WHERE id = "{idfilter}"''')
            print("Updated. Here is how it looks now: ")
            cur.execute(f'SELECT * FROM contacts WHERE id = "{idfilter}"')
            print(cur.fetchall())
            print("------------------------------------------")
        elif editfilter.lower() == '<':
            menu()
    elif asurance.lower() == 'n':
        editCont()
    elif asurance or idfilter == '<':
        menu()


def deleteCont():
    idfilter = input("Please enter contact ID you want to delete: ")
    cur.execute(f'SELECT * FROM contacts WHERE id = "{idfilter}"')
    print(cur.fetchall())
    asurance = input("Is this the right contact?: y / n: ")
    if asurance.lower() == 'y':
        cur.execute(f'DELETE FROM contacts WHERE id = "{idfilter}"')
        print("Deleted. RIP gone and forgotten")
    elif asurance.lower() == 'n':
        deleteCont()
    elif asurance.lower() == '<':
        menu()


def menu():
    print("-----------------------------------")
    print("1. Show all contacts (show)")
    print("2. Find contact by name (findname)")
    print("3. Find contact by number (findnum)")
    print("4. Add a new contact (addnew)")
    print("5. Edit existing contact (edit)")
    print("6. Delete contact (delete)")
    print("7. Exit (exit)")
    print("Type anywhere < to get back in menu ")
    print("-----------------------------------")
    option = input("What would you like to do: ")
    if option.lower() == "show":
        showAll()
    elif option.lower() == "findname":
        namefilter = input("Enter the name: ")
        cur.execute(
            f'SELECT * FROM contacts WHERE first_name LIKE "%{namefilter}%"')
        print("Search results: ")
        search = cur.fetchall()
        for s in search:
            print(s)
    elif option.lower() == "findnum":
        numfilter = input("Enter the number: ")
        cur.execute(
            f'SELECT * FROM contacts WHERE number LIKE "%{numfilter}%"')
        print("Search results: ")
        search = cur.fetchall()
        for s in search:
            print(s)
    elif option.lower() == "addnew":
        addNew()
    elif option.lower() == "edit":
        editCont()
    elif option.lower() == "delete":
        deleteCont()
    elif option.lower() == "exit":
        conn.commit()
        conn.close()
        sys.exit()
    else:
        print("Input a valid command. Dude, that's easy")


while run:
    menu()
