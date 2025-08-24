## Unique Name Collector with Error Handling

print("Enter the names of people attending the seminar.")
print("Type 'done' when you finish.\n")

# Using a set to store unique names
attendees = set()

while True:
    try:
        name = input("Enter name (or 'done' to finish): ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nInput interrupted. Exiting...")
        break
    except Exception as e:
        print(f"Unexpected error: {e}")
        continue

    if name.lower() == 'done':
        break
    if name == '':
        print("Empty input! Please enter a valid name.")
        continue
    if name in attendees:
        print(f"{name} is already in the list.")
    else:
        attendees.add(name)
        print(f"{name} added.")

# Display names sorted alphabetically
print("\nAttendees (alphabetical order):")
for name in sorted(attendees):
    print(name)
