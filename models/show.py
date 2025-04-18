from datetime import datetime

class Show:
    def __init__(self, show_id, movie, screen, start_time, end_time):
        self.show_id = show_id
        self.movie = movie              
        self.screen = screen            
        self.start_time = start_time    
        self.end_time = end_time        
        self.booked_seats = set()       

    def get_available_seats(self):
        return [seat for seat in self.screen.seats if seat.seat_id not in self.booked_seats]

    def book_seat(self, seat_id):
        if seat_id not in self.booked_seats:
            self.booked_seats.add(seat_id)
            return True
        return False

    def cancel_seat(self, seat_id):
        if seat_id in self.booked_seats:
            self.booked_seats.remove(seat_id)
            return True
        return False
