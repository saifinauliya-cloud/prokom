guest_list = ["Ara", "Nisa", "Tiara", "Maya", "Aurel", "Rosy"]

print("I can only invite two people for dinner.")

guest_removed = guest_list.pop()
print(f"Sorry, {guest_removed}, but you can't come to dinner.")

guest_removed = guest_list.pop()
print(f"Sorry, {guest_removed}, but you can't come to dinner.")

guest_removed = guest_list.pop()
print(f"Sorry, {guest_removed}, but you can't come to dinner.")

guest_removed = guest_list.pop()
print(f"Sorry, {guest_removed}, but you can't come to dinner.")

print(f"Hello, {guest_list[0]}! You are still invited to dinner.")
print(f"Hello, {guest_list[1]}! You are still invited to dinner.")

del guest_list[0]
del guest_list[0]

print(guest_list)