print("Assistant started")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Assistant stopped")
        break

    print("Assistant:", user)
