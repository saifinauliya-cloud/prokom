def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt size is {size} and the message is '{message}'.")

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt(size="Medium")

# Shirt with a different message
make_shirt(size="Small", message="Keep Learning")