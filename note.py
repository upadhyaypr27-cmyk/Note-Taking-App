def display_menu():
    print("\nNote-Taking App")
    print("1. Add a note")
    print("2. View all notes")
    print("3. Clear all notes")
    print("4. Exit")

    try:
        return int(input("Enter your choice (1-4): "))

    except ValueError:
        return 0


def add_note():
    add_note = input("Enter Note: ")
    with open("notes.txt", 'a') as f:
        f.write(add_note+"\n")
    print("Note Added")


def view_note():
    try:
        with open('notes.txt', 'r') as f:
            content = f.read()

            if content.strip() == "":
                print("-> Note FIle is Empty.")

            else:
                print(f"\n{content}\n")

    except FileNotFoundError:
        print("\n-> Note File Not Created.")


def clear_note():
    try:
        open('notes.txt', 'w').close()
        print(f"\nAll notes cleared.\n")

    except FileNotFoundError:
        print("\n-> Note File Not Created.")


def note_taking_app():
    filename = "notes.txt"

    while True:
        choice = display_menu()

        if choice == 1:
            add_note()

        elif choice == 2:
            view_note()

        elif choice == 3:
            clear_note()

        elif choice == 4:
            print(f"\nExiting the app... \n")
            break

        else:
            print("Invalid choice. please choose 1-4")


note_taking_app()
