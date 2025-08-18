#4
# Unique Voters Registration System

print("Enter voter names to register. Type 'done' to finish.\n")

voters = set()

while True:
    name = input("Enter voter name (or 'done' to finish): ").strip()
    
    if name.lower() == 'done':
        break
    
    if name == '':
        print("Empty input! Please enter a valid name.")
        continue
    
    if name in voters:
        print(f"Warning: '{name}' is already registered!")
    else:
        voters.add(name)
        print(f"'{name}' registered successfully.")

print(f"\nTotal unique voters registered: {len(voters)}")
