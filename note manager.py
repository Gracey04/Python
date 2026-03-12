while True:
    print("\n--- Notes Manager ---")
    print("1. Add a note")
    print("2. View notes")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        note = input("Write your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")
            print("Note saved!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                notes = file.read()

                if notes:
                    print("\nYour Notes:")
                    print(notes)
                else:
                    print("No notes yet.")

        except FileNotFoundError:
            print("No notes file found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")