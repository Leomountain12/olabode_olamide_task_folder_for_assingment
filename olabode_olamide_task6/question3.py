#3
# Initialize the set with seat numbers 1 to 50
seats = set(range(1, 51))

# Function to simulate booking a seat
def book_seat(seat_number):
    if seat_number in seats:
        seats.remove(seat_number)
        print(f"Seat {seat_number} booked successfully.")
        print(f"Remaining seats: {seats}")
    else:
        print(f"Seat {seat_number} is already booked or invalid.")

# Main loop to handle bookings
while seats:
    try:
        seat_to_book = int(input("Enter the seat number to book (or type 'quit' to exit): "))
        book_seat(seat_to_book)
    except ValueError:
        print("Invalid input. Please enter a number or 'quit'.")

print("All seats are booked!")
