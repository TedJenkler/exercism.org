"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    letters = ["A", "B", "C", "D"]
    for i in range(number):
        yield letters[i % 4] 
    


def generate_seats(number):
    letters = ["A", "B", "C", "D"]
    row = 1
    for i in range(number):
        while row == 13:
            row += 1
        
        yield f"{row}{letters[i % 4]}"
        
        if (i + 1) % 4 == 0:
            row += 1

def assign_seats(passengers):
    seats = generate_seats(len(passengers))
    return {person: next(seats) for person in passengers} 

def generate_codes(seat_numbers, flight_id):
    for seat in seat_numbers:
        zeros_needed = 12 - (len(seat) + len(flight_id))
        yield f"{seat}{flight_id}{zeros_needed * '0'}"