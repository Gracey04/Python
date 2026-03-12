while True:
    print("\n--- Daily Journal App ---")
    print("1. Write a new entry")
    print("2. View journal entries")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        entry = input("Write your journal entry: ")

        with open("journal.txt", "a") as file:
            file.write(entry + "\n")

        print("Entry saved!")

    elif choice == "2":
        try:
            with open("journal.txt", "r") as file:
                entries = file.read()
                print("\nYour Journal Entries:")
                print(entries)

        except FileNotFoundError:
            print("No journal entries yet.")

    elif choice == "3":
        print("Exiting journal app. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")