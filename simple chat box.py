while True:
    message = input("You: ").lower()

    if message == "hello":
        print("Friend: Hi!")

    elif message == "how are you?":
        print("Friend: I'm fine, thank you!")

    elif message == "bye":
        print("Friend: Goodbye!")
        break

    else:
        print("Friend: I don't understand.")