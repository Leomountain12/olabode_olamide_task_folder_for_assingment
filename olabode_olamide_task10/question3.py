# Initialize the set with seat numbers 1 to 50
seats = set(range(1, 51))

# Function to simulate booking a seat
def book_seat(seat_number):
    if seat_number in seats:
        seats.remove(seat_number)
        print(f"Seat {seat_number} booked successfully.")
        print(f"Remaining seats: {sorted(seats)}")
    else:
        print(f"Seat {seat_number} is already booked or invalid.")

# Main loop to handle bookings
while seats:
    user_input = input("Enter the seat number to book (or type 'quit' to exit): ").strip().lower()
    
    if user_input == 'quit':
        print("Exiting booking system. Goodbye!")
        break

    try:
        seat_to_book = int(user_input)
        book_seat(seat_to_book)
    except ValueError:
        print("Invalid input. Please enter a valid seat number (1–50) or 'quit'.")

if not seats:
    print("All seats are booked!")
