books = {
    "A234": {"name": "The 101 Dalmations", "available": True, "borrower": None},
    "A675": {"name": "The Adventures of Huckleberry Finn", "available": True, "borrower": None},
    "A212": {"name": "Bag of Bones", "available": True, "borrower": None},
    "B671": {"name": "Charlie and the Chocolate Factory", "available": True, "borrower": None},
    "B534": {"name": "Charlotte's Web", "available": True, "borrower": None},
    "B777": {"name": "A Christmas Carol", "available": True, "borrower": None},
    "B778": {"name": "Dracula", "available": True, "borrower": None},
    "B812": {"name": "A Farewell to Arms", "available": True, "borrower": None},
    "C101": {"name": "The Firm", "available": True, "borrower": None},
    "C102": {"name": "War and Peace", "available": True, "borrower": None}
}

borrowers = ["L34", "L22", "L19", "L84", "L77"]

while True:
    command = input("Enter command (checkout/return/exit): ")

    if command == "exit":
        break

    borrower_id = input("Enter borrower id: ")
    if borrower_id not in borrowers:
        print(f"{borrower_id} is not a valid borrower")
        continue

    book_id = input("Enter book id: ")
    if book_id not in books:
        print(f"there is no such book {book_id}")
        continue

    if command == "checkout":
        if not books[book_id]["available"]:
            print(f"{book_id} already checked out")
        else:
            books[book_id]["available"] = False
            books[book_id]["borrower"] = borrower_id
            print("checkout successful")

    elif command == "return":
        if books[book_id]["available"]:
            print(f"{book_id} not currently checked out")
        else:
            books[book_id]["available"] = True
            books[book_id]["borrower"] = None
            print("return successful")

print("LMS terminated.")
